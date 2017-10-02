#!/usr/bin/python

# Program to caculate PA-Rank scores
# Parameters: 
# 1) parank input file
# 2) alpha value
# 3) beta value
# 4) gamma value
# 5) convergence error

# Imports
import sys
import os

# Read and initialise arguments
if(len(sys.argv) < 6):
	print "Usage: ./parank.py <input_file> <alpha> <beta> <gamma> <convergence_error>"
	sys.exit(0)
else:
	parank_input 		= sys.argv[1]
	alpha 			= float(sys.argv[2])
	beta 			= float(sys.argv[3])
	gamma 			= float(sys.argv[4])
	max_delta 		= float(sys.argv[5])
		
# Set an initial (high) error value
delta = 100

# Get numbers of authors and papers
num_of_papers = os.popen('wc -l ' + parank_input + ' | cut -d " " -f 1').read()
# Remove whitespace
num_of_papers = num_of_papers.strip()

# Print initialisation messages

print
print "Number of Papers: ", num_of_papers
print "Alpha: ", alpha
print "Beta: ", beta 
print "Gamma: ", gamma
print "Paper citation file: ", parank_input

# Get the paper input file as graphstep file
os.popen('cat ' + parank_input + ' > paper_graphstep.txt')
# --------- ACTUAL START OF METHOD -------------- #

iterations = 0
	
# Do rounds of the futureRank algorithm
while(delta >= max_delta):
	
	iterations += 1
	print "Iteration #" + str(iterations)

	#1. Do simple pagerank dangling calculation
	dangling_sum = os.popen("cat paper_graphstep.txt | ./dangling_map.py " + str(num_of_papers) + " | sort -k1,1 | ./dangling_reduce.py").read()
	dangling_sum = str(dangling_sum)
	dangling_sum = dangling_sum.strip()
	
	print "\nDangling Sum: ", dangling_sum

	#2. Do the paper score calculation in a mapreduce fashion
	os.popen("cat paper_graphstep.txt | ./parank_map.py | sort -k1,1 | ./parank_reduce.py " + str(alpha) + " " + str(beta) + " "  + str(gamma) + " " + str(dangling_sum) + " " + str(num_of_papers) + " | sort -k1,1 > paper_nextstep.txt")
	
	#3. Calculate the errors
	error = os.popen("cat paper_nextstep.txt | ./parank_error_map.py | sort -k1,1 | ./parank_error_reduce.py").read()
	print "Error: ", error
	
	delta = float(error)

	#4. Move results to new file
	os.popen("mv paper_nextstep.txt paper_graphstep.txt")
	

# Output in new file
os.popen("export LC_ALL=C; cat paper_graphstep.txt | while IFS=$'\t' read paper dats score year attachment yearweight; do final_score=${dats##*|}; echo  \"${paper}\t${dats}\t${score}\t${year}\t${attachment}\t${yearweight}\t${final_score}\"; done | sort -k7 -gr > " + parank_input + "_a" + str(alpha) + "_b" + str(beta) + "_c" + str(gamma) + "_i" + str(iterations) + ".txt")
# Remove temporary files
os.popen("rm paper_graphstep.txt")

