import time
from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C

# Costanti per la configurazione
SET_OLED_WIDTH = 128
SET_OLED_HEIGHT = 64
SET_RST = 21
SET_SCL = 18
SET_SDA = 17

class DISPLAY_OUT:
    def __init__(self, *rows):
        self.rows = rows
        self.display_out()

    def display_out(self):
        i2c_rst = Pin(SET_RST, Pin.OUT)
        i2c_rst.value(0)
        time.sleep_ms(5)
        i2c_rst.value(1)

        i2c_scl = Pin(SET_SCL, Pin.OUT, Pin.PULL_UP)
        i2c_sda = Pin(SET_SDA, Pin.OUT, Pin.PULL_UP)

        # Create the SoftI2C object
        i2c = SoftI2C(scl=i2c_scl, sda=i2c_sda)

        # Create the display object
        oled = SSD1306_I2C(SET_OLED_WIDTH, SET_OLED_HEIGHT, i2c)

        oled.fill(0)
        y = 0
        for row in self.rows:
            oled.text(row, 0, y)
            y += 20
        oled.show()
