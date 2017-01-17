import mysql.connector

class DataBase:
    host = "localhost"
    password = 'myPassword'
    user = "myUser"
    db = "myDB"
    
    def __init__(self):
        self.connection = mysql.connector.connect(user = self.user, password = self.password, host = self.host,  database = self.db)

    def querry(self, q):
        cursor = self.connection.cursor()
        cursor.execute(q)
        return cursor.fetchall()
    
    def __del__(self):
        self.connection.close()

db = DataBase()
print "mysql-python-connector version", mysql.connector.__version__

q = "SELECT * FROM myTable"
table =  db.querry(q)
for register in table:
print "Found ",  field_0[0], field_1[1], field_2[2]



        
