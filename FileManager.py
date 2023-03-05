import os
import CurrencyUtils

class FileManager:

    def __init__(self, workFolder = "data"):
        self.__workFolder = workFolder

    def writeBranchCurrency(self, branch):

        branchFilePath = os.path.join(self.__workFolder, branch.getBranchID())
        branchFile = open(branchFilePath, "w+")

        branchFile.write(branch.getBranchData())

    def compareBranchCurrencies(self, branch):

        branchFilePath = os.path.join(self.__workFolder, branch.getBranchID())
        branchFile = open(branchFilePath, "r")

        oldCurrencies = branchFile.readlines()
        newBranchCurrencies = branch.getBranchCurrencies()
        currencyCounter = 0

        for currency in oldCurrencies:
            oldCurrencyHash = CurrencyUtils.extractCurrencyHash(currency)
            newCurrencyHash = newBranchCurrencies[currencyCounter].getCurrencyHash()
            currencyCounter += 1
            if self.isCurrencyDiffer(oldCurrencyHash, newCurrencyHash):
                return True
            
        return False



    def isCurrencyDiffer(self, oldCurrencyHash, newCurrencyHash):
        if oldCurrencyHash != newCurrencyHash:
            return True
        else:
            return False

    
    def updateBranchFiles(self, branchesList):
        for branch in branchesList:
            self.writeBranchCurrency(branch)


