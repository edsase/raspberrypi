import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN)
channel = GPIO.wait_for_edge(23, GPIO.RISING)

while True:
    if channel:
        print('Motion detected')

