# write in csv file
import csv
with open(r'C:\Users\Vikas\Downloads\courses\springboard\python using csv file\a.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['EmpId', 'Emp Name', 'Salary'])
    writer.writerow([1, 'Ramesh', 22001.00])
    writer.writerow([2, 'Rakesh', 26501.00])
