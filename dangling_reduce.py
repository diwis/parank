#!/usr/bin/python

# Reducer of dangling node sum calculation

# Imports
import sys

# Total dangling node transfer score
total_dangling_score = 0

# Read input lines, add scores
for line in sys.stdin:
	line = line.strip()
	# Get float from line
	line = float(line)
	# Add score
	total_dangling_score += line

print total_dangling_score
