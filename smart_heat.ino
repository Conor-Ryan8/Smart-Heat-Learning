#include <RCSwitch.h>
#include <DHT.h>

#define RADIO_PIN_TX 6
#define RADIO_PULSE_LENGTH 190
#define RADIO_BIT_LENGTH 24

#define HEAT_ON 5330227
#define HEAT_OFF 5330236

#define SENSOR_PIN 8
#define SENSOR_TYPE DHT22

#define IDEAL 21

RCSwitch radio = RCSwitch();

DHT sensor(SENSOR_PIN, SENSOR_TYPE);
float temp;

void setup()
{
  Serial.begin(9600);
  radio.enableTransmit(RADIO_PIN_TX);
  radio.setPulseLength(RADIO_PULSE_LENGTH);
  sensor.begin();
}

void loop()
{
  delay(2000);
  temp = sensor.readTemperature();
  Serial.print(temp, 1);
  Serial.println("°C");

  if (temp < IDEAL)
  {
    radio.send(HEAT_ON, RADIO_BIT_LENGTH);
    Serial.println("Too Cold! Heat On");
  }
  else if (temp > IDEAL)
  {
    radio.send(HEAT_OFF, RADIO_BIT_LENGTH);
    Serial.println("Too Warm!, Heat Off");
  }
  else
  {
    Serial.println("Temperature Perfect!");  
  }
  delay(1000);
}