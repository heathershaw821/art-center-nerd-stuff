#!/usr/bin/env python3

import sys
from termcolor import colored, cprint
from sympy.ntheory.primetest import isprime

grid_size = int(sys.argv[1])

if not grid_size %2 or grid_size <1:
	print(f"{grid_size} is not a valid grid size, please enter a valid width")
	exit(-1)


#grid_size = 3
def middle(n):
	return int((n + 1) / 2)



grid = []

for x in range(grid_size):
	grid.append([ 0 for x in range(grid_size)])


middle_index = middle(grid_size) - 1
grid[middle_index][middle_index] = 1
total_loop = middle(grid_size)
x_axis = middle_index
y_axis = x_axis



def new(y):
	x = ((y - 1) * 2)
	fr = 1
	u = x - 2
	l = x - 1
	d = x - 1
	r = x - 1
	return [fr, u, l, d, r]



current_loop = 0
total_loop = ((grid_size * 2) - 1)


first_right = 0
up = 0
left = 0
down = 0
right = 0



for i in range(grid_size ** 2):

	first_right = 0
	up = 0
	left = 0
	down = 0
	right = 0


	if first_right > 0:
		first_right = first_right - 1
		x_axis += 1
	elif up > 0:
		up = up - 1
		y_axis = y_axis - 1
	elif left > 0:
		left = left - 1
		x_axis = x_axis -1
	elif down > 0:
		down = down - 1
		y_axis += 1
	elif right > 0:
		right = right - 1
		x_axis += 1
	if grid[y_axis][x_axis] == 0:
		#last_number = len(str(grid_size ** 2))
		#current_number = len(str(i + 2))
		#zeros = last_number - current_number
		grid[y_axis][x_axis] = int(str(i + 2))
		#.zfill(zeros + 1)
	if (first_right + right + left + up + down) <= 0:
		first_right = new(current_loop)[0]
		up = new(current_loop)[1]
		left = new(current_loop)[2]
		down = new(current_loop)[3]
		right = new(current_loop)[4]
		current_loop += 1



# Printing


for x in grid:
	for y in x:
		if isprime(y) == True:
			cprint(y, "red", end = '')
		elif y == 0:
			cprint(y, "blue", "on_cyan", end='')
		else:	
			print(y, end = '')
		print(",", end = '')
	print()


#print(middle(grid_size))


#for z in [12, 34]:
#	print(z)
