import mysql.connector as m

con = m.connect(host='localhost', user='root', passwd='student', database='db1')
c = con.cursor()

def Create_Table():
    c.execute('CREATE TABLE IF NOT EXISTS MYPET (Pet_Id int, Pet_name varchar(20), Breed varchar(20), lifespan int, Price int, discount int)')

def Add_pet():
    while True:
        no = int(input("Enter pet number: "))
        name = input("Enter pet's name: ")
        breed = input("Enter the name of the breed: ")
        lsp = int(input("Enter lifespan of the breed: "))
        price = int(input("Enter the price of the breed: "))
        disc = int(input("Enter discount: "))
        c.execute("INSERT INTO MYPET values({},'{}','{}',{},{},{})".format(no, name, breed, lsp, price, disc))
        con.commit()
        yn = input("y to continue, n to stop: ")
        if yn.lower() == 'n':
            break

def Display_petdetails():
    c.execute("SELECT * FROM MYPET")
    print(c.fetchall())

def Reduce_Price():
    c.execute("UPDATE MYPET SET PRICE=PRICE*(DISCOUNT/100) WHERE DISCOUNT < 5")
    con.commit()
    print("Price updated successfully")

Create_Table()
Add_pet()
Display_petdetails()
Reduce_Price()
c.close()
