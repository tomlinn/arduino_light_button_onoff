#include <Servo.h>

Servo myservo; // 建立Servo物件，控制伺服馬達
int buttonPin = 4;
int buttonPin2 = 5;
int buttonState = 0;
int buttonState2 = 0;
#include <SoftwareSerial.h>
SoftwareSerial BT(3,2);
char v;
void setup()
{
  Serial.begin(9600);
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(buttonPin2, INPUT_PULLUP);
  Serial.println("OK");
  BT.begin(9600);
  myservo.attach(9);
  myservo.write(0);// 連接數位腳位9，伺服馬達的訊號線
}

void loop()
{
  buttonState = digitalRead(buttonPin);
  buttonState2 = digitalRead(buttonPin2);
  if (BT.available()) {

    v = BT.read();
    Serial.println(v);
    if (v == '1') {
      // turn LED on:
      Serial.println(32);
      myservo.write(32);
      BT.print('A');

    }
    if (v == '0') {
      // turn LED on:
      Serial.println(0);
      myservo.write(0);
      
      BT.print('B');
    }
  }

  if (buttonState == 0) {
    // turn LED on:
    Serial.println(32);
    myservo.write(32);

  }
  if (buttonState2 == 0) {
    // turn LED on:
    Serial.println(0);
    myservo.write(0);

  }
}
