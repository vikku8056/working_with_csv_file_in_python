# If you observe, we get a blank line between every record. This is because writerow inserts a newline after every insertion and also open method also inserts a newline character. It can be removed as follows:
import csv
with open(r'C:\Users\Vikas\Downloads\courses\springboard\python using csv file\a.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['EmpId', 'Emp Name', 'Salary'])
    writer.writerow([1, 'Ramesh', 22001.00])
    writer.writerow([2, 'Rakesh', 26501.00])
