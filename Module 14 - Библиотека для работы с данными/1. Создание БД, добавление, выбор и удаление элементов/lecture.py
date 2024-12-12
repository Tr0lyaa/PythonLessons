import sqlite3
# from random import randint

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

cursor.execute('''
CREATE INDEX IF NOT EXISTS idx_email ON Users (email)
''')

# for i in range(30):
#     cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)",
#                    (f"newuser{i}", f"{i}ex@gmail.com", str(randint(20, 40))))

# cursor.execute("UPDATE Users SET age = ? WHERE username = ?", (29, "newuser"))
# cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser",))

# Выбрать всё из таблицы пользователи.
# cursor.execute("SELECT * FROM Users")
# Выбрать с определённым условием
cursor.execute("SELECT username, age FROM Users WHERE age > ?", (25,))
users = cursor.fetchall()
for user in users:
    print(user)
print()
# ORDER BY, GROUP BY - первый сортирует, второй группирует.
cursor.execute("SELECT username, age FROM Users ORDER BY age")
users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()
