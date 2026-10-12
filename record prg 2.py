data = [
    ["Alice", 101, [85, 78, 92, 89]],
    ["Bob", 102, [76, 85, 90, 80]],
    ["Charlie", 103, [92, 88, 94, 91]],
    ["David", 104, [60, 72, 70, 65]]
]

def display_average(data):
    print("Average Marks of Students")
    for student in data:
        avg = sum(student[2]) / len(student[2])
        print(student[0], "Roll No:", student[1], "Average:", avg)

def below_70(data):
    print("\nStudents who scored below 70 in any subject")
    for student in data:
        for mark in student[2]:
            if mark < 70:
                print(student[0], "Roll No:", student[1], "Marks:", student[2])
                break

display_average(data)
below_70(data)
