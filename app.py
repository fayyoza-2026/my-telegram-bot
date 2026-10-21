import telebot
from google import genai

# Telegram Bot Token
TOKEN = '8838932242:AAEyshHzRyH76uk5qEKfDC-dyG2dAGiVpBU'
bot = telebot.TeleBot(TOKEN)

# Google Gemini AI Kaliti 
GEMINI_API_KEY = "AQ.Ab8RN6LTHAQoNZJ_sJZ5qXKmCrHqbmqDDW6yIyKImHSf_k2zlw"
client = genai.Client(api_key=GEMINI_API_KEY)

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
        "Assalomu alaykum! Nishon tuman axborot-kutubxona markazining rasmiy AI botiga xush kelibsiz! 📚 AI\n\n"
        "Men sizga kutubxonamiz, kitoblar hamda a'zolik qoidalari bo'yicha har qanday savolingizga sun'iy intellekt yordamida javob bera olaman.\n\n"
        "Savolingizni yozib yuboring!"
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(func=lambda message: True)
def handle_ai_messages(message):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{SYSTEM_INSTRUCTION}\n\nFoydalanuvchi savoli: {message.text}"
        )
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Hozirda javob berishda biroz texnik uzilish bo'ldi. Qayta urinib ko'ring.")

if __name__ == '__main__':
    bot.infinity_polling()
