# test_sender.py

from sender import send, cb
import json
import builtins

# Mocking the Pin, SX1262, DHTSensor, and display functions

class MockPin:
    def __init__(self, id):
        self.id = id

class MockSX1262:
    RX_DONE = 1
    TX_DONE = 2
    STATUS = {0: 'OK'}

    def __init__(self, spi_bus, clk, miso, mosi, cs, rst, irq, gpio):
        self.spi_bus = spi_bus

    def setBlockingCallback(self, state, callback):
        self.callback = callback

    def send(self, data):
        print(f"Mock send: {data}")

    def recv(self):
        return json.dumps({
            'n_samples': 5,
            'sampling_time': 0.1,
            'sampling_period': 5
        }), 0

class MockDHTSensor:
    def measure(self):
        return 25, 60

def mock_display(*args):
    print(f"Mock display: {args}")

def mock_sleep(duration):
    print(f"Mock sleep for {duration} seconds")

# Replacing actual classes and functions with mocks
builtins.Pin = MockPin
builtins.SX1262 = MockSX1262
builtins.DHTSensor = MockDHTSensor
builtins.display = mock_display
builtins.sleep = mock_sleep

# Configuration mock
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

# Test the send function
def test_send():
    sx = MockSX1262(1, None, None, None, None, None, None)
    send(sx)

# Test the cb function
def test_cb():
    sx = MockSX1262(1, None, None, None, None, None, None)
    lora = sx
    cb(SX1262.RX_DONE)
    cb(SX1262.TX_DONE)

# Running the tests
test_send()
test_cb()
