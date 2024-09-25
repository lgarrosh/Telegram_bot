import json

DIR = "resources/"
GET_PRICE = f"{DIR}getPrice.json"
GET_PRICE_MULTI = f"{DIR}getPriceMulti.json"

class Params:
    def __init__(self):
        with open(GET_PRICE, 'r') as file: self.get_price = json.load(file)
        with open(GET_PRICE_MULTI, 'r') as file: self.get_price_multi = json.load(file)