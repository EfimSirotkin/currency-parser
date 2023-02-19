import threading
import telebot

BOT_TOKEN = "YOUR_BOT_TOKEN"

bot = telebot.TeleBot(BOT_TOKEN,threaded=False)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


def polling():
    bot.infinity_polling()

pollingThread = threading.Thread(target=polling)
pollingThread.start()