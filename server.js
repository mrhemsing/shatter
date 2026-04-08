import express from "express";
import { chromium } from "playwright";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;
const SHOT_TIMEOUT_MS = 25000;
const CAPTURE_WIDTH = 1440;
const CAPTURE_HEIGHT = 2200;
const CAPTURE_WAIT_MS = 1500;

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

app.use(express.static(__dirname, { extensions: ["html"] }));

app.get("/api/screenshot", async (req, res) => {
  const url = normalizeUrl(req.query.url);
  if (!url) {
    res.status(400).json({ error: "Missing url query parameter." });
    return;
  }

  let page;
  let context;

  try {
    const browser = await ensureBrowser();
    context = await browser.newContext({
      viewport: { width: CAPTURE_WIDTH, height: CAPTURE_HEIGHT },
      deviceScaleFactor: 1,
    });
    page = await context.newPage();
    page.setDefaultNavigationTimeout(SHOT_TIMEOUT_MS);
    page.setDefaultTimeout(SHOT_TIMEOUT_MS);

    await page.goto(url, { waitUntil: "domcontentloaded", timeout: SHOT_TIMEOUT_MS });
    await page.waitForTimeout(CAPTURE_WAIT_MS);
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
