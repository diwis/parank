#!/usr/bin/python

# Reducer for error calculation

# Imports
import sys

max_error = 0

# Read line by line
for line in sys.stdin:
	line = line.strip()
	error = float(line)
	if (max_error <= error):
		max_error = error
	
print max_error
	
