// Include the Encoder library
#include <Encoder.h>

// Define the pins for the encoder
#define ENCODER_A_PIN 2
#define ENCODER_B_PIN 3
#define IN1 6 //D6
#define IN2 7 //D7
#define ENA A3
const int TRESH = 6000;
// Create an Encoder object
Encoder myEncoder(ENCODER_A_PIN, ENCODER_B_PIN);

void kick(){
  Serial.println(myEncoder.read());
  if(myEncoder.read() < TRESH){
    analogWrite(ENA, 250);
    digitalWrite(IN1,1);
    digitalWrite(IN2,0);
  }
  else{
    analogWrite(ENA, 0);
  }
}

void setup() {
  // Initialize Serial communication
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(ENA,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  kick();
}
