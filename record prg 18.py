import pickle
def createCinema():
    f = open("CINEMA.DAT","ab")
    while True:
        mno = int(input("Enter movie number: "))
        mname = input("Enter movie name: ")
        mtype = input("Enter movie type")
        rec = {'MNO':mno,'MNAME':mname,'MTYPE':mtype}
        pickle.dump(rec,f)
        ch = input("Add another movie? (Y/N)?")
        if ch.upper() == "N":
            break
f.close()

def findType(mtype):
    f = open("CINEMA.DAT","rb")
    found = False
    try:
        while True:
            rec = pickle.load(f)
            if rec['MTYPE'] = pickle.load(f)
                print(rec)
                found = True
    except EOFError:
        f.close()
    if found == False:
        print("No movie found with type",mtype)
createCinema()
typ = input("Enter movie type to search: ")
findType(typ)
