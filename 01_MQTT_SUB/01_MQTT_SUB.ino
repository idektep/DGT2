#include <WiFi.h>
#include <PubSubClient.h>

// ===== CONFIG: WiFi & MQTT =====
const char* WIFI_SSID     = "YOUR_WIFI_SSID";
const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";

const char* MQTT_SERVER   = "broker.emqx.io";
const int   MQTT_PORT     = 1883;
const char* MQTT_CLIENT_ID = "esp32-sub-multi";

// ===== TOPIC LIST =====
const char* SUB_TOPICS[] = {
  "test/topic1",
  "test/topic2",
  "test/topic3"
};
const int NUM_TOPICS = sizeof(SUB_TOPICS) / sizeof(SUB_TOPICS[0]);

// ===== OBJECTS =====
WiFiClient espClient;
PubSubClient mqttClient(espClient);


// ===== SETUP =====
void setup() {
  Serial.begin(115200);
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
}


// ===== CONNECT WIFI =====
void connectWiFi() {
  Serial.print("Connecting to WiFi");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println("\nWiFi connected: " + WiFi.localIP().toString());
}

// ===== MQTT CALLBACK =====
void mqttCallback(char* topic, byte* payload, unsigned int length) {
  String msg;
  for (unsigned int i = 0; i < length; i++) {
    msg += (char)payload[i];
  }

  Serial.printf("Message on [%s]: %s\n", topic, msg.c_str());

  // === ตรวจสอบ topic ที่รับมา ===
  if (strcmp(topic, "test/topic1") == 0) {
    Serial.println("topic1");
    // ใส่โค้ดควบคุม LED ได้ที่นี่
  } else if (strcmp(topic, "test/topic2") == 0) {
    Serial.println("topic2");
  } else if (strcmp(topic, "test/topic3") == 0) {
    Serial.println("topic3");
  } else {
    Serial.println("-> Topic N/A");
  }
}

// ===== CONNECT MQTT =====
void connectMQTT() {
  while (!mqttClient.connected()) {
    Serial.print("Connecting to MQTT...");
    if (mqttClient.connect(MQTT_CLIENT_ID)) {
      Serial.println("Connected.");

      // Subscribe หลาย topic ด้วย for loop
      for (int i = 0; i < NUM_TOPICS; i++) {
        mqttClient.subscribe(SUB_TOPICS[i]);
        Serial.println("Subscribed to: " + String(SUB_TOPICS[i]));
      }

    } else {
      Serial.printf("Failed (rc=%d), retrying in 5s...\n", mqttClient.state());
      delay(5000);
    }
  }
}