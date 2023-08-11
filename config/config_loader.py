from json import load
from os.path import join, dirname, abspath
from typing import Union, Dict, Any


def get_config(config_file_path: str = 'config.json') -> Dict[str, Any]:
    """
    Gets the configuration from a JSON file.

    args:
        - config_file_path: The path to the configuration file.

    returns:
        - config: The configuration dictionary.
    """

    config_file_path = join(dirname(abspath(__file__)), config_file_path)
    with open(config_file_path, 'r') as config_file:
        config = load(config_file)
    return config


def load_by_key(config: Dict[str, Any], key: str) -> Union[Dict[str, Any], Any]:
    """
    Gets a value from a dictionary by key.

    args:
        - config: The configuration dictionary.
        - key: The key to get the value for.

    returns:
        - value: The value for the given key.
    """

    value = config[key]
    return value
