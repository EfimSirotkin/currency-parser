import threading
import telebot
import time
import BranchesUtils
import Analyzer

from StatusBankParser import StatusBankParser
from AlphaBankParser import AlphaBankParser
from FileManager import FileManager



BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

ALPHA_DIR = "alpha_data"
STATUS_DIR = "status_data"

statusParser = StatusBankParser()
alphaParser = AlphaBankParser()

statusFileManager = FileManager(STATUS_DIR)
alphaFileManager = FileManager(ALPHA_DIR)

bot = telebot.TeleBot(BOT_TOKEN,threaded=False)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Бот-информатор запущен")


def polling():
    bot.infinity_polling()

pollingThread = threading.Thread(target=polling)
pollingThread.start()

#alphaBranchesList = alphaParser.parseAlphaBank()
#alphaFileManager.updateBranchFiles(alphaBranchesList)

#statusBranchesList = statusParser.parseStatusBank()
#statusFileManager.updateBranchFiles(statusBranchesList)


while True:
    time.sleep(2)

    Analyzer.AnalyzeStatusBank(statusFileManager, statusParser, bot, CHAT_ID)
    Analyzer.AnalyzeAlphaBank(alphaFileManager, alphaParser, bot, CHAT_ID)
    