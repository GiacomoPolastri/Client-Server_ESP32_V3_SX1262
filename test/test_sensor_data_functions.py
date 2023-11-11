from sensor.sensor_data import DHTSensor
import time

def test_measure():
    # Test del metodo measure
    dht_sensor = DHTSensor()
    result = dht_sensor.measure()
    assert isinstance(result, tuple), "Il metodo measure dovrebbe restituire una tupla"

def test_get_temperature():
    # Test del metodo get_temperature
    dht_sensor = DHTSensor()
    result = dht_sensor.get_temperature()
    assert isinstance(result, (int, float)), "Il metodo get_temperature dovrebbe restituire un numero"

def test_get_humidity():
    # Test del metodo get_humidity
    dht_sensor = DHTSensor()
    result = dht_sensor.get_humidity()
    assert isinstance(result, (int, float)), "Il metodo get_humidity dovrebbe restituire un numero"

# Esegui i test
test_measure()
time.sleep(0.22)
test_get_temperature()
time.sleep(0.22)
test_get_humidity()

