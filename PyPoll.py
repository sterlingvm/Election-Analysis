# Pseudocode Plan
# the data we need to retrieve:
# 1. the Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Modules
import os
import csv

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize variable for total votees
total_votes = 0

# Initialize list for all candidates in the running
candidate_options = []

# Initialize dictionary to count and store each candidate's votes
candidate_votes = {}

# Winning Candidate & Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load, 'r') as election_data:

    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)


    # Read the header row
    headers = next(file_reader)


    # Print each row in the CSV file
    for row in file_reader:
        # Add and count total vote count
        total_votes += 1
      
        # Collect the candidate name for each row
        candidate_name = row[2]

        # Condiditonal statement for unique names
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add candidate to list of candidates in the running
            candidate_options.append(candidate_name)

            # Initialize each candidate's vote counting
            candidate_votes[candidate_name] = 0

        # Count each vote for each candidate
        candidate_votes[candidate_name] += 1






# Print total vote count:
print(f'TOTAL VOTES: {total_votes}\n')

# Print the candidate list
print(f'LIST OF CANDIDATES: {candidate_options}\n')

# Print each candidate's votes
print(f'CANDIDATE VOTE COUNT: {candidate_votes}\n')

# Space for formatting & readability
print()

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes
        vote_percentage = (float(votes) / float(total_votes)) * 100
        
        # 4. Print each candidate's vote percentage (formatted to 2 decimal places)
        print(f"{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(f'{winning_candidate_summary}')








'''
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write(f"Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
'''

