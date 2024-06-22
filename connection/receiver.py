from time import time
from display.display_out import display
from sensor.sensor_data import DHTSensor
from LoRa.sx1262 import SX1262
import sys
import json
from select import select

def get_input(prompt, default_value=0, timeout=5):
    print(prompt)
    start_time = time()
    user_input = ""

    while time() - start_time < timeout:
        if sys.stdin in select([sys.stdin], [], [], timeout)[0]:
            user_input = sys.stdin.readline().strip()
            if user_input:
                return user_input

    print(f"Timeout reached. Using default value: {default_value}")
    return str(default_value)

def get_numeric_input(prompt, default_value=0, timeout=5):
    value = get_input(prompt, default_value, timeout)
    while not value.isdigit():
        value = get_input(prompt, default_value, timeout)
    return int(value)

def receive(sx):
    global lora, array_data
    array_data = []
    lora = sx

    # Sampling period
    sampling_period = get_numeric_input("Enter the sampling period in seconds:")
    print("You entered:", sampling_period)

    # Sampling time
    sampling_time = get_numeric_input("Enter after how many hours you want to sample:")
    print("You entered:", sampling_time)

    # Number of samples to acquire
    n_samples = get_numeric_input("Enter the number of samples to acquire:")
    print("You entered:", n_samples)

    # Create packet dictionary
    packet = {
        "sampling_period": sampling_period,
        "sampling_time": sampling_time,
        "n_samples": n_samples,
    }

    request = False  # Initialize the request variable

    if n_samples != 0:
        lora.send(bytes(json.dumps(packet).encode()))
        request = True
    else:
        n_samples = n_samples + 1  # Increment n_samples if it is zero

    print("Receiving...")
    display("Receiving...")

    while n_samples != 0:
        msg, err = lora.recv()
        if len(msg) > 0:
            error = SX1262.STATUS[err]
            print('Receive: {}, {}'.format(msg, error))
            try:
                message = json.loads(msg)
                if all (key in message for key in ['temperature', 'humidity']):

                    display ('Receive',
                             'Temperature',
                             str(message['temperature']),
                             'Humidity',
                             str(message['humidity']))
                else:
                    display('Receive',msg)
            except Exception as e:
                print(f"Error decoding JSON: {e}")
                display('Receive',msg)

            if request:
                array_data.append(msg)
            n_samples -= 1

    if request:
        print(array_data)
        request = False

# Testing functions manually
def test_functions():
    # Mocking select.select for manual testing
    def mock_select(r, w, x, timeout):
        return ([sys.stdin], [], []) if time() < 5 else ([], [], [])

    # Replace select.select with mock_select in the get_input function
    global select
    select = mock_select

    # Test get_input with timeout
    print("Testing get_input with timeout...")
    print(get_input("Enter something (timeout test):", "default", 5))

    # Test get_input with valid input
    print("Testing get_input with valid input...")
    print(get_input("Enter something (valid input test):", "default", 5))

    # Test get_numeric_input with invalid and valid input
    print("Testing get_numeric_input with invalid and valid input...")
    print(get_numeric_input("Enter a number (invalid input test):", 0, 5))
    print(get_numeric_input("Enter a number (valid input test):", 0, 5))

    # Mocking SX1262 for receive function testing
    class MockSX1262:
        def __init__(self):
            self.STATUS = {0: "Success"}

        def send(self, data):
            print("Sending data:", data)

        def recv(self):
            return (json.dumps({"temperature": 25, "humidity": 60}).encode(), 0)

    print("Testing receive function...")
    mock_sx1262 = MockSX1262()
    receive(mock_sx1262)

# Run tests
test_functions()
