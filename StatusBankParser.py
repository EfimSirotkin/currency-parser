from bs4 import BeautifulSoup
import URLReader

soup = BeautifulSoup(URLReader.getHtml(), 'html.parser')
currencyList = [ "RUB", "USD", "EUR" ]

parsedItems = soup.find_all("div", {"class":  "change-money__office"})
print(parsedItems)

for item in parsedItems:
    parsedBranch = item.find("div", {"class":  "change-money__office-name"}).find("h5").text
    parsedAddress = item.find("div", {"class":  "change-money__office-adress"}).find("span").text
    print(parsedBranch + "  " + parsedAddress)
    currencies = item.find_all("div", {"class":  "change-money__office-curency display"})
    
    for currency in currencies:
        quantity = currency.find("div", {"class":  "unit"}).find("span").text
        if any (x in quantity for x in currencyList):
            print(quantity)
            prices = currency.find_all("div", {"class":  "price"})
            for price in prices:
                print(price.find("p").text + " - " + price.find("span").text)

    print("********************")

