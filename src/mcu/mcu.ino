#include <Servo.h>

Servo servo;
Servo lift;

int data;

void setup() {
  Serial.begin(9600);
  servo.attach(9);
  lift.attach(8);
  lift.write(90);
  servo.write(90);
}

void loop() {

  while (Serial.available()) {
    data = Serial.read();
  
  if (data == '0') {
    servo.write(117);
    delay(1000);
    lift.write(40);
    delay(6000);
    servo.write(90);
    delay(1000);
    lift.write(90);
    delay(1000);
    
  }

  else if (data == '1') {
    servo.write(55);
    delay(1000);
    lift.write(40);
    delay(6000);
    servo.write(90);
    delay(1000);
    lift.write(90);
    delay(1000);
    
  }
  }
}
