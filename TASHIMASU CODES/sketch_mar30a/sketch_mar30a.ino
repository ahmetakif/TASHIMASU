//Led strip libraries
#include "Adafruit_WS2801.h"
#include "SPI.h"
#ifdef __AVR_ATtiny85__
#include <avr/power.h>
#endif

//Led strip cableary
uint8_t dataPin  = 3;
uint8_t clockPin = 2;
Adafruit_WS2801 strip = Adafruit_WS2801(30, dataPin, clockPin);

//Distance sensor shit
const int trigf = 10;
const int echof = 11;
const int trigb = 4;
const int echob = 5;
const int trigl = 8;
const int echol = 9;
const int trigr = 6;
const int echor = 7;
long durationf;
long durationb;
long durationl;
long durationr;
int distancef;
int distanceb;
int distancel;
int distancer;

int sttf;
int stff;
int th;

//Color Randomizer
int cr = 0;
int cg = 0;
int cb = 0;

//For serial comm
char serialData;

void setup() {
  //Distance sensors setup
  pinMode(trigf, OUTPUT);
  pinMode(echof, INPUT);
  pinMode(trigb, OUTPUT);
  pinMode(echob, INPUT);
  pinMode(trigl, OUTPUT);
  pinMode(echol, INPUT);
  pinMode(trigr, OUTPUT);
  pinMode(echor, INPUT);
  //Serial communicaton setup
  Serial.begin(9600);
  //Led strip setup
  #if defined(__AVR_ATtiny85__) && (F_CPU == 16000000L)
    clock_prescale_set(clock_div_1); // Enable 16 MHz on Trinket
  #endif
  strip.begin();
  // Update LED contents, to start they are all 'off'
  strip.show();
}

void loop() {
  if (Serial.available() > 0) {
    serialData = Serial.read();
    //Serial.print(serialData);
    if (serialData == 'a') {
      measuref();
    }
    else if (serialData == 'b') {
      measureb();
    }
    else if (serialData == 'c') {
      measurel();
    }
    else if (serialData == 'd') {
      measurer();
    }
    else if (serialData == 'e') {
      fan();
    }
    else if (serialData == 'f') {
      ban();
    }
    else if (serialData == 'g') {
      lan();
    }
    else if (serialData == 'h') {
      ran();
    }
    else if (serialData == 'i') {
      lpan();
    }
    else if (serialData == 'j') {
      rpan();
    }
    else if (serialData == 'D') {
      disco(20, 1000);
    }
  }
}

//Distance measuring functions
void measuref() {
  digitalWrite(trigf, LOW);
  delayMicroseconds(2);
  digitalWrite(trigf, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigf, LOW);
  durationf = pulseIn(echof, HIGH);
  distancef = durationf*0.034/2;
  Serial.println(distancef);
}
void measureb() {
  digitalWrite(trigb, LOW);
  delayMicroseconds(2);
  digitalWrite(trigb, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigb, LOW);
  durationb = pulseIn(echob, HIGH);
  distanceb = durationb*0.034/2;
  Serial.println(distanceb);
}
void measurel() {
  digitalWrite(trigl, LOW);
  delayMicroseconds(2);
  digitalWrite(trigl, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigl, LOW);
  durationl = pulseIn(echol, HIGH);
  distancel = durationl*0.034/2;
  Serial.println(distancel);
}
void measurer() {
  digitalWrite(trigr, LOW);
  delayMicroseconds(2);
  digitalWrite(trigr, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigr, LOW);
  durationr = pulseIn(echor, HIGH);
  distancer = durationr*0.034/2;
  Serial.println(distancer);
}

//LED strip animation functions
void fan() {
  colorrandomizer();
  colorWiperf(Color(cr, cg, cb), 25);
  colorWipelf(Color(cr, cg, cb), 25);
  sttf = 0;
  stff = 20;
  stclean();
}
void ban() {
  colorWiperb(Color(255, 0, 0), 25);
  colorWipelb(Color(255, 0, 0), 25);
  sttf = 1;
  stff = 20;
  stclean();
}
void ran() {
  colorWipelf(Color(0, 255, 0), 25);
  sttf = 2;
  stff = 20;
  stclean();
}
void lan() {
  colorWiperf(Color(0, 255, 0), 25);
  sttf = 3;
  stff = 20;
  stclean();
}
void rpan() {
  colorWiperb(Color(0, 0, 255), 25);
  colorWipelf(Color(0, 0, 255), 25);
  sttf = 4;
  stff = 20;
  stclean();
}
void lpan() {
  colorWiperf(Color(0, 0, 255), 25);
  colorWipelb(Color(0, 0, 255), 25);
  sttf = 5;
  stff = 20;
  stclean();
}
void stclean() {
  if (sttf == 0) {
    colorWiperf(Color(0, 0, 0), stff);
    colorWipelf(Color(0, 0, 0), stff);
  }
  else if (sttf == 1) {
    colorWiperb(Color(0, 0, 0), stff);
    colorWipelb(Color(0, 0, 0), stff);
  }
  else if (sttf == 2) {
    colorWipelf(Color(0, 0, 0), stff);
  }
  else if (sttf == 3) {
    colorWiperf(Color(0, 0, 0), stff);
  }
  else if (sttf == 4) {
    colorWiperb(Color(0, 0, 0), stff);
    colorWipelf(Color(0, 0, 0), stff);
  }
  else if (sttf == 5) {
    colorWiperf(Color(0, 0, 0), stff);
    colorWipelb(Color(0, 0, 0), stff);
  }
}

void disco(uint8_t wait, uint8_t th) {
  for (int i=0; i < th; i++) {
    strip.setPixelColor(random(0, strip.numPixels()), random(0,255), random(0,255), random(0,255));
    strip.show();
    delay(wait);
  }
  sttf = 0;
  stff = 20;
  stclean();
}

// fill the dots one after the other with said color
// good for testing purposes
void colorWiperf(uint32_t c, uint8_t wait) {
  int i;
  for (i=0; i < strip.numPixels()-19 ; i++) {
      strip.setPixelColor(i, c);
      strip.show();
      delay(wait);
  }
}
void colorWipelf(uint32_t c, uint8_t wait) {
  int i;
  for (i=strip.numPixels()-7; i > strip.numPixels()-20 ; i--) {
      strip.setPixelColor(i, c);
      strip.show();
      delay(wait);
  }
}
void colorWiperb(uint32_t c, uint8_t wait) {
  int i;
  for (i=strip.numPixels()-19; i > 0 ; i--) {
      strip.setPixelColor(i, c);
      strip.show();
      delay(wait);
  }
}
void colorWipelb(uint32_t c, uint8_t wait) {
  int i;
  for (i=strip.numPixels()-20; i < strip.numPixels()-7 ; i++) {
      strip.setPixelColor(i, c);
      strip.show();
      delay(wait);
  }
}
// Create a 24 bit color value from R,G,B
uint32_t Color(byte r, byte g, byte b)
{
  uint32_t c;
  c = r;
  c <<= 8;
  c |= g;
  c <<= 8;
  c |= b;
  return c;
}

void colorrandomizer(){
  cr = random(0,255);
  cg = random(0,255);
  cb = random(0,255);
}
