import os
import threading
from flask import Flask
import telebot
import google.generativeai as genai

# Render port talabini qondirish uchun kichik veb-server
app = Flask(name)

@app.route('/')
def home():
    return "Nishon Kutubxona Bot is live!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# Telegram Bot Token
TOKEN = '8838932242:AAFEK2AE8xAloJ35J85koH8SLh1_HMaZBT8'
bot = telebot.TeleBot(TOKEN)

# Google Gemini AI Kaliti
GEMINI_API_KEY = "AQ.Ab8RN6LTHAQoNZJ_sJZ5qXKmCrHqbmqDDW6yIyKImHSf_k2zlw"
genai.configure(api_key=GEMINI_API_KEY)

# Modelni ishga tushirish
model = genai.GenerativeModel('gemini-1.5-flash')

# Kutubxona ma'lumotlari va AI ko'rsatmasi
SYSTEM_INSTRUCTION = """
Siz Nishon tuman axborot-kutubxona markazining rasmiy aqlli sun'iy intellekt botisiz.
Kutubxona haqida ma'lumotlar:
- Manzil: Nishon tumani, Paxtakor MFY, Qora Niyoziy koʻchasi 1-uy.
- Ish vaqti: Dushanbadan Shanbagacha, soat 09:00 dan 18:00 gacha. Yakshanba — dam olish kuni.
- Fond: 43,000 dan ortiq kitoblar mavjud.
- Qoidalar: Kitoblar a'zolarga 10 kun muddatga bepul beriladi. A'zo bo'lish uchun pasport yoki guvohnoma kifoya.

Vazifangiz: Foydalanuvchilarning har qanday savollariga, kitoblar hamda adabiyot bo'yicha so'rovlariga xushmuomala hamda aniq javob berish.
"""

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Assalomu alaykum! Nishon tuman axborot-kutubxona markazining rasmiy AI botiga xush kelibsiz! 📚\n\n"
        "Men sizga kutubxonamiz, kitoblar hamda a'zolik qoidalari bo'yicha har qanday savolingizga sun'iy intellekt yordamida javob bera olaman.\n\n"
        "Savolingizni yozib yuboring!"
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(func=lambda message: True)
def handle_ai_messages(message):
    try:
        prompt = f"{SYSTEM_INSTRUCTION}\n\nFoydalanuvchi savoli: {message.text}"
        response = model.generate_content(prompt)
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Xatolik: {e}")
        fallback_text = (
            "📍 Nishon tuman axborot-kutubxona markazi\n\n"
            "• Manzil: Nishon tumani, Paxtakor MFY, Qora Niyoziy koʻchasi 1-uy.\n"
            "• Ish vaqti: Dushanba - Shanba, 09:00 dan 18:00 gacha.\n"
            "• Fond: 43,000 dan ortiq kitoblar.\n"
            "• Qoidalar: Kitoblar 10 kunga bepul beriladi (pasport kifoya)."
        )
        bot.reply_to(message, fallback_text, parse_mode="Markdown")

if __name__ == '__main__':
    # Veb-serverni alohida oqimda (thread) ishga tushiramiz
    threading.Thread(target=run_flask).start()
    # Telegram botni polling qilish
    bot.infinity_polling()
