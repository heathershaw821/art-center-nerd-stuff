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
  # MUST be byte strings b'command arg1 arg2 ...'
  # NOT default Unicode strings, they are more than a byte in length
  #  SEE -> https://en.wikipedia.org/wiki/UTF-8#Implementations_and_adoption:~:text=Code%20point%20%E2%86%94-,UTF%2D8%20conversion,-First%20code%20point
  ser.write(b'180')
  sleep(3)
  ser.write(b'90')
  sio.flush() # it is buffering. required to get the data out *now*
  hello = sio.readline()
  print(hello)



