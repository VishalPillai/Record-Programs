import mysql.connector as m
con = m.connect(host='localhost',user='root',passwd="student",database ='db1')
c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Fabric(\
FCODE varchar(3) primary key,TYPE varchar(20))")
c.execute("CREATE TABLE IF NOT EXISTS Garment\
(GCODE int primary key,Description varchar(30),PRICE int,FCODE varchar(3),READYDATE date)")
def garment():
        gcode = int(input("Enter GCODE"))
        desc = input("Enter description")
        price = int(input("Enter price"))
        fcode = str(input("Enter FCODE"))
        readydate = input("Enter Date")
        c.execute("INSERT INTO GARMENT values({},'{}',{},'{}','{}')".format(gcode,desc,price,fcode,readydate))    
        con.commit()
def fabric():
        fcode = str(input("Enter Fcode"))
        typ = input("Enter the type of fabric")
        c.execute("INSERT INTO FABRIC values('{}','{}')".format(fcode,typ))
        con.commit()
while True:
    choice = input("Enter g for garment or f for fabric")
    if choice.lower() == 'g':
        garment()
    elif choice.lower() == 'f':
        fabric()
    else:
        break
con.close()
        
    
        
