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
for i in range(1,len(data)):
    SSNSplit = data[i][4].split("-")
    NewSSN = "***-**-"+SSNSplit[2]
    data[i][4] = NewSSN

## Copy and pasted dictionary of state abbreviations from a public domain file on github
# United States of America Python Dictionary to translate States,
# Districts & Territories to Two-Letter codes and vice versa.
#
# https://gist.github.com/rogerallen/1583593
#
# Dedicated to the public domain.  To the extent possible under law,
# Roger Allen has waived all copyright and related or neighboring
# rights to this code.

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

# Use the above defined dictionary to convert states to abbreviations
for i in range(1,len(data)):
    temp = us_state_abbrev[data[i][5]]
    data[i][5] = temp

# Write everything out to a csv file
writepath = Path.cwd() / 'Analysis' / 'new_employee_data.csv'
with open(writepath, 'w', newline='') as outFile:
    csvwriter = csv.writer(outFile,delimiter = ',')
    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    for i in range(1,len(data)):
        csvwriter.writerow([data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5]])

####### DEBUGGING OUTPUTS ########
temp = False
if temp == True:
    rows = int(len(data))
    cols = int(len(data[0]))
    print(rows, cols)
    for i in range(1,rows):
        print(f'{data[i][0]}  {data[i][1]}  {data[i][2]}  {data[i][3]}  {data[i][4]} {data[i][5]}')
####### DEBUGGING OUTPUTS ########