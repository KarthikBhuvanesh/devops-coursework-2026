# Exercise 9: Jenkins Multi-Stage Pipeline

## Objective
Create a Jenkins Declarative Pipeline that builds, tests, deploys, launches, and verifies a sample Python Flask application.

## Tools and Technologies
- Jenkins 2.580.1
- Docker Desktop
- Git and GitHub
- Python 3
- Flask
- Jenkins Pipeline
- Python `unittest`

## Application
The Flask application exposes `/` and returns:

`Hello, Jenkins Multi-Stage Pipeline!`

The application dependencies are listed in `requirements.txt`, and `test_app.py` contains a unit test for the home route.

## Jenkins Configuration
- **Pipeline job:** `Python-MultiStage-Pipeline`
- **Build agent:** `exercise6-agent`
- **Repository:** `https://github.com/KarthikBhuvanesh/devops-coursework-2026.git`
- **Branch:** `main`
- **Pipeline definition:** Pipeline script from SCM
- **Script path:** `Exercise-09-Jenkins-Multi-Stage-Pipeline/Jenkinsfile`

## Pipeline Stages
1. **Build:** Create a Python virtual environment and install dependencies.
2. **Test:** Run the unit tests with Python `unittest`.
3. **Deploy:** Copy application files into `python-app-deploy`.
4. **Run Application:** Start the deployed Flask application and wait for it to respond.
5. **Test Application:** Send an HTTP request and validate the response.
6. **Post Actions:** Report the result and clean up the background application process.

## Local Verification
The application unit test was run locally and passed:

- Tests run: 1
- Result: `OK`

The Jenkins pipeline result will be documented after the first successful build.

## Evidence
The `evidence` directory will contain screenshots of the Jenkins pipeline configuration, stage results, and successful Console Output.

## Conclusion
This exercise demonstrates a multi-stage CI/CD workflow in Jenkins, including dependency installation, automated testing, mock deployment, application startup, and HTTP verification.
