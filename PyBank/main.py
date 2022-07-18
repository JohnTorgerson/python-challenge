#Import file along filepath
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#Read the CSV File
with open(csvpath, encoding='utf') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")

	print(csv_reader)

	csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")
	
	# Define start values of loop
	month = 0
	change = 0

	# Read each row and count them
	#for row[1] in csv_reader:
		#month = month + 1
		#tMonths = month -1
	#print(f"Months: {tMonths}")


		
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
#print(f"Total Months: {tMonths}")
print(f"Change: " +"string")
print(f"Average Change: " +"$" +"Average")
print(f"Greatest Increase in Profits: " + "Date + gInc")
print(f"Greatest Decrease in Profits: " + "Date + gDec")
