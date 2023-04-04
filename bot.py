from telegram.ext import Updater,Filters,CommandHandler,MessageHandler
from telegram import Update
from handler import start,tarjimon

TOKEN = '6004154698:AAEo2pZT8WqoCqRGAXZchoYMtdgozcq3Kbc'

updater = Updater(token=TOKEN)

dp = updater.dispatcher

dp.add_handler(CommandHandler('start',start))
dp.add_handler(MessageHandler(Filters.update,tarjimon))

updater.start_polling()
updater.idle()