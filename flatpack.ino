int micPin = A0;
int piezoPin = A1;
int lightPin = A2;
int buttonPin = 8;
int value1 = 0;
int value2 = 0;
int value3 = 0;
bool working = false;
void setup()
{
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
}
void loop()
{
  value1 = analogRead(micPin);
  value2 = analogRead(piezoPin);
  value3 = analogRead(lightPin);
  int value4 = digitalRead(buttonPin);
  if (value3 > 10) {
    Serial.println("3");
    while (true) {
      if (Serial.available() > 0) {
        char received = Serial.read();
        if (received == '5') {
          break;
        }
      }
    }

  }

  if (value4 == HIGH) {
    Serial.println("4");
    while (true) {
      if (Serial.available() > 0) {
        char received = Serial.read();
        if (received == '5') {
          break;
        }
      }
    }
  }
  if (value2 > 10) {
    Serial.println("2");
    while (true) {
      if (Serial.available() > 0) {
        char received = Serial.read();
        if (received == '5') {
          break;
        }
      }
    }
  }
  if (value1 > 200) {
    Serial.println("1");
    while (true) {
      if (Serial.available() > 0) {
        char received = Serial.read();
        if (received == '5') {
          break;
        }
      }
    }
  }






  delay(50);
}
