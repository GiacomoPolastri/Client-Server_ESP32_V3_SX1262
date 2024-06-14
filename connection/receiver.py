from time import sleep_ms, time
from display.display_out import display
from sensor.sensor_data import DHTSensor
from LoRa.sx1262 import SX1262
import sys
import json
from select import select

def cb(events):
    if events & SX1262.RX_DONE:
        msg, err = lora.recv()
        if len(msg) > 0:
            error = SX1262.STATUS[err]
            print('Receive: {}, {}'.format(msg, error))
    elif events & SX1262.TX_DONE:
        print('TX done.')

def get_input(prompt, default_value=0, timeout=5):
    print(prompt)
    start_time = time()
    user_input = ""
    
    while time() - start_time < timeout:
        if sys.stdin in select([sys.stdin], [], [], timeout)[0]:
            user_input = sys.stdin.readline().strip()
            if user_input:
                return user_input

    print(f"Timeout reached. Using default value: {default_value}")
    return str(default_value)

def get_numeric_input(prompt, default_value=0, timeout=5):
    value = get_input(prompt, default_value, timeout)
    while not value.isdigit():
        value = get_input(prompt, default_value, timeout)
    return int(value)

def receive(sx):
    
    global lora
    lora = sx
    
    # Periodo di campionamento
    periodo_campionamento = get_numeric_input("Inserisci il periodo di campionamento in secondi:")
    print("Hai inserito:", periodo_campionamento)

    # Orario in cui campionare
    orario_campionamento = get_numeric_input("Inserisci tra quante ore vuoi campionare :")
    print("Hai inserito:", orario_campionamento)

    # Numero di campioni da acquisire
    n_campionamento = get_numeric_input("Inserisci il numero di campioni da acquisire:")
    print("Hai inserito:", n_campionamento)

    # Crea il pacchetto come dizionario
    packet = {
        "periodo_campionamento": periodo_campionamento,
        "orario_campionamento": orario_campionamento,
        "n_campionamento": n_campionamento,
    }
    if n_campionamento != 0:
        lora.send(bytes(json.dumps(packet).encode()))
    print("Receiving")
    while n_campionamento != 0:
        msg, err = lora.recv()
        if len(msg) > 0:
            error = SX1262.STATUS[err]
            print('Receive: {}, {}'.format(msg, error))
            n_campionamento = n_campionamento - 1
            
    lora.setBlockingCallback(False, cb)

