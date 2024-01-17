from config.config_pin import lora_pin
from LoRa.sx1262 import SX1262
from machine import Pin, SoftSPI, ADC
import time

def test_hardware_connections():
    print("Verifica collegamenti hardware:")
    pins_to_check = ['sck', 'mosi', 'miso', 'ss', 'dio_0', 'reset', 'gpio']
    for pin_name in pins_to_check:
        pin = Pin(lora_pin[pin_name], Pin.IN)
        print("Stato del pin {}: {}".format(pin_name, pin.value()))

def test_power_supply():
    print("Verifica alimentazione:")
    adc = ADC(Pin(lora_pin['power_supply']))  # Assicurati di definire correttamente 'power_supply' nel file di configurazione
    adc.atten(ADC.ATTN_11DB)
    voltage = adc.read() * 3.6 / 4095

    print("Tensione di alimentazione:", voltage, "V")
    if 1.8 <= voltage <= 3.7:
        print("Tensione di alimentazione nella gamma corretta")
    else:
        print("Attenzione: Tensione di alimentazione fuori dalla gamma consigliata")

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

# Esegui le verifiche prima di inizializzare il modulo LoRa
test_hardware_connections()
test_power_supply()

# Creazione dell'oggetto SX1262 e inizializzazione del modulo LoRa
sx = SX1262(1,
              clk=lora_pin['sck'],
              mosi=lora_pin['mosi'],
              miso=lora_pin['miso'],
              cs=lora_pin['ss'],
              irq=lora_pin['dio_0'],
              rst=lora_pin['reset'],
              gpio=lora_pin['gpio'])
# LoRa
sx.begin(freq=923, bw=500.0, sf=12, cr=8, syncWord=0x12,
         power=-5, currentLimit=60.0, preambleLength=8,
         implicit=False, implicitLen=0xFF,
         crcOn=True, txIq=False, rxIq=False,
         tcxoVoltage=1.7, useRegulatorLDO=False, blocking=True)

sx.setBlockingCallback(False, cb)

while True:
    sx.send(b'Ping')
    time.sleep(10)

