import express from "express";
import { chromium } from "playwright";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;
const SHOT_TIMEOUT_MS = 25000;
const CAPTURE_WAIT_MS = 1500;

const PRESETS = {
  desktop: { width: 1440, height: 2200, isMobile: false },
  laptop: { width: 1280, height: 1800, isMobile: false },
  mobile: { width: 430, height: 1600, isMobile: true },
};

let browserPromise;

function ensureBrowser() {
  if (!browserPromise) {
    browserPromise = chromium.launch({ headless: true });
  }
  return browserPromise;
}

function normalizeUrl(value = "") {
  const raw = String(value).trim();
  if (!raw) return "";
  if (/^https?:\/\//i.test(raw)) return raw;
  return `https://${raw}`;
}

function getPreset(name = "desktop") {
  return PRESETS[String(name).toLowerCase()] || PRESETS.desktop;
}

async function cleanupPage(page) {
  await page.evaluate(() => {
    const hideSelectors = [
      "[id*='onetrust']",
      "[class*='onetrust']",
      "#onetrust-banner-sdk",
      "#onetrust-consent-sdk",
      "[aria-label*='cookie' i]",
      "[class*='cookie' i]",
      "[id*='cookie' i]",
      "[class*='consent' i]",
      "[id*='consent' i]",
      "[class*='modal' i]",
      "[class*='popup' i]",
      "[data-test*='overlay' i]",
      "[data-testid*='overlay' i]"
    ];

    for (const selector of hideSelectors) {
      for (const element of document.querySelectorAll(selector)) {
        if (!(element instanceof HTMLElement)) continue;
        const style = window.getComputedStyle(element);
        const rect = element.getBoundingClientRect();
        const looksLikeOverlay = style.position === 'fixed' || style.position === 'sticky' || rect.width > window.innerWidth * 0.35;
        if (looksLikeOverlay) {
          element.style.setProperty('display', 'none', 'important');
          element.style.setProperty('visibility', 'hidden', 'important');
          element.style.setProperty('opacity', '0', 'important');
        }
      }
    }

    document.querySelectorAll("body, html").forEach((node) => {
      if (!(node instanceof HTMLElement)) return;
      node.style.setProperty("overflow", "visible", "important");
      node.style.setProperty("position", "static", "important");
    });
  }).catch(() => {});
}

app.use(express.static(__dirname, { extensions: ["html"] }));

app.get("/", (_req, res) => {
  res.redirect(302, "/gallery");
});

app.get("/gallery", (_req, res) => {
  res.sendFile(path.join(__dirname, "gallery.html"));
});

app.get("/api/screenshot", async (req, res) => {
  const url = normalizeUrl(req.query.url);
  const preset = getPreset(req.query.preset);
  const waitMs = Math.min(Math.max(Number.parseInt(req.query.wait ?? `${CAPTURE_WAIT_MS}`, 10) || CAPTURE_WAIT_MS, 0), 10000);
  if (!url) {
    res.status(400).json({ error: "Missing url query parameter." });
    return;
  }

  let page;
  let context;

  try {
    const browser = await ensureBrowser();
    context = await browser.newContext({
      viewport: { width: preset.width, height: preset.height },
      deviceScaleFactor: 1,
      isMobile: preset.isMobile,
      hasTouch: preset.isMobile,
    });
    page = await context.newPage();
    page.setDefaultNavigationTimeout(SHOT_TIMEOUT_MS);
    page.setDefaultTimeout(SHOT_TIMEOUT_MS);

    await page.goto(url, { waitUntil: "domcontentloaded", timeout: SHOT_TIMEOUT_MS });
    await page.waitForLoadState("networkidle", { timeout: 5000 }).catch(() => {});
    await page.waitForTimeout(waitMs);
    await cleanupPage(page);
    await page.waitForTimeout(250);
    const image = await page.screenshot({ type: "png", fullPage: false, animations: "disabled" });

    res.setHeader("Content-Type", "image/png");
    res.setHeader("Cache-Control", "no-store");
    res.send(image);
  } catch (error) {
    res.status(502).json({
      error: "Failed to capture screenshot.",
      detail: error instanceof Error ? error.message : String(error),
      url,
    });
  } finally {
    if (page) await page.close().catch(() => {});
    if (context) await context.close().catch(() => {});
  }
});

app.listen(PORT, () => {
  console.log(`Shatter server listening on http://localhost:${PORT}`);
});
