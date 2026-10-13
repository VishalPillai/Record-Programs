import pickle

def Create():
    f = open("PASSENGERS.DAT", "ab")
    while True:
        pnr = input("Enter PNR: ")
        name = input("Enter passenger name: ")
        brd = input("Enter boarding station: ")
        dest = input("Enter destination: ")
        fare = float(input("Enter fare: "))
        rec = [pnr, name, brd, dest, fare]
        pickle.dump(rec, f)
        ch = input("Add another passenger? (Y/N): ")
        if ch.upper() == "N":
            break
    f.close()

def SearchDestn(D):
    f = open("PASSENGERS.DAT", "rb")
    found = False
    try:
        while True:
            rec = pickle.load(f)
            if rec[3].lower() == D.lower():
                print(rec)
                found = True
    except EOFError:
        f.close()
    if found == False:
        print("No passenger found")

def UpdateFare():
    f = open("PASSENGERS.DAT", "rb")
    data = []
    try:
        while True:
            rec = pickle.load(f)
            rec[4] = rec[4] + rec[4] * 5 / 100
            data.append(rec)
    except EOFError:
        f.close()
    f = open("PASSENGERS.DAT", "wb")
    for rec in data:
        pickle.dump(rec, f)
    f.close()
    print("Fare updated successfully")

def DeleteData():
    p = input("Enter PNR to delete: ")
    f = open("PASSENGERS.DAT", "rb")
    data = []
    found = False
    try:
        while True:
            rec = pickle.load(f)
            if rec[0] == p:
                found = True
            else:
                data.append(rec)
    except EOFError:
        f.close()
    f = open("PASSENGERS.DAT", "wb")
    for rec in data:
        pickle.dump(rec, f)
    f.close()
    if found:
        print("Passenger record deleted")
    else:
        print("PNR not found")

Create()
d = input("Enter destination to search: ")
SearchDestn(d)
UpdateFare()
DeleteData()
