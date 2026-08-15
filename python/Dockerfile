# Gebruik een lichte, officiële Python image
FROM python:3.9-slim

# Maak een mapje aan in de container
WORKDIR /app

# Installeer de paho-mqtt bibliotheek
RUN pip install paho-mqtt

# Kopieer jouw script naar de container
COPY sensor_simulatie.py .

# Start het script als de container opstart
CMD ["python", "-u", "sensor_simulatie.py"]