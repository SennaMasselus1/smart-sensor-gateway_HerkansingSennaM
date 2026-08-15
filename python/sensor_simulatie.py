import paho.mqtt.client as mqtt
import time
import json
import random

# MQTT Broker configuratie
BROKER = "mqtt-broker"
PORT = 1883
TOPIC_JOYSTICK = "sensor/joystick"
TOPIC_KNOP = "sensor/knop"

client = mqtt.Client()

def stuur_sensor_data():
    try:
        client.connect(BROKER, PORT, 60)
        print("Verbonden met MQTT Broker. Start met verzenden van data...")
        
        while True:
            # Genereer gesimuleerde joystick data (x en y waarden tussen -100 en 100)
            joystick_data = {
                "x": random.randint(-100, 100),
                "y": random.randint(-100, 100)
            }
            
            # Genereer gesimuleerde knop data (0 = losgelaten, 1 = ingedrukt)
            knop_data = {
                "status": random.choice([0, 1])
            }
            
            # Stuur de data (gepubliceerd als JSON strings)
            client.publish(TOPIC_JOYSTICK, json.dumps(joystick_data))
            client.publish(TOPIC_KNOP, json.dumps(knop_data))
            
            print(f"Verzonden -> Joystick: {joystick_data} | Knop: {knop_data}")
            
            time.sleep(2) # Wacht 2 seconden voor de volgende meting
            
    except Exception as e:
        print(f"Fout bij verbinden met broker: {e}")

if __name__ == "__main__":
    stuur_sensor_data()