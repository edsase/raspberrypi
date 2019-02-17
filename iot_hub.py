import pickle
import time
from dht22 import get_dht22_data


fp_iot_hub_credentials = r"../credentials/iothub_credentials"

with open(fp_iot_hub_credentials, 'rb') as f:
    # Azure IoT Hub
    URI = pickle.load(f)
    KEY = pickle.load(f)
    IOT_DEVICE_ID = pickle.load(f)
    POLICY = pickle.load(f)
    


def generate_sas_token():
    expiry=3600
    ttl = time.time() + expiry
    sign_key = "%s\n%d" % ((quote_plus(URI)), int(ttl))
    signature = b64encode(HMAC(b64decode(KEY), sign_key, sha256).digest())

    rawtoken = {
        'sr' :  URI,
        'sig': signature,
        'se' : str(int(ttl))
    }

    rawtoken['skn'] = POLICY

    return 'SharedAccessSignature ' + urlencode(rawtoken)



def send_message(token, message):
	url = 'https://{0}/devices/{1}/messages/events?api-version=2016-11-14'.format(URI, IOT_DEVICE_ID)
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = json.dumps(message)
    print data
    response = requests.post(url, data=data, headers=headers)




if __name__ == '__main__':

    # 2. Generate SAS Token
    token = generate_sas_token()

    # 3. Send Temperature to IoT Hub
    while True:
        data = get_dht22_data() 
        send_message(token, data)
        time.sleep(1)
