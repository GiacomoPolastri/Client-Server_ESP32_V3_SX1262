from machine import Pin
import dht
import time

class DHTSensor:
    Pin_Data = const(48)

    def __init__(self):
        self.pin_data = self.Pin_Data
        self.sensor = dht.DHT11(Pin(self.pin_data))

    def measure(self):
        self.sensor.measure()
        temperature = self.sensor.temperature()
        humidity = self.sensor.humidity()
        return temperature, humidity

    def get_temperature(self):
        temperature, _ = self.measure()
        return temperature

    def get_humidity(self):
        _, humidity = self.measure()
        return humidity
