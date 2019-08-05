#define BLYNK_PRINT Serial

#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

char auth[] = "YourAuthToken";

char ssid[] = "YourNetworkName";
char pass[] = "YourPassword";

void setup()
{
  Serial.begin(9600);

  Blynk.begin(auth, ssid, pass);

  pinMode(2,OUTPUT);
  digitalWrite(2,0);
}

void loop()
{
  Blynk.run();
  digitalWrite(2,0);
}

BLYNK_WRITE(V0)
{
  int pinValue = param.asInt();
  Serial.println(pinValue);
  if (pinValue == 0){
    digitalWrite(2,1);
    delay(200);
    digitalWrite(2,0);
    delay(600);
  }
  else if (pinValue == 1){
    digitalWrite(2,1);
    delay(400);
    digitalWrite(2,0);
    delay(400);
  }
  else if (pinValue == 2){
    digitalWrite(2,1);
    delay(600);
    digitalWrite(2,0);
    delay(200);
  }
}
