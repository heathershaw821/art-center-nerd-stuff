
///////////////////////////////////////////////////////////////////////////////////////////////////////////
/// SERVO CONTROL

#include <Servo.h>

Servo myservo;  // create servo object to control the servo

int head_pos = 91;
int head_speed = 15;

void turn_head(int address, int speed) {  // address 0 - 180
  if (address > head_pos) {
    // look right
    for (int pos = head_pos; pos <= address; pos += 1) { // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservo.write(pos);                 // tell servo to go to position in variable 'pos'
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

void Head_Handler(void) {
  if (Serial.available() > 0) {
    String cmd = Serial.readString();   // read in head position from serial
    cmd.trim();                         // trim new lines, or extra crap at the end

    if (cmd.length() > 0) {     // if there is input
      head_pos = cmd.toInt();   // convert it to a number
      turn_head(head_pos, head_speed);  // and turn the head
    }
  }
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////
/// ULTRA SONIC SENSOR

#define TRIG_PIN A1
#define ECHO_PIN A0
int object_distance=0;

float checkdistance(void) {
  digitalWrite(TRIG_PIN, LOW);  // reset the trigger pin
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH); // send a pulse for 10 microseconds
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);  // stop the pulse
  
  float duration = pulseIn(ECHO_PIN, HIGH); // measure the time it takes for the pulse to come back
  float distance = (duration * 0.034) / 2;  // convert the duration from m/s to cm / ms 
                                            // We divide by half to measure just the return bit
  return distance;
}

void UltraSonic_Handler(void) {
  // get the distance from sensor and print it out
  object_distance = checkdistance();
  Serial.print("Distance:");
  Serial.print(object_distance);
  Serial.println("CM");
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////
/// IR Control

#include <IRremote.hpp>
#define IR_RECEIVE_PIN 12

#define IR_UP 0xB946FF00
#define IR_DOWN 0xEA15FF00

#define IR_LEFT 0xBB44FF00
#define IR_RIGHT 0xBC43FF00

#define IR_OK 0xBF40FF00

void IRremote_Handler(void) {
  // if data received, print it
  if (IrReceiver.decode()) {
    uint32_t data = IrReceiver.decodedIRData.decodedRawData;
    switch (data) {
      case IR_UP:
        Serial.println("UP");
        break;
      case IR_DOWN:
        Serial.println("DOWN");
        break;
      case IR_LEFT:
        Serial.println("LEFT");
        break;
      case IR_RIGHT:
        Serial.println("RIGHT");
        break;
      case IR_OK:
        Serial.println("STOP");
        break;
      default:
        Serial.println(data, HEX);
        break;
    }
    
    IrReceiver.resume(); // Enable receiving of the next value

    
  }
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////
/// MAIN PROGRAM

void setup(void) {
  // Initialize serial communication at 9600 baud rate
  Serial.begin(115200);

  myservo.attach(A2);         // attaches the servo on pin 9 to the servo object
  turn_head(head_pos, head_speed);    // center the head

  pinMode(TRIG_PIN, OUTPUT);  // set trigger pin to output
  pinMode(ECHO_PIN, INPUT);   // set echo pin to input

  IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK); // Start the receiver
}


void loop(void) {
  IRremote_Handler();
  //Head_Handler();
  //UltraSonic_Handler();
}
