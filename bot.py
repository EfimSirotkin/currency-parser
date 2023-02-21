import threading
import telebot
import time

from StatusBankParser import StatusBankParser
from FileManager import FileManager

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "Your CHAT ID"

statusParser = StatusBankParser()
fileManager = FileManager()

bot = telebot.TeleBot(BOT_TOKEN,threaded=False)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Бот-информатор запущен")


def polling():
    bot.infinity_polling()

pollingThread = threading.Thread(target=polling)
pollingThread.start()

branchesList = statusParser.parseStatusBank()
for branch in branchesList:
   fileManager.writeBranchCurrency(branch)

while True:
    time.sleep(30)

    updatedBranchesList = statusParser.parseStatusBank()

    for updatedBranch in updatedBranchesList:
        if fileManager.compareBranchCurrencies(updatedBranch) == True:
            print("***Обновление***\n" + updatedBranch.getBranchDataValues())
            bot.send_message(CHAT_ID, "***Обновление***\n" + updatedBranch.getBranchDataValues())
            fileManager.writeBranchCurrency(updatedBranch)