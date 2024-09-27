import os
import json
import aiohttp
import aiofiles
from utils import logger
from config import config
from datetime import datetime


PATH_FILE = "resources/rates.json"


class CrbExchangeRate:

    CURRENCY_CODES = ['AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL', \
                  'HUF', 'VND', 'HKD', 'GEL', 'DKK', 'AED', 'USD', \
                  'EUR', 'EGP', 'INR', 'IDR', 'KZT', 'CAD', 'QAR', \
                  'KGS', 'CNY', 'MDL', 'NZD', 'NOK', 'PLN', 'RON', \
                  'XDR', 'SGD', 'TJS', 'THB', 'TRY', 'TMT', 'UZS', \
                  'UAH', 'CZK', 'SEK', 'CHF', 'RSD', 'ZAR', 'KRW', 'JPY']

    def __init__(self):
        logger.info("Create '%s' class", type(self).__name__)
        self.host = config.crb.host

    async def initialize(self):
        try:
            if not os.path.exists(PATH_FILE) or await self.is_outdated_data():
                logger.info("Создание файла '%s'", PATH_FILE)
                rates = await self._send_req_get_rates()
                await self._save_rates(rates)
        except Exception as e:
                logger.error("Ошибка при попытке получить курс валют и сохранить их в файл - %s", e)

    async def is_outdated_data(self):
        logger.info("проверка актуальности файла %s", PATH_FILE)
        now = datetime.now()
        midnight = datetime(now.year, now.month, now.day)
        timestamp_midnight = midnight.timestamp()
        try:
            rates = json.loads(await self._read_rates())
            timestamp_rates = rates["timestamp"]
            if timestamp_rates < timestamp_midnight:
                logger.info("Файл %s устарел и требует обновления", PATH_FILE)
                return True
        except Exception as e:
            logger.error("Ошибка при попытке прочесть файл %s с курсом валют - %s", PATH_FILE, e)
            return True
        else:
            logger.info("Файл %s актуален", PATH_FILE)
            return False
        
    async def get_rates(self, currencies: list):
        await self.initialize()
        curr = {}
        try:
            rates = json.loads(await self._read_rates())
            for i in currencies:
                if i in rates["rates"]:
                    curr[i] = rates["rates"][i]
        except Exception as e:
            logger.error("Ошибка при попытке прочесть файл с курсом валют - %s", e)
        return curr
            
    async def _send_req_get_rates(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.host, ssl=False) as response:
                resp = await response.text()
        return(resp)
    
    async def _save_rates(self, data):
        async with aiofiles.open(PATH_FILE, mode='w') as file:
            await file.write(data)

    async def _read_rates(self):
        async with aiofiles.open(PATH_FILE, mode='r') as file:
            value = await file.read()
            return (value)
        return None
