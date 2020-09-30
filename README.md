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
Every main.py file uses the csv and pathlib libraries for importing data, and that occurs before step 1 in each of the sections below. 

## PyBank
This script does the following:
1. Loops down the Profit/Losses column and adding each successive value to a helper variable to calculate the total sum. 
2. Loops down the Profit/Losses column, calculating the difference between the current row and next row. If the calculated value is greater or less  than the already found greatest Inc or Dec, it replaces the value of that variable. It also successively adds the difference to a helper variable for use in the next step. 
3. Uses the previously found sum of difference and divides by the total number of rows (i.e. months). The total number uses total length of list minus 2 to account for the header row and the fact that there is one less row used in the difference calculation.
4. Write to a .txt file and the terminal using problem statement specified formatting. 

## PyPoll 
This script does the following:
1. Calculates the total vote count by using the total row count minus 1 to account for the header row
2. Finds unique candidate names by starting with an empty list, checking each value in the source list to see if it is in the new list, and if it is not it is appended to the new list. 
3. Loops over the list of unique candidate names, then uses a nested loop to sum the number of rows that has that candidate's name listed.
4. Loops over the list of each candidate's vote count, then uses a nested loop to calculate the percentage of total vote count.
5. Finds the winner finding the max of vote count, then finding the index of that max and extracting respective value from the unique candidate names list. 
6. Write to a .txt file and the terminal using problem statement specified formatting. 

## PyBoss
This script does the following:
1. Insert a column after the existing name column, then use the .split() method to split up the employee names into First and Last name and write them to their respective columns.
2. Use the .split() method to break up the date column by the '-' delimiter and reassembly with string concatenation into the correct date format. 
3. Use the .split() method to break up the SSN column and extract the last 4 digits as a string, then concatenate that string with the prescribed "***-**-" masking of the first 5 digits.
4. Use a public domain dictionary from GitHub (reference given in code comment) to replace the state name with the state abbreviation. 
5. Write out to a csv file. 

## PyParagraph
This script does the following:
1. Use .split() to break up the input paragraph to with the space delimiter, then use the len() function to find the total word count. 
2. Use the re.split() method with the ReGex qualifier given in the problem statement, then use the len() function to find the total sentence count. 
3. Loop over the list of words using the len() function and adding that value succesively to a helper value to find the total character count, then dividing by the word count previously found to find the average word length.
4. Loop over the list of sentences using the len() function and adding that value succesively to a helper value to find the total length of each sentence, then dividing byt the sentence count previously found to find the average sentence length. 
5. Output to the .txt file.
