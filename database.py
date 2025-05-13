import sqlite3
#connect to database (creates a new one)
conn=sqlite3.connect("mydatabase.db")

cursor=conn.cursor()
# #define table structure
# # cursor.execute('''
# #              CREATE TABLE IF NOT EXISTS users(
# #                id integer PRIMARY KEY,
# #                username TEXT NOT NULL,
# #                age INTEGER,
# #                email TEXT UNIQUE
               
               
# #                )
# #            ''')
# # conn.commit()

# cursor.execute('INSERT INTO users(username,age,email) VALUES("Alice",20,"alice@gmail.com")')
# conn.commit()


#function to create a new record (create operation)
# def create_record(name,age,email):
#     conn=sqlite3.connect('mydatabase.db')
#     c=conn.cursor()
#     c.exeecute('INSERT INTO users(name,age,email) VALUES(?,?,?)', (name,age,email))
#     conn.commit
#     conn.close


# #insert multiple records

# users=[
#     ('Bob',25,'bob@'),
#     ('Cob',22,'cob@')
# ]
# cursor.executemany("INSERT INTO users(username,age,email) VALUES(?,?,?)", users)
# conn.commit()

#retrive all records
# cursor.execute("SELECT * FROM users")
# rows=cursor.fetchall()
# print(rows)
# print(type(rows))

# cursor.execute("SELECT username FROM users")
# rows=cursor.fetchall()
# print(rows)
# print(type(rows))

# #update query
# cursor.execute("UPDATE users SET age=31 WHERE username='Alice'")
# conn.commit()


#
# username='abc'
# age=12
# email="abc@"
# id=2
# conn.execute('UPDATE users SET username=?,age=?,email=? WHERE id=?', (username,age,email,id))
# conn.commit()

#DELETE query
cursor.execute("DELETE FROM users WHERE username='abc'")
conn.commit()




