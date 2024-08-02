#1. Write a Python program to read a CSV file and display its contents.

import csv

# Path to your CSV file
csv_path = 'ABC.csv'

# Open the CSV file
file = open(csv_path, mode='r')

# Create a CSV reader object
csv_reader = csv.reader(file)

# Read and display each row in the CSV file
for row in csv_reader:
    print(row)

# Close the file
file.close()


# Output

['Python is a popular programming language.']
['Python can be used on a server to create web applications.']
['File handling is an important part of any web application.']
