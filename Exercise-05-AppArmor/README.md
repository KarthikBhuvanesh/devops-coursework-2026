# Exercise 5: Docker Security with AppArmor and Python

## Objective
Build a Flask application in Docker, use the Docker SDK for Python to configure and inspect container security options, and test restricted actions.

## Technologies
- Docker Desktop
- Python 3.11
- Flask 3.1.2
- Docker SDK for Python
- Ubuntu 24.04 on WSL2
- AppArmor

## Files
- `app.py` — Flask web application
- `Dockerfile` — Container image definition
- `requirements.txt` — Flask dependency
- `apply_apparmor.py` — Builds the image, attempts to start a container with the requested AppArmor profile, inspects security settings, and cleans up
- `test_restricted_actions.py` — Tests file reading and shell execution
- `evidence/` — Screenshots and supporting evidence

## Application
The Flask application listens on port 5000 and returns a confirmation message at `/`.

The image was built as `flask-apparmor` and tested successfully at `http://localhost:5002/`.

## Docker SDK
The Docker SDK successfully connected to Docker Desktop, built the image, started a test container, inspected its configuration, and cleaned up the container.

Docker reported these security options:
- `name=seccomp,profile=builtin`
- `name=cgroupns`

The requested `apparmor=my-apparmor-profile` option appeared in the container configuration, but the actual AppArmor profile was not reported.

## Restricted-Action Test Results

| Test | Observed result |
|---|---|
| Read `/etc/passwd` | Allowed; exit code 0 |
| Execute `/bin/bash` | Allowed; exit code 0 |
| Actual AppArmor profile | Not reported |

These tests did not demonstrate custom AppArmor enforcement. The results must not be interpreted as proof that the requested profile was active.

## Environment Limitation
Ubuntu 24.04 under WSL2 reported that the AppArmor module was loaded but the AppArmor filesystem was not mounted. The expected `/sys/kernel/security/apparmor` interface was unavailable.

Docker Desktop reported `seccomp` and `cgroupns` security options but no AppArmor option. Therefore, custom AppArmor policy enforcement could not be verified in this environment.

## Conclusion
The Flask container and Docker SDK workflow were tested successfully. However, the custom AppArmor enforcement requirement remains incomplete. A compatible Linux environment with a functioning AppArmor interface is needed to validate the restrictions.

## Questions and Answers

### 1. What is the purpose of AppArmor with Docker?
AppArmor adds mandatory access control to help confine processes and limit access to files, capabilities, and other system resources.

### 2. How do AppArmor profiles secure containers?
Profiles define permitted and denied operations for confined processes, reducing the impact of application compromise.

### 3. Why restrict `/etc/` and `/var/`?
These directories can contain system configuration, account information, logs, and application state. Limiting access reduces exposure and the risk of unauthorized changes.

### 4. What other capabilities can be restricted?
Depending on the profile and kernel support, policies can restrict file access, execution, network operations, capabilities, and other process behaviors.

### 5. How can you verify that a profile is applied?
Inspect the container's configured security options and check the actual process profile using host-side AppArmor tools. Confirm enforcement with controlled tests and relevant audit logs; a configuration string alone is insufficient.
