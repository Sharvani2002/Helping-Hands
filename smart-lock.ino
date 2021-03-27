#include <Servo.h>

Servo servo1;
String serialread = "";
int motorpin = A0;
String passcode = "6512df4";
void setup() { 
  Serial.begin(9600);
  Serial.print("system starting.");
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, INPUT);
  pinMode(12, INPUT);
  pinMode(13, OUTPUT);
  Serial.print(" .");
  servo1.attach(7);
  servo1.write(0);
  Serial.println(" .");
  Serial.println("System loaded! Welcome!");
  Serial.println("Welcome!Please enter the code offered by the Administrator!");
} 

void loop() {
  if (digitalRead(4) == 1) {
    servo1.write(120);
    digitalWrite(3, 0);
    delay(1);
    serialread = "";
  }
  digitalWrite(2, 1);
  delay(200);
  digitalWrite(2, 0);
  delay(750);
  digitalRead(4);
  digitalRead(6);
  while (Serial.available() > 0) {
    serialread += char(Serial.read());
    delay(2);
  }
  if (serialread == passcode || digitalRead(12) == 1) { //passcode HERE!  
    Serial.println("Box unlocked");
    servo1.write(0);
    digitalWrite(3, 1);
    delay(10000);
    digitalWrite(3, 0);
    delay(1);
    serialread = "";
  } else {
    if (serialread == ("hold" + passcode)) {
      servo1.write(0);
      digitalWrite(3, 1);
      delay(1750);
    } else {
      if (digitalRead(4) == 0) {
        digitalWrite(2, 0);
        delay(1);
        digitalWrite(13, HIGH); 
        delay(1000);
        if (digitalRead(4) == 1);
        digitalWrite(13, LOW); 
        delay(1);
        serialread = "";
      } else {
        if (serialread == 0) {
          Serial.println("Welcome!Please enter the code offered by the Administrator!"); //循环发出
        } else {
          Serial.println("ERROR!");
          Serial.print("The code:[");
          Serial.print(serialread);
          Serial.println("] was wrong!");
          delay(750);
          serialread = "";
        }
      }
    }
  }
}