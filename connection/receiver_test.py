# test_receiver.py

from receiver import get_input, get_numeric_input, receive
import builtins
import sys
import json
from time import time, sleep

# Mocking select.select function
def mock_select(r, w, x, timeout):
    return ([sys.stdin], [], []) if time() % 10 < 5 else ([], [], [])

# Mocking the Pin and SX1262 classes
class MockPin:
    def __init__(self, id):
        self.id = id

class MockSX1262:
    STATUS = {0: 'Success'}

    def __init__(self):
        pass

    def send(self, data):
        print(f"Mock send: {data}")

    def recv(self):
        return json.dumps({"temperature": 25, "humidity": 60}).encode(), 0

# Mocking the display function
def mock_display(*args):
    print(f"Mock display: {args}")

# Mocking sleep function
def mock_sleep(duration):
    print(f"Mock sleep for {duration} seconds")

# Replacing actual functions and classes with mocks
builtins.Pin = MockPin
builtins.SX1262 = MockSX1262
builtins.display = mock_display
builtins.sleep = mock_sleep
select = mock_select

# Test the get_input function
def test_get_input():
    print("Testing get_input with timeout...")
    print(get_input("Enter something (timeout test):", "default", 5))

    print("Testing get_input with valid input...")
    print(get_input("Enter something (valid input test):", "default", 5))

# Test the get_numeric_input function
def test_get_numeric_input():
    print("Testing get_numeric_input with invalid and valid input...")
    print(get_numeric_input("Enter a number (invalid input test):", 0, 5))
    print(get_numeric_input("Enter a number (valid input test):", 0, 5))

# Test the receive function
def test_receive():
    mock_sx1262 = MockSX1262()
    receive(mock_sx1262)

# Running the tests
test_get_input()
test_get_numeric_input()
test_receive()
