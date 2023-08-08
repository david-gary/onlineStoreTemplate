from database.db import Database

def inv_empty():
    """
    Tests that the inventory is empty.

    args:
        - None

    returns:
        - True if inventory is empty.
    """
    db = Database("database/store_records.db")
    if len(db.get_full_inventory()) == 0:
        return True, "Inventory is empty"
    else:
        message = f"Inventory is not empty. Found {len(db.get_full_inventory())} items."
        return False, message

def inventory_contains_items():
    """
    Tests that the inventory is stocked with all necessary supplies.

    args:
        - None

    returns:
        - True if inventory is fully stocked.
    """
    db = Database("database/store_records.db")
    if len(db.get_full_inventory()) > 0:
        return True, "Items exist in inventory"
    else:
        message = f"Items not found in inventory. Found {len(db.get_full_inventory())} items."
        return False, message
    

def inv_check_name():
    """
    Tests that the inventory recognizes the name of an item from the inventory using its id.

    args:
        - None

    returns:
        - True if inventory recognizes item by its correct name.
    """
    db = Database("database/store_records.db")
    try:
        db.get_item_name_by_id(10)
        return True, "Item's name was found."
    except:
        return False, "Item's name was not found."
    
def inv_check_info():
    """
    Tests that the inventory recognizes the info of an item from the inventory using its id.

    args:
        - None

    returns:
        - True if inventory recognizes item by its correct info.
    """
    db = Database("database/store_records.db")
    try:
        db.get_item_info_by_id(10)
        return True, "Item's info was found."
    except:
        return False, "Item's info was not found."
    

def inv_add():
    """
    Tests that items can be added to inventory.

    args:
        - None

    returns:
        - True if items can be added to inventory.
    """
    db = Database("database/store_records.db")
    try:
        db.insert_new_item("item_name", 10, "item info")
        return True, "Item successfully added"
    except:
        return False, "Item failed to add"