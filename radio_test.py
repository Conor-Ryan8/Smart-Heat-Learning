import RPi.GPIO as GPIO
from rpi_rf import RFDevice
import time

RADIO_PIN = 14
RADIO_PULSE_LENGTH = 190
RADIO_PROTOCOL = 1

HEAT_ON = 5330227
HEAT_OFF = 5330236

GPIO.setwarnings(False)
radio = RFDevice(RADIO_PIN)
radio.enable_tx()

while True:
  radio.tx_code(HEAT_ON, RADIO_PROTOCOL, RADIO_PULSE_LENGTH)
  time.sleep(3)
  radio.tx_code(HEAT_OFF, RADIO_PROTOCOL, RADIO_PULSE_LENGTH)
  time.sleep(3)
