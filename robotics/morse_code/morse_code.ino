void blip() {
  digitalWrite(8, HIGH);
  delay(250);
  digitalWrite(8, LOW);
  delay(250);
}
  
void bloop() {
  digitalWrite(8, HIGH);
  delay(600);
  digitalWrite(8, LOW);
  delay(250);
}

void H(blip) {
for(int x=0; x<4; x++)  {
  blip();
}

void E() {
for(int x=0; x<1; x++)  {
  digitalWrite(8, HIGH);
  delay(250);
  digitalWrite(8, LOW);
  delay(250);
}

void L() {
for(int x=0; x<4; x++)  {
  digitalWrite(8, HIGH);
  delay(250);
  digitalWrite(8, LOW);
  delay(250);
}


}
