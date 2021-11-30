# Data need to retrieve.
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# Winner of the election based on popular vote

import csv
import os

# Assigning variable for file to load from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assigning variable for file to save to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open election results and read file.
with open(file_to_load) as election_data:

    # To Do: read and analyze data here.
    
    # Read file object with reader function
    file_reader = csv.reader(election_data)
    
    # Read and print header row
    headers = next(file_reader)
    print(headers)



