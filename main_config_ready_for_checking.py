from config.config_pin import *
from LoRa.sx1262 import SX1262
from machine import Pin, SoftSPI, ADC, SPI
import time
import esp
from flashbdev import bdev
from display.display_out import DISPLAY_OUT
import urequests as requests
import network
import ujson as json
'''
ADC_MODE_VCC = 255
ADC_MODE_ADC = 0

def set_adc_mode(mode):
    sector_size = bdev.SEC_SIZE
    flash_size = esp.flash_size() # device dependent
    init_sector = int(flash_size / sector_size - 4)
    data = bytearray(esp.flash_read(init_sector * sector_size, sector_size))
    if data[107] == mode:
        return  # flash is already correct; nothing to do
    else:
        data[107] = mode  # re-write flash
        esp.flash_erase(init_sector)
        esp.flash_write(init_sector * sector_size, data)
        print("ADC mode changed in flash; restart to use it!")
        return
'''

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print("Connessione al WiFi...")
        wlan.active(True)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print("Connesso al WiFi:", ssid)
    print("Indirizzo IP:", wlan.ifconfig()[0])
    
def register_gateway(gateway_id, gateway_key):
    # Dettagli del gateway
    gateway_data = {
        "gateway_id": gateway_id,
        "key": gateway_key,
        # Altri dettagli del gateway se necessario
    }

    # URL per registrare il gateway su TTN
    ttn_api_url = ttn_config['gateway_server_address']

    headers = {
        "Content-Type": "application/json",
        "Authorization": ttn_config['api_key']  # Sostituisci con il tuo token di accesso
    }

    try:
        response = requests.post(ttn_api_url, headers=headers, data=json.dumps(gateway_data))
        if response.status_code == 201:
            print("Gateway registrato con successo su TTN!")
        else:
            print("Errore durante la registrazione del gateway:", response.status_code, response.text)
    except Exception as e:
        print("Errore durante la richiesta:", e)

#check pins for spi
def test_hardware_connections():
    print("Verifica collegamenti hardware:")
    pins_to_check = ['sck', 'mosi', 'miso', 'ss', 'dio_0', 'reset', 'gpio']
    for pin_name in pins_to_check:
        pin = Pin(lora_pin[pin_name], Pin.IN)
        print("Stato del pin {}: {} /n".format(pin_name, pin.value()))
        time.sleep_ms(100)

def test_power_supply():
    print("Verifica alimentazione:")
    vcc = ADC(Pin(lora_pin['power_supply']))
    vcc.read()
    adc = ADC(Pin(lora_pin['power_supply']))  
    adc.atten(ADC.ATTN_11DB)
    voltage = adc.read() * 3.6 / 4095
    
    print("Tensione vcc alimentazione:", vcc, "V /n")
    print("Tensione di alimentazione:", voltage, "V /n")
'''
    if 1.8 <= voltage <= 3.7:
        print("Tensione di alimentazione nella gamma corretta")
    else:
        print("Attenzione: Tensione di alimentazione fuori dalla gamma consigliata")
'''
    time.sleep_ms(100)
    
def test_display_out():
    display = DISPLAY_OUT("Hello", "MicroPython", "Testing")
    print("Test completato con successo.")
    time.sleep_ms(100)

def cb(events):
    if events & SX1262.RX_DONE:
        msg, err = sx.recv()
        error = SX1262.STATUS[err]
        print('Receive: {}, {}'.format(msg, error))
    elif events & SX1262.TX_DONE:
        print('TX done.')
    time.sleep_ms(100)

def find_first_available_spi():
    for i in range(3):  # Si presume che gli ID dei bus SPI siano da 0 a 2
        try:
            spi = SPI(i)
            # Se l'inizializzazione non genera errori, restituisci l'ID trovato
            spi.deinit()  # Deinizializza il bus SPI per liberare le risorse
            return i
        except Exception as e:
            pass  # Se si verifica un errore, passa al prossimo ID
        time.sleep_ms(100)
    print("Nessun SPI ID trovato")  # Stampa il messaggio di errore
    raise SystemExit  # Termina lo script
    

# Esegui le verifiche prima di inizializzare il modulo LoRa
connect_to_wifi(hotspot_config['ssid'], hotspot_config['password'])
# Registrazione del gateway su TTN
register_gateway(ttn_config['gateway_id'], ttn_config['gateway_eui'])
test_hardware_connections()
test_power_supply()

# Creazione dell'oggetto SX1262 e inizializzazione del modulo LoRa
bus_id = find_first_available_spi()
sx = SX1262(  spi_bus=bus_id,
              clk=lora_pin['sck'],
              mosi=lora_pin['mosi'],
              miso=lora_pin['miso'],
              cs=lora_pin['ss'],
              irq=lora_pin['dio_0'],
              rst=lora_pin['reset'],
              gpio=lora_pin['gpio'])
print ("creato l'oggetto sx1262.", sx)

# LoRa
freq = SX1262.setFrequency(loraParameters['frequency'])
print ("frequenza settata a valore:", freq)
bw = SX1262.setBandwidth(loraParameters['signal_bandwidth'])
print (print ("bandwidth settato a valore:", bw)
sf = SX1262.setSpreadingFactor(loraParameters['speading_factor'])
print ("spreading factor settato a valore:", sf)
cr = SX1262.setCodingRate(loraParameters['coding_rate'])
print ("coding rate settato a valore:", cr)
syncWorld = SX1262.setSyncWord(loraParameters['sync_word'], [controlBits])
print ("syncworld settato a valore:", syncWord)
power = SX1262.setOutputPower(loraParameters['power']
print ("power settato a valore:", power)
power = SX1262.setPreambleLength(loraParameters['preamble_lenght']
print ("preamble lenght settato a valore:", preamble lenght)



'''
SX1262.begin(freq=434.0, bw=125.0, sf=9, cr=7, syncWord=0x12, power=14, currentLimit=60.0
preambleLength=8, implicit=False, implicitLen=0xFF, crcOn=True, txIq=False, rxIq=False,
tcxoVoltage=1.6, useRegulatorLDO=False, blocking=True)
'''
#sx.begin(
    

sx.setBlockingCallback(False, cb)

while True:
    sx.send(b'Ping')
    time.sleep(10)

