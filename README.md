# Jenkins CI/CD Pipeline for Flask Application

## Objective

The objective of this project is to implement a Continuous Integration and Continuous Deployment (CI/CD) pipeline using Jenkins for a Python Flask web application. The pipeline automates the process of building, testing, and deploying the application whenever changes are pushed to the GitHub repository.

---

# Project Architecture

```
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Webhook
    │
    ▼
Jenkins Pipeline
    │
    ├── Build
    ├── Test
    └── Deploy
    │
    ▼
Flask Application (Staging Environment)
```

---

# Technologies Used

* Jenkins
* Python 3.9
* Flask
* Git
* GitHub
* Pytest
* Linux (RHEL/Amazon Linux)
* Shell Script

---

# Prerequisites

The following software must be installed before configuring the pipeline:

* Jenkins
* Java 21
* Python 3.9+
* pip
* Git
* pytest
* GitHub Account

Verify the installation using:

```bash
python3 --version
pip3 --version
pytest --version
git --version
java -version
jenkins --version
```

---

# Project Structure

```
CI-CD-Project/
│
├── app.py
├── requirements.txt
├── test_app.py
├── start_flask.sh
├── Jenkinsfile
├── README.md
├── LICENSE
└── templates/
```

---

# Jenkins Pipeline

The pipeline is defined inside the `Jenkinsfile` located in the root directory of the project.

It consists of three stages:

## Stage 1: Build

The Build stage installs all required Python dependencies.

Commands executed:

```bash
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
```

---

## Stage 2: Test

The Test stage runs unit tests using Pytest.

Command:

```bash
pytest -v
```

If any test fails, the pipeline stops and the deployment stage is skipped.

---

## Stage 3: Deploy

The Deploy stage deploys the application to the staging environment using the deployment script.

Commands:

```bash
chmod +x start_flask.sh
./start_flask.sh
```

---

# Jenkins Job Configuration

1. Create a new Pipeline Job in Jenkins.
2. Select **Pipeline script from SCM**.
3. Choose **Git** as the SCM.
4. Enter the GitHub repository URL.
5. Select the `main` branch.
6. Set the Script Path to:

```
Jenkinsfile
```

7. Save the job.
8. Click **Build Now** to execute the pipeline.

---

# GitHub Integration

The source code is hosted on GitHub.

After cloning the repository to the Jenkins server:

```bash
git clone <repository-url>
```

The Jenkins Pipeline automatically pulls the latest code from the repository.

---

# Automatic Build Trigger

GitHub Webhook is configured to trigger Jenkins automatically whenever changes are pushed to the `main` branch.

Webhook URL:

```
http://<JENKINS_SERVER_IP>:8080/github-webhook/
```

This enables automatic execution of the CI/CD pipeline.

---

# Email Notification

Jenkins is configured to send email notifications for both successful and failed builds.

Configuration:

* SMTP Server
* Gmail App Password
* Email Notification Plugin

Notifications are sent after every pipeline execution.

---

# Running the Pipeline

Push the latest code to GitHub:

```bash
git add .
git commit -m "Updated Jenkins Pipeline"
git push origin main
```

The pipeline automatically performs:

1. Build
2. Test
3. Deploy

---

# Pipeline Flow

```
GitHub Push
      │
      ▼
Jenkins Trigger
      │
      ▼
Checkout Source Code
      │
      ▼
Build
      │
      ▼
Test
      │
      ▼
Deploy
      │
      ▼
Application Running
```

---

# Expected Output

The Jenkins pipeline executes successfully with the following stages:

* Build ✔
* Test ✔
* Deploy ✔

The Flask application is deployed successfully to the staging environment.

---

# Screenshots

Include the following screenshots in the repository or submission:

* Jenkins Dashboard
* Pipeline Job Configuration
* GitHub Webhook Configuration
* Build Stage
* Test Stage
* Deploy Stage
* Stage View
* Console Output
* Successful Build Status

---

# Repository URL

Replace the URL below with your GitHub repository URL.

```
https://github.com/<your-github-username>/<repository-name>
```

---
