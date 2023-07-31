import sqlite3

def initialize_database(database_path="store_records.db"):
    # Connect to the database or create a new one if it doesn't exist
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL DEFAULT 0,
            category TEXT NOT NULL,
            info TEXT NOT NULL,
            image_url TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            item_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            sale_date DATE NOT NULL,
            cost REAL NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            sale_id INTEGER NOT NULL,
            payment_status TEXT NOT NULL,
            amount REAL NOT NULL,
            payment_date DATE NOT NULL
        )
    ''')

    # Save changes and close the connection
    connection.commit()
    connection.close()

# Call the function to initialize the database
if __name__ == "__main__":
    initialize_database()
