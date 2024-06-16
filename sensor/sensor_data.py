from machine import Pin
import dht
import time


class DHTSensor:
    Pin_Data = const(48)

    def __init__(self):
        self.pin_data = self.Pin_Data
        try:
            self.sensor = dht.DHT11(Pin(self.pin_data))
            print("DHT11 sensor initialized successfully.")
        except Exception as e:
            print(f"Error initializing DHT11 sensor: {e}")

    def measure(self):
        try:
            self.sensor.measure()
            temperature = self.sensor.temperature()
            humidity = self.sensor.humidity()
            return temperature, humidity
        except Exception as e:
            print(f"Error measuring DHT11 sensor: {e}")
            return None, None

    def get_temperature(self):
        temperature, _ = self.measure()
        if temperature is not None:
            return temperature
        else:
            print("Unable to retrieve temperature.")

    def get_humidity(self):
        _, humidity = self.measure()
        if humidity is not None:
            return humidity
        else:
            print("Unable to retrieve humidity.")