#Import file along filepath
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#Read the CSV File
with open(csvpath, encoding='utf') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")

	print(csv_reader)

	#csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")
	
	## Creat Column [2] for Change Calculation

	# Define start values of loop
	#month = 0
	#change = 0
	#i = csv_reader[1]
	# Read each row and count them
	#for row[0] in csv_reader:
		#month = month + 1
		#tMonths = month -1
	#print(f"Months: {tMonths}")

	#for row[2] in csv_reader
		#(i, [change]) = (i +1) - i
		
	# The total amount of "Profit/Losses" over the entire period
	#gross_profit = [change].sum()

	# Mean of the change list
	#AVG_progit = [change].mean()


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
print(f"Total Months:" +"tMonths")
print(f"Change: " +"gross_profit")
print(f"Average Change: " +"$" +"Average")
print(f"Greatest Increase in Profits: " + "Date + gInc")
print(f"Greatest Decrease in Profits: " + "Date + gDec")

# Set variable for output file
output_file = os.path.join("PyBank")

#  Open the output file
with open(output_file, "w") as txtfile:
	writer = csv.writer(txtfile, delimiter=' ', quoting=csv.QUOTE_NONE)
	writer.writerow(".")
	writer.writerow("Financial.Analysis")
	writer.writerow("_._._._._._._._._._._._._._._._._")
	writer.writerow(".")
	writer.writerow(f"Total.Months:"+"tMonths")
	writer.writerow(f"Change:."+"gross_profit")
	writer.writerow(f"Average.Change:."+"$"+"Average")
	writer.writerow(f"Greatest.Increase.in.Profits:."+"Date.+.gInc")
	writer.writerow(f"Greatest.Decrease.in.Profits:."+"Date.+.gDec")
