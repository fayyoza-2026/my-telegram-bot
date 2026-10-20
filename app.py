import os
from flask import Flask, request
import telebot

TOKEN = '8838932242:AAEyshHzRyH76uk5qEKfDC-dyG2dAGiVpBU'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)


@app.route('/8838932242:AAEyshHzRyH76uk5qEKfDC-dyG2dAGiVpBU', methods=['POST'])
def webhook():
  if request.headers.get('content-type') == 'application/json':
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '', 200
  return 'OK', 200


@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(
      message, "Salom! Nishon tuman axborot-kutubxona markazi botiga xush kelibsiz!"
  )


@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, message.text)


if __name__ == '__main__':
  app.run()
