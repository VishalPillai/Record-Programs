def CreatePledge():
    file = open("pledge.txt","w")
    n = int(input("Enter no of lines"))
    for i in range(n):
        lines = input("Enter pledge")
        file.write(lines+
                   "\n")

    file.close()
def DisplayPledge():
    file = open("pledge.txt","r")
    for i in file:
        i = i.strip()
        print(i," - ",len(i)," characters")
    file.close()
CreatePledge()
DisplayPledge() 
