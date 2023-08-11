from os import path, remove
from sqlite3 import Cursor, connect


def remove_database(database_path: str) -> None:
    """
    Remove the database file if it exists.

    args:
        - database_path: The path to the database file.

    returns:
        - None
    """

    if path.exists(database_path):
        remove(database_path)
    return None


def execute_sql_file(cursor: Cursor, sql_file_path: str) -> None:
    """
    Executes an SQL file on a given database cursor.

    args:
        - cursor: The database cursor.
        - sql_file_path: The path to the SQL file.

    returns:
        - None
    """

    with open(sql_file_path, 'r') as sql_file:
        sql = sql_file.read()
        cursor.executescript(sql)
    return None


def create_database(schema_path: str, starting_data_path: str, database_path: str) -> None:
    """
    Set the database schema.

    args:
        - schema_path: The path to the schema file.
        - starting_data_path: The path to the starting data file.
        - database_path: The path to the database file.

    returns:
        - None
    """

    # Connects to the database.
    connection = connect(database_path)
    cursor = connection.cursor()

    # Builds the database from the schema and starting data.
    execute_sql_file(cursor, schema_path)
    execute_sql_file(cursor, starting_data_path)

    # Commits the changes and closes the connection.
    connection.commit()
    connection.close()
    return None


def reset_database(database_path: str, schema_path: str, starting_data_path: str) -> None:
    """Resets the database from the schema and starting data.

    args:
        - database_path: The path to the database file.
        - schema_path: The path to the schema file.
        - starting_data_path: The path to the starting data file.

    returns:
        - None
    """
    # Removes the database file and creates a new one.
    remove_database(database_path)
    create_database(schema_path, starting_data_path, database_path)
    return None
