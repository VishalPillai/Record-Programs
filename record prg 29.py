stack=[]
N=[12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
def PUSHNums(N):
    for i in N:
        if i%2 == 0:
            stack.append(i)
def PopNums():
    while len(stack) > 0:
        print(stack.pop(),end=" ")
    else:
        print("Stack Underflow")
while True:
    choice = int(input("Enter 1 to push, 2 to pop, 3 to exit"))
    if choice == 1:
        PUSHNums(N)
    elif choice == 2:
        PopNums()
    elif choice == 3:
        break
