#!/bin/bash

# Update system packages
sudo apt update && sudo apt upgrade -y

# Clean up old system logs
sudo rm -rf /var/log/*.log

# Clean up unnecessary files
sudo apt autoremove -y

# Restart the server
sudo reboot

echo "Maintenance tasks completed."
