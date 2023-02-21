import threading
import telebot
import time

BOT_TOKEN = "YOUR_TOKEN_HERE"

bot = telebot.TeleBot(BOT_TOKEN,threaded=False)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


def polling():
    bot.infinity_polling()

pollingThread = threading.Thread(target=polling)
pollingThread.start()

while True:
    time.sleep(10)

