import json
import sys
from pathlib import Path

METRICS_FILE = Path("metrics.json")
MIN_ACCURACY = 0.85

if not METRICS_FILE.exists():
    print("Error: metrics.json not found")
    sys.exit(1)

with open(METRICS_FILE, "r") as file:
    metrics = json.load(file)

accuracy = metrics.get("accuracy")

if accuracy is None:
    print("Error: accuracy field not found in metrics.json")
    print("Available fields:", list(metrics.keys()))
    sys.exit(1)

print(f"Model accuracy: {accuracy:.2%}")
print(f"Required accuracy: {MIN_ACCURACY:.2%}")

if accuracy >= MIN_ACCURACY:
    print("QUALITY GATE PASSED")
else:
    print("QUALITY GATE FAILED")
    sys.exit(1)
