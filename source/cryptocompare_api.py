import aiohttp
from config import config
from resources import params

class Crypto:
    def __init__(self) -> None:
        self.host = config.cryptocompare.host
    
    async def get_price(self, currency):
        async with aiohttp.ClientSession() as session:
            async with session.get(config.cryptocompare.host+"/data/price", params=params.get_price, ssl=False) as response:
                resp = await response.json()
        return(resp[currency])
