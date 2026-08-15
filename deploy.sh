#!/bin/bash

echo "🚀 Start met de automatische deployment van de Smart Sensor Gateway..."

echo "📥 Controleren op updates..."

echo "🛑 Oude containers stoppen..."
docker compose down

echo "🏗️ Nieuwe stack bouwen en opstarten..."
docker compose up -d --build

echo "✅ Deployment succesvol! Hier is de status van je containers:"
docker compose ps