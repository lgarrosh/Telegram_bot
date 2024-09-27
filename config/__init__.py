from .config import Config
import json

FILENAME = "config/config.json"

def load_config():
    with open(FILENAME, 'r') as file:
        data = json.load(file)
    return Config(**data)

config = load_config()