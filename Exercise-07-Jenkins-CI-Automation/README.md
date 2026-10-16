# Exercise 7: Jenkins CI Automation

## Objective
Understand Continuous Integration (CI) and explore Jenkins as an automation server for software development workflows.

## Tools and Technologies
- Jenkins 2.580.1
- Docker Desktop
- Docker containers
- Git and GitHub

## Environment Setup
The existing Jenkins installation from Exercise 6 was reused to avoid creating a duplicate server and to preserve the existing configuration.

- **Jenkins URL:** http://localhost:8080
- **Jenkins controller container:** `jenkins`
- **Jenkins agent:** `exercise6-agent`
- **Jenkins agent status:** Online
- **Existing CI pipeline:** `delivery-metrics-pipeline`

## Procedure
1. Started the existing Jenkins controller container.
2. Verified that the Jenkins dashboard was accessible through the browser.
3. Opened **Manage Jenkins → Nodes** to inspect the available execution nodes.
4. Started the dedicated Jenkins agent container.
5. Verified that `exercise6-agent` was online and communicating with the Jenkins controller.
6. Inspected the existing `delivery-metrics-pipeline` job and its build history.

## Evidence
The `evidence` directory contains the following screenshots:

- `Jenkins Dashboard.png` — Jenkins dashboard and job listing.
- `Jenkins nodes.png` — Jenkins nodes and agent status.
- `Build History.png` — Existing pipeline build history.
- `Successful Build.png` — Successful pipeline build.

## Result
The Jenkins controller was accessible, and the dedicated Jenkins agent was online. The existing CI pipeline and its previous successful build were visible in Jenkins.

## Conclusion
This exercise demonstrates the initial setup and inspection of Jenkins, a CI automation server. The existing Docker-based Jenkins environment provides a foundation for exploring automated build and integration workflows.
