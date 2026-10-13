import csv

def accept_record():
    f = open("Performance.csv", "w", newline='')
    csw = csv.writer(f)
    csw.writerow(['Emp_Id', 'Emp_Name', 'Project_Name', 'Review_Result'])
    while True:
        eid = int(input("Enter Employee ID: "))
        ename = input("Enter Employee Name: ")
        pname = input("Enter Project Name: ")
        result = input("Enter Review Result (Excellent/Satisfactory/Needs Improvement): ")
        csw.writerow([eid, ename, pname, result])
        ch = input("Add another record? (Y/N): ")
        if ch.upper() == "N":
            break
    f.close()

def excellent_count():
    f = open("Performance.csv", "r")
    d = csv.reader(f)
    next(d)
    count = 0
    for i in d:
        if i[3].lower() == "excellent":
            count += 1
            print(i)
    print("Number of employees with Excellent review:", count)
    f.close()

accept_record()
excellent_count()
