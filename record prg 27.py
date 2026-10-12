Book = []
while True:
    def PushBook():
        book_no= int(input("Enter book no"))
        book_title = input("Enter book title")
        Book.append([book_no,book_title])
    def PopBook():
        while len(Book)>0:
            print(Book[len(Book)-1][0],":",Book[len(Book)-1][1])
            Book.pop()

        else:
            print("Stack Underflow")
    def Disp_Stack():
        if Book == []:
            print("Stack empty")
        else:
            for i in range (len(Book)):
                print(Book[i][0],':',Book[i][1])

    choice = int(input("Enter 1 for push, 2 to Display or 3 to Pop"))
    if choice == 1:
        PushBook()
    elif choice == 3:
        PopBook()
    elif choice ==2:
        Disp_Stack()
