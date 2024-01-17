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
    'frequency': 868, 
    'power': 14,
    'current_limit':60.0,
    'tx_power_level': 2, 
    'signal_bandwidth': 125E3,    
    'spreading_factor': 8, 
    'coding_rate': 5, 
    'preamble_length': 8,
    'implicit_header': False, 
    'implicit_len': 0xFF,
    'sync_word': 0x12, 
    'enable_CRC': False,
    'invert_IQ': False,
}

wifi_config = {
    'ssid':'PrimoPiano',
    'password':'58652352692378578774'
}

hotspot_confi = {
    'ssid' : 'iPhone',
    'password' : 'cavalloBlu'
}

ttn_config = {
    'gateway_id' : 'eui-f412fafffe6f148c',
    'gateway_eui' : 'F412FAFFFE6F148C',
    'api_key' : 'NNSXS.4U3WKSJC7UBGLXJ2LOI4NZVUSXCPMKBIMUY4BFI.DAZJV4KBNP3KO5DMRDFETNVSLQQPG75J4X3BOFRQZ4VEKUCHXZDQ',
    'gateway_server_address' : 'eu1.cloud.thethings.network'
}