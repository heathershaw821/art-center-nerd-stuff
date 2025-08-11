
void setup() {
  // Initialize serial communication at 9600 baud rate
  Serial.begin(9600);
}


bool is_even(int n) {
  if (n % 2 == 0)
    return true;
  else
    return false;
}

void loop() {
  if ( is_even(8) ) {
    Serial.println("yay its even!");
  }
  Serial.println("Hello World!");
  delay(1000);
}

