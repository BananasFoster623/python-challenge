# Import all needed modules and libraries
import csv

# Open the election_data.csv file and assign to a list 'data'
with open('.\\Resources\\election_data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = list(reader)

rows = len(data)
cols = len(data[0])

print(f'There are {rows} rows and {cols} columns in this dataset. ')
print(f'The column names are: {data[0][0]} - {data[0][1]} - {data[0][2]}')






# Prepare the terminal output
print('\n\n') ### This is temporary until final formatting
print('Election Results')
print('---------------------------------------------------------------')
print(f'Total Votes: ')
print('---------------------------------------------------------------')
print(f'Khan:')
print(f'Correy: ')
print(f'Li: ')
print(f'O\'Tooley: ')
print('---------------------------------------------------------------')
print(f'Winner: ')
print('---------------------------------------------------------------')