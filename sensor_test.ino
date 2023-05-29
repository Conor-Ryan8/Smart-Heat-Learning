#include <DHT.h>;

#define DHT_PIN 8
#define DHT_TYPE DHT22

DHT dht_sensor(DHT_PIN, DHT_TYPE);

float temp;

void setup()
{
  Serial.begin(9600);
  dht_sensor.begin();
}

void loop()
{
  delay(2000);
  temp = dht_sensor.readTemperature();
  Serial.println(temp);
  delay(3000);
}