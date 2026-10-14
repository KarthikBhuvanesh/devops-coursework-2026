# Exercise 4: Docker Networking

## Objective
Create a custom Docker bridge network connecting a Flask REST API, MySQL, and Redis containers.

## Technologies
- Docker and custom bridge networking
- Python 3.11
- Flask 3.1.2
- MySQL 8.4
- Redis 7

## Architecture
All three containers run on the custom Docker bridge network `my-bridge-net`.

| Container | Purpose | Port |
|---|---|---|
| flask | Flask REST API | 5001 |
| mysql | MySQL database | 3306 |
| redis | Redis service | 6379 |

The Flask API is published on host port 5001. Docker's embedded DNS allows containers on the same custom bridge network to resolve each other by container name.

## API Endpoints

### GET /about
Returns the API name, version, and description.

### GET /health
Returns the API health status.

## Verification
- Tested the `/about` endpoint successfully.
- Tested the `/health` endpoint successfully.
- Verified MySQL hostname resolution from the Flask container.
- Verified Redis hostname resolution from the Flask container.
- Confirmed TCP connectivity from Flask to MySQL on port 3306.
- Confirmed TCP connectivity from Flask to Redis on port 6379.
- Inspected `my-bridge-net` and confirmed all three containers were attached.

## Evidence
See the `evidence/` directory for screenshots of the API response and networking verification.

## Build the Flask Image
Run from this directory:

```bash
docker build -t flask-api:1.0 .
```

## Recreate the Environment
Create the network:

```bash
docker network create --driver bridge my-bridge-net
```

Start MySQL and Redis:

```bash
docker run -d --name mysql --network my-bridge-net -e MYSQL_ROOT_PASSWORD=<your-password> -e MYSQL_DATABASE=devopsdb mysql:8.4
docker run -d --name redis --network my-bridge-net redis:7
```

Start Flask:

```bash
docker run -d --name flask --network my-bridge-net -p 5001:5001 flask-api:1.0
```

Test the API at `http://localhost:5001/about` and `http://localhost:5001/health`.

**Security note:** Replace `<your-password>` with a secure password. Do not commit real credentials to version control.
