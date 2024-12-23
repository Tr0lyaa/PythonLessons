import sqlite3

connection = sqlite3.connect("telegram_bot.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')


def get_all_products():
    all_products = cursor.execute("SELECT * FROM Products").fetchall()
    connection.commit()
    return all_products
