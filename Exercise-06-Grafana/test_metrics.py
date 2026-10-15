import time
import urllib.request

BASE_URL = "http://127.0.0.1:8000"

def fetch_metrics():
    with urllib.request.urlopen(
        f"{BASE_URL}/metrics", timeout=5
    ) as response:
        assert response.status == 200
        return response.read().decode("utf-8")

metrics = fetch_metrics()

required_metrics = [
    "total_deliveries ",
    "pending_deliveries ",
    "on_the_way_deliveries ",
    "average_delivery_time_count ",
    "average_delivery_time_sum ",
]

for metric in required_metrics:
    assert metric in metrics, f"Missing metric: {metric}"

print("PASS: All expected metrics are exposed.")

for _ in range(3):
    time.sleep(2)
    metrics = fetch_metrics()
    assert "pending_deliveries " in metrics

print("PASS: Metrics endpoint remains available.")
