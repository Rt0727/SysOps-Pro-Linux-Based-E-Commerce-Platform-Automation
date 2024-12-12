# SysOps Pro: Linux-Based E-Commerce Platform Automation

## Overview
This repository provides an automated setup for managing and maintaining a Linux-based e-commerce platform using Terraform and Docker. The project focuses on server automation, system performance monitoring, and automated backups for a PostgreSQL-powered e-commerce application hosted on an Ubuntu server.

## Features
- **Linux Server Setup**: Automates the creation and management of an Ubuntu server with necessary configurations for e-commerce hosting.
- **PostgreSQL Database**: Configured for local development, including performance tuning and automated backups.
- **E-Commerce Application**: Dockerized application for seamless deployment and scalability.
- **Server Maintenance**: Automates server maintenance tasks such as backups, log rotation, and software updates using Bash scripts and cron jobs.
- **Security Enhancements**: Configures security features like user permissions and intrusion prevention with **fail2ban**.
- **Performance Monitoring**: Tools such as **top** and **htop** are used for monitoring system performance and optimizing uptime.

## Technologies Used
- **Server**: Ubuntu Linux
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose
- **IaC**: Terraform
- **Automation**: Bash Scripts, Cron Jobs
- **Security**: fail2ban

## Prerequisites
- Install [Docker](https://www.docker.com/)
- Install [Terraform](https://www.terraform.io/)
- Install [Git](https://git-scm.com/)
- Basic knowledge of Bash scripting and system administration

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine and navigate into the directory:
```bash
git clone https://github.com/Rt0727/SysOps-Pro-Linux-Based-E-Commerce-Platform-Automation.git
cd SysOps Pro Linux-Based E-Commerce Platform Automation
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
3. **Server Access Issues**: Ensure SSH access to the server is configured correctly, and the firewall allows necessary connections.

### Logs
Access logs for debugging:
- Docker logs: Run `docker-compose logs`
- Server logs: Run `tail -f /var/log/syslog`

## Future Enhancements
- Implement more advanced monitoring and alerting for server performance.
- Integrate with cloud services like AWS or GCP for better scalability.
- Expand server automation to include more comprehensive security measures.

---

For any questions or issues, feel free to reach out at `rt07mahifan@gmail.com`.

---