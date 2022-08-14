from Stock import Stock
"""
The universe class will contain all the stocks that exists within a particular universe.
The universe can be specified using specific specifications
"""


class Universe:
    def __init__(self, volume, sector, price_range, exchanges=("nasdaq", "amex", "nyse")):
        self.volume = volume
        self.sector = sector
        self.price_range = price_range
        self.exchanges = exchanges
        self.stocks = self._generate_stocks()

    def _generate_stocks(self) -> [Stock]:
        pass