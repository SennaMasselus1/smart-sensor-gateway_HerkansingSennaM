# Smart Sensor Gateway
Dit project is een volledig geautomatiseerde, containerized IoT-oplossing (Internet of Things) ontworpen voor het verzamelen, verwerken en visualiseren van sensordata. Het geheel is opgebouwd met Docker Compose zodat het met één enkel commando volledig operationeel is.

## Systeemarchitectuur
De applicatie maakt gebruik van een microservices-architectuur waarbij elke component in een afgesloten Docker-container draait binnen een privé netwerk (`sensor_net`).

### Componenten
1. **Sensor Simulator (python):** Genereert gesimuleerde sensorwaarden en publiceert deze periodiek via het MQTT-protocol.
2. **MQTT broker (Mosquitto):** Ontvangt alle berichten van de sensor en fungeert als centrale berichtenbus (pub/sub).
3. **Node-RED:** Abonneert zich op de MQTT-broker, verwerkt de inkomende data en stuurt deze door naar het dashboard.
4. **InfluxDB:** Een high-performance tijdsreeksdatabase (time-series database) die geoptimaliseerd is voor het opslaan en bevragen van sensorhistorie.
5. **Portainer:** Biedt een webinterface voor het monitoren en beheren van alle actieve Docker-containers.

## Run Locally
Clone het project.
```bash
  git clone https://github.com/SennaMasselus1/smart-sensor-gateway_HerkansingSennaM.git
  cd smart-sensor-gateway_HerkansingSennaM
```

Kopieer het voorbeeld-configuratiebestand om je eigen omgevingsvariabelen in te stellen.
```bash
  cp .env.example .env
```

Open een terminal in de hoofdmap en start de containers via het deployment-script of direct met Docker Compose:
```bash
  docker-compose up -d --build
  of bash deploy.sh
```
Het systeem bouwt nu automatisch de Python-sensorcontainer en start Mosquitto, Node-RED, InfluxDB en Portainer.

## Werking en Dataflow
De werking van het systeem verloopt in een continue, geautomatiseerde cyclus:
1. Data Generatie: De Python-container start automatisch op en stuurt continu meetwaarden naar de Mosquitto MQTT broker.
2. Verwerking: Node-RED luistert mee op de juiste MQTT-topic, vangt het bericht op, valideert het en brengt via de InfluxDB-node een verbinding tot stand met de database.
3. Opslag: De data wordt weggeschreven naar de bucket sensordata binnen InfluxDB.
4. Visualisatie: InfluxDB dashboard je kan hier de live de data bekijken, gemiddelde (1h) en gemiddelde (24h).

## Links Webinterfaces
Zodra de containers actief zijn, kun je via de browser toegang krijgen tot de volgende diensten:
* Node-RED: http://localhost:1880
* InfluxDB: http://localhost:8086
* Portainer: http://localhost:9000

## Shellscript & CI/CD PipeLine Automatisering
### Het Shellscript ('deploy.sh')
Het meegeleverde script 'deploy.sh' automatiseert het volledige deploymentproces lokaal. Het script voert achtereenvolgens de volgende acties uit:
1. **'docker compose pull'**: Controleert en downloadt eventuele updates van de gebruikte Docker images (zoals InfluxDB en Node-RED).
2. **'docker compose down'**: Stopt en ruimt de oude containers netjes op.
3. **'docker compose up -d --build'**: Herbouwt de Python-sensorcontainer (zodat eventuele codewijzigingen direct worden doorgevoerd) en start de volledige stack in de achtergrond.
4. **'docker compose ps'**: Toont direct een overzicht van de actieve containers en hun status.

**Hoe deployen** (getest met bash deploy.sh Windows)
```bash
  chmod +x deploy.sh
  ./deploy.sh
```

### Automatisering in een echte CI/CD Pipeline
Hoewel we dit project nu lokaal starten door handmatig `./deploy.sh` uit te voeren, zou dit in een professionele productie-omgeving volledig geautomatiseerd worden met een CI/CD-tool (Continuous Integration & Continuous Deployment), zoals **GitHub Actions** of **GitLab CI**.

