#include <Servo.h>

Servo myservo;  // create servo object to control a servo

// Define the pin for the interrupt
const int interruptPin = 2;

int count = 0;

bool endReached = 0;

void setup() {
  Serial.begin(9600);
  myservo.attach(7);  // attaches the servo on pin 9 to the servo object
  // Initialize the interrupt pin as input
  pinMode(interruptPin, INPUT);
  
   // Attach interrupt to the interrupt pin
  // Arguments: interrupt number, ISR function, mode (RISING)
  attachInterrupt(digitalPinToInterrupt(interruptPin), trigger_kicker, RISING);
  
}

void loop() {
  // if(endReached){
    myservo.write(89);
  // }
  // else{
  //   myservo.write(0);
  //   // delay(2000);
  //   endReached = 0; 
  // }
  Serial.println(endReached); 
}

void trigger_kicker(){
  endReached = 1;  
}

void serialEvent() {  
  while (Serial.available()) {
    String receivedChar = Serial.readString();
    if (receivedChar.startsWith("Tigo")) {
      myservo.write(0);
      delay(600);
      myservo.write(89);
    }
  }
}

