# SQL-язык бд
# СУБД- субд 2вида

import sqlite3

# CRUD-create
# read
# update
# delete
db = sqlite3.connect('test.db')
c = db.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS 
user(
name TEXT,
age INTEGER,
view BOOLEAN,
lastname TEXT
)''')

c.execute('INSERT INTO user VALUES ("Мирлан",16,10,"Dreemann")')
c.execute('INSERT INTO user VALUES ("EМирлан",06,10,"Белетбеков")')

c.execute('INSERT INTO user VALUES ("Мирлан",16,10,"Dreemann")')
c.execute('INSERT INTO user VALUES ("EМирлан",06,10,"Белетбеков")')

c.execute('INSERT INTO user VALUES ("Мирлан",16,10,"Dreemann")')
c.execute('INSERT INTO user VALUES ("EМирлан",06,10,"Белетбеков")')


c.execute("UPDATE user SET name='ЖАннат' WHERE name='EМирлан' ")
c.execute("UPDATE user SET name='Садыр' WHERE name='Ахмад'")

c.execute("DELETE FROM user WHERE rowid>11")


c.execute("SELECT rowid,* FROM user")
item = c.fetchall()
for i in item:
    print(i)
print(c.fetchone())
print(c.fetchmany(4))
db.commit()
db.close()