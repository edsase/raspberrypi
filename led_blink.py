import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)

DURATION = 20
endtime = time.time() + DURATION

try:
    while time.time() < endtime:
        GPIO.output(19, True)
        time.sleep(0.5)
        GPIO.output(19, False)
        time.sleep(0.5)
    
finally:\
    # cleanup
    GPIO.cleanup()


