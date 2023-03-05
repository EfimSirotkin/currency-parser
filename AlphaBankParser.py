from bs4 import BeautifulSoup
import hashlib


from URLReader import URLReader
from Currency import Currency
from Branch import Branch
import time

ALPHA_URL = "https://www.alfabank.by/exchange/minsk/"

PARSE_BRANCHES = {"class":  "info-section"}
PARSE_BRANCH_TYPES = {"class":  "info-section__aside"}
PARSE_BRANCH_ADDRESSES = {"class":  "change-money__office-adress"}
PARSE_BRANCH_IDS = {"class":  "change-money__office-calculate"}
PARSE_BRANCH_CURRENCIES = {"class":  "exchange-table"}

currencyList = [ "RUB", "USD", "EUR" ]

class AlphaBankParser:

    def __init__(self) -> None:
        pass

    def parseCurrencies(self, currenciesSource):
        currenciesList = []

        for currency in currenciesSource:
            
            quantity = currency.find("h4", {"class":  "item-title"}).find_all("span")[1].text

            if any (x in quantity for x in currencyList):

                price_text = currency.find_all("div", { "class": "price__text"})
                price_values = currency.find_all("div", { "class", "price__value"})

                buyPrice = price_values[0].text
                sellPrice = price_values[1].text

                hash = (hashlib.md5((buyPrice + sellPrice).encode())).hexdigest()
                currenciesList.append(Currency(buyPrice, sellPrice, hash, quantity))

        return currenciesList


    def parseAlphaBank(self):

        soup = BeautifulSoup(URLReader.getWebDriverHtml(ALPHA_URL), 'html.parser')

        branchesList = []
        parsedBranches = soup.find_all("div", PARSE_BRANCHES)

        for item in parsedBranches:

            parsedBranchTitle = item.find("div", PARSE_BRANCH_TYPES)
            try:
                parsedBranchName = parsedBranchTitle.find("a", {"class":  "info-section__title"}).text
            except:
                print("No specified item was parsed")
                return branchesList
           
            parsedBranchAddress = parsedBranchTitle.find("p", {"class":  "info-section__aside-text"}).text
            parsedBranchID = hashlib.md5((parsedBranchName + parsedBranchAddress).encode()).hexdigest()
            
            currencies = item.find("div", PARSE_BRANCH_CURRENCIES)
            parsedCurrencies = currencies.find_all("div", "table-item")
            
            currenciesList = self.parseCurrencies(parsedCurrencies)
            
            branchesList.append(Branch(branchID = parsedBranchID,
                                        branchName=parsedBranchName,
                                        branchAddress=parsedBranchAddress,
                                        branchCurrency=currenciesList))

        return branchesList