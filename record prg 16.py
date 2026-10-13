import pickle

def MakeFile():
    f = open("Items.dat", "ab")
    while True:
        code = int(input("Enter item code: "))
        desc = input("Enter description: ")
        price = int(input("Enter price: "))
        rec = [code, desc, price]
        pickle.dump(rec, f)
        ch = input("Add another item? (Y/N): ")
        if ch.upper() == "N":
            break
    f.close()

def SearchRec(Code):
    f = open("Items.dat", "rb")
    total = 0
    count = 0
    try:
        while True:
            rec = pickle.load(f)
            total += 1
            if rec[0] == Code:
                print(rec)
                count += 1
    except EOFError:
        f.close()
    if count == 0:
        print("Item not found")
    print("Number of items having code", Code, "=", count)
    print("Total number of items =", total)

MakeFile()
c = int(input("Enter code to search: "))
SearchRec(c)
