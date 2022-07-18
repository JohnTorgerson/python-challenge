#Import file along filepath
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#Read the CSV File
with open(csvpath, encoding='utf') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    ## Assing preloop values
    win = object
    cVoteC = 0
    cVoteD = 0
    cVoteR = 0
    #cVoteO = 0 (( I added this to ensure there weren't any odd entries))

    ## Count 3 unique occurances of each name per ballot/row
    for row in csv_reader:
        if row [2] == "Charles Casper Stockham":
            cVoteC = cVoteC + 1
        elif row [2]=="Diana DeGette":
            cVoteD = cVoteD + 1
        elif row [2] == "Raymon Anthony Doane":
            cVoteR = cVoteR + 1
        #else:
            #cVoteO = CVoteO + 1

## Total votes
    tVotes = (cVoteC) + (cVoteD) + (cVoteR)# + (cVoteO)

## Divide the 3 occurance counts by the total
    pVoteC = (cVoteC) / (tVotes)
    pVoteD = (cVoteD) / (tVotes)
    pVoteR = (cVoteR) / (tVotes)

## Format percentages
    fpVoteC = "{:.3%}".format(pVoteC)
    fpVoteD = "{:.3%}".format(pVoteD)
    fpVoteR = "{:.3%}".format(pVoteR)

## Find the largest total
    if (cVoteC) > (cVoteD) and (cVoteC) > (cVoteR):
        win = "Charles.Casper.Stockham"
    elif (cVoteD) > (cVoteC) and (cVoteD) > (cVoteR):
        win = "Diana.DeGette"
    else:
        win = "Raymon.Anthony.Doane"
    
print(" ")
print("Election Results")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print(" ")
print(f"Total votes: {tVotes}")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print(" ")
print(f"Charles Casper Stockham: {fpVoteC} ({cVoteC})")
print(f"Diana DeGette: {fpVoteD} ({cVoteD})")
print(f"Raymon Anthony Doane: {fpVoteR} ({cVoteR})")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print(" ")
print(f"Winner: {win}")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print(" ")

# Set variable for output file
output_file = os.path.join("PyPoll")

#  Open the output file
with open(output_file, "w") as txtfile:
    writer = csv.writer(txtfile, delimiter=' ', quoting=csv.QUOTE_NONE)
    writer.writerow(".")
    writer.writerow("Election.Results")
    writer.writerow("_._._._._._._._._._._._._._._._._._._")
    writer.writerow(".")
    writer.writerow(f"Total.votes:.{tVotes}")
    writer.writerow("_._._._._._._._._._._._._._._._._._._")
    writer.writerow(".")
    writer.writerow(f"Charles.Casper.Stockham:.{fpVoteC}.({cVoteC})")
    writer.writerow(f"Diana.DeGette:.{fpVoteD}.({cVoteD})")
    writer.writerow(f"Raymon.Anthony.Doane:.{fpVoteR}.({cVoteR})")
    writer.writerow("_._._._._._._._._._._._._._._._._._._")
    writer.writerow(".")
    writer.writerow(f"Winner:.{win}")
    writer.writerow("_._._._._._._._._._._._._._._._._._._")
    writer.writerow(".")
    