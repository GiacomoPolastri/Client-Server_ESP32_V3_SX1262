import time
from machine import Pin, SoftI2C
from display.ssd1306 import SSD1306_I2C
from config.config_pin import *

class DISPLAY_OUT:
    def __init__(self, *rows):
        self.rows = rows
        self.display_out()

    def display_out(self):
        i2c_rst = Pin(oled_config['rst'], Pin.OUT)
        i2c_rst.value(0)
        time.sleep_ms(5)
        i2c_rst.value(1)
    #device_config['sck']
        i2c_scl = Pin(oled_config['scl'], Pin.OUT, Pin.PULL_UP)
        i2c_sda = Pin(oled_config['sda'], Pin.OUT, Pin.PULL_UP)

        # Create the SoftI2C object
        i2c = SoftI2C(scl=i2c_scl, sda=i2c_sda)

        # Create the display object
        oled = SSD1306_I2C(oled_config['width'], oled_config['wight'], i2c)

        oled.fill(0)
        y = 0
        for row in self.rows:
            oled.text(row, 0, y)
            y += 20
        oled.show()
