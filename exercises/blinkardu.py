from pyfirmata import Arduino
from time import sleep

board = Arduino('/dev/ttyACM2')
while(1):
   board.digital[13].write(1)
   sleep(5000)
   board.digital[13].write(0)
   sleep(5000)
