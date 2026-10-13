def CreatePledge():
    file = open("pledge.txt", "w")
    n = int(input("Enter no of lines: "))
    for i in range(n):
        line = input("Enter pledge: ")
        file.write(line + "\n")
    file.close()

def DisplayPledge():
    file = open("pledge.txt", "r")
    for line in file:
        line = line.strip()
        print(line, "-", len(line), "characters")
    file.close()

CreatePledge()
DisplayPledge()
