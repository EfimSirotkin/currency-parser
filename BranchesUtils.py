
def getBranchesNames(branchesList):
    str = ""
    for branch in branchesList:
        str += branch.getBranchFullName() + "\n"
    return str