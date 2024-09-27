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
    
class Crb:
    def __init__(self, host) -> None:
        self.host = host

    def __repr__(self) -> str:
        return f"Crb(host={self.host})"

class Config:
    def __init__(self, telegram, cryptocompare, crb) -> None:
        self.telegram = Telegram(**telegram)
        self.cryptocompare = Cryptocompare(**cryptocompare)
        self.crb = Crb(**crb)

    def __repr__(self) -> str:
        return f"Config({self.telegram}, {self.cryptocompare}, {self.crb})"