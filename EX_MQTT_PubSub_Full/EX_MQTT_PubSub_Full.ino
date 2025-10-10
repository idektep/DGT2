#include <WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"

// ======= Pin Definitions =======
#define LDR_PIN    34
#define DHTPIN     23
#define DHTTYPE    DHT22
#define LED1_PIN   33
#define LED2_PIN   25
#define LED3_PIN   26

// ======= WiFi & MQTT Config =======
const char* WIFI_SSID     = "YOUR_WIFI_SSID";
const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";

const char* MQTT_SERVER   = "broker.emqx.io";
const int   MQTT_PORT     = 1883;
const char* MQTT_CLIENT_ID = "esp32_device_01";

// ======= MQTT Topics =======
const char* PUB_TOPIC_LDR    = "______/sensor/ldr";
const char* PUB_TOPIC_TEMP   = "______/sensor/temp";
const char* PUB_TOPIC_HUMID  = "______/sensor/humid";
const char* PUB_TOPIC_STATUS = "______/status";

const char* SUB_TOPICS[] = {
  "____/control/led1",
  "____/control/led2",
  "____/control/led3"
};
const int NUM_TOPICS = sizeof(SUB_TOPICS) / sizeof(SUB_TOPICS[0]);

// ======= Global Objects =======
WiFiClient espClient;
PubSubClient mqttClient(espClient);
DHT dht(DHTPIN, DHTTYPE);

// ======= Setup =======
void setup() {
  Serial.begin(115200);

  // Sensor and LED setup
  pinMode(LDR_PIN, INPUT);
  pinMode(LED1_PIN, OUTPUT);
  pinMode(LED2_PIN, OUTPUT);
  pinMode(LED3_PIN, OUTPUT);
  digitalWrite(LED1_PIN, LOW);
  digitalWrite(LED2_PIN, LOW);
  digitalWrite(LED3_PIN, LOW);
  dht.begin();

  connectWiFi();
  mqttClient.setServer(MQTT_SERVER, MQTT_PORT);
  mqttClient.setCallback(mqttCallback);
}

// ======= Loop =======
void loop() {
  if (!mqttClient.connected()) {
    connectMQTT();
  }
  mqttClient.loop();

  publishSensorData();
  publishHeartbeat();
}

/////////////////////// FUNCTIONS ///////////////////////

// Connect WiFi
void connectWiFi() {
  Serial.print("Connecting to WiFi");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println("\nWiFi connected: " + WiFi.localIP().toString());
}

// Connect MQTT
void connectMQTT() {
  while (!mqttClient.connected()) {
    Serial.print("Connecting to MQTT...");
    if (mqttClient.connect(MQTT_CLIENT_ID)) {
      Serial.println("Connected.");
      for (int i = 0; i < NUM_TOPICS; i++) {
        mqttClient.subscribe(SUB_TOPICS[i]);
        Serial.println("Subscribed to: " + String(SUB_TOPICS[i]));
      }
    } else {
      Serial.printf("Failed (rc=%d). Retrying...\n", mqttClient.state());
      delay(5000);
    }
  }
}

// Callback: Handle MQTT messages
void mqttCallback(char* topic, byte* payload, unsigned int length) {
  String msg;
  for (unsigned int i = 0; i < length; i++) {
    msg += (char)payload[i];
  }
  Serial.printf("Message on [%s]: %s\n", topic, msg.c_str());

  // LED control based on topic
  if (strcmp(topic, "_____/control/led1") == 0) {
    digitalWrite(LED1_PIN, msg == "on" ? HIGH : LOW);
  } else if (strcmp(topic, "_____/control/led2") == 0) {
    digitalWrite(LED2_PIN, msg == "on" ? HIGH : LOW);
  } else if (strcmp(topic, "_____/control/led3") == 0) {
    digitalWrite(LED3_PIN, msg == "on" ? HIGH : LOW);
  }
}

// Publish Sensor Data
void publishSensorData() {
  static unsigned long lastSensorMillis = 0;
  const unsigned long interval = 1000;
  if (millis() - lastSensorMillis >= interval) {
    lastSensorMillis = millis();

    // LDR
    int ldr = analogRead(LDR_PIN);
    mqttClient.publish(PUB_TOPIC_LDR, String(ldr).c_str());
    Serial.println("LDR: " + String(ldr));

    // DHT22
    float temp = dht.readTemperature();
    float humid = dht.readHumidity();
    if (!isnan(temp)) {
      mqttClient.publish(PUB_TOPIC_TEMP, String(temp, 2).c_str());
      Serial.println("Temp: " + String(temp, 2));
    }
    if (!isnan(humid)) {
      mqttClient.publish(PUB_TOPIC_HUMID, String(humid, 2).c_str());
      Serial.println("Humid: " + String(humid, 2));
    }

    Serial.println("-----------------------------");
  }
}

// Publish Heartbeat
void publishHeartbeat() {
  static unsigned long lastHeartbeat = 0;
  const unsigned long hbInterval = 10000; // ทุก 15 วิ
  if (millis() - lastHeartbeat >= hbInterval) {
    lastHeartbeat = millis();
    String msg = "ESP32 is alive!";
    mqttClient.publish(PUB_TOPIC_STATUS, msg.c_str());
    Serial.println("Published heartbeat: " + msg);
  }
}
