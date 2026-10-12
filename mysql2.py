import mysql.connector as m
def createt():
    con = m.connect(user='root',passwd='student',host='localhost',database="f2_26_27")  
    c = con.cursor()
    c.execute('CREATE TABLE student(rno int,name varchar(20), dob date,gender char(1), mark decimal(5,2) )')
    print('Table created succesfully')
    con.close()
createt()
