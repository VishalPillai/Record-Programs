import csv
def add_book():
    r=[]
    f = open('Inventory.csv','a',newline='')
    csw = csv.writer(f)
    csw.writerow(['BookID','Title','Author','Available'])
    while True:
        r = int(input("Enter new book id"))
        title = input('Enter title of book')
        atr = input("Enter the author's name")
        avl = int(input("Enter availability"))
        csw.writerow([r,title,atr,avl])
        x = input("Y to continue, n to stop")
        if x.lower()=="n":
            break
    f.close()
            
def check_availability(id1):
    f = open('Inventory.csv','r')
    d = csv.reader(f)
    next(d)
    for i in d:
        if int(i[0]) == id1:
            return(i[3])
    else:
        return(-1)
    f.close()
add_book()
id1 = int(input("Enter book id to check availability"))
print(check_availability(id1))
