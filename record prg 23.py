import csv

def Newgadget():
    f = open('gadgets.csv', 'w', newline='')
    csw = csv.writer(f)
    csw.writerow(['Deviceno', 'Name', 'Price', 'Brand'])
    while True:
        dno = int(input("Enter device number: "))
        name = input("Enter device name: ")
        price = int(input("Enter price of gadget: "))
        brand = input("Enter brand name: ")
        csw.writerow([dno, name, price, brand])
        x = input("Enter y to continue and n to stop: ")
        if x.lower() == 'n':
            break
    f.close()

def Countgadget():
    f = open('gadgets.csv', 'r')
    d = csv.reader(f)
    count = 0
    next(d)
    for i in d:
        if 1000 <= int(i[2]) <= 2500:
            count += 1
            print(i)
    print("There are", count, "no of devices in the price range 1000-2500")
    f.close()

Newgadget()
Countgadget()
