#include <RCSwitch.h>

#define RC_PIN_TX 6
#define RC_PULSE_LENGTH 190
#define RC_BIT_LENGTH 24

#define HEAT_ON 5330227
#define HEAT_OFF 5330236

RCSwitch sendSwitch = RCSwitch();

void setup()
{
  sendSwitch.enableTransmit(RC_PIN_TX);
  sendSwitch.setPulseLength(RC_PULSE_LENGTH);
}

void loop()
{
  sendSwitch.send(HEAT_ON, RC_BIT_LENGTH);
  delay(30000);
  sendSwitch.send(HEAT_OFF, RC_BIT_LENGTH);
  delay(30000);
}