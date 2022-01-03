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

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1


# Write the data to a text file
with open(file_to_save, 'w') as textfile:

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
            #print(f"{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n")

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

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    textfile.write(election_results)
    # Print the candidate summaries to the terminal (I used a for loop for this)
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes
        vote_percentage = (float(votes) / float(total_votes)) * 100
            
        # 4. Print each candidate's vote percentage (formatted to 2 decimal places)
        candidate_results = (f"\n{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n")

        # Print each candidate's results to the terminal
        print(candidate_results)

        #Save each candidate's results ot the textfile
        textfile.write(candidate_results)

    # Print the winning candidate summary to the terminal
    print(winning_candidate_summary, end="")

    # Save the winning candidate summary to the textfile
    textfile.write(winning_candidate_summary)