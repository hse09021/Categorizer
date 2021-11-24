#include <Servo.h>

Servo classifier;
Servo lift;

int data;

void setup() {
  Serial.begin(9600);
  classifier.attach(9);
  lift.attach(8);
  lift.write(90);
  classifier.write(90);
}

void loop() {

  while (Serial.available()) {
    data = Serial.read();
  
    if (data == '0') {
      classifier.write(117);
      delay(1000);
      lift.write(40);
      delay(6000);
      classifier.write(90);
      delay(1000);
      lift.write(90);
      delay(1000);

    }

    else if (data == '1') {
      classifier.write(55);
      delay(1000);
      lift.write(40);
      delay(6000);
      classifier.write(90);
      delay(1000);
      lift.write(90);
      delay(1000);

    }
  }
}
