#include <WiFi.h>
#include <PubSubClient.h>

// WiFi & MQTT Config
const char* WIFI_SSID = "YOUR_WIFI_SSID";
const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";
const char* MQTT_SERVER = "broker.emqx.io";
const int   MQTT_PORT = 1883;
const char* MQTT_CLIENT_ID = "DEVICE_NAME";


WiFiClient espClient;
PubSubClient mqttClient(espClient);


void setup() {
  Serial.begin(115200);
  connectWiFi();
  mqttClient.setServer(MQTT_SERVER, MQTT_PORT);
}


void loop() {
  if (!mqttClient.connected()) {
    connectMQTT();
  }
  mqttClient.loop();
  publishMessage();
}

//////////////////////////////////////////////////Function/////////////////////////////////////////////////////////////////
// WiFi Connect
void connectWiFi() {
  Serial.print("Connecting to WiFi");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println("\nWiFi connected: " + WiFi.localIP().toString());
}


// MQTT Connect
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


// Publish every 5 sec
void publishMessage() {
  static unsigned long last = 0;
  const unsigned long interval = 5000;
  if (millis() - last >= interval) {
    last = millis();
    String msg = "Hello from publisher!";
    mqttClient.publish("TOPIC NAME", msg.c_str());
    Serial.println("Published: " + msg);
  }
}
