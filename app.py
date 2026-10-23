import os
import threading
from flask import Flask
import telebot
import google.generativeai as genai

app = Flask(name)

@app.route('/')
def home():
    return "Bot is live!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

TOKEN = '8838932242:AAFEK2AE8xAloJ35J85koH8SLh1_HMaZBT8'
bot = telebot.TeleBot(TOKEN)

GEMINI_API_KEY = "AQ.Ab8RN6LTHAQoNZJ_sJZ5qXKmCrHqbmqDDW6yIyKImHSf_k2zlw"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

SYSTEM_INSTRUCTION = """
Siz Nishon tuman axborot-kutubxona markazining rasmiy aqlli sun'iy intellekt botisiz.
Kutubxona haqida ma'lumotlar:
- Manzil: Nishon tumani, Paxtakor MFY, Qora Niyoziy koʻchasi 1-uy.
- Ish vaqti: Dushanbadan Shanbagacha, soat 09:00 dan 18:00 gacha. Yakshanba — dam olish kuni.
- Fond: 43,000 dan ortiq kitoblar mavjud.
- Qoidalar: Kitoblar a'zolarga 10 kun muddatga bepul beriladi. A'zo bo'lish uchun pasport yoki guvohnoma kifoya.
"""

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Nishon tuman axborot-kutubxona markazining rasmiy AI botiga xush kelibsiz! 📚\n\nSavolingizni yozib yuboring!")

@bot.message_handler(func=lambda message: True)
def handle_ai_messages(message):
    try:
        response = model.generate_content(SYSTEM_INSTRUCTION + "\n\nSavol: " + message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Kutubxona manzili: Nishon tumani, Paxtakor MFY, 1-uy. Ish vaqti: 09:00 - 18:00. Tel: 10 kunlik muddatga kitob beriladi.")

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    bot.infinity_polling()
   
