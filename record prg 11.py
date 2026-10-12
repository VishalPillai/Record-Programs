def CreateStory():
    f1 =open("story.txt","w")
    n=  int(input("Enter number of lines"))
    for i in range(n):
        lines = input("Enter line: ")
        f1.write(lines+"\n")
    f1.close()
def DisplayWord():
    f2 = open("story.txt","r")
    d = f2.read()
    words = d.split()
    print("#".join(words))

        
CreateStory()
DisplayWord()
