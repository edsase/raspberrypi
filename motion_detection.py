import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)



while True:
    channel = GPIO.wait_for_edge(23, GPIO.RISING)
    if channel is not None:
        print('Motion detected')
        #sleep(1)

