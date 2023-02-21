from bs4 import BeautifulSoup
import hashlib


from URLReader import URLReader
from Currency import Currency
from Branch import Branch

PARSE_BRANCHES = {"class":  "change-money__office"}
PARSE_BRANCH_TYPES = {"class":  "change-money__office-name"}
PARSE_BRANCH_ADDRESSES = {"class":  "change-money__office-adress"}
PARSE_BRANCH_IDS = {"class":  "change-money__office-calculate"}
PARSE_BRANCH_CURRENCIES = {"class":  "change-money__office-curency display"}

currencyList = [ "RUB", "USD", "EUR" ]

class StatusBankParser:

    def __init__(self) -> None:
        pass

    def parseCurrencies(self, currenciesSource):
        currenciesList = []

        for currency in currenciesSource:
            
            quantity = currency.find("div", {"class":  "unit"}).find("span").text
            
            if any (x in quantity for x in currencyList):
                prices = currency.find_all("div", {"class":  "price"})
                buyPrice = 0
                sellPrice = 0
                if prices[0].find("p").text == "покупка":
                    buyPrice = prices[0].find("span").text
                    sellPrice = prices[1].find("span").text

                hash = (hashlib.md5((buyPrice + sellPrice).encode())).hexdigest()
                currenciesList.append(Currency(buyPrice, sellPrice, hash, quantity))

        return currenciesList


    def parseStatusBank(self):

        soup = BeautifulSoup(URLReader.getHtml(), 'html.parser')

        branchesList = []
        parsedBranches = soup.find_all("div", PARSE_BRANCHES)

        for item in parsedBranches:

            parsedBranchName = item.find("div", PARSE_BRANCH_TYPES).find("h5").text
            parsedBranchAddress = item.find("div", PARSE_BRANCH_ADDRESSES).find("span").text
            parsedBranchID = item.find("div", PARSE_BRANCH_IDS)['data-filial-id']
            
            currencies = item.find_all("div", PARSE_BRANCH_CURRENCIES)
            
            currenciesList = self.parseCurrencies(currencies)
            
            branchesList.append(Branch(branchID = parsedBranchID,
                                        branchName=parsedBranchName,
                                        branchAddress=parsedBranchAddress,
                                        branchCurrency=currenciesList))

        return branchesList