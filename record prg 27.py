Book = []

def PushBook():
    book_no = int(input("Enter book no: "))
    book_title = input("Enter book title: ")
    Book.append([book_no, book_title])

def PopBook():
    while len(Book) > 0:
        item = Book.pop()
        print(item[0], ":", item[1])
    else:
        print("Stack Underflow")

def Disp_Stack():
    if len(Book) == 0:
        print("Stack empty")
    else:
        for i in range(len(Book) - 1, -1, -1):
            print(Book[i][0], ':', Book[i][1])

while True:
    choice = int(input("Enter 1 for push, 2 to Display or 3 to Pop: "))
    if choice == 1:
        PushBook()
    elif choice == 2:
        Disp_Stack()
    elif choice == 3:
        PopBook()
        break
