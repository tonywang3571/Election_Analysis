# Data need to retrieve.
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# Winner of the election based on popular vote

#Adding dependencies
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

# Tracking winning Candidate, vote counts, and percent of votes
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open election results and read file.
with open(file_to_load) as election_data:
    
    # Read file object with reader function
    file_reader = csv.reader(election_data)
    
    # Read and print header row (helps skip first row when tallying votes)
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

#Saves reults to our text file.
with open(file_to_save, "w") as txt_file:

# Print final vote count to the terminal
    election_results = (
        f"\nElection Reults\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Finding percentage of votes per candidate
    # Remember that 'candidate_name' in the loop is an iterator ('i')
    for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print the results for each candidate's name, vote percent and votes
            print(candidate_results)
            # Save the results for each candidate into text file
            txt_file.write(candidate_results)

            # Comparing vote count and percentage of each candidate to see who has the highest count and percentage
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

    # Declaring winner
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------")
    print(winning_candidate_summary)
    #Save winning candidate's name into text file
    txt_file.write(winning_candidate_summary)

