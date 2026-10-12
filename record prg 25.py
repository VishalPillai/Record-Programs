Books=[]
while True:
    choice = int(input("Enter 1 to PUSH, 2 to display stack, 3 to pop"))
    def PUSH (Books,N):
        for i in range(N):
            bno = int(input("Enter book number"))
            bnm = input("Enter book's name")
            cost = int(input("Enter price"))
            Books.append([bno,bnm,cost])
            
    def DispStack():
        if Books == []:
            print("Stack empty")
        else:
            for i in range (len(Books)-1,-1,-1):
                print(Books[i])


    def pop():
        while len(Books)>0:
            print(Books.pop())
        else:
            print("Stack Underflow")

    if choice == 1:
        N= int(input("Enter no of books"))
        PUSH(Books,N)
    elif choice == 2:
        DispStack()
    elif choice == 3:
        pop()
    
