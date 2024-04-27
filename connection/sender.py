from time import sleep_ms
from display.display_out import display
from sensor.sensor_data import  DHTSensor
from config.config_pin import lora_parameters

def send(lora):
    counter = 0
    print("LoRa Sender")
    sensor = DHTSensor()
    while True:
        lora.setBlockingCallback(False, cb)
        print("Send lora parameters", str(lora_parameters))
        package = bytes(str(lora_parameters),  'utf-8')
        lora.send(package)
        display("send lora params", "number", str(counter))
        counter += 1
        sleep_ms(10000)
        '''
        temperature, humidity = sensor.measure()
        print("Send temperature", str(temperature))
        lora.send(temperature)
        display("send temperature", "number", str(counter))
        counter += 1
        sleep_ms(10000)
        print("Send humidity", str(humidity))
        lora.send(humidity)
        display("send humidity", "number", str(counter))
        counter += 1
        sleep_ms(10000)
        '''
        
def cb(events):
    if events & SX1262.RX_DONE:
        msg, err = lora.recv()
        error = SX1262.STATUS[err]
        print('Receive: {}, {}'.format(msg, error))
    elif events & SX1262.TX_DONE:
        print('TX done.')