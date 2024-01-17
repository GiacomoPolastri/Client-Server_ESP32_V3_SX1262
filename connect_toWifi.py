import time
from ttn import TTN, Gateway

# Configura le informazioni del gateway
app_id = 'progetto-lora'
access_key = 'NNSXS.YWTZWWCR2TV5EJM5JNBVP7FK5ONQIHUU4QBNVIQ.PZIUCF6V65ZQXOALRCNBIYMT5PTVUKGK3QORTXNNYKACB2RTHKFQ'
gateway_eui = 'F412FAFFFE6F148C'  # Il tuo Gateway EUI

# Configura le informazioni TTN
handler = TTN(app_id, access_key)

# Crea un gateway con l'ID e l'EUI specifici
gateway = Gateway(handler, gateway_eui, 'eui-f412fafffe6f148c')

# Funzione per la gestione dei messaggi ricevuti
def downlink_callback(msg, client):
    print("Messaggio ricevuto:", msg)

# Imposta la funzione di callback per i messaggi ricevuti
gateway.set_callback(downlink_callback)

# Avvia il gateway LoRa
gateway.start()

# Loop principale
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break

# Termina il gateway
gateway.stop()
