import requests
from config.config import config
import json


def generate_json_params_get_price():
    params = {
        'fsym': 'Toncoin',
        'tsyms': 'USD,RUB'
    }
    return(params)

def get_price():
    params = generate_json_params_get_price()
    responce = requests.get(config.cryptocompare.host+"/data/price", params=params)
    return(responce)
