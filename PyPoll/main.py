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

# Find the count of votes for for EACH candidate
candVoteCounts = []
for i in range(len(candidateNames)):   
    candVoteCounts.append(sum(x.count(candidateNames[i]) for x in data))

candVotePercent = []
for i in range(len(candVoteCounts)):
    candVotePercent.append(candVoteCounts[i]/(rows-1))

print(candVotePercent)

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