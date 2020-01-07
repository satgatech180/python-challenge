# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:06:08 2020

@author: chris
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:28:54 2020

@author: chris
"""

"""
  * In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
  * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
  *     The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that 
  *     analyzes the votes and calculates each of the following:
  * The total number of votes cast
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote.
  * As an example, your analysis should look similar to the one below:
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  
  In addition, your final script should both fthe analysis to the terminal and export a text file with the results
"""

import os
import csv

#poll_data_csv = os.path.join("C:\\Users\\Manoj.Chandran\\Desktop\\Scot\\election_data_new.csv")
poll_data_csv = os.path.join("C:\\Users\\chris\Desktop\\GT-ATL-DATA-PT-12-2019-U-C\\Homework\\03-Python\\Instructions\\PyPoll\\Resources\\election_data.csv")
poll_analysis = os.path.join("Analysis", "poll_analysis.txt")

#poll_data_csv = os.path.join("C:\\Users\\chris\Desktop\\GT-ATL-DATA-PT-12-2019-U-C\\Homework\\03-Python\\Instructions\\PyPoll\\Resources\\election_data.csv")

vote_total = 0
candidate = []
electoral_votes = {}


with open(poll_data_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    next(csv_reader)    
  
    
    for row in csv_reader:
        vote_total += 1
        
        candidate.append(row[2])        


for item in candidate:
    electoral_votes[item] = electoral_votes.get(item, 0) + 1
    
output=(
    f"Election Results\n"
    f"------------------------\n"
    f"Total Votes: {sum(electoral_votes.values())}\n"
    f"------------------------\n"
)    

for key in electoral_votes:
    output += f"{key}: {str('%.3f'%((electoral_votes[key]/sum(electoral_votes.values()))*100))}% ({electoral_votes[key]})\n"
    #output.append(f"{key}: {round((electoral_votes[key]/sum(electoral_votes.values()))*100,3)}% ({electoral_votes[key]})\n")

output += (f"------------------------\n"
           f"Winner: {max(electoral_votes, key=electoral_votes.get)}\n" 
           f"------------------------\n")

print(output)
with open(poll_analysis,"w") as txt_file:
    txt_file.write(output)     
