# Testing Review

## Tests Reviewed

- **Test Source File:** [/testing/inv_tests.py](../../testing/inv_tests.py)
  - **Test Function Name:** `inv_empty`
    - **Date Reviewed:** 08/07/2023
    - **Comments:**
      - checks if the inventory stored in the database is empty. Works fine.

- **Test Source File:** [/testing/inv_tests.py](../../testing/inv_tests.py)
  - **Test Function Name:** `inventory_contains_items`
    - **Date Reviewed:** 08/07/2023
    - **Comments:**
      - checks if our inventory has anything in it. Only thing I don't like is that the naming convention is inconsistent. It's "inventory" here where in other functions it is usually "inv".

- **Test Source File:** [/testing/inv_tests.py](../../testing/inv_tests.py)
  - **Test Function Name:** `inv_check_name`
    - **Date Reviewed:** 08/07/2023
    - **Comments:**
      - tests if our inventory can retreive the correct item if given the name.

- **Test Source File:** [/testing/inv_tests.py](../../testing/inv_tests.py)
  - **Test Function Name:** `inv_check_info`
    - **Date Reviewed:** 08/07/2023
    - **Comments:**
      - given an ID checks if the inventory retrieves the correct item.

- **Test Source File:** [/testing/inv_tests.py](../../testing/inv_tests.py)
  - **Test Function Name:** `inv_add`
    - **Date Reviewed:** 08/07/2023
    - **Comments:**
      - Makes sure that the inventory can handle items being added to it. Good test.

- **Test Source File:** [/testing/sys_tests.py](../../testing/sys_tests.py)
  - **Test Function Name:** `sys_productRequest`
    - **Date Reviewed:** 08/07/2023
    - **Comments:**
      - will test that an item can be selected in our system.

- **Test Source File:** [/testing/sys_tests.py](../../testing/sys_tests.py)
  - **Test Function Name:** `sys_transaction`
    - **Date Reviewed:** 08/07/2023
    - **Comments:**
      - currently runs Database(), will test that transactions can follow the expected procedures.

- **Test Source File:** [/testing/sys_tests.py](../../testing/sys_tests.py)
  - **Test Function Name:** `sys_walletBalanceChange`
    - **Date Reviewed:** 08/07/2023
    - **Comments:**
      - checks that the wallet balance has been deducted the appropriate amount following a transaction.

- **Test Source File:** [/testing/sys_tests.py](../../testing/sys_tests.py)
  - **Test Function Name:** `sys_cancelTransaction`
    - **Date Reviewed:** 08/07/2023
    - **Comments:**
      -  checks that the user has the ability to cancel a transaction - no harm no foul.

- **Test Source File:** [/testing/sys_tests.py](../../testing/sys_tests.py)
  - **Test Function Name:** `sys_fulfillOrder`
    - **Date Reviewed:** 08/07/2023
    - **Comments:**
      - checks that the user receives the items requested. No more no less.

- **Additional Comment: **
	- sys_tests are pending completion at this time.
