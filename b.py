# read as dictionary, dict reader method
import csv
with open(r'C:\Users\Vikas\Downloads\courses\springboard\python using csv file\a.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for record in reader:
        print(record)
