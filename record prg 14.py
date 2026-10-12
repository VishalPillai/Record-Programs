def createText():
    f = open("wisdom.txt","w")
    n = int(input("Enter no of lines : "))
    for i in range(n):
        line = input("Enter line: ")
        f.write(line+"\n")
    f.close()
def NoVowels():
    f = open("wisdom.txt","r")
    txt = f.read()
    f.close()
    words = txt.split()
    for i in words:
        flag = True
        for ch in i.lower():
            if ch in "aeiou":
                flag = False
                break
        if flag:
            print(i)
def vowelWord():
    f = open("wisdom.txt","r")
    print("Words with vowels:")
    for line in f:
        txt = line.split()
        if len(words)>0:
            first = words[0]
            if len(first)>=2 and first[1].lower() in "aeiou":
                print(line.strip())
    f.close()
createText()
NoVowels()
vowelWord()
