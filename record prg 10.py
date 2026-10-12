def CreateWord():
    f1 =open("word.txt","w")
    l1=[]
    while True:
        txt = input("Enter sentences, enter ! to stop entering text")
        if txt == "!":
            break
        else:
            l1+=[txt]
    global l2
    l2 = []
    for i in l1:
        l2+= [i]
    f1.writelines(l2)
def DisplayFile():
    c1 = 0
    for i in l2:
        while i != "":
            c1+=1
            i = i[:-1:]
    print("The number of characters is : ",c1)
    c2 = 0
    for i in l2:
        c2+=1
    print("The number of words is : ",c2)
CreateWord()
DisplayFile()
