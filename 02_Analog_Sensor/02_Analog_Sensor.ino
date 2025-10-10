#define LDR_pin 34
int ldr=0;
void setup() {
  Serial.begin(9600);
  pinMode(LDR_pin, INPUT);
}
void loop() {
  ldr=analogRead(LDR_pin);
  Serial.println(ldr);
}