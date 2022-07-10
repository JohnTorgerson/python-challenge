#Import file along filepath
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#Read the CSV File
with open(csvpath, encoding='utf') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
