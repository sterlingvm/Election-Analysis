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

# Initialize list of all counties
county_options = []

# Initialize dictionary to count and store counties
county_turnout = {}

# Winning County & Winning Turnout Tracker
winning_county = ""
winning_turnout = 0
winning_turnout_percentage = 0

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

        # Collect the county name for each row
        county_name = row[1]

        # Condiditonal statement for unique names
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add candidate to list of candidates in the running
            candidate_options.append(candidate_name)

            # Initialize each candidate's vote counting
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Conditional statement for unique names
        # If the county does not match any existing counties...
        if county_name not in county_options:

            # Add county to list of counties
            county_options.append(county_name)

            # Initialize each unique county after initialization
            county_turnout[county_name] = 0

        # Add a county turnout tally to the county turnout dictionary
        county_turnout[county_name] += 1

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

    print(f"--- CANDIDATE DATA ---")

    textfile.write(f"--- CANDIDATE DATA ---")


    # Print the candidate summaries to the terminal
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

    print(f"--- COUNTY DATA ---\n")

    textfile.write(f"--- COUNTY DATA ---\n")

    # Reports for County Data
    # Print the county_turnout to the terminal.
    print(f'VOTER TURNOUT PER COUNTY: {county_turnout}\n')

    # Define county vote-percentage
    turnout = county_turnout[county_name]
    county_vote_percentage = (float(turnout) / float(total_votes)) * 100

    for county_name in county_turnout:
        # 2. Retrieve turnout of a county.
        turnout = county_turnout[county_name]
        # 3. Calculate turnout percentage
        county_vote_percentage = (float(turnout) / float(total_votes)) * 100

        # 4. Print each county's turnout
        turnout_results = (f"\n{county_name}: {county_vote_percentage:.2f}% ({turnout:,})\n")

        # Print each county's turnout results to the terminal
        print(turnout_results)

        # Save each county's turnout results to the textfile
        textfile.write(turnout_results)

        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (turnout > winning_turnout) and (county_vote_percentage > winning_turnout_percentage):
            # 2. If true then set winning_turnout = turnout and winning_turnout_percentage = county_vote_percentage
            winning_turnout = turnout
            winning_turnout_percentage = county_vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_county = county_name

    winning_county_summary = (
        f"-------------------------\n"
        f"Winner: {winning_county}\n"
        f"Winning Vote Count: {winning_turnout:,}\n"
        f"Winning Percentage: {winning_turnout_percentage:.1f}%\n"
        f"-------------------------\n")

    # Print the winning candidate summary to the terminal
    print(winning_county_summary, end="")

    # Save the winning candidate summary to the textfile
    textfile.write(winning_county_summary)