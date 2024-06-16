from machine import SPI, Pin
from LoRa.sx1262 import SX1262
from config.config_pin import lora_pin, lora_parameters

# Creazione dell'oggetto SX1262 e inizializzazione del modulo LoRa
def set_spi_connection():
    #bus_id = find_first_available_spi()
    try:
        sx = SX1262(spi_bus=1,
              clk=Pin(lora_pin['sck']),
              miso=Pin(lora_pin['miso']),
              mosi=Pin(lora_pin['mosi']),
              cs=Pin(lora_pin['ss']),
              rst=Pin(lora_pin['reset']),
              irq=Pin(lora_pin['dio_0']),
              gpio=Pin(lora_pin['gpio']))
        print ("creato l'oggetto sx1262.", sx)
        return sx
    except Exception as e:
        pass
    print ("Non è stato creato l'oggetto")
        
def begin(sx):
    try:
        sx.begin(freq=lora_parameters['frequency'],
                 bw=lora_parameters['bw'],
                 sf=lora_parameters['spreading_factor'],
                 cr=lora_parameters['coding_rate'],
                 syncWord=lora_parameters['sync_word'],
                 power=lora_parameters['power'],
                 currentLimit=lora_parameters['current_limit'],
                 preambleLength=lora_parameters['preamble_length'],
                 implicit=False,
                 implicitLen=lora_parameters['implicit_len'],
                 crcOn=True,
                 txIq=False,
                 rxIq=False,
                 tcxoVoltage=1.7,
                 useRegulatorLDO=False,
                 blocking=True)
        print("Modulo LoRa inizializzato correttamente.")
    except Exception as e:
        print(f"Errore durante l'inizializzazione del modulo LoRa: {e}")