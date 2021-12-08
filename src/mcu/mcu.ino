#include <Servo.h>

Servo door;
Servo lift;

int data;

void setup() {
  Serial.begin(9600);
  door.attach(9);
  lift.attach(8);
  lift.write(90);
  door.write(90);
}

void loop() {

  while (Serial.available()) {
    data = Serial.read();
  
    if (data == '0') {
      door.write(117);
      delay(1000);
      lift.write(40);
      delay(6000);
      door.write(90);
      delay(1000);
      lift.write(90);
      delay(1000);
    }

    else if (data == '1') {
      door.write(55);
      delay(1000);
      lift.write(40);
      delay(6000);
      door.write(90);
      delay(1000);
      lift.write(90);
      delay(1000);
    }
  }
}
