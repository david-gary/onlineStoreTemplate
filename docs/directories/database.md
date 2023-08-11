# Database Directory

This directory contains the database files for the application, which includes a reset script (`reset_database.py`), the schema file (`schema.sql`), a set of starter data (`starting_data.sql`), and the main database management file (`db.py`). Upon creation, the `store_records.db` file will be located in this directory, and will be used to store the data for the application.

## db.py File

This script contains the core `Database` class, wherein all querying and database management methods are defined. When exploring the current functionality, notice that large comment headers have been added to organize methods by the table they are associated with. Extra querying methods or refactoring of existing methods into a more elegant structure would be a great addition to the codebase.

## reset_database.py File

This script contains functions to delete the `store_records.db` file (if it exists), and then run the `schema.sql` and `starting_data.sql` files to create a new database with the correct schema and starter data.

## schema.sql File

This file contains the SQL commands to create the database based on a predefined schema. This file is run by the `reset_database.py` script, and should not be run manually.

## starting_data.sql File

This file contains the SQL commands to insert the starter data into the database. This file is run by the `reset_database.py` script, and should not be run manually.
