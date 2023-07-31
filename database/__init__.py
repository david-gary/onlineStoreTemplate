# Import the classes and functions from db.py to make them accessible directly from the package
import sqlite3
from .db import Database, User, Item, ShoppingCart, Payment, SearchEngine

# Define the path to the schemas.sql file within the package
SCHEMA_PATH = "schemas.sql"

# Define a function to initialize the database using the schemas.sql file
def initialize_database():
    with open(SCHEMA_PATH, "r") as schema_file:
        schema_sql = schema_file.read()
    connection = sqlite3.connect("store_records.db")
    cursor = connection.cursor()
    cursor.executescript(schema_sql)
    connection.commit()
    connection.close()

# Call the initialize_database() function when this package is imported
initialize_database()
