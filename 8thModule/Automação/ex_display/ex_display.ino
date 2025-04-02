#include <LiquidCrystal.h>
#define sensor A1

LiquidCrystal lcd(7, 6, 5, 4, 3, 2);

void setup() {
  lcd.begin(16,2);
  lcd.clear();
  pinMode(sensor, INPUT);
  Serial.begin(9600);
}

void loop() {
  int sensor_vle = analogRead(sensor);
  Serial.println(sensor_vle);
  lcd.setCursor(0,0);
  if (sensor_vle >= 500){
    lcd.print("Sound detected");
    delay(500);
    lcd.clear();
    }
}
