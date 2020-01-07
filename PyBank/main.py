# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 13:30:04 2019

@author: chris
"""

# Your task is to create a Python script that analyzes the records to calculate each of the following:

  # The total number of months included in the dataset

  # The net total amount of "Profit/Losses" over the entire period

  # The average of the changes in "Profit/Losses" over the entire period

  # The greatest increase in profits (date and amount) over the entire period

  # The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

#  ```text
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
#  ```

import os
import csv

budget_data_csv = os.path.join("C:\\Users\\chris\\Desktop\\GT-ATL-DATA-PT-12-2019-U-C\\Homework\\03-Python\\Instructions\\PyBank\\Resources\\budget_data.csv")
budget_analysis = os.path.join("Analysis", "budget_analysis.txt")

month_total = 0
total_sum = 0
profit_values = []
month_count = []
res = []


# Read csv file (budget_data)
with open(budget_data_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    #csv_header = next(csvfile)
    next(csv_reader)
     
#Calculate number of months under Months column    
    for row in csv_reader:
        month_total += 1
        
    
#Calculate sum for Proft/Losses column        
        total_sum += int(row[1])
        
#Add all profits/losses values in a list in order to loop through to calculate average MoM profit/loss change.
        profit_values.append(int(row[1]))
        month_count.append(row[0])

##print(profit_values)
res = [profit_values[i+1] - profit_values[i] for i in range(len(profit_values)-1)]
       
profit_sum = round(sum(res)/len(res), 2) 

big = max(res)
little = min(res)
max_date = month_count[res.index(big)+1]
min_date = month_count[res.index(little)+1]

output = (
    f"Financial Analysis\n"
    f"--------------------------------\n"    
    f"Total Months: {month_total}\n"
    f"Total: ${total_sum:,}\n"  
    f"Average Change: ${profit_sum:,.2f}\n"  
    f"Greatest Increase in Profits: {max_date} (${big:,})\n"
    f"Greatest Decrease in Profits: {min_date} (${little:,})\n"
)

print(output)

with open(budget_analysis,"w") as txt_file:
    txt_file.write(output)     

    
    



      
      
      
      
      