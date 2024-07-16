# test_spi_connection.py

from spi_connection import set_spi_connection, begin

# Mocking the Pin class
class MockPin:
    def __init__(self, id):
        self.id = id

# Mocking the SPI class
class MockSPI:
    def __init__(self, spi_bus):
        self.spi_bus = spi_bus

# Mocking the SX1262 class
class MockSX1262:
    def __init__(self, spi_bus, clk, miso, mosi, cs, rst, irq, gpio):
        self.spi_bus = spi_bus
        self.clk = clk
        self.miso = miso
        self.mosi = mosi
        self.cs = cs
        self.rst = rst
        self.irq = irq
        self.gpio = gpio

    def begin(self, freq, bw, sf, cr, syncWord, power, currentLimit, preambleLength, implicit, implicitLen, crcOn, txIq, rxIq, tcxoVoltage, useRegulatorLDO, blocking):
        print(f"MockSX1262 initialized with freq={freq}, bw={bw}, sf={sf}, cr={cr}")

# Replace the actual machine.Pin and SX1262 with our mocks
import builtins
builtins.Pin = MockPin
builtins.SPI = MockSPI
SX1262 = MockSX1262

# Configuration mock
lora_pin = {
    'sck': 5,
    'miso': 19,
    'mosi': 27,
    'ss': 18,
    'reset': 23,
    'dio_0': 26,
    'gpio': 14
}

lora_parameters = {
    'frequency': 868.1,
    'bw': 125,
    'spreading_factor': 12,
    'coding_rate': 5,
    'sync_word': 0x12,
    'power': 14,
    'current_limit': 100,
    'preamble_length': 8,
    'implicit_len': 0
}

# Test the set_spi_connection function
def test_set_spi_connection():
    sx = set_spi_connection()
    assert isinstance(sx, MockSX1262), "Failed to create SX1262 object"
    print("set_spi_connection() passed.")

# Test the begin function
def test_begin():
    sx = set_spi_connection()
    begin(sx)
    print("begin() passed.")

# Run the tests
test_set_spi_connection()
test_begin()
