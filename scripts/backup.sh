#!/bin/bash

# Define backup location and date format
BACKUP_DIR="./backups"
DATE=$(date +\%Y-\%m-\%d_\%H-\%M-\%S)
BACKUP_FILE="$BACKUP_DIR/ecommerce-server-backup-$DATE.tar.gz"

# Create backup directory if not exists
mkdir -p $BACKUP_DIR

# Backup the entire server file system (excluding unnecessary directories)
tar -czf $BACKUP_FILE --exclude=$BACKUP_DIR /etc /var /home /usr

echo "Backup completed: $BACKUP_FILE"
