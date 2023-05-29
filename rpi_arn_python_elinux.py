import Adafruit_DHT
from rpi_rf import RFDevice
import time

GPIO.setwarnings(False)
radio = RFDevice(14)
radio.enable_tx()

IDEAL = 29

HEAT_ON = 5330227
HEAT_OFF = 5330236
PIN = 189

while True:

  humid, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,4)
  print(str(round(temp, 1)) + "°C")

  if temp < IDEAL:
    radio.tx_code(HEAT_ON, 1, PIN)
    print("Too Cold! Heat On!")
  elif temp > IDEAL:
    radio.tx_code(HEAT_OFF, 1, PIN)
    print("Too Warm, Heat Off")
  else:
    print("Temperature Perfect!")

  time.sleep(15)
