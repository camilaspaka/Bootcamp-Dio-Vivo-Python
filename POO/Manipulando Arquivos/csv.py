import csv 

with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)