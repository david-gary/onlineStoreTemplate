# Config Directory

This directory contains the configuration files for the application. Specifically, the `config_loader.py` file and a `config.json` file, which are used to load and store information like the database connection information and application runtime settings.

## config_loader.py File

This file contains two simple functions that enable easy interaction with the config file (`config.json` by default). The `get_config()` function returns the contents of the config file as a dictionary, and the `load_by_key()` function returns the value of a specific key in the config file.

## config.json File

This file contains the configuration information for the application. It is a simple JSON file that contains key-value pairs. The keys are the names of the configuration options, and the values are the values of the configuration options. The file is loaded into the application using the `config_loader.py` file. Default keys and values (as explained below) are provided in the file, but they can be changed to suit your needs.

- `database_path`: The relative path to the starting data file - defaults to `database/store_records.db`.
- `schema_path`: The relative path to the starting data file - defaults to `database/schema.sql`.
- `starting_data_path`: The relative path to the starting data file - defaults to `database/starting_data.sql`.
- `reset_database`: A boolean value that determines whether or not the database should be reset on startup - defaults to `true`.
- `host`: The host address for the application - defaults to `localhost`.
- `port`: The port for the application - defaults to `8080`.
- `username`: The username for the application - defaults to `default`.
