from time import sleep_ms
from display.display_out import display
from sensor.sensor_data import  DHTSensor
from config.config_pin import lora_parameters
from LoRa.sx1262 import SX1262
import sys
import json
from machine import reset


def get_input(prompt):
    value = sys.stdin.readline().strip()
    return value

def get_numeric_input(prompt):
    print(prompt)
    value = get_input(prompt)
    while not value.isdigit():
        value = get_input(prompt)
    return int(value)

def receive(lora):
    global sx, periodo_campionamento, orario_campionamento, n_campionamento
    sx = lora
    
    # Periodo di campionamento
    periodo_campionamento = get_numeric_input("Inserisci il periodo di campionamento:")
    print("Hai inserito:", periodo_campionamento)
    
    # Orario in cui campionare
    print
    orario_campionamento = get_numeric_input("Inserisci tra quante ore vuoi campionare :")
    print("Hai inserito:", orario_campionamento)

    # Numero di campioni da acquisire
    n_campionamento = get_numeric_input("Inserisci il numero di campioni da acquisire:")
    print("Hai inserito:", n_campionamento)
   
    # Crea il pacchetto come dizionario
    packet = {
        "periodo_campionamento": periodo_campionamento,
        "orario_campionamento": orario_campionamento,
    }

    # Converte il dizionario in una stringa JSON
    j = json.dumps(packet)
    #print("Pacchetto JSON:", j)
    sx.send(bytes(json.dumps(j).encode()))
            
    print("Receiving")
    display("Receiving")
    lora.setBlockingCallback(False, cb)
        
def cb(events):
    global sx, n_campionamento
    if events & SX1262.RX_DONE:
        print ("event true")
        msg, err = sx.recv()
        if len(msg) > 0:
            error = SX1262.STATUS[err]
            print(msg)
            print(error)
            display("receive", msg)
            print (n_campionamento)
            if (n_campionamento == 0):
                reset()
                print("resettato")
            n_campionamento = n_campionamento-1
