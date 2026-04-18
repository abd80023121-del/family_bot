import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)

def main_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    
    btn1 = InlineKeyboardButton("📌 معلومات عنا", callback_data="info")
    btn2 = InlineKeyboardButton("🛒 خدماتنا", callback_data="services")
    btn3 = InlineKeyboardButton("📞 تواصل معنا", callback_data="contact")
    btn4 = InlineKeyboardButton("📅 جدول المهام", callback_data="tasks")
    btn5 = InlineKeyboardButton("💬 واتساب", url="https://wa.me/0998816982")
    
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5)
    
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome = "👋 أهلاً بكم في بوت المنزل!\n\nاختر ما تحتاجه:"
    bot.send_message(message.chat.id, welcome, reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: True)
def handle_buttons(call):
    bot.answer_callback_query(call.id)
    data = call.data

    if data == "info":
        bot.send_message(call.message.chat.id, "📌 بوت خاص بعائلتنا للتواصل والتنسيق.")
    elif data == "services":
        bot.send_message(call.message.chat.id, "🛒 خدماتنا داخل المنزل:\n• تنسيق المهام\n• جدول الأعمال\n• تواصل سريع")
    elif data == "contact":
        bot.send_message(call.message.chat.id, "📞 يمكنك استخدام زر الواتساب أعلاه للتواصل.")
    elif data == "tasks":
        bot.send_message(call.message.chat.id, "📅 جدول المهام:\n\nحالياً لا توجد مهام مسجلة.\nأرسل المهمة وسأساعدك لاحقًا.")

print("✅ بوت المنزل يعمل...")
bot.infinity_polling()
