import RPi.GPIO as GPIO
import io_settings
from led_blink import blink


while True:
    channel = GPIO.wait_for_edge(23, GPIO.RISING)
    if channel is not None:
        print('Motion detected')
        blink(8)

