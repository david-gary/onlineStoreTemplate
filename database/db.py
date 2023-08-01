from core.utils import dict_factory, calculate_cost
import datetime as dt
import sqlite3


class Database:
    """
    A class that handles all database operations.

    args:
        - database_path: The path to the database file.

    attributes:
        - database_path: The path to the database file.
        - connection: The connection to the database.
        - cursor: The cursor of the database.
    """

    def __init__(self, database_path: str = "store_records.db") -> None:
        self.database_path = database_path
        self.connection = sqlite3.connect(
            database_path, check_same_thread=False)
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    # --------------------------------------------
    # ----------------- FOOD ---------------------
    # --------------------------------------------

    def insert_new_item(self, log_id: int, item_name: str, info: str, calorie: int, protein: int, carbs: int, allergy: str) -> None:
        """
        Inserts a new item_item into the database.

        args:
            - log_id: The log id of the entry.
            - item_name: The name of the item.
            - info: The info of the item.
            - calorie: The calories in an item.
            - protein: The protein in an item.
            - carbs: The carb in an item.
            - allergy: Any applicable allergy warnings.

        returns:
            - None
        """
        self.cursor.execute(
            "INSERT INTO inventory (log_id, item_name, info, calorie, protein, carbs, allergy) VALUES (?, ?, ?, ?, ?, ?)", 
            (log_id, item_name, info, calorie, protein, carbs, allergy))
        self.connection.commit()

    # ------ Getter methods ------

    def get_full_inventory(self):
        """
        Gets all inventory in the database.

        args:
            - None

        returns:
            - List of the full inventory table from the database.
        """
        self.cursor.execute("SELECT * FROM food")
        return self.cursor.fetchall()
    
    def get_log_id_by_entry_id(self, entry_id: int):
        """
        Gets the log id for a entry from the database.

        args:
            - entry_id: The id of the entry whose log id to get.

        returns:
            - The log id for the sale with the given id.
        """
        self.cursor.execute("SELECT log_id FROM logs WHERE entry_id = ?", (entry_id,))
        return self.cursor.fetchone()
    
    def get_entries_by_log_id(self, log_id: int):
        """
        Gets the entries for a log from the database.

        args:
            - log_id: The id of the log whose entries to get.

        returns:
            - The entries for the log with the given id.
        """
        self.cursor.execute(
            "SELECT * FROM logs WHERE log_id = ?", (log_id,))
        return self.cursor.fetchall()

    def get_all_item_ids(self):
        """
        Gets all item ids in the database.

        args:
            - None

        returns:
            - List of all item ids in the database.
        """
        self.cursor.execute("SELECT id FROM food")
        return self.cursor.fetchall()

    def get_item_name_by_id(self, item_id: int):
        """
        Gets an item's name from the database.

        args:
            - item_id: The id of the item to get.

        returns:
            - The item with the given id.
        """
        self.cursor.execute("SELECT * FROM food WHERE id = ?", (item_id,))
        return self.cursor.fetchone()

    def get_item_info_by_id(self, item_id: int):
        """
        Gets the info (description) of an item from the database.

        args:
            - item_id: The id of the item to get.

        returns:
            - The info of the item with the given id.
        """
        self.cursor.execute(
            "SELECT info FROM food WHERE id = ?", (item_id,))
        return self.cursor.fetchone()

    def get_item_image_url_by_id(self, item_id: int):
        """
        Gets the image_url of an item from the database.

        args:
            - item_id: The id of the item to get.

        returns:
            - The image_url of the item with the given id.
        """
        self.cursor.execute(
            "SELECT image_url FROM food WHERE id = ?", (item_id,))
        return self.cursor.fetchone()

    def get_item_category_by_id(self, item_id: int):
        """
        Gets the category of an item from the database.

        args:
            - item_id: The id of the item to get.

        returns:
            - The category of the item with the given id.
        """
        self.cursor.execute(
            "SELECT category FROM food WHERE id = ?", (item_id,))
        return self.cursor.fetchone()

    # ------ Setter methods ------

    def set_entry_log_id(self, entry_id: int, new_log_id: int):
        """
        Updates the log id of a entry in the database.

        args:
            - entry_id: The id of the entry to update.
            - new_log_id: The new log id of the entry.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE logs SET log_id = ? WHERE id = ?", (new_log_id, entry_id))
        self.connection.commit()

    def set_item_name(self, item_id: int, new_name: str):
        """
        Updates the name of an item in the database.

        args:
            - item_id: The id of the item to update.
            - new_name: The new name of the item.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE food SET name = ? WHERE id = ?", (new_name, item_id))
        self.connection.commit()

    def set_item_info(self, item_id: int, new_info: str):
        """
        Updates the information of an item in the database.

        args:
            - item_id: The id of the item to update.
            - new_info: The new information of the item.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE food SET info = ? WHERE id = ?", (new_info, item_id))
        self.connection.commit()

    def set_item_calorie(self, item_id: int, new_cal: int):
        """
        Updates the information of an item in the database.

        args:
            - item_id: The id of the item to update.
            - new_info: The new information of the item.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE food SET calorie = ? WHERE id = ?", (new_cal, item_id))
        self.connection.commit()

    def set_item_protein(self, item_id: int, new_pro: int):
        """
        Updates the information of an item in the database.

        args:
            - item_id: The id of the item to update.
            - new_info: The new information of the item.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE food SET protein = ? WHERE id = ?", (new_pro, item_id))
        self.connection.commit()

    def set_item_carbs(self, item_id: int, new_carb: int):
        """
        Updates the information of an item in the database.

        args:
            - item_id: The id of the item to update.
            - new_info: The new information of the item.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE food SET carbs = ? WHERE id = ?", (new_carb, item_id))
        self.connection.commit()

    def set_item_allergy(self, item_id: int, new_al: str):
        """
        Updates the information of an item in the database.

        args:
            - item_id: The id of the item to update.
            - new_info: The new information of the item.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE food SET allergy = ? WHERE id = ?", (new_al, item_id))
        self.connection.commit()

    def set_item_image_url(self, item_id: int, new_image_url: str):
        """
        Updates the image_url of an item in the database.

        args:
            - item_id: The id of the item to update.
            - new_image_url: The new image of the item.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE food SET image_url = ? WHERE id = ?", (new_image_url, item_id))
        self.connection.commit()

    def set_item_category(self, item_id: int, new_category: str):
        """
        Updates the category of an item in the database.

        args:
            - item_id: The id of the item to update.
            - new_category: The new category of the item.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE food SET category = ? WHERE id = ?", (new_category, item_id))
        self.connection.commit()

    # --------------------------------------------
    # ------------------ Users -------------------
    # --------------------------------------------

    def insert_user(self, username: str, password_hash: str, email: str, first_name: str, last_name: str) -> None:
        """
        Inserts a new user into the database.

        args:
            - username: The username of the user to insert.
            - password_hash: The password_hash of the user to insert.
            - email: The email of the user to insert.

        returns:
            - None
        """
        self.cursor.execute(
            "INSERT INTO users (username, password_hash, email, first_name, last_name) VALUES (?, ?, ?, ?, ?)",
            (username, password_hash, email, first_name, last_name))
        self.connection.commit()

    # ------ Getter methods ------

    def get_all_user_information(self):
        """
        Gets all user information from the database.

        args:
            - None

        returns:
            - A list of all user information in the database.
        """
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def get_password_hash_by_username(self, username: str):
        """
        Gets the password hash of a user from the database.

        args:
            - username: The username of the user whose password hash to get.

        returns:
            - The password hash for the user with the given username.
        """
        self.cursor.execute(
            "SELECT password_hash FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def get_email_by_username(self, username: str):
        """
        Gets the email of a user from the database.

        args:
            - username: The username of the user whose email to get.

        returns:
            - The email for the user with the given username.
        """
        self.cursor.execute(
            "SELECT email FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def get_first_name_by_username(self, username: str):
        """
        Gets the first name of a user from the database.

        args:
            - username: The username of the user whose first name to get.

        returns:
            - The first name for the user with the given username.
        """
        self.cursor.execute(
            "SELECT first_name FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def get_last_name_by_username(self, username: str):
        """
        Gets the last name of a user from the database.

        args:
            - username: The username of the user whose last name to get.

        returns:
            - The last name for the user with the given username.
        """
        self.cursor.execute(
            "SELECT last_name FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    # ------ Setter methods ------

    def set_password_hash(self, username: str, new_password_hash: str):
        """
        Updates the password hash of a user in the database.

        args:
            - username: The username of the user to update.
            - new_password_hash: The new password hash of the user.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE users SET password_hash = ? WHERE username = ?", (new_password_hash, username))
        self.connection.commit()

    def set_email(self, username: str, new_email: str):
        """
        Updates the email of a user in the database.

        args:
            - username: The username of the user to update.
            - new_email: The new email of the user.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE users SET email = ? WHERE username = ?", (new_email, username))
        self.connection.commit()

    def set_first_name(self, username: str, new_first_name: str):
        """
        Updates the first name of a user in the database.

        args:
            - username: The username of the user to update.
            - new_first_name: The new first name of the user.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE users SET first_name = ? WHERE username = ?", (new_first_name, username))
        self.connection.commit()

    def set_last_name(self, username: str, new_last_name: str):
        """
        Updates the last name of a user in the database.

        args:
            - username: The username of the user to update.
            - new_last_name: The new last name of the user.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE users SET last_name = ? WHERE username = ?", (new_last_name, username))
        self.connection.commit()

    # --------------------------------------------
    # ------------------ Logs --------------------
    # --------------------------------------------

    def insert_new_entry(self, username: str, item_id: int, quantity: int, entry_date: dt.date, total_calorie: int, total_protein: int, total_carbs: int):
        """
        Inserts a new entry into the database.

        args:
            - username: The username of the entry.
            - item_id: The item id of the entry.
            - quantity: The quantity of the entry.
            - entry_date: The sale date of the entry.
            - total_calorie: The total calories in the entry.
            - total_protein: The total protein in the entry.
            - total_carbs: The total carbs in the entry.

        returns:
            - None
        """
        self.cursor.execute(
            "INSERT INTO logs (username, item_id, quantity, entry_date, total_calorie, total_protein, total_carbs) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (username, item_id, quantity, entry_date, total_calorie, total_protein, total_carbs))
        self.connection.commit()

    # ------ Getter methods ------

    def get_full_entries_information(self):
        """
        Gets all entries information from the database.

        args:
            - None

        returns:
            - A list of all entries information in the database.
        """
        self.cursor.execute("SELECT * FROM logs")
        return self.cursor.fetchall()

    def get_username_by_entry_id(self, entry_id: int):
        """
        Gets the username for a entry from the database.

        args:
            - entry_id: The id of the entry whose username to get.

        returns:
            - The username for the entry with the given id.
        """
        self.cursor.execute(
            "SELECT username FROM logs WHERE entry_id = ?", (entry_id,))
        return self.cursor.fetchone()

    def get_item_id_by_entry_id(self, entry_id: int):
        """
        Gets the item id for an entry from the database.

        args:
            - entry_id: The id of the entry whose item id to get.

        returns:
            - The item id for the entry with the given id.
        """
        self.cursor.execute(
            "SELECT item_id FROM logs WHERE entry_id = ?", (entry_id,))
        return self.cursor.fetchone()

    def get_quantity_by_entry_id(self, entry_id: int):
        """
        Gets the quantity for a entry from the database.

        args:
            - entry_id: The id of the entry whose quantity to get.

        returns:
            - The quantity for the entry with the given id.
        """
        self.cursor.execute(
            "SELECT quantity FROM logs WHERE entry_id = ?", (entry_id,))
        return self.cursor.fetchone()

    def get_entry_date_by_entry_id(self, entry_id: int):
        """
        Gets the entry date for a entry from the database.

        args:
            - entry_id: The id of the entry whose entry date to get.

        returns:
            - The entry date for the entry with the given id.
        """
        self.cursor.execute(
            "SELECT entry_date FROM logs WHERE entry_id = ?", (entry_id,))
        return self.cursor.fetchone()

    def get_full_entry_by_id(self, entry_id: int):
        """
        Gets the entries for a entry from the database.

        args:
            - entry_id: The id of the entry whose information to get.

        returns:
            - The entry records for the entry with the given id.
        """
        self.cursor.execute(
            "SELECT * FROM logs WHERE entry_id = ?", (entry_id,))
        return self.cursor.fetchone()

    def get_entries_by_username(self, username: str):
        """
        Gets the entries for a user from the database.

        args:
            - username: The username of the user whose entries to get.

        returns:
            - The entries for the user with the given username.
        """
        self.cursor.execute(
            "SELECT * FROM logs WHERE username = ?", (username,))
        return self.cursor.fetchall()

    def get_entry_by_item_id(self, item_id: int):
        """
        Gets the entries for an item from the database.

        args:
            - item_id: The id of the item we are getting entries for.

        returns:
            - The entries for the item with the given id.
        """
        self.cursor.execute(
            "SELECT * FROM logs WHERE item_id = ?", (item_id,))
        return self.cursor.fetchall()

    def get_entries_by_date_range(self, start_date: dt.date, end_date: dt.date):
        """
        Gets the entries for a date range from the database.

        args:
            - start_date: The start date of the date range.
            - end_date: The end date of the date range.

        returns:
            - The entries for the given date range.
        """
        self.cursor.execute(
            "SELECT * FROM logs WHERE entry_date BETWEEN ? AND ?", (start_date, end_date))
        return self.cursor.fetchall()

    def get_entries_by_quantity_range(self, start_quantity: int, end_quantity: int):
        """
        Gets the entries for a quantity range from the database.

        args:
            - start_quantity: The start quantity of the quantity range.
            - end_quantity: The end quantity of the quantity range.

        returns:
            - The entries for the given quantity range.
        """
        self.cursor.execute(
            "SELECT * FROM logs WHERE quantity BETWEEN ? AND ?", (start_quantity, end_quantity))
        return self.cursor.fetchall()

    def get_entries_by_cost_range(self, start_cost: float, end_cost: float):
        """
        Gets the entries for a cost range from the database.

        args:
            - start_cost: The start cost of the cost range.
            - end_cost: The end cost of the cost range.

        returns:
            - The entries for the given cost range.
        """
        self.cursor.execute(
            "SELECT * FROM logs WHERE cost BETWEEN ? AND ?", (start_cost, end_cost))
        return self.cursor.fetchall()

    # ------ Setter methods ------

    def set_entry_username(self, entry_id: int, new_username: str):
        """
        Updates the username of a entry in the database.

        args:
            - entry_id: The id of the entry to update.
            - new_username: The new username of the entry.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE logs SET username = ? WHERE id = ?", (new_username, entry_id))
        self.connection.commit()

    def set_entry_item_id(self, entry_id: int, new_item_id: int):
        """
        Updates the item id of a entry in the database.

        args:
            - entry_id: The id of the entry to update.
            - new_item_id: The new item id of the entry.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE logs SET item_id = ? WHERE id = ?", (new_item_id, entry_id))
        self.connection.commit()

    def set_entry_date(self, entry_id: int, new_entry_date: dt.date):
        """
        Updates the entry date of a entry in the database.

        args:
            - entry_id: The id of the entry_id to update.
            - new_entry_date: The new entry_id date of the sale.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE logs SET entry_date = ? WHERE id = ?", (new_entry_date, entry_id))
        self.connection.commit()

    def set_entry_quantity(self, entry_id: int, new_quantity: int):
        """
        Updates the quantity of a entry in the database.

        args:
            - entry_id: The id of the entry to update.
            - new_quantity: The new quantity of the entry.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE logs SET quantity = ? WHERE id = ?", (new_quantity, entry_id))
        self.connection.commit()

    def set_entry_calorie(self, entry_id: int, new_calorie: int):
        """
        Updates the calorie of a entry in the database.

        args:
            - entry_id: The id of the entry to update.
            - new_calorie: The new calorie of the entry.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE logs SET total_calorie = ? WHERE id = ?", (new_calorie, entry_id))
        self.connection.commit()
    
    def set_entry_protein(self, entry_id: int, new_protein: int):
        """
        Updates the protein of a entry in the database.

        args:
            - entry_id: The id of the entry to update.
            - new_protein: The new protein of the entry.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE logs SET total_protein = ? WHERE id = ?", (new_protein, entry_id))
        self.connection.commit()
    
    def set_entry_carbs(self, entry_id: int, new_carbs: int):
        """
        Updates the carbs of a entry in the database.

        args:
            - entry_id: The id of the entry to update.
            - new_carbs: The new carbs of the entry.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE logs SET total_carbs = ? WHERE id = ?", (new_carbs, entry_id))
        self.connection.commit()