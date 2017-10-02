#!/usr/bin/python

# Mapper for PARank scoring 
# Outputs paper id's as keys 
# and their various data as values

# Imports
import sys
import math

# Read line by line
for line in sys.stdin:
	# Strip whitespace
	line = line.strip()
	# Here we do calculations based on paper - paper associations

	# Break line to parts
	line_parts = line.split()
	# Get each required value
	pub_id = line_parts[0]
	pub_citation_data = line_parts[1]
	previous_score = line_parts[2]
	pub_year = line_parts[3]
	
	##################################
	pref_attachment_score = line_parts[-2]
	##################################
	
	##################################
	year_weight_score = line_parts[-1]
	##################################
	
	# Get reference list
	pub_citation_data = pub_citation_data.split("|")
	reference_list = pub_citation_data[0]
	number_of_references = pub_citation_data[1]
	# Get current rank score
	current_score = pub_citation_data[2]	
		
	# Output self first (otherwise, if no other ranks are passed to this key, we will lose it)
	print pub_id + "\talpha|0"
	print pub_id + "\tbeta|0"
	print pub_id + "\tgamma|0"
	# Output pmid previous data
	print pub_id + "\t" + "<" + reference_list + "|" + number_of_references + "|" + current_score + "|" + pub_year + "|" + pref_attachment_score + "|" + year_weight_score + ">"

	####################################################################
	# OUTPUT alpha * rank
		
	# If we have references, output our score to them. This should be done in a random walk probability fashion
	if(number_of_references != "0"):
		reference_list = reference_list.split(",")
		# Loop references and output alpha value!
		for ref in reference_list:
			print ref + "\talpha|" + str(float(current_score)/float(number_of_references))
			
	####################################################################		
	# OUTPUT beta * rank
	
	# Output also the exponential personalised score
	print pub_id + "\t" + "gamma|" + str(year_weight_score)
	####################################################################
	# OUTPUT gamma * rank
	
	# Also output density vector score
	print pub_id + "\t" + "beta|" + str(pref_attachment_score)
	####################################################################
