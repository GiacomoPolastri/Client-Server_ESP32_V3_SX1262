from time import sleep_ms
from connection.spi_connection import set_spi_connection, begin
from connection.sender import send

sx = set_spi_connection()
sleep_ms(1000)
begin(sx)
sleep_ms(1000)
send(sx)
