#!/bin/bash

# Maak een backup map aan als deze nog niet bestaat
BACKUP_DIR="./backups"
mkdir -p "$BACKUP_DIR"

# Bepaal een timestamp (datum en tijd) voor de bestandsnaam
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/backup_$TIMESTAMP.tar.gz"

echo "📦 Start volledige backup van de Smart Sensor Gateway..."

# Comprimeer alle belangrijke data-mappen naar één backup archief
tar -czf "$BACKUP_FILE" ./influxdb/data ./portainer/data ./node-red/data ./mosquitto/config

echo "✅ Backup succesvol opgeslagen in: $BACKUP_FILE"