import json

FILENAME = "config/config.json"

class Telegram:
    def __init__(self, token, host) -> None:
        self.token = token
        self.host = host

    def __repr__(self) -> str:
        return f"Telegram(token={self.token})"

class Cryptocompare:
    def __init__(self, token, host) -> None:
        self.token = token
        self.host = host

    def __repr__(self) -> str:
        return f"Cryptocompare(token={self.token}, host={self.host})"

class Config:
    def __init__(self, telegram, cryptocompare) -> None:
        self.telegram = Telegram(**telegram)
        self.cryptocompare = Cryptocompare(**cryptocompare)

    def __repr__(self) -> str:
        return f"Config(telegram={self.telegram}, cryptocompare={self.cryptocompare})"
    
def load_config():
    with open(FILENAME, 'r') as file:
        data = json.load(file)
    return Config(**data)

config = load_config()