from time import sleep
from display.display_out import display
from sensor.sensor_data import DHTSensor
from config.config_pin import lora_parameters
from LoRa.sx1262 import SX1262
import json

def cb(events):
    global sampling_period, n_samples
    if events & SX1262.RX_DONE:
        
        msg, err = lora.recv()
        error = SX1262.STATUS[err]
        print('Receive: {}, {}'.format(msg, error))
        try:
            message = json.loads(msg)
            
            if all(key in message for key in ['n_samples', 'sampling_time', 'sampling_period']):
                
                sampling_period = message['sampling_period']
                sleep(float(message['sampling_time']) * 3600)
                n_samples = message['n_samples']  
        except Exception as e:
            print(f"Error decoding JSON: {e}")
    elif events & SX1262.TX_DONE:
        print('TX done.')

def send(sx):
    #define the global variable so that it is also used in the callback function
    global lora, sampling_period, n_samples
    n_samples = 0
    sampling_period = 10
    lora = sx
    sensor = DHTSensor()
    lora.setBlockingCallback(False, cb)
    print("Sending with LoRa")
    
    while True:
        
        temperature, humidity = sensor.measure()
        print("Send temperature and humidity")
        packet = {
            "temperature": temperature,
            "humidity": humidity,
        }
        
        lora.send(bytes(json.dumps(packet).encode()))
        print ("sent : ", json.dumps(packet))
        print("n_samples: ", n_samples)
        display("temperature", str(packet['temperature']),"humidity",str(packet['humidity']))
        #periodo di campionamento di default = 10 secondi
        if (n_samples != 0):
            n_samples = n_samples - 1
        if (n_samples == 0):
                sampling_period = 10
        sleep(sampling_period)