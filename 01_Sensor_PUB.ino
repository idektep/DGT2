#include <WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"

// ---------- Config ----------
#define DHTPIN 23
#define DHTTYPE DHT22

const char* WIFI_SSID = "#######";
const char* WIFI_PASSWORD = "#######";
const char* MQTT_SERVER = "broker.emqx.io";
const int   MQTT_PORT = 1883;
const char* MQTT_CLIENT_ID = "#######";

// ---------- MQTT Topic ----------
const char* TOPIC_TEMP = "sensor/temp";

// ---------- Global ----------
WiFiClient espClient;
PubSubClient mqttClient(espClient);
DHT dht(DHTPIN, DHTTYPE);

// ---------- Setup ----------
void setup() {
  Serial.begin(115200);

  dht.begin();

  connectWiFi();
  mqttClient.setServer(MQTT_SERVER, MQTT_PORT);
}

// ---------- Main Loop ----------
void loop() {
  if (!mqttClient.connected()) {
    connectMQTT();
  }
  mqttClient.loop();
  publishSensorData();
}

// ---------- Function: Connect WiFi ----------
void connectWiFi() {
  Serial.print("Connecting to WiFi");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println("\nWiFi connected: " + WiFi.localIP().toString());
}

// ---------- Function: Connect MQTT ----------
void connectMQTT() {
  while (!mqttClient.connected()) {
    Serial.print("Connecting to MQTT...");
    if (mqttClient.connect(MQTT_CLIENT_ID)) {
      Serial.println("Connected.");
    } else {
      Serial.printf("Failed (rc=%d). Retrying...\n", mqttClient.state());
      delay(5000);
    }
  }
}

// ---------- Function: Publish Temperature ----------
void publishSensorData() {
  static unsigned long lastMillis = 0;
  const unsigned long interval = 5000;

  if (millis() - lastMillis >= interval) {
    lastMillis = millis();

    float temp = dht.readTemperature();

    if (!isnan(temp)) {
      String tempStr = String(temp, 2);
      mqttClient.publish(TOPIC_TEMP, tempStr.c_str());
      Serial.println("Temp: " + tempStr + " C");
    }

    Serial.println("-----------------------------");
  }
}