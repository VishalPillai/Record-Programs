import mysql.connector as m;
con = m.connect(host='localhost',user='root',passwd='student',database='db1')
c = con.cursor()
def list_table():
    c.execute("SHOW TABLES")
    data = c.fetchall()
    print(data)
c.execute("CREATE TABLE IF NOT EXISTS GARMENT \
(GCODE int, Description varchar(30),PRICE int,FCODE varchar(3),READYDATE date)")
c.execute("CREATE TABLE IF NOT EXISTS FABRIC (FCODE varchar(3),TYPE varchar(20))")
def garment():
        gcode = int(input("Enter GCODE"))
        desc = input("Enter description")
        price = int(input("Enter price"))
        fcode = str(input("Enter FCODE"))
        readydate = input("Enter Date")
        c.execute("INSERT INTO GARMENT values({},'{}',{},'{}','{}')"\
                  .format(gcode,desc,price,fcode,readydate))    
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
def display_Structure():
    c.execute("DESC FABRIC")
    data = c.fetchall()
    print(data)
def delete_record():
    ask = input("Enter a GCODE to delete")
    c.execute("DELETE FROM GARMENT WHERE GCODE='{}'".format(ask))
    con.commit()
    print("Record deleted successfully")
def modifytble():
    gcode = input("Enter a GCODE to change the price")
    price = int(input("Enter new price for garment"))
    c.execute("UPDATE GARMENT SET PRICE={} WHERE GCODE={}".format(price,gcode))
    print("Price modified successfully")
    con.commit()
    c.execute("select *from garment where gcode = {}".format(gcode))
    print(c.fetchall())
def displayrecords():
    tble = input("Enter g or f to display garment or fabric")
    if tble.lower() == 'g':
        c.execute("select * from garment")
        for row in c.fetchall():
            print(*row,sep = " | ")
    elif tble.lower == 'f':
        c.execute("select * from fabric")
        for row in c.fetchall():
            print(*row,sep = " | ")
        
list_table()
display_Structure()
displayrecords()
modifytble()
delete_record()
con.close()
