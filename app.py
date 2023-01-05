import sqlite3

connect = sqlite3.connect("test.db")

# connect.execute("DROP TABLE IF EXIST CUSTOMER")

# connect.execute('''CREATE TABLE CUSTOMER 
#             (ID INT PRIMARY KEY NOT NULL,
#             NAME TEXT NOT NULL,
#             AGE INT NOT NULL);''')

connect.execute('INSERT INTO CUSTOMER (ID,NAME,AGE) VALUES (1, "Jeff", 32)')
connect.execute('INSERT INTO CUSTOMER (ID,NAME,AGE) VALUES (2, "Rina", 30)')

all_data = connect.execute('''SELECT * FROM CUSTOMER''')

for row in all_data:
    print(row)

connect.close()
