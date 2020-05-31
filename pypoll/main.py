#import modules
import os
import csv

#define list variable: candidates
candidate_votes = []

#specify election csv path
pollpath = os.path.join ("resources", "election_data.csv")

#read election csv file
with open (pollpath) as pollfile:
    pollreader = csv.reader (pollfile, delimiter = ',')
    
    #specify header
    pollheader = next (pollreader)
    
    #begin loop through rows, add candidate votes to list
    for row in pollreader:
        candidate_votes.append (row[2])

#identify unique candidates
unique_candidates = list (set (candidate_votes))

#create dictionary for individuals & vote counts; votes set as key to sort later
individual_votes = {}

for candidate in unique_candidates:
    individual_votes [candidate_votes.count(candidate)] = candidate

#sort dictionary by descending vote count, generate iterable list
sorted_votes = sorted (individual_votes.items(), reverse = True)

#calculate total votes
total_votes = len (candidate_votes)

#loop through sorted votes to create list of results
individual_results = []
for x in range(len(sorted_votes)):
    candidate_name = sorted_votes[x][1]
    vote_count = sorted_votes[x][0]
    vote_percent = round (vote_count / total_votes * 100, 3)
    results = f"{candidate_name}: {vote_percent}% ({vote_count})"
    individual_results.append (results)

#define output
output = (f"""election results
--------------------------------
total votes: {total_votes}
--------------------------------""")

#loop through individual results, add to output
for result in individual_results:
    output += f"\n{result}"

output += f"""\n--------------------------------
winner: {sorted_votes[0][1]}
--------------------------------"""

#print to terminal
print (output)

#export analysis to .txt file
analysis_output = "analysis/analysis_output.txt"

#write analysis contents to .txt file
with open (analysis_output, 'w') as text:
    text.write (output)