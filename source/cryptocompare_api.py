import requests
from config import config
from resources import params

def get_price():
    responce = requests.get(config.cryptocompare.host+"/data/price", params=params.get_price)
    return(responce)
