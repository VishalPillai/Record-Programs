status = []
contact = {101: ['Aron', 18181, 24000]}

def Push():
    for i in contact:
        status.append([contact[i][0], contact[i][1]])

def pop():
    while len(status) > 0:
        print(status.pop())
    else:
        print("Stack Underflow")

def Display():
    if len(status) == 0:
        print("Stack empty")
    else:
        for i in range(len(status) - 1, -1, -1):
            print(status[i])

while True:
    choice = int(input("Enter 1 for push, 2 to Display or 3 to Pop: "))
    if choice == 1:
        Push()
    elif choice == 2:
        Display()
    elif choice == 3:
        pop()
        break
