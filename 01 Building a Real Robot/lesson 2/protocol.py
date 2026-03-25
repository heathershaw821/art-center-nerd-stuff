#!/usr/bin/env python3

import serial
import io
from time import sleep

class Protocol:
	def __init__(self):
		actions =  {  # our "commands" (remember these are bidirectional on agreed terms)
		# OUTPUTS (Actions)
			"head": None,     # <<< right now
			"forward": None,
			"backward": None,
			"left": None,
			"right": None,
			"blink": None,
			# INPUTS (Sensors)
			"distance": None, # <<< right now
			# .........
		}

		SOL = ""   # start of action "string" (not always a literal "string")
		EOL = "\n" # End of action "string"

class Serial(Protocol):
	def __init__(self):
		# for every protocol application, you will change these to fit
		self.SOL = ""
		self.EOL = "\n"
		actions["head"] = head_function
		actions["distance"] = distance_function
		actions["blink"] = blink_function

	def head_function(self):
		pass
	def distance_function(self):
		pass
	def blink_function(self):
		pass
		
if __name__ == "__main__":
	print("This is a library.... Do better.")


