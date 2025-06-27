import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.getenv("7837677293:AAEOTpZRbIm-atO7kj6rQ9Tc_sXmEV0_SuQ")

products = {
    "1": "Gift Box - 50,000 so'm",
    "2": "Sovg'a kartasi - 20,000 so'm",
    "3": "Mini quti - 30,000 so'm"
}

def start(update: Update, context: CallbackContext):
    text = "Salom! Men Humoyunning do‘koni botiman 😊\nBuyurtma berish uchun /products deb yozing."
    update.message.reply_text(text)

def products_list(update: Update, context: CallbackContext):
    msg = "Bizning mavjud tovarlar:\n"
    for key, value in products.items():
        msg += f"{key}. {value}\n"
    update.message.reply_text(msg)

updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("products", products_list))

print("Bot ishga tushdi...")
updater.start_polling()
updater.idle()
