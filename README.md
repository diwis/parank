# PA-RANK

## Overview

Several methods have been proposed to rank scientific papers based on their popularity. These methods are variations of citation count-based methods or Page-Rank, which promote papers recently published or cited. However, these methods have several weaknesses, since they can not differentiate papers published in the same year or  cannot deal with very recently published papers that have only few citations. 

PA-Rank is a method that effectively ranks scientific papers dealing with the above problems. Our method incorporates into the Page-Rank random surfer model (a) a preferential attachment factor to identify papers that are likely to continue receiving citations, and (b) a time-based factor to promote recently published papers that have not yet received sufficient citations. 

Here, we provide a Python/MapReduce implementation of PA-Rank.  


## Input Files

PA-Rank requires the Weight-PA input file which is created automatically using the citation inut file. 

### 1. Citation input file (next level heading)

File structure: 


```
<paper_id> <tab> <paper_referenced_ids>|<#referenced_ids>|<score> <tab> <previous_score> <tab> <publication_year>
```
where:

- <tab> corresponds to a tab character ("\t")
- <paper_referenced_ids> is a comma separated string of the paper ids referenced by paper <paper_id>
- <#referenced_ids> is the number of referenced ids
- <publication_year> is the year <paper_id> was published.
  
### 2. Weight-PA input file
  
To produce Weight-PA input file run calculate_weights.py as follows:

```
./calculate_weights.py <citation_input_file> <exponent> <current_year> <start_year> > <weight_pa_file>
``` 
where: 

- <citation_input_file>: is the citation_input_file described in 1.
- \<exponent>: is the value of the exponential constant (**including the minus sign for negative exponents**), e.g. -0.48.
- <current_year>: is the latest year for which there exist an entry in <citation_input_file>.
- <start_year>: is the year from which we use references to calculate preferential attachment
- <weight_pa_file>: is the name of the file that will be used as input in our method, and, which contains, per paper, an exponential weight and a preferential attachment probability.
  
## Running PA-Rank

Run our method as follows:

```
./parank.py <weight_pa_file> <alpha> <beta> <gamma> <current_year> <convergence_error>
```
where:

- <weight_pa_file>: is the input file created in 2.
- <alpha>\/<beta>\/<gamma>: are the probabilities defined by our method
- <convergence_error>: is the value of the least maximum error between scores in consecutive iterations, per paper, which when achieved the method finishes.
  
