from database.db import Database

def inv_empty():
    """
    Tests that the inventory is empty.

    args:
        - None

    returns:
        - True if inventory is empty.
    """

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
    

def inv_check():
    """
    Tests that the inventory recognizes what is missing from inventory.
    Checks what items are not fully stocked in inventory.

    args:
        - None

    returns:
        - True if inventory recognizes correct items that are not fully stocked.
    """

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

def inv_remove():
    """
    Tests that items can be removed from inventory.

    args:
        - None

    returns:
        - True if items can be removed from inventory.
    """

def inv_back():
    """
    Tests that user can click out of inventory check.

    args:
        - None

    returns:
        - True if user can exit successfully.
    """
