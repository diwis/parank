#!/usr/bin/python

# Mapper for error calculation

# Imports
import sys
import math

max_error = 0

# Read line by line and calculate rank score difference squared
for line in sys.stdin:
	line = line.strip()
	# No matter if we have author or paper, scores will be situated at the same place
	line_parts = line.split("\t")
	line_data = line_parts[1]
	current_score = line_data.split("|")[-1]
	previous_score = line_parts[2]
	score_difference = math.fabs(float(current_score) - float(previous_score))
	if(score_difference >= max_error):
		max_error = score_difference
		
print max_error	
