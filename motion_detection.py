import RPi.GPIO as GPIO
from led_blink import blink

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)



while True:
    channel = GPIO.wait_for_edge(23, GPIO.RISING)
    if channel is not None:
        print('Motion detected')
        blink(8)

