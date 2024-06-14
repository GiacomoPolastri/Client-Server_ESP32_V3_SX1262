from time import sleep
from display.display_out import display
from sensor.sensor_data import DHTSensor
from config.config_pin import lora_parameters
from LoRa.sx1262 import SX1262
import json

def send(sx):
    #define the global variable so that it is also used in the callback function
    global lora, counter, periodo_campionamento
    periodo_campionamento = 10
    lora = sx
    counter = 0
    sensor = DHTSensor()
    lora.setBlockingCallback(False, cb)
    print("Sending with LoRa")
    
    while True:
        '''
        temperature, humidity = sensor.measure()
        print("Send temperature and humidity")
        packet = {
            "temperature": temperature,
            "humidity": humidity,
        }
        j = json.dumps(packet)
        lora.send(bytes(json.dumps(j).encode()))
        '''
        print("Send message Hello")
        package = bytes("Hello", 'utf-8')
        lora.send(package)
        #periodo di campionamento di default = 10 secondi
        sleep(periodo_campionamento)

def cb(events):
    if events & SX1262.RX_DONE:
        
        msg, err = lora.recv()
        error = SX1262.STATUS[err]
        print('Receive: {}, {}'.format(msg, error))
        message = json.loads(msg)
        
        if all(key in message for key in ['n_campionamento', 'orario_campionamento', 'periodo_campionamento']):
            
            periodo_campionamento = message['periodo_campionamento']
            sleep(float(message['orario_campionamento']) * 3600)

    elif events & SX1262.TX_DONE:
        print('TX done.')

