Arr = []

def PUSH(L):
    for i in L:
        if i % 5 == 0:
            Arr.append(i)

def display():
    if len(Arr) != 0:
        print(Arr)
    else:
        print("Stack Empty")

def POP():
    if len(Arr) == 0:
        print("Stack Underflow")
    else:
        print(Arr.pop())

while True:
    choice = int(input("Enter 1 to push, 2 to display, 3 to Pop: "))
    if choice == 1:
        l1 = list(eval(input("Enter random numbers, seperated by comma: ")))
        PUSH(l1)
    elif choice == 2:
        display()
    elif choice == 3:
        POP()
        break
