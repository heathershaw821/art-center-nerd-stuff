#!/usr/bin/env python3

import sys
from termcolor import colored, cprint
from sympy.ntheory.primetest import isprime

#grid_size = int(sys.argv[1]) ^ 2
grid_size = 3
def middle(n):
	return int((n + 1) / 2)
	
grid = [
 [5, 4, 3],
 [6, 1, 2],
 [7, 8, 9]
]

for x in grid:
	for y in x:
		if isprime(y) == True:
			cprint(y, "red", end = '')
		else:	
			print(y, end = '')
	print()
print(middle(grid_size))
