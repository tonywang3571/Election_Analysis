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


# Totaling up the votes set to zero. (above 'open' b/c it must be set to 0 everytime we run file)
total_votes = 0
# Candidates to vote for (above 'open' b/c list set to empty everytime before we run file)
candidate_options = []
# Votes for each candidate (need to set to empty everytime before we run file)
candidate_votes = {}

# Winning Candidate and count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open election results and read file.
with open(file_to_load) as election_data:

    # To Do: read and analyze data here.
    
    # Read file object with reader function
    file_reader = csv.reader(election_data)
    
    # Read and print header row
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
        # Adds up total votes
        total_votes += 1

        # Adds candidates to options
        candidate_name = row[2]
        # Which candidates are on the ballots without repeats
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Sets votes for each candidate to 0
            candidate_votes[candidate_name] = 0
        
        # Adds up votes for each candidate
        candidate_votes[candidate_name] += 1
        
# Gives us results        
print(str(total_votes) + " total votes\n")

# Finding percentage of votes per candidate
# Remember that 'candidate_name' in the loop is an iterator ('i')
for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------")
print(winning_candidate_summary)



    