In een geautomatiseerde pipeline neemt een server het handwerk over. De flow ziet er dan als volgt uit:
1. **Code Push:** Een developer past de code aan (bijvoorbeeld een wijziging in de Python-sensor of Node-RED configuratie) en pusht dit naar de `main`-branch op GitHub.
2. **Trigger:** De CI/CD-tool detecteert de wijziging en start automatisch een deployment-workflow.
3. **Serververbinding:** De pipeline maakt via een beveiligde SSH-verbinding contact met de productieserver.
4. **Code Update & Deploy:** De pipeline voert automatisch een `git pull` uit om de nieuwste code op te halen, en roept daarna direct ons `./deploy.sh` script aan.
5. **Zero-Touch Update:** Het deployment-script herbouwt de gewijzigde containers en herstart de services. Het systeem is geüpdatet zonder dat een beheerder zelf hoefde in te loggen op de server.

## BONUS Backup-script
Dit script pakt de volumes in en slaat ze op als een gecomprimeerd `.tar.gz` archief in de map `./backups`.

**Uitvoeren van een backup:** (getest met bash backup.sh Windows)
```bash
  chmod +x backup.sh
  ./backup.sh
```

## Poorten
| Service | Poort | Beschrijving / URL |
| :--- | :--- | :--- |
| **Node-RED** | `1880` | [http://localhost:1880](http://localhost:1880) *(Dataflows & Logica)* |
| **InfluxDB** | `8086` | [http://localhost:8086](http://localhost:8086) *(Database & Dashboard)* |
| **Portainer** | `9000` | [http://localhost:9000](http://localhost:9000) *(Container Management)* |
| **MQTT Broker (Mosquitto)** | `1883` | MQTT Client verbindingen |
| **MQTT Broker (Websocket)** | `9001` | MQTT over WebSockets |

## Foto's
Node-RED flow:
 * <img width="929" height="165" alt="image" src="https://github.com/user-attachments/assets/9d60ee43-3bf0-4a4b-9e23-b062ef367b60" />

Node-RED debug:
 * <img width="226" height="148" alt="image" src="https://github.com/user-attachments/assets/32c5bccc-a315-41b3-be19-645937b8933c" />

InfluxDB dashboard:
 * <img width="1791" height="536" alt="image" src="https://github.com/user-attachments/assets/cb461f2f-14ac-482a-ba68-7cb7c083fcf9" />

Portainer:
 * <img width="1586" height="337" alt="image" src="https://github.com/user-attachments/assets/1772dd67-03b9-4166-9a6d-b202c03e5615" />

MQTT Explorer:
 * <img width="202" height="52" alt="image" src="https://github.com/user-attachments/assets/1209b6ef-5834-49b7-9de2-c636bae4babc" />

## Reflectie
Voor deze herkansing heb ik het Smart Sensor Gateway project volledig opnieuw opgebouwd. 

**Wat ging goed?**
Het opzetten van het Docker Compose-bestand verliep heel goed. Daarnaast heb ik de Node-RED flow vlot kunnen uitwerken en kon ik zonder problemen een stabiele verbinding met InfluxDB tot stand brengen.

**Waar liep ik tegenaan? (Uitdagingen)**
Tijdens het schrijven van de automatiseringsscripts (`deploy.sh` en `backup.sh`) liep ik tegen een typisch cross-platform probleem aan. Omdat ik op Windows ontwikkelde, kregen mijn bash-scripts automatisch CRLF (Windows) line-endings in plaats van LF (Linux). Hierdoor faalde het script in eerste instantie. Door dit te debuggen en de line-endings aan te passen, heb ik geleerd hoe belangrijk het is om rekening te houden met het besturingssysteem waarop je code uiteindelijk draait.

**Wat heb ik geleerd?**
Deze herkansing heeft mijn inzicht in CloudComputing-principes enorm vergroot. Bij het maken van het back-upscript dacht ik in eerste instantie alleen aan de database (InfluxDB). Toen ik kritischer ging nadenken, realiseerde ik me dat de visuele logica (Node-RED flows) en de broker-configuraties (Mosquitto) net zo cruciaal zijn om het systeem na een crash volledig te kunnen herstellen. Ook begrijp ik nu veel beter hoe lokale bash-scripts de fundering vormen voor grotere, geautomatiseerde CI/CD pipelines.

**Conclusie**
Ik kijk met een goed gevoel terug op dit project. Het systeem werkt naar behoren en ik heb hier veel door bijgeleerd.
