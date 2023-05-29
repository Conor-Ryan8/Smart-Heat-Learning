import RPi.GPIO as GPIO
import Adafruit_DHT
from rpi_rf import RFDevice
import time

RADIO_PIN = 14
RADIO_PULSE_LENGTH = 190
RADIO_PROTOCOL = 1

HEAT_ON = 5330227
HEAT_OFF = 5330236
SENSOR_PIN = 4
SENSOR_TYPE = Adafruit_DHT.DHT22

IDEAL = 21

GPIO.setwarnings(False)
radio = RFDevice(RADIO_PIN)
radio.enable_tx()

while True:

  h, temp = Adafruit_DHT.read_retry(SENSOR_TYPE, SENSOR_PIN)
  print(str(round(temp, 1)) + "°C")

  if temp < IDEAL:
    radio.tx_code(HEAT_ON, RADIO_PROTOCOL, RADIO_PULSE_LENGTH)
    print("Too Cold! Heat On!")
  elif temp > IDEAL:
    radio.tx_code(HEAT_OFF, RADIO_PROTOCOL, RADIO_PULSE_LENGTH)
    print("Too Warm, Heat Off")
  else:
    print("Temperature Perfect!")

  time.sleep(15)
