import mysql.connector as m
def insertv():
    con = m.connect(host = 'localhost',user='root',passwd='student',database='f2_26_27')
    c = con.cursor()
    c.execute("INSERT INTO student values(1,'Aagney','2009-01-23','M',300.35)")
    con.commit()
    print('Table modified succesfully')
    con.close()
insertv()
