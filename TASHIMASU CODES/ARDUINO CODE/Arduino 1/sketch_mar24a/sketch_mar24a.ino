#include <Servo.h>
//#include "HX711.h"

//HX711 scale(A1, A0);
//float calibration_factor = -96650;
//float glasslimit = 150; //In grams
//loat currentweight;


//The sg90 servos for the head
Servo udservo;
Servo lrservo;
int servoudval = 90;
int servolrval = 90;

//For serial comm
char serialData;

//Robots main motor pins
int leftf = 5;
int leftb = 6;
int rightf = 9;
int rightb = 10;

//Pins for drink water pumps
int pump1f = 3;
int pump1b = 4;
int pump2f = 7;
int pump2b = 8;

String readString;

void setup() {
//Normal setup
  Serial.begin(9600);
  pinMode(leftf, OUTPUT);
  pinMode(leftb, OUTPUT);
  pinMode(rightf, OUTPUT);
  pinMode(rightb, OUTPUT);
  pinMode(pump1f, OUTPUT);
  pinMode(pump1b, OUTPUT);
  pinMode(pump2f, OUTPUT);
  pinMode(pump2b, OUTPUT);
  udservo.attach(11);
  lrservo.attach(12);
  udservo.write(servoudval);
  lrservo.write(servolrval);
//Setup for the scale
//  scale.set_scale(2280.f);
//  scale.tare();
}

void loop() {
  if (Serial.available() > 0) {
    serialData = Serial.read(); 
    //Serial.print(serialData);
//    Serial.println(scale.get_units());
    if (serialData == 'a') {
      forward();
    }
    else if (serialData == 'b') {
      backward();
    }
    else if (serialData == 'c') {
      left();
    }
    else if (serialData == 'd') {
      right();
    }
    else if (serialData == 'e') {
      leftp();
    }
    else if (serialData == 'f') {
      rightp();
    }
    else if (serialData == 'g') {
      stopp();
    }
    else if (serialData == 'h') {
      fillfrom1();
    }
    else if (serialData == 'i') {
      fillfrom2();
    }
    else if (serialData == 'j') {
      fillfrom12mix();
    }
    else if (serialData == 'K') {
      servou();
    }
    else if (serialData == 'k') {
      servod();
    }
    else if (serialData == 'L') {
      servol();
    }
    else if (serialData == 'l') {
      servor();
    }
    else if (serialData == 'Z') {
      servoudmid();
    }
    else if (serialData == 'z') {
      servolrmid();
    }
    else if (serialData == 'm') {
      stopfilling();
    }
    else if (serialData == 'o') {
      cleanpump1();
    }
    else if (serialData == 'p') {
      cleanpump2();
    }
    else if (serialData == 'r') {
      cleanpump12();
    }
  }
}

void forward() {
  digitalWrite(leftf, HIGH);
  digitalWrite(leftb, LOW);
  digitalWrite(rightf, HIGH);
  digitalWrite(rightb, LOW);
}
void backward() {
  digitalWrite(leftf, LOW);
  digitalWrite(leftb, HIGH);
  digitalWrite(rightf, LOW);
  digitalWrite(rightb, HIGH);
}
void left() {
  digitalWrite(leftf, LOW);
  digitalWrite(leftb, HIGH);
  digitalWrite(rightf, HIGH);
  digitalWrite(rightb, LOW);
}
void right() {
  digitalWrite(leftf, HIGH);
  digitalWrite(leftb, LOW);
  digitalWrite(rightf, LOW);
  digitalWrite(rightb, HIGH);
}
void leftp() {
  digitalWrite(leftf, LOW);
  digitalWrite(leftb, LOW);
  digitalWrite(rightf, HIGH);
  digitalWrite(rightb, LOW);
}
void rightp() {
  digitalWrite(leftf, HIGH);
  digitalWrite(leftb, LOW);
  digitalWrite(rightf, LOW);
  digitalWrite(rightb, LOW);
}
void stopp() {
  digitalWrite(leftf, LOW);
  digitalWrite(leftb, LOW);
  digitalWrite(rightf, LOW);
  digitalWrite(rightb, LOW);
}

void fillfrom1() {
  digitalWrite(pump1f, HIGH);
}

void fillfrom2() {
  digitalWrite(pump2f, HIGH);
}

void fillfrom12mix() {
  digitalWrite(pump1f, HIGH);
  digitalWrite(pump2f, HIGH);
}

void stopfilling() {
  digitalWrite(pump1f, LOW);
  digitalWrite(pump2f, LOW);
  digitalWrite(pump1b, LOW);
  digitalWrite(pump2b, LOW);
}

void cleanpump1() {
  digitalWrite(pump1b, HIGH);
}
void cleanpump2() {
  digitalWrite(pump2b, HIGH);
}
void cleanpump12() {
  digitalWrite(pump1b, HIGH);
  digitalWrite(pump2b, HIGH);
}

/*
void fillfrom1s() {
  digitalWrite(pump1f, LOW);
  //Read the current weight
  currentweight = scale.get_units();
  //Start the pump
  while (currentweight < glasslimit) {
    digitalWrite(pump1f, HIGH);
    currentweight = scale.get_units();
  }
  digitalWrite(pump1f, LOW);
}
void fillfrom2s() {
  digitalWrite(pump2f, LOW);
  //Read the current weight
  currentweight = scale.get_units();
  //Start the pump
  while (currentweight < glasslimit) {
    digitalWrite(pump2f, HIGH);
    currentweight = scale.get_units();
  }
  digitalWrite(pump2f, LOW);
}
void fillfrom12mixs() {
  digitalWrite(pump1f, LOW);
  digitalWrite(pump2f, LOW);
  //Read the current weight
  currentweight = scale.get_units();
  //Start the pump
  while (currentweight < glasslimit) {
    digitalWrite(pump1f, HIGH);
    digitalWrite(pump2f, HIGH);
    currentweight = scale.get_units();
  }
  digitalWrite(pump1f, LOW);
  digitalWrite(pump2f, LOW);
}
*/

void servou() {
  delay(10);
  servoudval = servoudval - 10;
  udservo.write(servoudval);
}

void servod() {
  delay(10);
  servoudval = servoudval + 10;
  udservo.write(servoudval);
}

void servol() {
  delay(10);
  servolrval = servolrval + 10;
  lrservo.write(servolrval);
}

void servor() {
  delay(10);
  servolrval = servolrval - 10;
  lrservo.write(servolrval);
}

void servoudmid() {
  delay(10);
  servoudval = 90;
  udservo.write(servoudval);
}

void servolrmid() {
  delay(10);
  servolrval = 90;
  lrservo.write(servolrval);
}
