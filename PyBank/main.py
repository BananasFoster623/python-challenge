# Import all needed modules and libraries
import csv
from pathlib import Path

# Open the budget_data.csv file and assign to a list 'data'
readpath = Path.cwd() / 'Resources' / 'budget_data.csv'
with open(readpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = list(reader)

# Loop down the Profit/Losses column and calculate the total sum    
netTally = 0
for i in range(1,len(data),1):
    netTally = netTally + int(data[i][1])

# Loop down the Profit/Losses column and find the greatest increase and greatest decrease in profits
greatInc = ["",0]
greatDec = ["",0]
avgCalc = 0
for i in range(1,len(data)-1,1): # loop for the increase AND decrease using two if statements
    diff = int(data[i+1][1])-int(data[i][1])
    avgCalc = avgCalc + diff
    if (diff > greatInc[1]):
        greatInc[0] = data[i+1][0]
        greatInc[1] = diff
    if (diff < greatDec[1]):
        greatDec[0] = data[i+1][0]
        greatDec[1] = diff

# Calculate the average change in profits over the time period
avgCalc = avgCalc/(len(data)-2) # we use len(data)-2 to account for headers (-1) and there being 1 less than the total number of rows for differnce calculation

# Now we write to the file
writepath = Path.cwd() / 'Analysis' / 'analysis.txt'
with open(writepath,'w') as outFile:
    outFile.write('Financial Analysis\n')
    outFile.write('---------------------------------------------------------------\n')
    outFile.write(f'Total Months: {len(data)-1}\n') # Need to subtract 1 because of the headers
    outFile.write(f'Total: ${netTally}\n')
    outFile.write(f'Average Change: ${avgCalc:.2f}\n')
    outFile.write(f'The greatest increase in profits: {greatInc[0]}  (${greatInc[1]})\nThe greatest decrease in profits: {greatDec[0]}  (${greatDec[1]})\n')

print('Financial Analysis')
print('---------------------------------------------------------------')
print(f'Total Months: {len(data)-1}') # Need to subtract 1 because of the headers
print(f'Total: ${netTally}')
print(f'Average Change: ${avgCalc:.2f}')
print(f'The greatest increase in profits: {greatInc[0]}  (${greatInc[1]})\nThe greatest decrease in profits: {greatDec[0]}  (${greatDec[1]})')