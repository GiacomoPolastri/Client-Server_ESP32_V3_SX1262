# test_display_out.py

from display_out import display

def mock_sleep_ms(duration):
    print(f"Mock sleep for {duration}ms")

def mock_pin(id, mode):
    class MockPin:
        def __init__(self, id, mode):
            self.id = id
            self.mode = mode
            self.state = None

        def value(self, val=None):
            if val is not None:
                self.state = val
            return self.state

    return MockPin(id, mode)

def mock_softi2c(scl, sda):
    class MockSoftI2C:
        def __init__(self, scl, sda):
            self.scl = scl
            self.sda = sda

    return MockSoftI2C(scl, sda)

def mock_ssd1306_i2c(width, height, i2c):
    class MockSSD1306_I2C:
        def __init__(self, width, height, i2c):
            self.width = width
            self.height = height
            self.i2c = i2c
            self.buffer = [[" "]*width for _ in range(height // 12)]

        def fill(self, color):
            for row in self.buffer:
                for i in range(len(row)):
                    row[i] = " " if color == 0 else "#"

        def text(self, text, x, y):
            row = y // 12
            for i, char in enumerate(text):
                if 0 <= x + i < self.width:
                    self.buffer[row][x + i] = char

        def show(self):
            for row in self.buffer:
                print("".join(row))

    return MockSSD1306_I2C(width, height, i2c)

# Replace the hardware-specific functions with mocks
import builtins
builtins.sleep_ms = mock_sleep_ms
builtins.Pin = mock_pin
builtins.SoftI2C = mock_softi2c

# Configuration mock
oled_config = {
    'rst': 16,
    'scl': 5,
    'sda': 4,
    'width': 128,
    'weight': 64
}

# Test the display class
def test_display():
    test_rows = ["Hello,", "MicroPython!"]
    d = display(*test_rows)

test_display()
