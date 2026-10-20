import telebot

TOKEN = '8838932242:AAEyshHzRyH76uk5qEKfDC-dyG2dAGiVpBU'
bot = telebot.TeleBot(TOKEN)

# Start buyrug'i uchun
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Assalomu alaykum! Nishon tuman axborot-kutubxona markazining rasmiy botiga xush kelibsiz! 📚\n\n"
        "Men sizga kutubxonamiz haqida ma'lumot berishim mumkin:\n"
        "📍 Joylashuv va manzil\n"
        "⏰ Ish vaqti\n"
        "📖 Kitob olish va a'zolik qoidalari\n\n"
        "Savolingizni yozib yuboring!"
    )
    bot.reply_to(message, welcome_text)

# Kutubxona haqidagi savollarga javob berish
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    text = message.text.lower()
    
    if 'qayerda' in text or 'manzil' in text or 'joylashuv' in text:
        bot.reply_to(message, "📍 Kutubxonamiz manzili: Nishon tumani, Paxtakor MFY, Qora Niyoziy koʻchasi 1-uy.")
    
    elif 'vaqt' in text or 'soat' in text or 'ochiq' in text or 'ish' in text:
        bot.reply_to(message, "⏰ Ish vaqtimiz: Dushanbadan Shanbagacha, soat 09:00 dan 18:00 gacha. Yakshanba — dam olish kuni.")
    
    elif 'kitob' in text or 'olish' in text or 'muddati' in text:
        bot.reply_to(message, "📖 Kutubxonamizda 43,000 dan ortiq kitoblar mavjud. Kitoblar kitobxonlarga 10 kun muddatga bepul beriladi.")
    
    elif 'a\'zolik' in text or 'a\'zo' in text or 'hujjat' in text:
        bot.reply_to(message, "🪪 Kutubxonaga a'zo bo'lish uchun shaxsni tasdiqlovchi hujjat (pasport yoki guvohnoma) yetarli. A'zolik mutlaqo bepul!")
    
    else:
        bot.reply_to(message, "Tushundim. Sizning savolingiz bo'yicha kutubxona xodimlarimiz tez orada siz bilan bog'lanishadi! Yoki manzil, ish vaqti, kitob olish haqida so'rashingiz mumkin.")

if __name__ == '__main__':
    bot.infinity_polling()  
