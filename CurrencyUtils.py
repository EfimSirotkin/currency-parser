separator = "-"

def extractCurrencyHash(encodedString):
    splittedString = encodedString.split(separator)
    return splittedString[1].replace("\n", "")
