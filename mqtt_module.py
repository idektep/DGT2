# mqtt_module.py
import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, broker, port, topics, on_message_callback):
        self.client = mqtt.Client()
        self.broker = broker
        self.port = port
        self.topics = topics

        self.client.on_connect = self.on_connect
        self.client.on_message = on_message_callback

    def on_connect(self, client, userdata, flags, rc):
        print("✅ Connected to MQTT broker with code", rc)
        for topic in self.topics:
            client.subscribe(topic)
            print(f"📡 Subscribed to topic: {topic}")

    def start(self):
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_forever()
