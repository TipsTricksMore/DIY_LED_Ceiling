/* Encoder Library - Basic Example
 * http://www.pjrc.com/teensy/td_libs_Encoder.html
 *
 * This example code is in the public domain.
 */

#include <Encoder.h>

// Change these two numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability
//   Low Performance:  neither pin has interrupt capability
Encoder myEnc(2, 3);
const int encButton = 7;
//   avoid using pins with LEDs attached

void setup() {
  Serial.begin(9600);
  pinMode(encButton, INPUT_PULLUP);
}

long oldPosition  = 0;
int effect_id = 0;

void loop() {
  long newPosition = myEnc.read();
  if (newPosition < 0){ //set the effect_id down limit to 0
    oldPosition = 0;
    newPosition = 0;
    myEnc.write(0);
  }

  if (newPosition > 234){ //set the effect_id upper limit to 117 (234/2)
    oldPosition = 234;
    newPosition = 234;
    myEnc.write(234);
  }
  
  if (newPosition != oldPosition) {
    oldPosition = newPosition;
    //Serial.println(newPosition);
    }

  if (newPosition < 0){
    effect_id = 0;
  }
  if (newPosition > 0){
    effect_id = newPosition;
  }

  if (digitalRead(encButton) == 0){
    oldPosition = 0;
    newPosition = 0;
    myEnc.write(0);
    effect_id = newPosition;
  }

  
  Serial.print("effect_id: ");
  Serial.println(effect_id/2);
  delay(100);
}
