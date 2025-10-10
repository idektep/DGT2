#include <WiFi.h>
#include <PubSubClient.h>

// ===== CONFIG: WiFi & MQTT =====
const char* WIFI_SSID     = "YOUR_WIFI_SSID";
const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";

const char* MQTT_SERVER   = "broker.emqx.io";
const int   MQTT_PORT     = 1883;
const char* MQTT_CLIENT_ID = "esp32-pubsub";

// ===== TOPIC CONFIG =====
const char* PUB_TOPIC = "_____/status"; 
const char* SUB_TOPICS[] = {
  "____/topic1",
  "____/topic2",
  "____/topic3"
};
const int NUM_TOPICS = sizeof(SUB_TOPICS) / sizeof(SUB_TOPICS[0]);

// ===== LED CONFIG =====
#define LED1_PIN 33
#define LED2_PIN 25
#define LED3_PIN 26

// ===== OBJECTS =====
WiFiClient espClient;
PubSubClient mqttClient(espClient);

// ===== SETUP =====
void setup() {
  Serial.begin(115200);

  // ตั้งค่า LED
  pinMode(LED1_PIN, OUTPUT);
  pinMode(LED2_PIN, OUTPUT);
  pinMode(LED3_PIN, OUTPUT);
  digitalWrite(LED1_PIN, LOW);
  digitalWrite(LED2_PIN, LOW);
  digitalWrite(LED3_PIN, LOW);

  connectWiFi();
  mqttClient.setServer(MQTT_SERVER, MQTT_PORT);
  mqttClient.setCallback(mqttCallback);
}

// ===== LOOP =====
void loop() {
  if (!mqttClient.connected()) {
    connectMQTT();
  }
  mqttClient.loop();
  publishMessage();
}

//////////////////////////////////////////////
// CONNECT WIFI
void connectWiFi() {
  Serial.print("Connecting to WiFi");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println("\nWiFi connected: " + WiFi.localIP().toString());
}

//////////////////////////////////////////////
// CONNECT MQTT
void connectMQTT() {
  while (!mqttClient.connected()) {
    Serial.print("Connecting to MQTT...");
    if (mqttClient.connect(MQTT_CLIENT_ID)) {
      Serial.println("Connected.");

      // Subscribe ทุก topic ที่ตั้งไว้
      for (int i = 0; i < NUM_TOPICS; i++) {
        mqttClient.subscribe(SUB_TOPICS[i]);
        Serial.println("Subscribed to: " + String(SUB_TOPICS[i]));
      }

    } else {
      Serial.printf("Failed (rc=%d). Retrying in 5s...\n", mqttClient.state());
      delay(5000);
    }
  }
}

//////////////////////////////////////////////
// PUBLISH MESSAGE ทุก 5 วินาที
void publishMessage() {
  static unsigned long last = 0;
  const unsigned long interval = 5000;
  if (millis() - last >= interval) {
    last = millis();

    String msg = "ESP32 is alive!";
    mqttClient.publish(PUB_TOPIC, msg.c_str());
    Serial.println("Published: " + msg);
  }
}

//////////////////////////////////////////////
// MQTT CALLBACK: รับข้อความจาก topic
void mqttCallback(char* topic, byte* payload, unsigned int length) {
  String msg;
  for (unsigned int i = 0; i < length; i++) {
    msg += (char)payload[i];
  }

  Serial.printf("Message on [%s]: %s\n", topic, msg.c_str());

  // ควบคุม LED ตาม topic
  if (strcmp(topic, "____/topic1") == 0) {
    digitalWrite(LED1_PIN, msg == "on" ? HIGH : LOW);
  } else if (strcmp(topic, "____/topic2") == 0) {
    digitalWrite(LED2_PIN, msg == "on" ? HIGH : LOW);
  } else if (strcmp(topic, "____/topic3") == 0) {
    digitalWrite(LED3_PIN, msg == "on" ? HIGH : LOW);
  }
}
