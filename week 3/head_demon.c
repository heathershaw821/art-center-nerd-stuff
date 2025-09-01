
#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int head_pos = 0;    // variable to store the servo position

void turn_head(int address, int speed) { // address 0 - 180
  if (address > head_pos) {
    // look right
    for (int pos = head_pos; pos <= address; pos += 1) { // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservo.write(pos);              // tell servo to go to position in variable 'pos'
      delay(speed);                       // waits 15ms for the servo to reach the position
    }
  } else {
    // look left
    for (int pos = head_pos; pos >= address; pos -= 1) { // goes from 180 degrees to 0 degrees
      myservo.write(pos);              // tell servo to go to position in variable 'pos'
      delay(speed);                       // waits 15ms for the servo to reach the position
    }
  }
}

void setup() {
  // Initialize serial communication at 9600 baud rate
  Serial.begin(9600);

  myservo.attach(A2);  // attaches the servo on pin 9 to the servo object

  turn_head((180/2)+1, 15);
}


void loop() {
  String cmd = Serial.readString();
  cmd.trim();
  if (cmd.length() > 0) {
    head_pos = cmd.toInt();
    turn_head(head_pos, 15);
  }
}
