# Import all needed modules and libraries
import csv

# Open the election_data.csv file and assign to a list 'data'
with open('.\\Resources\\election_data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = list(reader)

rows = len(data) ## This value -1 is our total number of votes cast
cols = len(data[0]) ## This is our number of columns

candidateNames = []
for i in range(1,len(data),1):
    # if current (i,2) value is not in candidateNames list, append
    if data[i][2] not in candidateNames:
        candidateNames.append(data[i][2])

voteCounts = []
for i in range(len(candidateNames)):   
    voteCounts.append(sum(x.count(candidateNames[i]) for x in data))

votePercent = []
for i in range(len(voteCounts)):
    votePercent.append(voteCounts[i]/(rows-1))

print(votePercent)

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