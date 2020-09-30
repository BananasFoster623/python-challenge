# python-challenge
Homework 2 for the Georgia Tech Professional Education Data Science and Analytics BootCamp. This project has four parts:

- PyBank
- PyPoll
- PyBoss (extra credit)
- PyParagraph (extra credit)

# Summary of Deliverables
This repository is broken up into 4 directories, one for each of the parts listed above. Each repository has the following:
- main.py
- Analysis
  - Contains the output file (i.e. results of the code)
- Resources
  - Contains the source data that is manipulated to produce the output

# Code Descriptions

## General
Every main.py file uses the csv and pathlib libraries for importing data. 

## PyBank
This script does the following:
1. Loops down the Profit/Losses column and adding each successive value to a helper variable to calculate the total sum. 
2. Loops down the Profit/Losses column, calculating the difference between the current row and next row. If the calculated value is greater or less  than the already found greatest Inc or Dec, it replaces the value of that variable. It also successively adds the difference to a helper variable for use in the next step. 
3. Uses the previously found sum of difference and divides by the total number of rows (i.e. months). The total number uses total length of list minus 2 to account for the header row and the fact that there is one less row used in the difference calculation.
4. Write to a .txt file and the terminal using problem statement specified formatting. 


