import mysql.connector as m
def created():
    con = m.connect(host='localhost',user='root',passwd='student')
    c= con.cursor()
    c.execute("CREATE DATABASE IF NOT EXISTS db1")
    print("Created Succesfully")
    con.close()
created()
