// code that is run once when the device is turned on
void setup() {
  // Initialize serial communication at 9600 baud rate
  Serial.begin(9600);
}

// this code is run repeatedly in a "loop"
void loop() {
  Serial.println("Hello World!");
  delay(1000);
}

