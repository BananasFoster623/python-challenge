# Import all needed modules and libraries
import csv
import re
from pathlib import Path

# Open the election_data.csv file and assign to a list 'data'
# value = input("Please enter filename (include extension): \n")
value = 'paragraph_2.txt'
readpath = Path.cwd() / 'Resources' / value
with open(readpath) as readfile:
    text = str(readfile.read())

# Split total string up to get word count
wordStrings = text.split()
wordCount = int(len(wordStrings))

# Split total string up to get sentence count
sentenceStrings = re.split("(?<=[.!?]) +", text)
sentenceCount = (len(sentenceStrings))

# Find all the words to find the average word length
temp = 0
for i in wordStrings:
    temp = temp + int(len(i))
wordLength = temp / wordCount

# Find all the sentences to find the average sentence length
temp = 0
for i in sentenceStrings:
    temp = temp + int(len(i))
sentenceLength = temp / sentenceCount

# Output to terminal
print('\n\n')
print('Paragraph Analysis')
print('------------------')
print(f'Approximate Word Count: {wordCount}')
print(f'Approximate Sentence Count: {sentenceCount}')
print(f'Average Letter Count: {wordLength:.2f}')
print(f'Average Sentence Length: {sentenceLength:.2f}')