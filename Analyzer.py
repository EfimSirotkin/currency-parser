import BranchesUtils

def AnalyzeStatusBank(statusFileManager, statusParser, bot, chat_id):
    
    statusUpdatedBranchesList = statusParser.parseStatusBank()

    newStatusBranchesList = []
    ifUpdated = False
    for updatedBranch in statusUpdatedBranchesList:
        if statusFileManager.compareBranchCurrencies(updatedBranch) == True:
            newStatusBranchesList.append(updatedBranch)
            statusFileManager.writeBranchCurrency(updatedBranch)
            ifUpdated = True
 #           print("***Обновление***\n" + updatedBranch.getBranchDataValues())
    if ifUpdated == True:
        bot.send_photo(chat_id, "https://www.aidapioneer.by/upload/iblock/a1c/a1c7d968f6a18e7e11c197d776fa5b68.jpg")
        bot.send_message(chat_id, "***Обновление курсов валют Статус-Банка***\n" + BranchesUtils.getBranchesNames(newStatusBranchesList))

def AnalyzeAlphaBank(alphaFileManager, alphaParser, bot, chat_id):
    alphaUpdatedBranchesList = alphaParser.parseAlphaBank()

    newAlphaBranchesList = []
    ifUpdated = False
    for updatedBranch in alphaUpdatedBranchesList:
        if alphaFileManager.compareBranchCurrencies(updatedBranch) == True:
            newAlphaBranchesList.append(updatedBranch)
            alphaFileManager.writeBranchCurrency(updatedBranch)
            ifUpdated = True
 #           print("***Обновление***\n" + updatedBranch.getBranchDataValues())
    if ifUpdated == True:
        bot.send_photo(chat_id, 'https://ftime.by/sites/default/files/banki/alfa-bank_logo.jpg')
        bot.send_message(chat_id, "***Обновление курсов валют Альфа-Банка***\n" + BranchesUtils.getBranchesNames(newAlphaBranchesList))
        