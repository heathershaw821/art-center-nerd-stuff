
	elif left > 0:
		left = left - 1
		x_axis = x_axis -1#!/usr/bin/env python3

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

print(total_loop)

x_axis = middle_index - 0
y_axis = x_axis



def new(y):
	x = ((y * 2) - 1)
	#print("x=", x, y)
	x= y
	u = x - 1
	l = x
	d = x
	r = x + 1
	return [u, l, d, r]



current_loop = 1
total_loop = ((grid_size * 2) - 1)


up = 0
left = 0
down = 0
right = 1



for i in range(grid_size ** 2):


#	if first_right > 0:
#		first_right = first_right - 1
#		x_axis += 1
	if up > 0:
		up = up - 1
		y_axis = y_axis - 1
	elif down > 0:
		down = down - 1
		y_axis += 1
	elif right > 0:
		right = right - 1
		x_axis += 1
#( )
#( ) | (3) ( ) ( ) ( ) ( )
#( ) | ( ) (2) ( ) ( ) ( )
#( ) | ( ) ( ) ( ) ( ) ( )
#( ) | ( ) ( ) ( ) ( ) ( )
#( ) | ( ) ( ) ( ) ( ) ( )


	print("y x", y_axis, x_axis)
	if grid[y_axis][x_axis] == 0:
		#last_number = len(str(grid_size ** 2))
		#current_number = len(str(i + 2))
		#zeros = last_number - current_number
		grid[y_axis][x_axis] = int(str(i + 2))
		#.zfill(zeros + 1)
	if (right + left + up + down) <= 0:
		up = new(current_loop)[0]
		left = new(current_loop)[1]
		down = new(current_loop)[2]
		right = new(current_loop)[3]
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
		print("|", end = '')
	print()
	print("_________________________")


#print(middle(grid_size))


#for z in [12, 34]:
#	print(z)
