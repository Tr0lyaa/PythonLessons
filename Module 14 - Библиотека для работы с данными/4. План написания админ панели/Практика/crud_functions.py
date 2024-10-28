import sqlite3

connection = sqlite3.connect("telegram_bot.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
);
''')

# names = ["Яблоко", "Банан", "Вишня", "Клубника"]
# names_desc = ["Спелые яблоки", "Свежие бананы", "Сладкая вишня", "Вкусная клубника"]
#
# for i in range(4):
#     cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                    (names[i], names_desc[i], (i + 1) * 100))


def get_all_products():
    all_products = cursor.execute("SELECT * FROM Products").fetchall()
    connection.commit()
    return all_products
