import mysql.connector
db = connect = None
def initialize(user, password):
    global connect
    global db
    connect = mysql.connector.connect(host='localhost', user=user, password=password)
    db = connect.cursor()
    db.execute('SHOW DATABASES')
    if ('company',) not in db.fetchall():
        db.execute('CREATE DATABASE Company')
    db.execute('USE Company')
    db.execute('SHOW TABLES')
    if ('employee',) not in db.fetchall():
        db.execute('CREATE TABLE Employee(ID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(25) NOT NULL, EMail VARCHAR(30) NOT NULL, Contact VARCHAR(10) NOT NULL, Salary INT NOT NULL, Address VARCHAR(50) NOT NULL)')
def search(key):
    db.execute('SELECT * FROM Employee WHERE ID = %s',[key])
    return db.fetchone()
def show():
    db.execute('SELECT * FROM Employee')
    return db.fetchall()
def add(record):
    db.execute('INSERT INTO Employee (Name, Email, Contact, Salary, Address) VALUES (%s,%s,%s,%s,%s)',record)
    connect.commit()
def remove(record):
    db.execute('DELETE FROM Employee WHERE ID = %s',[record])
    connect.commit()
def modify(record):
    db.execute('UPDATE Employee SET Name=%s, Email=%s, Contact=%s, Salary=%s, Address=%s WHERE ID=%s',record)
    connect.commit()