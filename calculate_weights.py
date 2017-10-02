#!/usr/bin/python

# This script reads a file containing lines of the following format:
# paper_id <tab> cited_paper_id_list|cited_paper_num|current_score <tab> previous_score <tab> publication_year
# The file is processed and a new one is produced, which adds two additional columns: 
# (a) the calculated preferential attachment weight and
# (b) the calculated exponential publication age-based weight

# ------------------------ Imports ----------------------------------- #

import sys
import os
import math

# -------------------------------------------------------------------- #

# ----------------------- Functions ---------------------------------- #	

########################################################################
# Returns a dictionary of pub - year pairs
def get_year_dict(year_file):
	year_dict = dict()
	with open(year_file) as f:
		for line in f:
			line_parts 		= line.strip().split()
			pub			= line_parts[0]
			year			= line_parts[-1]
			year_dict[pub] 	= year
	return year_dict

########################################################################

########################################################################	

# Get the year exponential weight value for each pub - and normalize!
def get_year_weight(year_dict, exponent, current_year):
	year_weight_dict = dict()
	for pub in year_dict:
		year = year_dict[pub]
		# Calculate initial pub weight
		year_diff = int(current_year) + 1 - int(year)
		exponential_weight = math.exp(float(exponent)*year_diff)
		year_weight_dict[pub] = exponential_weight
	# Get total of weights to normalize
	weight_sum = sum(year_weight_dict.values())
	for pub in year_weight_dict:
		unnormalized_weight = year_weight_dict[pub]
		normalized_weight	= float(float(unnormalized_weight)/float(weight_sum))
		year_weight_dict[pub] = normalized_weight
	# Return the dictionary
	return year_weight_dict	
	
########################################################################

########################################################################	
# Returns a dictionary of pubs and their hereto accumulated references
def get_citation_dict_in_timespan(input_file, start_year):
	# TODO: fix this. count citations from particular year onwards.
	offset_citation_dict = dict()
	with open(input_file) as f:
		for line in f:
			line = line.strip()
			pub, data, prev_score, year = line.split()
			if pub not in offset_citation_dict:
				offset_citation_dict[pub] = 0
			cited_pubs = data.split("|")[0].split(",")
			if cited_pubs == "0" or cited_pubs == ["0"]:
				continue
			for cited_pub in cited_pubs:
				if cited_pub not in offset_citation_dict:
					offset_citation_dict[cited_pub] = 0
				# Only add citations if examined  
				# pub is published after start_year
				if int(year) >= int(start_year):
					offset_citation_dict[cited_pub] += 1
	# Return dictionary
	return offset_citation_dict
		
			
########################################################################		
	
########################################################################			
# Get probability of new node attachment for each node
def get_pref_attachment_probability(citation_dict):
	total_citations = sum(citation_dict.values())
	
	## Now calculate the probability per pub
	citation_prob_dict = dict()
	# Loop publications
	for pub in citation_dict:
		if total_citations == 0:
			citation_prob_dict[pub] = 0
		else:
			attachment_probability = float(citation_dict[pub]) / float(total_citations)
			citation_prob_dict[pub] = attachment_probability
			
	# Return the dictionary
	return citation_prob_dict

########################################################################	
	
########################################################################

if len(sys.argv) < 4:
	print "Run as follows: "
	print "./calculate_weights.py <input_file> <exponent> <current_year> <start_year>"
	sys.exit(0)

# READ INPUT
input_file	= sys.argv[1]
exponent	= sys.argv[2]
current_year	= sys.argv[3]
start_year 	= sys.argv[4]


########################################################################

# MAIN PROGRAM	

# Get dictionary with publication years per paper
year_dict = get_year_dict(input_file)
# Preferential attachment based on citations in latest years (specified by start year)
partial_citation_dict	= get_citation_dict_in_timespan(input_file, start_year)
# Get preferential attachment probabilities
pref_attachment_probs 	= get_pref_attachment_probability(partial_citation_dict)
# Calculate Year based weights
year_weight_dict	= get_year_weight(year_dict, exponent, current_year)
# Use the preferential attachment weights calculated
weight_dictionary = pref_attachment_probs

# Output input file with added weight
with open(input_file) as f:
	for line in f:
		line 		= line.strip()
		pub  		= line.split("\t")[0]
		weight 		= weight_dictionary[pub]
		year_weight = year_weight_dict[pub]
		print line + "\t" + str(weight) + "\t" + str(year_weight)
			
			
			
			
			
			
			
			
			
			
			
			
			
				
	
