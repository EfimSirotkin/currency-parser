import os

class FileManager:

    def __init__(self, workFolder = "data"):
        self.__workFolder = workFolder

    def writeBranchCurrency(self, branch):

        branchFilePath = os.path.join(self.__workFolder, branch.getBranchID())
        branchFile = open(branchFilePath, "w+")

        branchFile.write(branch.getBranchData())
