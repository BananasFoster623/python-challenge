# Import all needed modules and libraries
import csv

# Open the election_data.csv file and assign to a list 'data'
with open('.\\Resources\\election_data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = list(reader)

for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j])
    print()
