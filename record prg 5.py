d = {}
def create_dict():
    n = int(input('Number of students: '))
    for i in range(n):
        roll = int(input('Roll no: '))
        name = input('Name: ')
        marks = int(input('Marks: '))
        d[roll] = [name, marks]
    return d

def above_75(d):
    for roll in d:
        if d[roll][1] > 75:
            print(d[roll][0])
            
create_dict()
above_75(d)
