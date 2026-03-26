#!/usr/bin/env python3

import pickle
import serial
import io
from time import sleep

class Protocol:
	actions =	{	# our "commands" (remember these are bidirectional on agreed terms)
		# OUTPUTS (Actions)
		"head": None,		 # <<< right now
		"forward": None,
		"backward": None,
		"left": None,
		"right": None,
		"blink": None,
		# INPUTS (Sensors)
		"distance": None, # <<< right now
		# .........
	}

	SOL = ""	 # start of action "string" (not always a literal "string")
	EOL = "\n" # End of action "string"
	send = None
	receive = None

class Serial(Protocol):
	def __init__(self):
		# for every protocol application, you will change these to fit
		self.SOL = ""
		self.EOL = "\r\n"
		self.actions["head"] = self.head_function
		self.actions["distance"] = self.distance_function
		self.actions["blink"] = self.blink_function

	def send(self):
		pass
	def receive(self):
		with serial.Serial() as ser:
			ser.baudrate = 115200
			ser.port = '/dev/serial0'
			ser.open()
			sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
			# MUST be byte strings b'command arg1 arg2 ...'
			# NOT default Unicode strings, they are more than a byte in length
			#	SEE -> https://en.wikipedia.org/wiki/UTF-8#Implementations_and_adoption:~:text=Code%20point%20%E2%86%94-,UTF%2D8%20conversion,-First%20code%20point
			data = sio.readline()
			sio.flush() # it is buffering. required to get the data out *now*
		return data
	def head_function(self):
		pass
	def distance_function(self):
		pass
	def blink_function(self):
		pass
	def save_state(self):
		with open("./Serial.pickle" "wb") as f:
			pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
	def load_state(self):
		with open("./Serial.pickle" "rb") as f:
			self = pickle.load(f)
		
if __name__ == "__main__":
	while True:
		arduino = Serial()
		data = arduino.receive()
		print(data)


