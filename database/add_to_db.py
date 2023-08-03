import csv
import sqlite3

# Connect to database
connection = sqlite3.connect("store_records.db")

# Create cursor
cursor = connection.cursor()

# Open and read csv
file = open('foods_table.csv')
contents = csv.reader(file)

insert_statement = "INSERT into `food` (item_name, info, calorie, protein, carbs, allergy, image_url, category) VALUES(?,?,?,?,?,?,?,?)"

cursor.executemany(insert_statement, contents)

select_all = "SELECT * FROM `food`"
rows = cursor.execute(select_all).fetchall()

connection.commit()

connection.close()



