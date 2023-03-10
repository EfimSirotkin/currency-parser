class Branch:
    def __init__(self, branchID, branchName, branchAddress, branchCurrency):
        self.branchID = branchID
        self.branchName = branchName
        self.branchAddress = branchAddress
        self.branchCurrencies = branchCurrency

    def getFormattedData(self):
        str = self.filialId + "\n" + self.filialName

        for currencyDto in self.currencyDtos:
            str += "\n" + currencyDto.getFormattedData()
       
        return str

    def getBranchID(self):
        return self.branchID

    def updateBranchHash(self, branchHash):
        self.branchHash = branchHash

    def updateBranchCurrencies(self, branchCurrencies):
        self.branchCurrencies = branchCurrencies

    def getBranchCurrencies(self):
        return self.branchCurrencies

    def getBranchDataValues(self):
        str = self.branchName + " " + self.branchAddress + "\n"
        for currency in self.branchCurrencies:
            str += currency.getCurrencyValues() + "\n"

        return str

    def getBranchFullName(self):
        return self.branchName + " ," + self.branchAddress

    def getBranchData(self):
        str = ""
        for currency in self.branchCurrencies:
            str += currency.getCurrencyData() + "\n" 

        return str
