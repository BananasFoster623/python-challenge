# Import all needed modules and libraries
import csv
from pathlib import Path

# Open the election_data.csv file and assign to a list 'data'
readpath = Path.cwd() / 'Resources' / 'election_data.csv'
with open(readpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = list(reader)

rows = len(data) ## This value -1 is our total number of votes cast
cols = len(data[0]) ## This is our number of columns

# Calculate Total Vote Count
# It will be the total number of rows minus the header row
totalVoteCount = rows - 1

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
    candVotePercent.append(100*(candVoteCounts[i]/(rows-1)))

# Find the winner
winner = candidateNames[candVoteCounts.index(max(candVoteCounts))]

# Print out to analysis.txt
outpath = Path.cwd() / 'Analysis' / 'analysis.txt'
with open(outpath,'w') as outFile:
    outFile.write('Election Results\n')
    outFile.write('---------------------------------------------------------------\n')
    outFile.write(f'Total Votes: {totalVoteCount}\n')
    outFile.write('---------------------------------------------------------------\n')
    for x in range(len(candidateNames)):
        outFile.write(f'{candidateNames[x]}: {candVotePercent[x]:4f}% ({candVoteCounts[x]})\n')
    outFile.write('---------------------------------------------------------------\n')
    outFile.write(f'Winner: {winner}\n')
    outFile.write('---------------------------------------------------------------\n')

# Prepare the terminal output
print('Election Results')
print('---------------------------------------------------------------')
print(f'Total Votes: {totalVoteCount}')
print('---------------------------------------------------------------')
for x in range(len(candidateNames)):
    print(f'{candidateNames[x]}: {candVotePercent[x]:4f}% ({candVoteCounts[x]})')
print('---------------------------------------------------------------')
print(f'Winner: {winner}')
print('---------------------------------------------------------------')