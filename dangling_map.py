#!/usr/bin/python

# Mapper for getting dangling node sum

# Imports
import sys

# Sum of dangling node ranks
dangling_sum = 0
node_count = int(sys.argv[1])

# Read line by line and add score if we have a dangling node
for line in sys.stdin:
	# Strip whitespace
	line = line.strip()
	# Get line parts
	line_parts = line.split()
	# First string is article id
	pub_id = line_parts[0]
	# Data <cited|num_citations|current_rank> is the second field
	pub_data = line_parts[1]
	pub_data = pub_data.split("|")
	reference_list = pub_data[0]
	num_of_references = pub_data[1]
	current_score = pub_data[2]
	# Previous score is next field
	previous_score = line_parts[2]
	# Final Field is year
	pub_year = line_parts[3]
	
	# If there are no references, this pub 
	# distributes its score evenly to all others
	if(num_of_references == "0"):
		# Add the probability of jumping to any node
		dangling_sum += float(current_score)/float(node_count)
	else:
		# If we have outgoing links, we don't need to do anything
		continue

# Finally output summed dangling score
print dangling_sum
