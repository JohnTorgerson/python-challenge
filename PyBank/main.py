#Import file along filepath
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#Read the CSV File
with open(csvpath, encoding='utf') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")

	#Read the header row first
	csv_header = next(csv_file)
	print(f"Header: {csv_header}")
	
	# Define start values of loop
	month = 1
	#prof = (row[2])

	# Read each row and count them
	for row in csv_reader:
 		
		month = month + 1
	tMonths = month -1

# result = int(row[Profits/Losses])
	pLoss = sum(row[2])
	print(pLoss)
		
	
	# The net total amount of "Profit/Losses" over the entire period
# (cumulative/sum of column)
	# (row[2]) 

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# (average of column)
# Average =

# The greatest increase in profits (date and amount) over the entire period
# (find “max?” “find()”biggest winner+ output result and date/2 cells)
# “gInc = max(2)”

# The “min?” greatest decrease in profits (date and amount) over the entire period
# (find biggest loser+ "same as previous")
# “gDec = min(2)”
print(" ")
print("Financial Analysis")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print(" ")
print(f"Total Months: {tMonths}")
print("Total: " + "  ")
print("Average Change: " +"$" +"Average")
print("Greatest Increase in Profits: " + "Date + gInc")
print("Greatest Decrease in Profits: " + "Date + gDec")
