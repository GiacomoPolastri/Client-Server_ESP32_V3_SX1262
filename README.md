# LoRa Communication System: Client-Server Implementation

Welcome to the GitHub repository for the LoRa Communication System project. This project demonstrates a client-server system using the LoRa protocol, enabling data exchange between IoT devices based on ESP32 LoRa. The system uses the LoRa SX1262 module for long-distance, low-power communication, integrated with an OLED SSD1306 display for data visualization and a DHT11 sensor for temperature and humidity detection.

## Repository Link
[LoRa Communication System on GitHub](https://github.com/GiacomoPolastri/LoRa_Comunication)

## Table of Contents
1. [Introduction](#introduction)
2. [System Architecture](#system-architecture)
3. [UML Schemas](#uml-schemas)
4. [File Descriptions](#file-descriptions)
5. [Installation and Setup](#installation-and-setup)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction
This project aims to develop a client-server system using the LoRa protocol to facilitate communication and data exchange between ESP32 LoRa-based IoT devices. It employs the LoRa SX1262 module for long-range data transmission with low power consumption, integrated with an SSD1306 OLED display for data visualization and a DHT11 sensor for temperature and humidity detection.

## System Architecture
The system consists of the following main components:
- **LoRa SX1262 Module**: Manages LoRa communication between devices, configured with specific parameters like frequency, power, and spreading factor.
- **OLED SSD1306 Display**: Displays status information and relevant data, configured via an I2C connection.
- **DHT11 Sensor**: Detects ambient temperature and humidity, providing context data to the system.

## UML Schemas

## Class Diagram
![image](https://github.com/user-attachments/assets/ea25eb12-d977-4ccf-86be-0c0d0b03b4b2)

## Sequence Diagram
![image](https://github.com/user-attachments/assets/28c126fa-41b2-4984-90db-3298aa858e60)

## File Descriptions

### `config_pin.py`
Defines the pin configurations and parameters for the hardware devices used in the project.

- **Display OLED**:
  - Width: 128
  - Height: 64
  - Reset Pin: 21
  - SCL Pin: 18
  - SDA Pin: 17

- **LoRa Module**:
  - MISO Pin: 11
  - MOSI Pin: 10
  - SS Pin: 8
  - SCK Pin: 9
  - DIO_0 Pin: 14
  - Reset Pin: 12
  - LED Pin: 35
  - GPIO Pin: 13
  - Power Supply Pin: 1

- **LoRa Parameters**:
  - Frequency: 434 MHz
  - Bandwidth: 500 kHz
  - Power: 14 dBm
  - Current Limit: 60 mA
  - TX Power Level: 2
  - Signal Bandwidth: 125 kHz
  - Spreading Factor: 8
  - Coding Rate: 5
  - Preamble Length: 8
  - Implicit Length: 0xFF
  - Sync Word: 0x12

### `spi_connection.py`
Configures and initializes the LoRa SX1262 module using an SPI connection.

- **Libraries Imported**:
  - `machine.SPI`, `machine.Pin`: For SPI communication and hardware pin management.
  - `LoRa.sx1262.SX1262`: Interacts with the LoRa SX1262 module.
  - `config.config_pin`: Imports LoRa pin and parameter configurations.

- **Functions**:
  - `set_spi_connection()`: Initializes the SX1262 instance with the specified pins.
  - `begin(sx)`: Initializes the SX1262 module with specified parameters.

### `display_out.py`
Manages the OLED SSD1306 display via an I2C connection.

- **Libraries Imported**:
  - `time.sleep_ms`: Manages delays in milliseconds.
  - `machine.Pin`, `machine.SoftI2C`: Manages hardware pins and I2C communication.
  - `display.ssd1306.SSD1306_I2C`: Interacts with the OLED display.
  - `config.config_pin`: Imports OLED display configurations.

- **Class `display`**:
  - `__init__(self, *rows)`: Constructor to initialize and display rows of text.
  - `display(self)`: Configures and displays data on the OLED.

### `server_receiver.py`
Operates as the server, receiving data sent by the client via the LoRa SX1262 module.

- **Libraries Imported**:
  - `time`, `sys`, `json`, `select`: For time management, input/output operations, JSON manipulation, and I/O multiplexing.
  - `display.display_out`: For OLED display management.
  - `sensor.sensor_data`: For DHT11 sensor data acquisition.
  - `LoRa.sx1262.SX1262`: For LoRa SX1262 module interaction.

- **Functions**:
  - `cb(events)`: Callback function for handling LoRa events (data reception and transmission).
  - `get_input(prompt, default_value=0, timeout=5)`: Gets user input with a timeout.
  - `get_numeric_input(prompt, default_value=0, timeout=5)`: Gets numeric input from the user with a timeout.
  - `receive(sx)`: Manages data reception from the client and processes the received information.

### `sensor_data.py`
Defines the `DHTSensor` class for interacting with the DHT11 sensor.

- **Libraries Imported**:
  - `machine.Pin`: Manages hardware pins.
  - `dht`: Interfaces with the DHT11 sensor.
  - `time`: For time management.

- **Class `DHTSensor`**:
  - `Pin_Data`: Constant representing the DHT11 data pin.
  - `__init__(self)`: Initializes the DHT11 sensor.
  - `measure(self)`: Measures and returns temperature and humidity.
  - `get_temperature(self)`: Returns only the temperature.
  - `get_humidity(self)`: Returns only the humidity.

### `client_sender.py`
Operates as the client, acquiring data from the DHT11 sensor and sending it to the server.

- **Libraries Imported**:
  - `time.sleep`: For managing delays.
  - `display.display_out`: For OLED display management.
  - `sensor.sensor_data`: For DHT11 sensor data acquisition.
  - `config.config_pin`: For LoRa module configuration parameters.
  - `LoRa.sx1262.SX1262`: For LoRa SX1262 module interaction.
  - `json`: For JSON data manipulation.

- **Functions**:
  - `cb(events)`: Callback function for handling LoRa events.
  - `send()`: Acquires sensor data, encapsulates it in a JSON packet, and sends it to the server.

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/GiacomoPolastri/LoRa_Comunication.git
   ```
2. Install the necessary libraries and dependencies.
3. Configure the hardware connections according to the pin configurations in `config_pin.py`.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to explore, modify, and enhance the project. For any questions or support, please contact Giacomo Polastri at giacomo.polastri@example.com.
