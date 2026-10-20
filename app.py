import telebot

TOKEN = '8838932242:AAEyshHzRyH76uk5qEKfDC-dyG2dAGiVpBU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Nishon tuman axborot-kutubxona markazi botiga xush kelibsiz!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Siz yozdingiz: {message.text}")

if __name__ == '__main__':
    bot.infinity_polling()
