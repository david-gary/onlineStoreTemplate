from database.db import Database

def sys_productRequest():
    """
    Tests that items can be selected (requested).

    args:
        - None

    returns:
        - True if items can be selected.
    """

def sys_transaction():
    """
    Tests that items chosen by user are charged to wallet or 
    at least put in their cart.

    args:
        - None

    returns:
        - True if user's items are in cart or ready for transaction. 
        (Either walletBalanceChange or cancelTransaction)
    """

def sys_walletBalanceChange():
    """
    Tests that wallet balance changes after transaction is successful.

    args:
        - None

    returns:
        - True if wallet balance is changed to correct amount after transaction.
    """

def sys_cancelTransaction():
    """
    Tests that transaction can be canceled if wallet balance is insufficient.

    args:
        - None

    returns:
        - True if transaction cancels.
    """

def sys_fulfillOrder():
    """
    Tests that users order is fullfilled and item is removed from inventory.

    args:
        - None

    returns:
        - True if items are given to customer.
    """