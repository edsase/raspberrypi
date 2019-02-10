import RPi.GPIO as GPIO
import time

def blink(duration=6):

    endtime = time.time() + duration

    try:
        while time.time() < endtime:
            GPIO.output(19, True)
            time.sleep(0.5)
            GPIO.output(19, False)
            time.sleep(0.5)
        
    finally:\
        # cleanup
        GPIO.cleanup()


