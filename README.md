````markdown
# DevSecOps Pipeline with GitHub Actions & AWS

A security-focused DevSecOps simulation project built as part of the Cyber Agoge Bootcamp.

This project demonstrates how automated security testing can be integrated into a CI/CD pipeline to identify vulnerabilities in application code, open-source dependencies, Infrastructure as Code, secrets, and container images.

> **Educational lab:** The application and infrastructure contain intentional security weaknesses so that the security tools have findings to detect.

## Scenario

NexusCore Technologies is a simulated fintech company looking to introduce security earlier into its software development lifecycle.

The goal of this project is to implement an automated DevSecOps pipeline that performs multiple security checks whenever code is pushed or a pull request is created.

## Pipeline Architecture

```text
Developer Push / Pull Request
        |
        v
GitHub Actions
        |
        +--> CodeQL SAST
        |
        +--> Trivy SCA
        |
        +--> Trivy IaC Scanning
        |
        +--> Gitleaks Secret Detection
        |
        +--> Docker Build
                |
                v
        Trivy Container Scan
                |
                v
        Security Scan Summary
````

## Security Tools

| Tool           | Purpose                                    |
| -------------- | ------------------------------------------ |
| CodeQL         | Static Application Security Testing (SAST) |
| Trivy          | Dependency / Software Composition Analysis |
| Trivy          | Terraform Infrastructure as Code scanning  |
| Gitleaks       | Secret detection                           |
| Docker         | Container image creation                   |
| Trivy          | Container vulnerability scanning           |
| GitHub Actions | CI/CD automation                           |

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── devsecops-pipeline.yml
├── src/
│   └── vulnerable_app.py
├── terraform/
│   └── main.tf
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md
```

## Intentional Application Security Issues

The Flask application contains deliberately insecure code for security testing, including examples of:

* hardcoded secrets
* SQL injection
* command injection
* server-side template injection
* insecure data handling
* path traversal
* Flask debug mode enabled

These issues are included only for educational security scanning.

## Intentional Infrastructure Misconfigurations

The Terraform configuration contains intentionally insecure AWS settings, including:

* disabled S3 public access protections
* unrestricted security group rules using `0.0.0.0/0`
* an EC2 instance with a public IP
* an unencrypted root volume
* a hardcoded password in EC2 user data

The infrastructure is intended to be scanned by Trivy and is not intended for production deployment.

## CI/CD Security Pipeline

The GitHub Actions workflow performs the following stages:

1. **SAST - CodeQL**

   * Analyses Python source code for security vulnerabilities.

2. **SCA - Trivy**

   * Scans project dependencies for known vulnerabilities.

3. **IaC Security - Trivy**

   * Analyses Terraform configuration for cloud security misconfigurations.

4. **Secret Detection - Gitleaks**

   * Scans source files and Git history for exposed secrets.

5. **Container Security - Trivy**

   * Builds the Docker image and scans it for known vulnerabilities.

6. **Security Summary**

   * Displays the result of each security job in the GitHub Actions workflow summary.

## DevSecOps Concepts Demonstrated

This project demonstrates:

* shift-left security
* automated security testing
* Static Application Security Testing
* Software Composition Analysis
* Infrastructure as Code security scanning
* secret detection
* container security
* CI/CD security automation
* GitHub Code Scanning integration

## Important

This repository intentionally contains vulnerable code and insecure infrastructure configurations for training purposes.

Do not deploy the Terraform infrastructure or use the application in a production environment.

```
```
