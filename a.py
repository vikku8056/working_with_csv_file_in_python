# read a csv reader method
import csv
with open(r'C:\Users\Vikas\Downloads\courses\springboard\python using csv file\a.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for record in reader:
        print(record)
