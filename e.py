# using dictwrite
import csv
with open(r'C:\Users\Vikas\Downloads\courses\springboard\python using csv file\a.csv', 'w', newline='') as csvfile:
    fields = ['EmpId', 'Emp Name', 'Salary']
    writer = csv.DictWriter(csvfile, fields)
    writer.writeheader()
    writer.writerow({'EmpId': 1, 'Emp Name': 'Ramesh', 'Salary': 22001.00})
    writer.writerow({'EmpId': 2, 'Emp Name': 'Rakesh', 'Salary': 26501.00})
