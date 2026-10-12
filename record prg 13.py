def CreatePoem():
    f = open("poem.txt","w")
    n = int(input("Enter no of lines"))
    for i in range(n):
        lines = input("Enter poem"+"\n")
        f.write(lines)
    f.close()
def DisplayPoem():
    f = open("poem.txt","r")
    lines = f.read()
    lines = lines.lower()
    words = lines.split()
    occ ={}
    l1 =[]
    for i in words:
        if i in occ:
            occ[i] = occ[i] + 1
        else:
            occ[i] = 1
    print("\nOccurence Dictionary:")
    print(occ)
    items = list(occ.items())
    for i in range(len(items) - 1):
        for j in range(i+1, len(items)):
            if items[i][1] < items[j][1]:
                temp = items[i]
                items[i] = items[j]
                items[j] = temp
    sorted_occ = {}
    for item in items:
        word = item[0]
        count = item[1]
        sorted_occ[word] = count
    print("\nDictionary sorted by occurence:")
    print(sorted_occ)
    n = int(input("\nEnter  number of most common words: "))
    print("\nMost commonly occurring words:")
    count = 0
    for word in sorted_occ:
        if count < n:
            print(word,"-",sorted_occ[word])
            count = count+1
        else:
            break
    
CreatePoem()
DisplayPoem()
