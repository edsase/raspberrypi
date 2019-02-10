import Adafruit_DHT as dht    # Importing Adafruit library for DHT22
from time import sleep           # Impoting sleep from time library to add delay
import time

DURATION = 20
end_time = time.time() + DURATION


try:
    while time.time() < end_time:                # Loop will run forever
        humi, temp = dht.read_retry(dht.DHT22, 8)  # Reading humidity and temperature
        print('Temp: {0:0.1f}*C  Humidity: {1:0.1f}%'.format(temp, humi)) 
        sleep(3)
# If keyboard Interrupt is pressed
except KeyboardInterrupt:
    pass  			# Go to next line