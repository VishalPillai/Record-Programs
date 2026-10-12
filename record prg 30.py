Arr=[]
l1=[]
def PUSH(L):
    for i in l1:
        if i%5 ==0:
            Arr.append(i)
def display():
    if Arr != []:
        print(Arr)
    else:
        print("Stack Empty")
def POP():
    if Arr == []:
        print("Stack Underflow")
    else:
        print(Arr.pop())
while True:
    choice = int(input("Enter 1 to push, 2 to display, 3 to Pop"))
    if choice == 1:
        l1 = list(eval(input("Enter random numbers, seperated by comma")))
        PUSH(l1)
    elif choice == 2:
        display()
    elif choice == 3:
        POP()
