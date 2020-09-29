# Import all needed modules and libraries
import csv
from pathlib import Path

# Open the election_data.csv file and assign to a list 'data'
value = input("Please enter filename (include extension): \n")
readpath = Path.cwd() / 'Resources' / value
with open(readpath) as readfile:
    print(readfile.read())