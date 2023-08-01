import sqlite3
import uuid


def dict_factory(cursor: sqlite3.Cursor, row: tuple) -> dict:
    """
    Creates a dictionary from a row in the database. This is used to convert the rows into dictionaries.

    args:
        - cursor: The cursor of the database, which is a built-in sqlite3 class.
        - row: The row to convert into a dictionary.

    returns:
        - The dictionary of the row.
    """

    row_dict = {}
    for index, column in enumerate(cursor.description):
        row_dict[column[0]] = row[index]
    return row_dict


def calculate_calories(calories: int, quantity: int) -> float:
    """
    Calculates the cost of an item.

    args:
        - calories: The calories in the item.
        - quantity: The quantity of the item.

    returns:
        - The calories of the item as a float.
    """
    return (calories * quantity)

def calculate_total_calories(items: dict) -> float:
    """
    Calculates the total cost of a set of items.

    args:
        - items: A dictionary of items to calculate the total calories of.

    returns:
        - The total cost of the sale as a float.
    """
    total_cal = 0
    print(items)
    for i in items:
        item = items[i]
        total_cal += calculate_calories(float(item["calorie"]), int(item["quantity"]))
    return total_cal

def generate_unique_id() -> str:
    """
    Generates a unique ID.

    args:
        - None

    returns:
        - A unique ID as a string.
    """
    return str(uuid.uuid4())
