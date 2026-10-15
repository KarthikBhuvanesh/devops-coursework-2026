# Exercise 6: Grafana Real-Time Monitoring of a Quick-Commerce Application

## Objective
Build a simulated delivery metrics application and monitor it with Prometheus and Grafana, configure alert rules, and validate the project using a Jenkins CI pipeline.

## Architecture
- **Python application:** Generates simulated delivery metrics.
- **Prometheus:** Scrapes application metrics every 5 seconds and evaluates alert rules.
- **Grafana:** Displays real-time delivery metrics in a dashboard.
- **Jenkins:** Checks out the GitHub repository and validates project files, expected metrics, and alert rules.

## Metrics
The application exposes Prometheus metrics on port 8000:
- `total_deliveries`
- `pending_deliveries`
- `on_the_way_deliveries`
- `average_delivery_time` (Summary metric)

## Prometheus
Prometheus runs on port 9090 and scrapes:
- Its own metrics endpoint.
- `delivery-metrics:8000/metrics` over the Docker bridge network.

Alert rules are defined in `alert_rules.yml`:
- `HighPendingDeliveries`: triggers when pending deliveries exceed 10 for 15 seconds.
- `HighAverageDeliveryTime`: triggers when average delivery time exceeds 30 seconds for 15 seconds.

## Grafana
Grafana runs on port 3000 and uses Prometheus as its data source. The dashboard **Quick Commerce Real-Time Monitoring** includes:
- Total Deliveries
- Pending Deliveries
- Deliveries On The Way
- Average Delivery Time

The dashboard refreshes every 5 seconds.

## Jenkins CI Pipeline
Jenkins LTS runs on port 8080 with persistent storage. The job `delivery-metrics-pipeline`:
1. Checks out the repository's `main` branch.
2. Verifies that required project files exist.
3. Checks for expected Prometheus metrics and alert rules in the source and configuration files.

Jenkins Build #2 completed successfully. The pipeline performs source and configuration checks; it does not currently compile Python, run automated application tests, or build Docker images.

## Environment
Implemented on Windows using Docker Desktop. The monitoring components communicate over a custom Docker bridge network named `monitoring-net`.

The metrics are simulated for demonstration and are not production delivery data.

## Evidence
The `evidence/` directory contains screenshots of:
- Grafana dashboard
- Prometheus target health
- Prometheus alert states
- Successful Jenkins build
- Jenkins pipeline stages
