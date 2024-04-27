#Display OLED
oled_config = {
	'width': 128,
	'weight': 64,
	'rst': 21,
	'scl': 18,
	'sda': 17
}

#Heltec Lora32 v3.1
lora_pin = {
    'miso':11,
    'mosi':10,
    'ss':8,
    'sck':9,
    'dio_0':14,
    'reset':12,
    'led':35,
    'gpio':13, #BUSY pin
    'power_supply':1,
}

lora_parameters = {
    'frequency': 434,
    'bw' : 500,
    'power': 14,
    'current_limit':60.0,
    'tx_power_level': 2, 
    'signal_bandwidth': 125.0,    
    'spreading_factor': 8, 
    'coding_rate': 5, 
    'preamble_length': 8,
    'implicit_len': 0xFF,
    'sync_word': 0x12, 
}