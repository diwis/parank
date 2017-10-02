# parank
PA-Rank (paper ranking method) map-reduce scripts in python


To run this ranking method, put all .py script in the same folder.

An initial input file with lines of the following form is required:

<paper_id> <tab> <paper_referenced_ids>|<#referenced_ids>|<score> <tab> <previous_score> <tab> <publication_year>
  
<tab> corresponds to a tab character ("\t")
<paper_referenced_ids> is a comma separated string of the paper ids referenced by paper <paper_id>
<#referenced_ids> is the number of referenced ids
<publication_year> is the year <paper_id> was published.
  
To run PA-Rank initially the exponential weight-scores and preferential attachment probabilities must be calculated.
To do this, run calculate_weights.py as follows:

./calculate_weights.py <input_file> <exponent> <current_year> <start_year> > <new_input_file>
  
<input_file>: is the input file described above
<exponent>: is the value of the exponential constant described in our method 
<current_year>: is the latest year that papers in <input_file> were published
<start_year>: is the year from which onward we use references to calculate preferential attachment
<new_input_file>: is the name of the original input file, which additionally contains, per paper, an exponential weight and a preferential attachment probability.
  
To run the ranking method, we use the previously created input file as input. 
Our method runs as follows:

./parank.py <new_input_file> <alpha> <beta> <gamma> <current_year> <convergence_error>
  
 <new_input_file>: is the input file created by calculate_weights.py
 <alpha>/<beta>/<gamma>: are the probabilities defined by our method
 <convergence_error>: is the value of the least maximum error between scores in consecutive iterations, per paper, which when achieved the method finishes.
  
