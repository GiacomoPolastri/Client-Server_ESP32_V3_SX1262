# test_sensor_data.py

from sensor_data import DHTSensor

# Mocking the Pin class
class MockPin:
    def __init__(self, id):
        self.id = id

# Mocking the dht.DHT11 class
class MockDHT11:
    def __init__(self, pin):
        self.pin = pin
        self._temperature = 25  # Mock temperature value
        self._humidity = 60     # Mock humidity value

    def measure(self):
        # Simulate measurement delay
        time.sleep(0.2)

    def temperature(self):
        return self._temperature

    def humidity(self):
        return self._humidity

# Mocking the time.sleep function
def mock_sleep(duration):
    print(f"Mock sleep for {duration} seconds")

# Replace the actual machine.Pin and dht.DHT11 with our mocks
import builtins
builtins.Pin = MockPin
dht.DHT11 = MockDHT11
time.sleep = mock_sleep

# Test the DHTSensor class
def test_dhtsensor():
    sensor = DHTSensor()
    
    # Test measure method
    temperature, humidity = sensor.measure()
    assert temperature == 25, f"Expected temperature to be 25, but got {temperature}"
    assert humidity == 60, f"Expected humidity to be 60, but got {humidity}"
    print("measure() method passed.")

    # Test get_temperature method
    temperature = sensor.get_temperature()
    assert temperature == 25, f"Expected temperature to be 25, but got {temperature}"
    print("get_temperature() method passed.")

    # Test get_humidity method
    humidity = sensor.get_humidity()
    assert humidity == 60, f"Expected humidity to be 60, but got {humidity}"
    print("get_humidity() method passed.")

test_dhtsensor()
