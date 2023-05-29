import Adafruit_DHT
import RPi.GPIO as GPIO
import time

SENSOR_PIN = 4
SENSOR_TYPE = Adafruit_DHT.DHT22

GPIO.setwarnings(False)

while True:

  h, temp = Adafruit_DHT.read_retry(SENSOR_TYPE, SENSOR_PIN)
  print(temp)
  time.sleep(3)
