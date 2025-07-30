int trig = 5;
int echo = 6;

void setup() {
  pinMode(9, OUTPUT);             // 10번핀을 출력모드로 설정합니다.
  pinMode(10, OUTPUT);           // 11번핀을 출력모드로 설정합니다.
}

void loop() {
  analogWrite(9, 0);
  analogWrite(10, 0);
}
