# Testing Review

## Tests Reviewed

- **Test Source File:** [tests/db_tests.py](../../tests/db_tests.py)
  - **Test Function Name:** `test_init_db`
    - **Date Reviewed:** 08/08/2023
    - **Comments:**
      - Works well. Only issue is perhaps the hardcoded path.

- **Test Source File:** [tests/inv_tests.py](../../tests/inv_tests.py)
  - **Test Function Name:** `inv_check_name`
    - **Date Reviewed:** 08/08/2023
    - **Comments:**
      - Only works if an item with id 10 exists

- **Test Source File:** [tests/inv_tests.py](../../tests/inv_tests.py)
  - **Test Function Name:** `inv_empty`
    - **Date Reviewed:** 08/08/2023
    - **Comments:**
      - This test should only be run after creating an empty inventory
