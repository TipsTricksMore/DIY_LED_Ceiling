#include <Encoder.h>    // Verwendung der <Encoder.h> Bibliothek 


const int buttonSegment1 = 42;
const int buttonSegment2 = 43;
const int buttonSegment3 = 44;
const int buttonSegment4 = 45;
const int buttonSegment5 = 46;
const int buttonSegment6 = 47;
const int buttonSegment7 = 48;
const int buttonSegment8 = 49;
const int buttonSegment9 = 50;
const int buttonSegment10 = 33;
const int buttonSegment11 = 34;
const int buttonSegment12 = 35;
const int buttonSegment13 = 36;
const int buttonSegment14 = 37;
const int buttonSegment15 = 38;
const int buttonSegment16 = 39;
const int buttonSegment17 = 40;
const int buttonSegment18 = 41;
const int buttonSegment19 = 24;
const int buttonSegment20 = 25;
const int buttonSegment21 = 26;
const int buttonSegment22 = 27;
const int buttonSegment23 = 28;
const int buttonSegment24 = 29;
const int buttonSegment25 = 30;
const int buttonSegment26 = 31;
const int buttonSegment27 = 32;
const int buttonSegment28 = 7;
const int buttonSegment29 = 8;
const int buttonSegment30 = 9;
const int buttonSegment31 = 10;
const int buttonSegment32 = 11;
const int buttonSegment33 = 12;
const int buttonSegment34 = 13;
const int buttonSegment35 = 22;
const int buttonSegment36 = 23;
const int buttonSegment37 = A12;
const int buttonSegment38 = A13;
const int buttonSegment39 = A14;
const int buttonSegment40 = A15;
const int buttonSegment41 = 2;
const int buttonSegment42 = 3;
const int buttonSegment43 = 4;
const int buttonSegment44 = 5;
const int buttonSegment45 = 6;
const int buttonSegment46 = A3;
const int buttonSegment47 = A4;
const int buttonSegment48 = A5;
const int buttonSegment49 = A6;
const int buttonSegment50 = A7;
const int buttonSegment51 = A8;
const int buttonSegment52 = A9;
const int buttonSegment53 = A10;
const int buttonSegment54 = A11;
const int mainbutton = 51;
const int led_relay = 52;



const int ColorPotPin = A0;
const int BrightnessPotPin = A1;
const int ColorWPotPin = A2;


int buttonSegment1state = 0;
int buttonSegment2state = 0;
int buttonSegment3state = 0;
int buttonSegment4state = 0;
int buttonSegment5state = 0;
int buttonSegment6state = 0;
int buttonSegment7state = 0;
int buttonSegment8state = 0;
int buttonSegment9state = 0;
int buttonSegment10state = 0;
int buttonSegment11state = 0;
int buttonSegment12state = 0;
int buttonSegment13state = 0;
int buttonSegment14state = 0;
int buttonSegment15state = 0;
int buttonSegment16state = 0;
int buttonSegment17state = 0;
int buttonSegment18state = 0;
int buttonSegment19state = 0;
int buttonSegment20state = 0;
int buttonSegment21state = 0;
int buttonSegment22state = 0;
int buttonSegment23state = 0;
int buttonSegment24state = 0;
int buttonSegment25state = 0;
int buttonSegment26state = 0;
int buttonSegment27state = 0;
int buttonSegment28state = 0;
int buttonSegment29state = 0;
int buttonSegment30state = 0;
int buttonSegment31state = 0;
int buttonSegment32state = 0;
int buttonSegment33state = 0;
int buttonSegment34state = 0;
int buttonSegment35state = 0;
int buttonSegment36state = 0;
int buttonSegment37state = 0;
int buttonSegment38state = 0;
int buttonSegment39state = 0;
int buttonSegment40state = 0;
int buttonSegment41state = 0;
int buttonSegment42state = 0;
int buttonSegment43state = 0;
int buttonSegment44state = 0;
int buttonSegment45state = 0;
int buttonSegment46state = 0;
int buttonSegment47state = 0;
int buttonSegment48state = 0;
int buttonSegment49state = 0;
int buttonSegment50state = 0;
int buttonSegment51state = 0;
int buttonSegment52state = 0;
int buttonSegment53state = 0;
int buttonSegment54state = 0;
int mainbuttonstate = 0;




// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
  pinMode(led_relay, OUTPUT);

}

// the loop routine runs over and over again forever:
void loop() { 
  
   delay(500); //delay for serial read error inside python...

   
  //read BrightnessPotPinValue:
  int BrightnessPotPinValue = map(analogRead(BrightnessPotPin), 0, 1023, 0, 255);
  
  //adding serial output space management for python...
  if ((BrightnessPotPinValue > -1) & (BrightnessPotPinValue < 10)) {

      Serial.print("BrightnessPotPinValue: ");
      Serial.print(BrightnessPotPinValue);
      Serial.print("  ");

  } 
  if ((BrightnessPotPinValue > 9) & (BrightnessPotPinValue < 100)) {

      Serial.print("BrightnessPotPinValue: ");
      Serial.print(BrightnessPotPinValue);
      Serial.print(" ");

  }  
  if ((BrightnessPotPinValue > 99) & (BrightnessPotPinValue < 256)) {

      Serial.print("BrightnessPotPinValue: ");
      Serial.print(BrightnessPotPinValue);
      Serial.print("");

  }
  
  //read ColorPotPinValue:
  int ColorPotPinValue = map(analogRead(ColorPotPin), 0, 1023, 0, 255);

  //fixing range output:
  if ((ColorPotPinValue < 30) & (ColorPotPinValue > 0)){
    ColorPotPinValue = 30;
  }
  if (ColorPotPinValue > 225){
    ColorPotPinValue = 225;
  }

   //fixing range 2 output for colorW activation:
  if (ColorPotPinValue == 0){
    ColorPotPinValue = 0;
     }

  
  //adding serial output space management for python...
  if ((ColorPotPinValue > -1) & (ColorPotPinValue < 10)) {

      Serial.print(" ColorPotPinValue: ");
      Serial.print(ColorPotPinValue);
      Serial.print("  ");

  } 
  if ((ColorPotPinValue > 9) & (ColorPotPinValue < 100)) {

      Serial.print(" ColorPotPinValue: ");
      Serial.print(ColorPotPinValue);
      Serial.print(" ");

  }  
  if ((ColorPotPinValue > 99) & (ColorPotPinValue < 256)) {

      Serial.print(" ColorPotPinValue: ");
      Serial.print(ColorPotPinValue);
      Serial.print("");

  }

  //read ColorWPotPinValue:
  int ColorWPotPinValue = map(analogRead(ColorWPotPin), 0, 1023, 0, 255);
  
  //adding serial output space management for python...
  if ((ColorWPotPinValue > -1) & (ColorWPotPinValue < 10)) {

      Serial.print(" ColorWPotPinValue: ");
      Serial.print(ColorWPotPinValue);
      Serial.print("  ");

  } 
  if ((ColorWPotPinValue > 9) & (ColorWPotPinValue < 100)) {

      Serial.print(" ColorWPotPinValue: ");
      Serial.print(ColorWPotPinValue);
      Serial.print(" ");

  }  
  if ((ColorWPotPinValue > 99) & (ColorWPotPinValue < 256)) {

      Serial.print(" ColorWPotPinValue: ");
      Serial.print(ColorWPotPinValue);
      Serial.print("");

  }

  //read buttonSegment1 state:
  buttonSegment1state = digitalRead(buttonSegment1);

  
  Serial.print(" buttonSegment1state: ");
  Serial.print(buttonSegment1state);
  if (buttonSegment1state == HIGH) {
    //set button state to 1
    buttonSegment1state = 1;
  } else {
    //set button state to 0
    buttonSegment1state = 0;
  }

  //read buttonSegment2 state:
  buttonSegment2state = digitalRead(buttonSegment2);

  
  Serial.print(" buttonSegment2state: ");
  Serial.print(buttonSegment2state);
  if (buttonSegment2state == HIGH) {
    //set button state to 1
    buttonSegment2state = 1;
  } else {
    //set button state to 0
    buttonSegment2state = 0;
  }

  //read buttonSegment3 state:
  buttonSegment3state = digitalRead(buttonSegment3);

  
  Serial.print(" buttonSegment3state: ");
  Serial.print(buttonSegment3state);
  if (buttonSegment3state == HIGH) {
    //set button state to 1
    buttonSegment3state = 1;
  } else {
    //set button state to 0
    buttonSegment3state = 0;
  }

    //read buttonSegment4 state:
  buttonSegment4state = digitalRead(buttonSegment4);

  
  Serial.print(" buttonSegment4state: ");
  Serial.print(buttonSegment4state);
  if (buttonSegment4state == HIGH) {
    //set button state to 1
    buttonSegment4state = 1;
  } else {
    //set button state to 0
    buttonSegment4state = 0;
  }
    //read buttonSegment5 state:
  buttonSegment5state = digitalRead(buttonSegment5);

  
  Serial.print(" buttonSegment5state: ");
  Serial.print(buttonSegment5state);
  if (buttonSegment5state == HIGH) {
    //set button state to 1
    buttonSegment5state = 1;
  } else {
    //set button state to 0
    buttonSegment5state = 0;
  }
  //read buttonSegment6 state:
  buttonSegment6state = digitalRead(buttonSegment6);

  
  Serial.print(" buttonSegment6state: ");
  Serial.print(buttonSegment6state);
  if (buttonSegment6state == HIGH) {
    //set button state to 1
    buttonSegment6state = 1;
  } else {
    //set button state to 0
    buttonSegment6state = 0;
  }

  //read buttonSegment7 state:
  buttonSegment7state = digitalRead(buttonSegment7);

  
  Serial.print(" buttonSegment7state: ");
  Serial.print(buttonSegment7state);
  if (buttonSegment7state == HIGH) {
    //set button state to 1
    buttonSegment7state = 1;
  } else {
    //set button state to 0
    buttonSegment7state = 0;
  }

  //read buttonSegment8 state:
  buttonSegment8state = digitalRead(buttonSegment8);

  
  Serial.print(" buttonSegment8state: ");
  Serial.print(buttonSegment8state);
  if (buttonSegment8state == HIGH) {
    //set button state to 1
    buttonSegment8state = 1;
  } else {
    //set button state to 0
    buttonSegment8state = 0;
  }

  //read buttonSegment9 state:
  buttonSegment9state = digitalRead(buttonSegment9);

  
  Serial.print(" buttonSegment9state: ");
  Serial.print(buttonSegment9state);
  if (buttonSegment9state == HIGH) {
    //set button state to 1
    buttonSegment9state = 1;
  } else {
    //set button state to 0
    buttonSegment9state = 0;
  }

  //read buttonSegment10 state:
  buttonSegment10state = digitalRead(buttonSegment10);

  
  Serial.print(" buttonSegment10state: ");
  Serial.print(buttonSegment10state);
  if (buttonSegment10state == HIGH) {
    //set button state to 1
    buttonSegment10state = 1;
  } else {
    //set button state to 0
    buttonSegment10state = 0;
  }

  //read buttonSegment11 state:
  buttonSegment11state = digitalRead(buttonSegment11);

  
  Serial.print(" buttonSegment11state: ");
  Serial.print(buttonSegment11state);
  if (buttonSegment11state == HIGH) {
    //set button state to 1
    buttonSegment11state = 1;
  } else {
    //set button state to 0
    buttonSegment11state = 0;
  }

  //read buttonSegment12 state:
  buttonSegment12state = digitalRead(buttonSegment12);

  
  Serial.print(" buttonSegment12state: ");
  Serial.print(buttonSegment12state);
  if (buttonSegment12state == HIGH) {
    //set button state to 1
    buttonSegment12state = 1;
  } else {
    //set button state to 0
    buttonSegment12state = 0;
  }

  //read buttonSegment13 state:
  buttonSegment13state = digitalRead(buttonSegment13);

  
  Serial.print(" buttonSegment13state: ");
  Serial.print(buttonSegment13state);
  if (buttonSegment13state == HIGH) {
    //set button state to 1
    buttonSegment13state = 1;
  } else {
    //set button state to 0
    buttonSegment13state = 0;
  }

  //read buttonSegment14 state:
  buttonSegment14state = digitalRead(buttonSegment14);

  
  Serial.print(" buttonSegment14state: ");
  Serial.print(buttonSegment14state);
  if (buttonSegment14state == HIGH) {
    //set button state to 1
    buttonSegment14state = 1;
  } else {
    //set button state to 0
    buttonSegment14state = 0;
  }

  //read buttonSegment15 state:
  buttonSegment15state = digitalRead(buttonSegment15);

  
  Serial.print(" buttonSegment15state: ");
  Serial.print(buttonSegment15state);
  if (buttonSegment15state == HIGH) {
    //set button state to 1
    buttonSegment15state = 1;
  } else {
    //set button state to 0
    buttonSegment15state = 0;
  }

  //read buttonSegment16 state:
  buttonSegment16state = digitalRead(buttonSegment16);

  
  Serial.print(" buttonSegment16state: ");
  Serial.print(buttonSegment16state);
  if (buttonSegment16state == HIGH) {
    //set button state to 1
    buttonSegment16state = 1;
  } else {
    //set button state to 0
    buttonSegment16state = 0;
  }

  //read buttonSegment17 state:
  buttonSegment17state = digitalRead(buttonSegment17);

  
  Serial.print(" buttonSegment17state: ");
  Serial.print(buttonSegment17state);
  if (buttonSegment17state == HIGH) {
    //set button state to 1
    buttonSegment17state = 1;
  } else {
    //set button state to 0
    buttonSegment17state = 0;
  }

  //read buttonSegment18 state:
  buttonSegment18state = digitalRead(buttonSegment18);

  
  Serial.print(" buttonSegment18state: ");
  Serial.print(buttonSegment18state);
  if (buttonSegment18state == HIGH) {
    //set button state to 1
    buttonSegment18state = 1;
  } else {
    //set button state to 0
    buttonSegment18state = 0;
  }

  //read buttonSegment19 state:
  buttonSegment19state = digitalRead(buttonSegment19);

  
  Serial.print(" buttonSegment19state: ");
  Serial.print(buttonSegment19state);
  if (buttonSegment19state == HIGH) {
    //set button state to 1
    buttonSegment19state = 1;
  } else {
    //set button state to 0
    buttonSegment19state = 0;
  }

  //read buttonSegment20 state:
  buttonSegment20state = digitalRead(buttonSegment20);

  
  Serial.print(" buttonSegment20state: ");
  Serial.print(buttonSegment20state);
  if (buttonSegment20state == HIGH) {
    //set button state to 1
    buttonSegment20state = 1;
  } else {
    //set button state to 0
    buttonSegment20state = 0;
  }

  //read buttonSegment21 state:
  buttonSegment21state = digitalRead(buttonSegment21);

  
  Serial.print(" buttonSegment21state: ");
  Serial.print(buttonSegment21state);
  if (buttonSegment21state == HIGH) {
    //set button state to 1
    buttonSegment21state = 1;
  } else {
    //set button state to 0
    buttonSegment21state = 0;
  }

  //read buttonSegment22 state:
  buttonSegment22state = digitalRead(buttonSegment22);

  
  Serial.print(" buttonSegment22state: ");
  Serial.print(buttonSegment22state);
  if (buttonSegment22state == HIGH) {
    //set button state to 1
    buttonSegment22state = 1;
  } else {
    //set button state to 0
    buttonSegment22state = 0;
  }

  //read buttonSegment23 state:
  buttonSegment23state = digitalRead(buttonSegment23);

  
  Serial.print(" buttonSegment23state: ");
  Serial.print(buttonSegment23state);
  if (buttonSegment23state == HIGH) {
    //set button state to 1
    buttonSegment23state = 1;
  } else {
    //set button state to 0
    buttonSegment23state = 0;
  }

  //read buttonSegment24 state:
  buttonSegment24state = digitalRead(buttonSegment24);

  
  Serial.print(" buttonSegment24state: ");
  Serial.print(buttonSegment24state);
  if (buttonSegment24state == HIGH) {
    //set button state to 1
    buttonSegment24state = 1;
  } else {
    //set button state to 0
    buttonSegment24state = 0;
  }

  //read buttonSegment25 state:
  buttonSegment25state = digitalRead(buttonSegment25);

  
  Serial.print(" buttonSegment25state: ");
  Serial.print(buttonSegment25state);
  if (buttonSegment25state == HIGH) {
    //set button state to 1
    buttonSegment25state = 1;
  } else {
    //set button state to 0
    buttonSegment25state = 0;
  }

  //read buttonSegment26 state:
  buttonSegment26state = digitalRead(buttonSegment26);

  
  Serial.print(" buttonSegment26state: ");
  Serial.print(buttonSegment26state);
  if (buttonSegment26state == HIGH) {
    //set button state to 1
    buttonSegment26state = 1;
  } else {
    //set button state to 0
    buttonSegment26state = 0;
  }

  //read buttonSegment27 state:
  buttonSegment27state = digitalRead(buttonSegment27);

  
  Serial.print(" buttonSegment27state: ");
  Serial.print(buttonSegment27state);
  if (buttonSegment27state == HIGH) {
    //set button state to 1
    buttonSegment27state = 1;
  } else {
    //set button state to 0
    buttonSegment27state = 0;
  }

  //read buttonSegment28 state:
  buttonSegment28state = digitalRead(buttonSegment28);

  
  Serial.print(" buttonSegment28state: ");
  Serial.print(buttonSegment28state);
  if (buttonSegment28state == HIGH) {
    //set button state to 1
    buttonSegment28state = 1;
  } else {
    //set button state to 0
    buttonSegment28state = 0;
  }

  //read buttonSegment29 state:
  buttonSegment29state = digitalRead(buttonSegment29);

  
  Serial.print(" buttonSegment29state: ");
  Serial.print(buttonSegment29state);
  if (buttonSegment29state == HIGH) {
    //set button state to 1
    buttonSegment29state = 1;
  } else {
    //set button state to 0
    buttonSegment29state = 0;
  }

  //read buttonSegment30 state:
  buttonSegment30state = digitalRead(buttonSegment30);

  
  Serial.print(" buttonSegment30state: ");
  Serial.print(buttonSegment30state);
  if (buttonSegment30state == HIGH) {
    //set button state to 1
    buttonSegment30state = 1;
  } else {
    //set button state to 0
    buttonSegment30state = 0;
  }

  //read buttonSegment31 state:
  buttonSegment31state = digitalRead(buttonSegment31);

  
  Serial.print(" buttonSegment31state: ");
  Serial.print(buttonSegment31state);
  if (buttonSegment31state == HIGH) {
    //set button state to 1
    buttonSegment31state = 1;
  } else {
    //set button state to 0
    buttonSegment31state = 0;
  }

  //read buttonSegment32 state:
  buttonSegment32state = digitalRead(buttonSegment32);

  
  Serial.print(" buttonSegment32state: ");
  Serial.print(buttonSegment32state);
  if (buttonSegment32state == HIGH) {
    //set button state to 1
    buttonSegment32state = 1;
  } else {
    //set button state to 0
    buttonSegment32state = 0;
  }

  //read buttonSegment33 state:
  buttonSegment33state = digitalRead(buttonSegment33);

  
  Serial.print(" buttonSegment33state: ");
  Serial.print(buttonSegment33state);
  if (buttonSegment33state == HIGH) {
    //set button state to 1
    buttonSegment33state = 1;
  } else {
    //set button state to 0
    buttonSegment33state = 0;
  }

  //read buttonSegment34 state:
  buttonSegment34state = digitalRead(buttonSegment34);

  
  Serial.print(" buttonSegment34state: ");
  Serial.print(buttonSegment34state);
  if (buttonSegment34state == HIGH) {
    //set button state to 1
    buttonSegment34state = 1;
  } else {
    //set button state to 0
    buttonSegment34state = 0;
  }

  //read buttonSegment35 state:
  buttonSegment35state = digitalRead(buttonSegment35);

  
  Serial.print(" buttonSegment35state: ");
  Serial.print(buttonSegment35state);
  if (buttonSegment35state == HIGH) {
    //set button state to 1
    buttonSegment35state = 1;
  } else {
    //set button state to 0
    buttonSegment35state = 0;
  }

  //read buttonSegment36 state:
  buttonSegment36state = digitalRead(buttonSegment36);

  
  Serial.print(" buttonSegment36state: ");
  Serial.print(buttonSegment36state);
  if (buttonSegment36state == HIGH) {
    //set button state to 1
    buttonSegment36state = 1;
  } else {
    //set button state to 0
    buttonSegment36state = 0;
  }

  //read buttonSegment37 state:
  buttonSegment37state = digitalRead(buttonSegment37);

  
  Serial.print(" buttonSegment37state: ");
  Serial.print(buttonSegment37state);
  if (buttonSegment37state == HIGH) {
    //set button state to 1
    buttonSegment37state = 1;
  } else {
    //set button state to 0
    buttonSegment37state = 0;
  }

  //read buttonSegment38 state:
  buttonSegment38state = digitalRead(buttonSegment38);

  
  Serial.print(" buttonSegment38state: ");
  Serial.print(buttonSegment38state);
  if (buttonSegment38state == HIGH) {
    //set button state to 1
    buttonSegment38state = 1;
  } else {
    //set button state to 0
    buttonSegment38state = 0;
  }

  //read buttonSegment39 state:
  buttonSegment39state = digitalRead(buttonSegment39);

  
  Serial.print(" buttonSegment39state: ");
  Serial.print(buttonSegment39state);
  if (buttonSegment39state == HIGH) {
    //set button state to 1
    buttonSegment39state = 1;
  } else {
    //set button state to 0
    buttonSegment39state = 0;
  }

  //read buttonSegment40 state:
  buttonSegment40state = digitalRead(buttonSegment40);

  
  Serial.print(" buttonSegment40state: ");
  Serial.print(buttonSegment40state);
  if (buttonSegment40state == HIGH) {
    //set button state to 1
    buttonSegment40state = 1;
  } else {
    //set button state to 0
    buttonSegment40state = 0;
  }

  //read buttonSegment41 state:
  buttonSegment41state = digitalRead(buttonSegment41);

  
  Serial.print(" buttonSegment41state: ");
  Serial.print(buttonSegment41state);
  if (buttonSegment41state == HIGH) {
    //set button state to 1
    buttonSegment41state = 1;
  } else {
    //set button state to 0
    buttonSegment41state = 0;
  }

  //read buttonSegment42 state:
  buttonSegment42state = digitalRead(buttonSegment42);

  
  Serial.print(" buttonSegment42state: ");
  Serial.print(buttonSegment42state);
  if (buttonSegment42state == HIGH) {
    //set button state to 1
    buttonSegment42state = 1;
  } else {
    //set button state to 0
    buttonSegment42state = 0;
  }

  //read buttonSegment43 state:
  buttonSegment43state = digitalRead(buttonSegment43);

  
  Serial.print(" buttonSegment43state: ");
  Serial.print(buttonSegment43state);
  if (buttonSegment43state == HIGH) {
    //set button state to 1
    buttonSegment43state = 1;
  } else {
    //set button state to 0
    buttonSegment43state = 0;
  }

  //read buttonSegment44 state:
  buttonSegment44state = digitalRead(buttonSegment44);

  
  Serial.print(" buttonSegment44state: ");
  Serial.print(buttonSegment44state);
  if (buttonSegment44state == HIGH) {
    //set button state to 1
    buttonSegment44state = 1;
  } else {
    //set button state to 0
    buttonSegment44state = 0;
  }

  //read buttonSegment45 state:
  buttonSegment45state = digitalRead(buttonSegment45);

  
  Serial.print(" buttonSegment45state: ");
  Serial.print(buttonSegment45state);
  if (buttonSegment45state == HIGH) {
    //set button state to 1
    buttonSegment45state = 1;
  } else {
    //set button state to 0
    buttonSegment45state = 0;
  }

  //read buttonSegment46 state:
  buttonSegment46state = digitalRead(buttonSegment46);

  
  Serial.print(" buttonSegment46state: ");
  Serial.print(buttonSegment46state);
  if (buttonSegment46state == HIGH) {
    //set button state to 1
    buttonSegment46state = 1;
  } else {
    //set button state to 0
    buttonSegment46state = 0;
  }

  //read buttonSegment47 state:
  buttonSegment47state = digitalRead(buttonSegment47);

  
  Serial.print(" buttonSegment47state: ");
  Serial.print(buttonSegment47state);
  if (buttonSegment47state == HIGH) {
    //set button state to 1
    buttonSegment47state = 1;
  } else {
    //set button state to 0
    buttonSegment47state = 0;
  }

  //read buttonSegment48 state:
  buttonSegment48state = digitalRead(buttonSegment48);

  
  Serial.print(" buttonSegment48state: ");
  Serial.print(buttonSegment48state);
  if (buttonSegment48state == HIGH) {
    //set button state to 1
    buttonSegment48state = 1;
  } else {
    //set button state to 0
    buttonSegment48state = 0;
  }

  //read buttonSegment49 state:
  buttonSegment49state = digitalRead(buttonSegment49);

  
  Serial.print(" buttonSegment49state: ");
  Serial.print(buttonSegment49state);
  if (buttonSegment49state == HIGH) {
    //set button state to 1
    buttonSegment49state = 1;
  } else {
    //set button state to 0
    buttonSegment49state = 0;
  }

  //read buttonSegment50 state:
  buttonSegment50state = digitalRead(buttonSegment50);

  
  Serial.print(" buttonSegment50state: ");
  Serial.print(buttonSegment50state);
  if (buttonSegment50state == HIGH) {
    //set button state to 1
    buttonSegment50state = 1;
  } else {
    //set button state to 0
    buttonSegment50state = 0;
  }

  //read buttonSegment51 state:
  buttonSegment51state = digitalRead(buttonSegment51);

  
  Serial.print(" buttonSegment51state: ");
  Serial.print(buttonSegment51state);
  if (buttonSegment51state == HIGH) {
    //set button state to 1
    buttonSegment51state = 1;
  } else {
    //set button state to 0
    buttonSegment51state = 0;
  }

  //read buttonSegment52 state:
  buttonSegment52state = digitalRead(buttonSegment52);

  
  Serial.print(" buttonSegment52state: ");
  Serial.print(buttonSegment52state);
  if (buttonSegment52state == HIGH) {
    //set button state to 1
    buttonSegment52state = 1;
  } else {
    //set button state to 0
    buttonSegment52state = 0;
  }

  //read buttonSegment53 state:
  buttonSegment53state = digitalRead(buttonSegment53);

  
  Serial.print(" buttonSegment53state: ");
  Serial.print(buttonSegment53state);
  if (buttonSegment53state == HIGH) {
    //set button state to 1
    buttonSegment53state = 1;
  } else {
    //set button state to 0
    buttonSegment53state = 0;
  }

  //read buttonSegment54 state:
  buttonSegment54state = digitalRead(buttonSegment54);

  
  Serial.print(" buttonSegment54state: ");
  Serial.print(buttonSegment54state);
  if (buttonSegment54state == HIGH) {
    //set button state to 1
    buttonSegment54state = 1;
  } else {
    //set button state to 0
    buttonSegment54state = 0;
  }

  //read mainSegment state:
  mainbuttonstate = digitalRead(mainbutton);
  Serial.print(" mainbuttonstate: ");
  Serial.print(mainbuttonstate);
  if (mainbuttonstate == HIGH) {
    //set mainbuttonstate to 1
    mainbuttonstate = 1;
    digitalWrite(led_relay, HIGH);
  } else {
    //set mainbuttonstate to 0
    mainbuttonstate = 0;
    digitalWrite(led_relay, LOW);
  }



 Serial.println("");
}
