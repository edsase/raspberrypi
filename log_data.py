import Adafruit_DHT as dht    # Importing Adafruit library for DHT22
from time import sleep           # Impoting sleep from time library to add delay
import time
import os
from dht22 import get_dht22_data

LOG_FILE = "./sensor-data/dht22.log"

#  log all data to a file

def log_data(interval):
    #  check if dht22.log file exists, otherwise create it using w+
    logfile = open(LOG_FILE, 'w+') 

    while True:
        # read data
        data = get_dht22_data()
        # convert data to csv string
        csv_string = '{timestamp},{humidity},{temperature}\n'.format(**data._asdict())
        try:    
            # save data in file, add headers if file is empty
            if os.path.getsize(LOG_FILE) > 0:    
                logfile.write(csv_string)
            else:
                # write headers
                file_headers = "Timestamp,Humidity,Temperature\n"
                logfile.write(file_headers + csv_string)
            sleep(interval)
        except KeyboardInterrupt:
            logfile.close()



# every x intervals, copy logged data in file to usb folder if usb is in drive




if __name__ == "__main__":
    log_data(3)