# Exercise 8: Jenkins Hello World Job

## Objective
Create a Jenkins Freestyle project that retrieves source code from GitHub, executes a shell script, and displays the expected output.

## Tools and Technologies
- Jenkins 2.580.1
- Docker Desktop
- Git and GitHub
- Bash shell

## Source Code

The script `hello-world.sh` is stored in this exercise directory.

```bash
#!/bin/bash
echo "Hello, Jenkins!"
```

## Jenkins Job Configuration
- **Job name:** `HelloWorld`
- **Job type:** Freestyle project
- **Source Code Management:** Git
- **Repository:** `https://github.com/KarthikBhuvanesh/devops-coursework-2026.git`
- **Branch:** `main`
- **Build agent:** `exercise6-agent`
- **Build step:** Execute shell

The build step changes to the Exercise 8 directory and runs `hello-world.sh`.

## Procedure
1. Created `hello-world.sh`.
2. Added the script to the coursework GitHub repository.
3. Created a Jenkins Freestyle project named `HelloWorld`.
4. Configured Jenkins to clone the `main` branch of the repository.
5. Restricted the job to the `exercise6-agent` node.
6. Configured the shell build step to execute the script.
7. Ran the job and inspected its Console Output.

## Evidence
The `evidence` directory contains screenshots documenting the Jenkins job and its execution.

## Result
The Jenkins `HelloWorld` job completed successfully and printed:

`Hello, Jenkins!`

The build finished with status `SUCCESS`.

## Conclusion
This exercise demonstrates how a Jenkins Freestyle project retrieves source code from GitHub, executes a shell script on a configured agent, and reports the build result.
