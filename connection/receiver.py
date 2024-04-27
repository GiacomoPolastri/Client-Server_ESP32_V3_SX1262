from time import sleep_ms
from display.display_out import display
from sensor.sensor_data import  DHTSensor
from config.config_pin import lora_parameters

def receive(lora):
    print("LoRa Receive")
    display("LoRa Receive")
    while True:
        lora.setBlockingCallback(False, cb)
    sleep_ms(1000)    
        
def cb(events):
    if events & SX1262.RX_DONE:
        msg, err = lora.recv()
        if len(msg) > 0:
            error = SX1262.STATUS[err]
            print(msg)
            print(error)
            display("receive", msg)
        sleep_ms(100)
