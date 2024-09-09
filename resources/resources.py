import json

DIR = "resources/"
GET_PRICE = f"{DIR}getPrice.json"

class Params:
    def __init__(self):
        with open(GET_PRICE, 'r') as file: self.get_price = json.load(file)