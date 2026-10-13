import pickle

def CreateEmp():
    f = open("emp.dat", "ab")
    while True:
        eno = int(input("Enter employee number: "))
        name = input("Enter employee name: ")
        job = input("Enter job: ")
        sal = float(input("Enter salary: "))
        rec = {eno: [name, job, sal]}
        pickle.dump(rec, f)
        ch = input("Add another employee? (Y/N): ")
        if ch.upper() == "N":
            break
    f.close()

def DisplayEmps():
    f = open("emp.dat", "rb")
    print("\nEmpNo\tName\t\tJob\t\tSalary")
    print("-" * 55)
    try:
        while True:
            rec = pickle.load(f)
            for eno in rec:
                data = rec[eno]
                print(eno, "\t", data[0], "\t\t", data[1], "\t\t", data[2])
    except EOFError:
        f.close()

def SearchEmp():
    f = open("emp.dat", "rb")
    found = False
    print("\nEmployees with salary between 25000 and 30000")
    print("EmpNo\tName\t\tJob\t\tSalary")
    print("-" * 55)
    try:
        while True:
            rec = pickle.load(f)
            for eno in rec:
                data = rec[eno]
                if 25000 <= data[2] <= 30000:
                    print(eno, "\t", data[0], "\t\t", data[1], "\t\t", data[2])
                    found = True
    except EOFError:
        f.close()
    if found == False:
        print("No employee found")

def SearchEmpno(eno):
    f = open("emp.dat", "rb")
    found = False
    try:
        while True:
            rec = pickle.load(f)
            if eno in rec:
                data = rec[eno]
                print("EmpNo:", eno, "Name:", data[0], "Job:", data[1], "Salary:", data[2])
                found = True
    except EOFError:
        f.close()
    if found == False:
        print("Employee not found")

CreateEmp()
DisplayEmps()
SearchEmp()
eno = int(input("\nEnter employee number to search: "))
SearchEmpno(eno)
