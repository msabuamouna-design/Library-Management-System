import sqlite3

def connect_database():
    try:
        connection = sqlite3.connect('library_db.sqlite')
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                isbn TEXT,
                price REAL
            )
        ''')
        connection.commit()
        return connection
    except:
        return None


def check_login(username, password):
    if username == "admin" and password == "123":
        return True
    else:
        return False


def add_book(title, author, isbn, price):
    conn = connect_database()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO books (title, author, isbn, price) VALUES (?, ?, ?, ?)",
            (title, author, isbn, price)
        )
        conn.commit()
        conn.close()
        print("Book added successfully")
    else:
        print("Database connection failed")


def main():
    print("Bookshop Management System")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if check_login(username, password):
        print("Login successful")
        title = input("Enter book title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        price = float(input("Enter price: "))
        add_book(title, author, isbn, price)
    else:
        print("Invalid login")


if __name__ == "__main__":
    main()   
          
