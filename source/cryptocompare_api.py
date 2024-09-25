import aiohttp
from config import config
from resources import params

class Crypto:
    def __init__(self) -> None:
        self.host = config.cryptocompare.host
    
    async def get_price(self, coin):
        param = dict(params.get_price)
        param["fsym"] = coin
        async with aiohttp.ClientSession() as session:
            async with session.get(config.cryptocompare.host+"/data/price", params=param, ssl=False) as response:
                resp = await response.json()
        return(resp)
    
    async def get_price_multi(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(config.cryptocompare.host+"/data/pricemulti", params=params.get_price_multi, ssl=False) as response:
                resp = await response.json()
        return(resp)
