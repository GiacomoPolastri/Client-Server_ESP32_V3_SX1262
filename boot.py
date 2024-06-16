from connection.spi_connection import set_spi_connection, begin
from connection.sender import send
#from connection.receiver import receive

sx = set_spi_connection()
begin(sx)
#receive(sx)
send(sx)