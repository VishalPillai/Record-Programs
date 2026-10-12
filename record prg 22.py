import csv

def Add_data(filename):
    f = open(filename, "a+", newline="")
    f.seek(0)
    
    
    if f.read() == "":
        f.seek(0)
        w = csv.writer(f)
        w.writerow(["student_id", "name", "class", "div", 
                    "subject", "score", "grade_level"])
                    
    f.seek(0, 2)
    w = csv.writer(f)
    
    while True:
        sid = int(input("Enter Student ID: "))
        name = input("Enter Name: ")
        cls = input("Enter Class: ")
        div = input("Enter Division: ")
        subject = input("Enter Subject: ")
        score = float(input("Enter Score: "))
        grade = input("Enter Grade Level: ")
        
        w.writerow([sid, name, cls, div, subject, score, grade])
        
        ch = input("Add another record? (Y/N): ")
        if ch.upper() == "N":
            break
            
    f.close()

def Display_data(filename):
    subject = input("Enter Subject: ")
    cls = input("Enter Class: ")
    div = input("Enter Division: ")
    
    f = open(filename, "r", newline="")
    r = csv.reader(f)
    
    next(r)        
    
    total = 0
    count = 0
    
    for rec in r:
        if (rec[4].lower() == subject.lower() and
            rec[2] == cls and
            rec[3].lower() == div.lower()):
            
            total = total + float(rec[5])
            count = count + 1
            
    f.close()
    
    if count > 0:
        avg = total / count
        print("Average Score =", avg)
    else:
        print("No matching records found")


Add_data("students.csv")
Display_data("students.csv")
