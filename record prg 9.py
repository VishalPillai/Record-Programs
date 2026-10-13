f1 = open("Names.txt", "r")
d = f1.readlines()
f1.close()

def extract_unique_name():
    l1 = []
    for i in d:
        t = i.strip().lower()
        if t not in l1:
            l1 += [t]
    l1.sort()
    print(l1)

extract_unique_name()
