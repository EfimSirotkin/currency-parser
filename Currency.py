class Currency:

    def __init__(self, buyPrice = "", sellPrice = "", hash = "", currencyTag = ""):
        self.buyPrice = buyPrice 
        self.sellPrice = sellPrice 
        self.hash = hash 
        self.currencyTag = currencyTag

    def getCurrencyData(self):
        return self.currencyTag + "-" + self.hash