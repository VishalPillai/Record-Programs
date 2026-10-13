def CreateWord():
    f = open("word.txt", "w")
    while True:
        txt = input("Enter sentences, enter ! to stop entering text: ")
        if txt == "!":
            break
        f.write(txt + "\n")
    f.close()

def DisplayFile():
    f = open("word.txt", "r")
    text = f.read()
    chars = len(text.replace("\n", ""))
    words = len(text.split())
    print("The number of characters is :", chars)
    print("The number of words is :", words)
    f.close()

CreateWord()
DisplayFile()
