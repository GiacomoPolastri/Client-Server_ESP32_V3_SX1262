#Display OLED
oled_config = {
	'width': 128,
	'weight': 64,
	'rst': 21,
	'scl': 18,
	'sda': 17
}

#Heltec Lora32 v3.1
device_config = {
    'miso':11,
    'mosi':10,
    'ss':8,
    'sck':9,
    'dio_0':14,
    'reset':12,
    'led':35,  
}


lora_parameters = {
    'frequency': 915E6, 
    'tx_power_level': 2, 
    'signal_bandwidth': 125E3,    
    'spreading_factor': 8, 
    'coding_rate': 5, 
    'preamble_length': 8,
    'implicit_header': False, 
    'sync_word': 0x12, 
    'enable_CRC': False,
    'invert_IQ': False,
}

wifi_config = {
    'ssid':'PrimoPiano',
    'password':'58652352692378578774'
}
