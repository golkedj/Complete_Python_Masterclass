import sqlite3

db = sqlite3.connect("contacts.sqlite")

for row in db.execute("SELECT * FROM sqlite_master"):
    print(row)

db.close()
