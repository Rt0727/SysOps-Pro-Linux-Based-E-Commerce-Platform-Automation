# SysOps Pro: Linux-Based E-Commerce Platform Automation

## Overview
This repository provides an automated setup for managing and maintaining a Linux-based e-commerce platform using Terraform, Docker, and Python-based monitoring and server management tools. The project focuses on server automation, system performance monitoring, automated backups, and log analysis for a PostgreSQL-powered e-commerce application hosted on an Ubuntu server.

## Features
- **Linux Server Setup**: Automates the creation and management of an Ubuntu server with necessary configurations for e-commerce hosting.
- **PostgreSQL Database**: Configured for local development, including performance tuning and automated backups.
- **E-Commerce Application**: Dockerized application for seamless deployment and scalability.
- **Server Maintenance**: Automates server maintenance tasks such as backups, log rotation, and software updates using Bash scripts and cron jobs.
- **Security Enhancements**: Configures security features like user permissions and intrusion prevention with **fail2ban**.
- **Performance Monitoring**: Python-based tools for monitoring the e-commerce application, analyzing server logs, and performing server management tasks.
- **Log Analysis**: Python script to analyze server logs for insights into system performance.

## Technologies Used
- **Server**: Ubuntu Linux
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose
- **IaC**: Terraform
- **Automation**: Bash Scripts, Cron Jobs, Python
- **Security**: fail2ban

  ## 🛠️ Technologies Used

| Technology        | Purpose                               |
|-------------------|---------------------------------------|
| **PostgreSQL**    | Database for library data            |
| **Docker**        | Containerization                     |
| **Terraform**     | Infrastructure provisioning          |
| **Bash Scripts**  | Automation of routine tasks          |
| **Ubuntu Linux**  | Server                               |
| **Security**      | fail2ban                             |

---

## Prerequisites
- Install [Docker](https://www.docker.com/)
- Install [Terraform](https://www.terraform.io/)
- Install [Git](https://git-scm.com/)
- Install [Python 3](https://www.python.org/)
- Install necessary Python libraries with `pip install -r requirements.txt`
- Basic knowledge of Bash scripting and system administration

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine and navigate into the directory:
```bash
git clone https://github.com/Rt0727/SysOps-Pro-Linux-Based-E-Commerce-Platform-Automation.git
cd SysOps-Pro-Linux-Based-E-Commerce-Platform-Automation
```

### 2. Configure Terraform Variables
Create a `.tfvars` file in the `terraform/` directory with the following contents:
```hcl
server_ip    = "your-server-ip"
server_user  = "ubuntu"
db_username  = "ecommerce_user"
db_password  = "password"
db_name      = "ecommerce_db"
```

### 3. Initialize and Deploy Infrastructure
Use Terraform to initialize and deploy the necessary infrastructure:
```bash
cd terraform
terraform init
terraform apply -var-file="variables.tfvars"
```
This will set up a Linux server and deploy the necessary resources for the e-commerce platform, including the PostgreSQL database and Docker containers.

### 4. Build and Start Docker Containers
Navigate back to the root directory and build the Docker containers:
```bash
docker-compose up --build
```
This will:
- Build the Docker image for the e-commerce application.
- Start the PostgreSQL and application containers.

### 5. Server Maintenance Automation
To automate server maintenance tasks such as backups and updates, use the provided scripts:

#### Run Backup Script
```bash
./scripts/backup.sh
```
This script creates a backup of the PostgreSQL database to ensure data safety.

#### Run Maintenance Script
```bash
./scripts/maintenance.sh
```
This script automates regular maintenance tasks such as software updates and log rotation.

### 6. Security Enhancements
Configure fail2ban for intrusion prevention and secure the server by adjusting user permissions. For example:
```bash
sudo ufw allow ssh
sudo ufw enable
```
This will enable firewall rules and set up basic security measures.

### 7. Python-Based Monitoring and Management

#### Server Management
Run the `server_manager.py` script to perform various server management operations such as checking server health and performing basic server configurations:
```bash
python3 python/server_manager.py
```

#### Application Monitoring
Run the `app_monitor.py` script to monitor the e-commerce application and report any performance issues:
```bash
python3 python/app_monitor.py
```

#### Log Analysis
Run the `log_analyzer.py` script to analyze server logs and gain insights into system performance and potential issues:
```bash
python3 python/log_analyzer.py
```

### 8. Unit Tests for Python Modules
To test the Python modules, run the following unit tests:
```bash
python3 -m unittest discover python/tests
```
This will run all the unit tests in the `tests/` folder, ensuring the reliability of the server management, application monitoring, and log analysis scripts.

## Project Structure
```plaintext
linux-system-admin-ecommerce-setup/
│
├── terraform/
│   ├── main.tf                    # Defines infrastructure resources for server and PostgreSQL
│   ├── variables.tf               # Contains variables for server and database setup
│   └── outputs.tf                 # Outputs server IP, database credentials
│
├── docker/
│   ├── Dockerfile                 # Dockerfile for e-commerce app
│   └── docker-compose.yml         # Docker Compose file for local dev setup
│
├── python/
│   ├── server_manager.py         # Python module for server management
│   ├── app_monitor.py            # Script for monitoring the e-commerce application
│   ├── log_analyzer.py           # Analyzes server logs for insights
│   └── tests/
│       ├── test_server_manager.py # Unit tests for server management module
│       ├── test_app_monitor.py    # Unit tests for app monitoring script
│       └── test_log_analyzer.py   # Unit tests for log analysis module
│
├── scripts/
│   ├── backup.sh                  # Backup script for PostgreSQL
│   └── maintenance.sh             # Automated server maintenance script
│
├── README.md                      # Documentation
└── .gitignore                     # Git ignore file
```

## Troubleshooting

### Common Issues
1. **Terraform Errors**: Ensure Terraform is installed and that the `variables.tfvars` file is correctly configured.
2. **Docker Issues**: Verify that Docker is running and that the containers are properly built.
3. **Python Errors**: Make sure Python and necessary libraries are installed. You can install dependencies using `pip install -r requirements.txt`.
4. **Server Access Issues**: Ensure SSH access to the server is configured correctly, and the firewall allows necessary connections.

### Logs
Access logs for debugging:
- Docker logs: Run `docker-compose logs`
- Server logs: Run `tail -f /var/log/syslog`

## Future Enhancements
- Implement more advanced monitoring and alerting for server performance.
- Integrate with cloud services like AWS or GCP for better scalability.
- Expand server automation to include more comprehensive security measures.

```

For any questions or issues, feel free to reach out at `rt07mahifan@gmail.com`.

---
