import time
from machine import Pin, SoftI2C
import ssd1306

# Heltec LoRa 32 with OLED Display
width = 128
height = 64

#Set Pins
rst = 21
scl = 18
sda = 17

# OLED reset pin
i2c_rst = Pin(rst, Pin.OUT)
# Initialize the OLED display
i2c_rst.value(0)
time.sleep_ms(5)
i2c_rst.value(1)  # must be held high after initialization

# Setup the I2C lines
i2c_scl = Pin(scl, Pin.OUT, Pin.PULL_UP)
i2c_sda = Pin(sda, Pin.OUT, Pin.PULL_UP)

# Create the SoftI2C object
i2c = SoftI2C(scl=i2c_scl, sda=i2c_sda)

# Create the display object
oled = ssd1306.SSD1306_I2C(width, height, i2c)

def dispaly_out(text):
    oled.fill(0)
    oled.text('text', 0, 15)
    oled.show()
    return print('done')
