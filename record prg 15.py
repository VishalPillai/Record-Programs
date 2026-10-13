import pickle

def crtBookFile():
    f = open("book.dat", "wb")
    n = int(input("Enter number of books: "))
    for i in range(n):
        bid = int(input("Enter Book id: "))
        bname = input("Enter book name: ")
        author = input("Enter author name: ")
        price = float(input("Enter price: "))
        book = [bid, bname, author, price]
        pickle.dump(book, f)
    f.close()

def BookPrice():
    f = open("book.dat", "rb")
    p = float(input("Enter price: "))
    try:
        while True:
            book = pickle.load(f)
            if book[3] > p:
                print(book)
    except EOFError:
        f.close()

def SearchBook():
    f = open("book.dat", "rb")
    name = input("Enter Book Name to search: ")
    found = False
    try:
        while True:
            book = pickle.load(f)
            if book[1].lower() == name.lower():
                print(book)
                found = True
    except EOFError:
        f.close()
    if found == False:
        print("Book Not Found")

crtBookFile()
BookPrice()
SearchBook()
