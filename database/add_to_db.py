import pandas as pd
from database.db import Database

def csv_to_database():
    """
    A function that imports foods_table.csv into the store_records.db file via Database

    """

    foods = pd.read_csv('foods_table.csv')
    for index, row in foods.iterrows():
        Database.insert_new_item(row['item_name'],row['info'],row['calorie'],row['protein'],row['carbs'],row['allergy'])




