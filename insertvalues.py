import sqlite3

conn = sqlite3.connect('employee.db')
print("Connected")


conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)"
             "VALUES(1,'Andrew','Mark',21,45000.00,'Employer')")
conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)"
             "VALUES(2,'Laurine','Maina',20,30000.00,'Employee')")
conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)"
             "VALUES(3,'Mike','Millan',19,25000.00,'Cleaning')")
conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)"
             "VALUES(4,'Ann','Mark',21,15000.00,'Cook')")

conn.commit()
print("Successfully inserted values into staff table")
conn.close()