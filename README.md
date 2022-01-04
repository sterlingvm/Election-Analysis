# Election-Analysis

## Project Overview
Seth, A Colorado Board of Elections employee has asked for help completing the election audit of a recent local congressional election. He has asked us to build code in Python complete the audit and needs help with the following tasks:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winnder of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.8, Visual Studio Code, 1.63.2

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.05% of the votes and 85,213 number of votes
    - Diana DeGette received 73.81% of the votes and 272,892 number of votes
    - Raymon Anthony Doane received 3.14% of the votes and 11,606 number of votes
- The winner of the election was:
    - Diana DeGette, who received 23.05% of the votes and 85,213 number of votes, won.
- The counties the received votes were:
    - Jefferson
    - Denver
    - Arapahoe
- The county turnout results were:
    - Jefferson had 10.51% of voter turnout with 38,855 votes cast there
    - Denver had 82.78% of voter turnout with 306,055 votes cast there
    - Arapahoe had 6.71% of voter turnout with 24,801 cotes cast there
- The county with the largest turnout was:
    - Denver, with 82.78% of voter turnout at 306,055 total votes, had the largest voter turnout.

Executive Summary:
- This data (and script) allows us to ascertain vote percentage, total votes, and majority winners for both candidates and county voter turnout.
- This script can be used to calculate which counties produce the most voter turnout and from that, the election committee can better understand what political activity is like in all counties throughout a state.
- This script can also be used to quickly calculate which candidate has won in an election (winning candidate) as well as how they won  (total votes) and why they won (vote percentage).
- This script also offers total vote count and vote percentage for all candidates in the election and all counties with voter turnout
- With modificaitons to the candidates, counties, and/or amount of votes cast (A.K.A. unique vote IDs) [As long as the column format and data is the same type as the election_results.csv file], election results can be easily calculated, tallied, and organizaed by changing the file paths within the python script as appropriate and simply running the code!


## Challenge Overview
- In this Python-based challenge, we tackled applications of reading .csv files, utilizing dictionaries, calling keys and values, iterating across dictionary item keys and running computations across their values, compiling our election calculations into analyses, operating our python script in the terminal, and writing the analyses onto a textfile.

## Challenge Summary
- This challenge allowed us to harness all of our python skills and apply them to simplify the election audit and automatically process that data and information.
- This challenge took a bit of time, and while additional information was appended to the assignment after completing the original assignment, after establishing the code script for the original data on candidates, re-applying our candidate-based script for county data was very natural.
- The limits to this challenge are minimal, though improvements that could be made by me are condensing my code and simplifying it to be more optimalized and use fewer lines to accomplish the same product!
