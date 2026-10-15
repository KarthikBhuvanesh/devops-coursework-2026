# Exercise 6: Grafana Real-Time Monitoring of a Quick-Commerce Application

## Objective

Build a simulated delivery-metrics application, monitor it with Prometheus and Grafana, configure alert rules, and validate the application and monitoring configuration through a Jenkins CI pipeline.

## Architecture

- **Python application:** Generates simulated delivery metrics and exposes them on port 8000.
- **Prometheus:** Scrapes application metrics every 5 seconds and evaluates alert rules.
- **Grafana:** Displays real-time delivery metrics in a dashboard.
- **Jenkins:** Checks out the GitHub repository and runs Python syntax validation, monitoring-configuration checks, a Docker image build, and a container smoke test.

## Metrics

The application exposes Prometheus metrics on port 8000:

- `total_deliveries`
- `pending_deliveries`
- `on_the_way_deliveries`
- `average_delivery_time` (Summary metric, represented by its `_sum` and `_count` series)

## Prometheus

Prometheus runs on port 9090 and scrapes:

- Its own metrics endpoint.
- `delivery-metrics:8000` over the `monitoring-net` Docker bridge network.

Alert rules are defined in `alert_rules.yml`:

- **HighPendingDeliveries:** Triggers when pending deliveries exceed 10 for 15 seconds.
- **HighAverageDeliveryTime:** Triggers when average delivery time exceeds 30 seconds for 15 seconds.

## Grafana

Grafana runs on port 3000 and uses Prometheus as its data source. The **Quick Commerce Real-Time Monitoring** dashboard includes:

- Total Deliveries
- Pending Deliveries
- Deliveries On The Way
- Average Delivery Time

The dashboard refreshes every 5 seconds.

## Jenkins CI Pipeline

Jenkins LTS runs on port 8080 with persistent storage. The job is named `delivery-metrics-pipeline`, checks out the repository's `main` branch, and runs on the `exercise6-agent` node.

The pipeline contains these stages:

1. **Checkout:** Checks out the repository from GitHub.
2. **Validate Python:** Prints the Python version and runs `python3 -m py_compile delivery_metrics.py test_metrics.py` to validate Python syntax.
3. **Validate Monitoring Configuration:** Checks that the Prometheus target `delivery-metrics:8000`, both alert-rule names, and the expected delivery metric names are present in the relevant files.
4. **Build Docker Image:** Builds the application image from the Exercise 6 Dockerfile and tags it as `delivery-metrics:ci`.
5. **Container Smoke Test:** Starts a temporary application container on the existing `monitoring-net` network, waits for its `/metrics` endpoint, verifies an HTTP 200 response, and checks for the expected metric series. A cleanup trap removes the temporary test container without deleting the shared monitoring network.
6. **Pipeline Complete:** Reports completion when all preceding stages pass.

### Successful Jenkins Run

Jenkins build **#8** completed successfully in approximately **7.4 seconds**, using commit `cb339d1` (`Fix Jenkins smoke test shared network`).

The successful run confirms that repository checkout, Python syntax validation, monitoring-configuration checks, Docker image building, and the container smoke test all passed.

**Testing note:** The pipeline syntax-checks `test_metrics.py` but does not execute it as a separate test suite. The smoke test independently verifies the running container's metrics endpoint and expected metric series.

## Environment

Implemented on Windows using Docker Desktop. The monitoring components and CI smoke-test container use the custom Docker bridge network `monitoring-net`.

The metrics are simulated for demonstration and are not production delivery data.

## Evidence

The `evidence/` directory contains screenshots of:

- Grafana dashboard
- Prometheus target health
- Prometheus alert states
- Successful Jenkins build
- Jenkins pipeline stages and console output showing the successful validation and smoke-test stages
