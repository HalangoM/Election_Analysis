# The data we need to retrieve
# 1. The total number of votes cast
# 2. The complete list of the candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

#Add or dependencies
import csv

import os

# Assign a variable to load the file from a path.
file_to_load = os.path.join("Resources", "election_results.csv") 

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    
    #To do: read and amalyze the data here
    file_reader = csv.reader(election_data)
    
    #Read and print the header row.
    headers = next(file_reader)
    print(headers)





