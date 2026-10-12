import mysql.connector as m
def insert():
    con = m.connect(host='localhost',user='root',passwd='student',database='f2_26_27')
    c = con.cursor()
    rno = int(input('Enter roll no'))
    name=input('Enter name')
    gender = input('Enter gender')
    dob = input('Enter dob')
    marks = float(input('Enter marks'))
    c.execute("INSERT INTO student values({},'{}','{}','{}',{})".format(rno,name,dob,gender,marks))
    con.commit()
    print('Values inserted into table')
def display():
    con = m.connect(host='localhost',user='root',passwd='student',database='f2_26_27')
    c = con.cursor()
    c.execute("SELECT * FROM student")
    con.close()
insert()
