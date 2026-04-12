from pathlib import Path

path = Path(r"C:\Users\Matt\.openclaw\workspace\shatter\gallery.html")
text = path.read_text(encoding="utf-8")
start = text.index("      const defaultTargetDefs = [")
end = text.index("      function loadTargetDefs() {", start)
replacement = '''      const defaultTargetDefs = [
        { id: "clown-1", nx: 0.1621, ny: 0.6847, nr: 0.0288, points: 100, maxHits: 2 },
        { id: "clown-2", nx: 0.3074, ny: 0.6878, nr: 0.0288, points: 100, maxHits: 2 },
        { id: "clown-3", nx: 0.4697, ny: 0.6572, nr: 0.0288, points: 150, maxHits: 2 },
        { id: "clown-4", nx: 0.8755, ny: 0.6856, nr: 0.0288, points: 100, maxHits: 2 },
        { id: "duck-1", nx: 0.0941, ny: 0.8475, nr: 0.0240, points: 75, maxHits: 1 },
        { id: "duck-2", nx: 0.2411, ny: 0.8491, nr: 0.0240, points: 75, maxHits: 1 },
        { id: "duck-3", nx: 0.3842, ny: 0.8475, nr: 0.0240, points: 75, maxHits: 1 },
        { id: "duck-4", nx: 0.5568, ny: 0.8513, nr: 0.0240, points: 75, maxHits: 1 },
        { id: "duck-5", nx: 0.7353, ny: 0.8459, nr: 0.0240, points: 75, maxHits: 1 },
        { id: "duck-6", nx: 0.8935, ny: 0.8506, nr: 0.0240, points: 75, maxHits: 1 },
        { id: "bullseye-1", nx: 0.3151, ny: 0.4549, nr: 0.0192, points: 50, maxHits: 1 },
        { id: "bullseye-2", nx: 0.4626, ny: 0.3920, nr: 0.0192, points: 50, maxHits: 1 },
        { id: "bullseye-3", nx: 0.5985, ny: 0.3831, nr: 0.0192, points: 50, maxHits: 1 },
        { id: "bullseye-4", nx: 0.7086, ny: 0.4546, nr: 0.0192, points: 50, maxHits: 1 },
        { id: "bullseye-5", nx: 0.7984, ny: 0.4554, nr: 0.0192, points: 50, maxHits: 1 },
        { id: "flag-1", nx: 0.3207, ny: 0.3815, nr: 0.0192, points: 25, maxHits: 1 },
        { id: "flag-2", nx: 0.4461, ny: 0.3769, nr: 0.0192, points: 25, maxHits: 1 },
        { id: "flag-3", nx: 0.8060, ny: 0.3911, nr: 0.0192, points: 25, maxHits: 1 },

        { id: "bulb-1", nx: 0.0194, ny: 0.3096, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-2", nx: 0.0558, ny: 0.2874, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-3", nx: 0.0914, ny: 0.2644, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-4", nx: 0.1286, ny: 0.2484, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-5", nx: 0.1647, ny: 0.2338, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-6", nx: 0.2035, ny: 0.2193, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-7", nx: 0.2395, ny: 0.2085, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-8", nx: 0.2783, ny: 0.1985, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-9", nx: 0.3178, ny: 0.1923, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-10", nx: 0.3566, ny: 0.1869, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-11", nx: 0.3977, ny: 0.1839, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-12", nx: 0.4388, ny: 0.1824, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-13", nx: 0.4783, ny: 0.1816, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-14", nx: 0.5194, ny: 0.1816, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-15", nx: 0.5581, ny: 0.1839, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-16", nx: 0.5984, ny: 0.1893, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-17", nx: 0.6380, ny: 0.1962, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-18", nx: 0.6760, ny: 0.2062, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-19", nx: 0.7132, ny: 0.2177, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-20", nx: 0.7481, ny: 0.2322, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-21", nx: 0.7853, ny: 0.2484, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-22", nx: 0.8225, ny: 0.2653, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-23", nx: 0.8574, ny: 0.2866, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-24", nx: 0.8985, ny: 0.3104, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-25", nx: 0.3124, ny: 0.4549, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-26", nx: 0.5047, ny: 0.3412, nr: 0.0096, points: 10, maxHits: 1 },
        { id: "bulb-27", nx: 0.8000, ny: 0.4554, nr: 0.0096, points: 10, maxHits: 1 },

        { id: "back-left-1", nx: 0.0744, ny: 0.4902, nr: 0.0144, points: 50, maxHits: 1 },
        { id: "back-left-2", nx: 0.1171, ny: 0.4656, nr: 0.0144, points: 50, maxHits: 1 },
        { id: "back-left-3", nx: 0.1613, ny: 0.4472, nr: 0.0144, points: 50, maxHits: 1 },
        { id: "back-left-4", nx: 0.2047, ny: 0.4333, nr: 0.0144, points: 50, maxHits: 1 },
        { id: "back-left-5", nx: 0.0574, ny: 0.5728, nr: 0.0144, points: 50, maxHits: 1 },
        { id: "back-left-6", nx: 0.1016, ny: 0.5498, nr: 0.0144, points: 50, maxHits: 1 },
        { id: "back-left-7", nx: 0.1450, ny: 0.5275, nr: 0.0144, points: 50, maxHits: 1 },
        { id: "back-left-8", nx: 0.1884, ny: 0.5025, nr: 0.0144, points: 50, maxHits: 1 },

        { id: "back-right-1", nx: 0.8140, ny: 0.4909, nr: 0.0144, points: 50, maxHits: 1 },
        { id: "back-right-2", nx: 0.8574, ny: 0.4664, nr: 0.0144, points: 50, maxHits: 1 },
        { id: "back-right-3", nx: 0.9000, ny: 0.4472, nr: 0.0144, points: 50, maxHits: 1 },
        { id: "back-right-4", nx: 0.9419, ny: 0.4356, nr: 0.0144, points: 50, maxHits: 1 },
        { id: "back-right-5", nx: 0.8295, ny: 0.5267, nr: 0.0144, points: 50, maxHits: 1 },
        { id: "back-right-6", nx: 0.8736, ny: 0.5491, nr: 0.0144, points: 50, maxHits: 1 },
        { id: "back-right-7", nx: 0.9155, ny: 0.5744, nr: 0.0144, points: 50, maxHits: 1 },
      ];

'''
text = text[:start] + replacement + text[end:]
path.write_text(text, encoding="utf-8")
print("updated gallery targets")
