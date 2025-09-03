
///////////////////////////////////////////////////////////////////////////////////////////////////////////
/// SERVO CONTROL

#include <Servo.h>

Servo myservo;  // create servo object to control the servo

int head_pos = 91;
int head_speed = 15;

void Head_Turn(int address, int speed) {  // address 0 - 180
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
      Head_Turn(head_pos, head_speed);  // and turn the head
    }
  }
}

void Head_Setup(void) {
  myservo.attach(A2);         // attaches the servo on pin 9 to the servo object
  Head_Turn(head_pos, head_speed);    // center the head
}


///////////////////////////////////////////////////////////////////////////////////////////////////////////
/// Motor Control

// Speed Control Pins
#define LEFT_PWM_PIN  5     // ENA of motor driver board
#define RIGHT_PWM_PIN  6    // ENB of motor driver board

// Turning Control Pins
#define LEFT_IN1_PIN 2     // IN1 of motor driver board
#define LEFT_IN2_PIN 4     // IN2 of motor driver board
#define RIGHT_IN3_PIN 7    // IN3 of motor driver board
#define RIGHT_IN4_PIN 8    // IN4 of motor driver board

bool Is_Moving = false;

void Motor_Setup(void) {
  pinMode(LEFT_IN1_PIN, OUTPUT);
  pinMode(LEFT_IN2_PIN, OUTPUT);
  pinMode(RIGHT_IN3_PIN, OUTPUT);
  pinMode(RIGHT_IN4_PIN, OUTPUT);
  pinMode(LEFT_PWM_PIN, OUTPUT);
  pinMode(RIGHT_PWM_PIN, OUTPUT);
}

void Motor_Forward(unsigned char speed) {
  Is_Moving = true;
  
  digitalWrite(RIGHT_IN3_PIN, HIGH); 
  digitalWrite(RIGHT_IN4_PIN, LOW);
  digitalWrite(LEFT_IN1_PIN, HIGH);
  digitalWrite(LEFT_IN2_PIN, LOW);
  analogWrite(LEFT_PWM_PIN, speed);
  analogWrite(RIGHT_PWM_PIN, speed);
}

void Motor_Backward(unsigned char speed) {
  Is_Moving = true;
  
  digitalWrite(RIGHT_IN3_PIN, LOW);  
  digitalWrite(RIGHT_IN4_PIN, HIGH);
  digitalWrite(LEFT_IN1_PIN, LOW);  
  digitalWrite(LEFT_IN2_PIN, HIGH);
  analogWrite(LEFT_PWM_PIN, speed);
  analogWrite(RIGHT_PWM_PIN, speed);
}

void Motor_Rotate_Left(unsigned char speed) {
  Is_Moving = true;
  
  digitalWrite(RIGHT_IN3_PIN, HIGH);
  digitalWrite(RIGHT_IN4_PIN, LOW );  
  digitalWrite(LEFT_IN1_PIN, LOW); 
  digitalWrite(LEFT_IN2_PIN, HIGH);
  analogWrite(LEFT_PWM_PIN, speed);
  analogWrite(RIGHT_PWM_PIN, speed);
}

void Motor_Rotate_Right(unsigned char speed) {
  Is_Moving = true;
  
  digitalWrite(RIGHT_IN3_PIN, LOW);  
  digitalWrite(RIGHT_IN4_PIN, HIGH);
  digitalWrite(LEFT_IN1_PIN, HIGH);
  digitalWrite(LEFT_IN2_PIN, LOW);  
  analogWrite(LEFT_PWM_PIN, speed);
  analogWrite(RIGHT_PWM_PIN, speed);
}

void Motor_Stop(void) {
  Is_Moving = false;
  
  digitalWrite(RIGHT_IN3_PIN, HIGH);
  digitalWrite(RIGHT_IN4_PIN, HIGH);
  digitalWrite(LEFT_IN1_PIN, HIGH);
  digitalWrite(LEFT_IN2_PIN, HIGH);
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
        Motor_Forward(150);
        break;
      case IR_DOWN:
        Serial.println("DOWN");
        Motor_Backward(150);
        break;
      case IR_LEFT:
        Serial.println("LEFT");
        Motor_Rotate_Left(100);
        break;
      case IR_RIGHT:
        Serial.println("RIGHT");
        Motor_Rotate_Right(100);
        break;
      case IR_OK:
        Serial.println("STOP");
        Motor_Stop();
        break;
      default:
        // Serial.println(data, HEX);
        break;
    }
    
    IrReceiver.resume(); // Enable receiving of the next value

    
  }
}

void IRremote_Setup(void) {
  IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK); // Start the receiver
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////
/// ULTRA SONIC SENSOR

#define TRIG_PIN A1
#define ECHO_PIN A0

float checkdistance(void) {
  digitalWrite(TRIG_PIN, LOW);  // reset the trigger pin
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH); // send a pulse for 10 microseconds
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);  // stop the pulse
  
  float duration = pulseIn(ECHO_PIN, HIGH, 30000); // measure the time it takes for the pulse to come back
  float distance = (duration * 0.0343) / 2;  // convert the duration from m/s to cm / ms 
                                            // We divide by half to measure just the return bit
  return distance;
}

void UltraSonic_Handler(void) {
  // get the distance from sensor and print it out
  int object_distance=0;
  object_distance = checkdistance();
  
  if (object_distance != 0) {
    Serial.print("Distance:");
    Serial.print(object_distance);
    Serial.println("CM");

    if (object_distance <= 5) {
      Motor_Backward(200);
      delay(800);
      Motor_Stop();
    }
  }
}

void UltraSonic_Setup(void) {
  pinMode(TRIG_PIN, OUTPUT);  // set trigger pin to output
  pinMode(ECHO_PIN, INPUT);   // set echo pin to input

  delay(50);  // give sensor 50ms to settle
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////
/// MAIN PROGRAM

void setup(void) {
  // Initialize serial communication at 9600 baud rate
  Serial.begin(115200);
  Head_Setup();
  UltraSonic_Setup();
  IRremote_Setup();
  Motor_Setup();
}


void loop(void) {
  Head_Handler();
  UltraSonic_Handler();
  IRremote_Handler();
}
