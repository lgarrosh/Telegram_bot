import aiohttp
from config import config
from resources import params
from utils import logger

GET_PRICE = "/data/price"
GET_PRICE_MULTI = "/data/pricemulti"


class Crypto:
    def __init__(self) -> None:
        logger.info("Create '%s' class", type(self).__name__)
        self.host = config.cryptocompare.host
    
    async def get_price(self, coin):
        param = dict(params.get_price)
        param["fsym"] = coin
        async with aiohttp.ClientSession() as session:
            async with session.get(self.host+GET_PRICE, params=param, ssl=False) as response:
                resp = await response.json()
        if not resp:
            logger.info("response is empty")
            return None
        elif "Response" in resp:
            logger.info("Error: %s", response["Message"])
            return response["Message"]
        return(resp)
    
    async def get_price_multi(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.host+GET_PRICE_MULTI, params=params.get_price_multi, ssl=False) as response:
                resp = await response.json()
        return(resp)
