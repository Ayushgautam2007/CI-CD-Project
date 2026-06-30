# Flask Student Management Application

A Flask-based CRUD web application for managing student records using MongoDB Atlas.

This project demonstrates complete CI/CD implementation using both **Jenkins** and **GitHub Actions**.

---
# Combined Architecture of CI/CD Pipeline using Jenkins and Github Actions
                 Developer
                     │
                 Git Push
                     │
                     ▼
            GitHub Repository
             │              │
     Webhook │              │ GitHub Events
             ▼              ▼
         Jenkins      GitHub Actions
             │              │
        Build/Test/Deploy   │
             └──────┬────────┘
                    ▼
            Flask Application
                    │
                    ▼
          Notification / Deployment

# Tech Stack

- Python 3.9
- Flask
- MongoDB Atlas
- PyMongo
- Git & GitHub
- GitHub Actions
- Jenkins
- AWS EC2 (Amazon Linux 2023)
- Linux Shell

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
│
├── templates/
│     ├── index.html
│     ├── add.html
│     └── update.html
│
├── .github/
│    └── workflows/
│         └── ci-cd.yml
│
└── README.md
```

---

# Features

- Add Student
- Update Student
- Delete Student
- View Students
- MongoDB Atlas Integration
- Automated Testing
- CI/CD Pipeline
- Staging Deployment
- Production Deployment

---

# Clone Repository

```bash
git clone https://github.com/<your-username>/CI-CD-Project.git

cd CI-CD-Project
```

---

# Create Virtual Environment

Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```env
MONGO_URI=your_mongodb_connection_string

SECRET_KEY=your_secret_key
```

Example

```env
MONGO_URI=mongodb+srv://db_user:password@cluster.mongodb.net/mydb?retryWrites=true&w=majority

SECRET_KEY=flask_secret_key
```

---

# Run Application

```bash
python app.py
```

Application runs on

```
http://localhost:5000
```

---

# Run Tests

```bash
pytest -v
```

---

# Jenkins CI/CD Pipeline

## Objective

Automate Build, Test and Deployment using Jenkins.

---

## Jenkins Pipeline Stages

- Clone Repository
- Install Dependencies
- Run Unit Tests
- Code Quality Checks
- Build Application
- Deploy Application
- Email Notification

---

## Jenkins Plugins Used

- Git
- Pipeline
- Email Extension
- Workspace Cleanup

---

## Jenkins Credentials

### GitHub Credentials

```
github-creds
```

Contains

- GitHub Username
- GitHub Personal Access Token

---

### Gmail Credentials

```
gmail-creds
```

Used for Email Notification.

---

## Jenkins Environment Variables

```
MONGO_URI

SECRET_KEY
```

---

## Jenkins Build Trigger

Manual Build

or

GitHub Webhook

---

## Jenkins Deployment

Deploys Flask Application on AWS EC2 (Amazon Linux 2023)

---

# GitHub Actions CI/CD Pipeline

Workflow File

```
.github/workflows/ci-cd.yml
```

---

## Pipeline Triggers

### Push to Main

```
Build

Test
```

---

### Push to Staging

```
Build

Test

Deploy to Staging
```

---

### GitHub Release

```
Build

Test

Deploy to Production
```

---

# Workflow Jobs

## Build and Test

- Checkout Code
- Setup Python
- Install Dependencies
- Run Pytest
- Build Application

---

## Deploy to Staging

Runs only when

```
staging branch
```

Tasks

- Checkout Repository
- Load GitHub Secrets
- Deploy Flask Application

---

## Deploy to Production

Runs only when

```
GitHub Release is published
```

Tasks

- Checkout Repository
- Load Production Secrets
- Deploy Flask Application

---

# GitHub Secrets

## Repository Secrets

### Application

```
MONGO_URI

SECRET_KEY
```

---

### Staging

```
STAGING_HOST

STAGING_USER

DEPLOY_KEY

API_TOKEN
```

---

### Production

```
PROD_HOST

PROD_USER

PROD_DEPLOY_KEY

PROD_API_TOKEN
```

---

# Branch Strategy

```
main
```

Production-ready code

```
staging
```

Testing and validation before production

---

# Deployment Flow

```
Developer

↓

Push Code

↓

GitHub

↓

GitHub Actions

↓

Build

↓

Install Dependencies

↓

Run Tests

↓

If Success

↓

Deploy to Staging
```

After Release

```
GitHub Release

↓

GitHub Actions

↓

Production Deployment
```

---

# AWS Environment

Operating System

```
Amazon Linux 2023
```

Application Server

```
Flask
```

Database

```
MongoDB Atlas
```

---

# Security

Sensitive values are stored using GitHub Repository Secrets.

Examples

- MongoDB URI
- Secret Key
- API Tokens
- Deployment Keys
- Server Information

No credentials are stored inside the repository.

---

# Testing

Framework

```
pytest
```

Test Cases

- Home Page
- Add Student
- Update Student
- Delete Student

---

# Code Quality

Tools

- Black
- Bandit
- Pylint

---

# Continuous Integration

Every push automatically

- Installs dependencies
- Runs unit tests
- Validates build

---

# Continuous Deployment

### Staging

Automatic deployment after successful build from the **staging** branch.

### Production

Automatic deployment after publishing a **GitHub Release**.

---

# Screenshots

Include screenshots of

- Flask Application
- Jenkins Dashboard
- Jenkins Pipeline
- GitHub Actions Workflow
- Successful Build
- Successful Tests
- Staging Deployment
- Production Deployment
- MongoDB Atlas

---

# Author

**Ayush Gautam**

DevOps Engineer

GitHub

https://github.com/Ayushgautam2007

---

# License

This project is developed for educational and DevOps learning purposes.
