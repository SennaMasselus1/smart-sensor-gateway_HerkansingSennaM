
## Run Locally

Clone het project.

```bash
  git clone https://github.com/SennaMasselus1/smart-sensor-gateway_HerkansingSennaM.git
```

Open de hoofdmap.

```bash
  smart-sensor-gateway
```

Pas naam aan file gegevens, in het echt zou je de wachtwoorden/usernames via mail krijgen.

```bash
  .env.example -> .env
```

Open Windows Powershell in de hoofdmap, en start de stack.

```bash
  docker-compose up -d --build
  of bash deploy.sh
```
Het systeem bouwt nu de Python-sensor container en start alle benodigde services (Mosquitto, Node-RED, InfluxDB, Portainer).

## Links Webinterfaces
Zodra de containers actief zijn, kun je via de browser toegang krijgen tot de volgende diensten:
* Node-RED: http://localhost:1880
* InfluxDB: http://localhost:8086
* Portainer: http://localhost:9000




