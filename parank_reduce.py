#!/usr/bin/python

# Reducer for PARank

# Imports
import sys

# Read command line arguments
alpha = float(sys.argv[1])
beta  = float(sys.argv[2])
gamma = float(sys.argv[3])
dangling_parank = float(sys.argv[4])
num_nodes = float(sys.argv[5])

# Do initialisations
key = "initial_key"
prev_key = "initial_prev_key"
current_data = ""
parank = 0
current_data_dict = dict()
alpha_sum = 0
beta_sum = 0
gamma_sum = 0


total_reduce_scores 	= 0
total_attachment_weight	= 0
total_year_weight		= 0
val						= 0

# Read lines and do calculations
for line in sys.stdin:
	# Remove whitespace
	line = line.strip()
	# Get key and value
	key, val = line.split()
	
	# ---------------------------------------------------------------- #
	
	# If we just get paper data, continue, but keep the data in the dictionary
	if(val.startswith("<")):
		current_data_dict[key] = val
		continue
	
	# ---------------------------------------------------------------- #
	
	# If we are on the same key as previously, simply add the value where needed
	if(key == prev_key):
		# print "Same key"
		coefficient, value = val.split("|")
		if(coefficient == "alpha"):
			alpha_sum += float(value)
		elif(coefficient == "beta"):
			beta_sum += float(value)
			total_attachment_weight += float(value)
		elif(coefficient == "gamma"):
			gamma_sum += float(value)
			total_year_weight += float(value)
	
	# ---------------------------------------------------------------- #
	
	# Else if key changed and we are not just starting, re-initialise variables
	elif(prev_key != "initial_prev_key"):
		
		# Create the line of the pub again
		current_data 		= current_data_dict[prev_key]
		current_data 		= current_data.replace("<", "")
		current_data 		= current_data.replace(">", "")
		current_data 		= current_data.split("|")
		
		# Get data parts
		outlinks 			= current_data[0]
		outlink_num 		= current_data[1]
		old_parank 		= current_data[2]
		publication_year 	= current_data[3]		
		attachment_score 	= current_data[4]	
		year_weight_score 	= current_data[5]	
		
		# Add to each coefficient what is left
		alpha_sum += dangling_parank
		# Calculate as sum of the three vector scores
		parank = alpha * alpha_sum + beta * float(beta_sum) + gamma * float(gamma_sum)
	
		
		# Output Data
		print prev_key + "\t" + outlinks + "|" + outlink_num + "|" + str(parank) + "\t" + old_parank + "\t" + publication_year + "\t" + attachment_score + "\t" + str(year_weight_score)
		
		################################## 
		##################################
		
		# POP KEY BEFORE CHANGING IT
		current_data_dict.pop(prev_key, None)
		
		# Re-initialisations
		prev_key = key
		alpha_sum = 0
		beta_sum = 0
		gamma_sum = 0
		coefficient, value = val.split("|")
		
		# Start calculations for new key
		if(coefficient == "alpha"):
			alpha_sum += float(value)
		elif(coefficient == "beta"):
			beta_sum += float(value)
			total_attachment_weight += float(value)
		elif(coefficient == "gamma"):
			gamma_sum += float(value)	
			total_year_weight += float(value)	
		
	# ---------------------------------------------------------------- #
	
	# Previous key == initial_prev_key
	else:
		#print >>sys.stderr, "At part 4"
		prev_key = key
		alpha_sum = 0
		beta_sum = 0
		gamma_sum = 0
		coefficient, value = val.split("|")
		if(coefficient == "alpha"):
			alpha_sum += float(value)
		elif(coefficient == "beta"):
			beta_sum += float(value)
			total_attachment_weight += float(value)
		elif(coefficient == "gamma"):
			gamma_sum += float(value)
			total_year_weight += float(value)
			
# -------------------------------------------------------------------- #

# If we're done looping, check if we have an entry that hasn't been output
if(key == prev_key):
	
	# Format latest data
	current_data = current_data_dict[key]
	current_data = current_data.replace("<", "")
	current_data = current_data.replace(">", "")
	current_data = current_data.split("|")
	current_data_dict.pop(key, None)
	
	# Get data parts
	outlinks 			= current_data[0]
	outlink_num 		= current_data[1]
	old_parank 		= current_data[2]
	publication_year 	= current_data[3]
	density_score 		= current_data[-1]
	year_weight_score 	= current_data[5]	
		
	# Add to each coefficient what is left
	alpha_sum += dangling_parank
	# Calculate as sum of the three vector scores
	parank = alpha * alpha_sum + beta * float(beta_sum) + gamma * float(gamma_sum)
	# Output Data
	print prev_key + "\t" + outlinks + "|" + outlink_num + "|" + str(parank) + "\t" + old_parank + "\t" + publication_year + "\t" + attachment_score + "\t" + str(year_weight_score)

