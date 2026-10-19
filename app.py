import os
from flask import Flask, request
import telebot

TOKEN = "8838932242:AAHnmUseuhq0pg6lqleCbak4mdJ82iOOGM8_OLGAN_TOKENINGIZNI_YOZING"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def index():
    return "Bot ishlayapti!", 200

if __name__ == "main":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))