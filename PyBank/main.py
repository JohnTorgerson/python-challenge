#Import file along filepath
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#Read the CSV File
with open(csvpath, encoding='utf') as csv_file:	
	csv_reader = csv.reader(csv_file, delimiter=",")

output_path = os.path.join('Resources', 'budget_data.csv')	
with open(output_path, 'w') as csvfile:
## Append Header Row
	for row in csv_reader:
		row.append(row[0])


	#Read the header row first
	csv_header = next(csv_file)
	print(f"Header: {csv_header}")

	
	# Define start values of loop
	month = 0
	change = 0

	# Read each row and count them
	for row in csv_reader:

		month = month + 1
	tMonths = month -1

	print(f"Months: {month}")


		
	# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
	# for row in csv_reader:
		#Average = int(row[Profit/Losses])
	# print(Average)

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
print(f"Total Months: Months")
print(f"Change: " +"string")
print(f"Average Change: " +"$" +"Average")
print(f"Greatest Increase in Profits: " + "Date + gInc")
print(f"Greatest Decrease in Profits: " + "Date + gDec")
