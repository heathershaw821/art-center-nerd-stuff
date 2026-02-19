#!/usr/bin/env python3
# https://pyserial.readthedocs.io/en/stable/shortintro.html

import serial
import io
from time import sleep


with serial.Serial() as ser:
  ser.baudrate = 115200
  ser.port = '/dev/serial0'
  ser.open()
  sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
  
  ser.write(b'180')
  sleep(3)
  ser.write(b'90')
  sio.flush() # it is buffering. required to get the data out *now*
  hello = sio.readline()
  print(hello)



