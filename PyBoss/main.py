# Import all modules, libraries, and dependencies
import csv
from pathlib import Path

# Open the employee_data.csv and assign it to a list data
readpath = Path.cwd() / 'Resources' / 'employee_data.csv'
with open(readpath) as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    data = list(reader) # This file has headers, so our data starts at row index 1

# Insert column after name that all says "temp"
for i in range(1,len(data)):
    NameSplit = data[i][1].split()
    data[i][1] = NameSplit[0]
    data[i].insert(2,NameSplit[1])

# Convert the date column into a list of strings, then rewrite over the column value
# Starting format: yyyy-mm-dd
# Ending format:   mm/dd/yyyy
for i in range(1,len(data)):
    DateSplit = data[i][3].split("-")
    NewDate = DateSplit[1]+'/'+DateSplit[2]+'/'+DateSplit[0]
    data[i][3] = NewDate

# Convert the SSN column such that the first five DIGITS are asterisks (*)

####### TEMP SECTION ########
temp = True
if temp == True:
    rows = int(len(data))
    cols = int(len(data[0]))
    print(rows, cols)

    for i in range(1,len(data)):
        print(f'{data[i][0]}  {data[i][1]}  {data[i][2]}  {data[i][3]}  {data[i][4]} ')
####### TEMP SECTION ########