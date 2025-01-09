import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Bot tokenini kiriting
BOT_TOKEN = "7802991917:AAGYROH8e2N2wc37fub6OoeES2VfjPm4TZg"
bot = telebot.TeleBot(BOT_TOKEN)

ADMIN_ID = 6333139241
user_states = {}


# Start komandasi uchun handler
@bot.message_handler(commands=['start'])
def start(message):
    # Reply Keyboard (doimiy klaviatura)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(KeyboardButton("📄 Mashinalar turi"), KeyboardButton("⚙️ Ranglar"))
    keyboard.row(KeyboardButton("📩 Qo'shimcha Ma'lumot uchun raqamlar"), KeyboardButton("🚀 Boshlash"))
    keyboard.row ( KeyboardButton ( "✍️ Izoh qoldirish" ))
    bot.send_message(message.chat.id, "Salom! Quyidagi tugmalardan birini tanlashingiz mumkin:", reply_markup=keyboard)

# Mashinalar menyusi
@bot.message_handler(func=lambda message: message.text == "📄 Mashinalar turi")
def show_car_menu(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(KeyboardButton("Mers"), KeyboardButton("BMW"), KeyboardButton("Audi"))
    keyboard.row(KeyboardButton("TESLA"), KeyboardButton("KIA"))
    keyboard.row(KeyboardButton("⬅️ Asosiy menuga o'tish "))
    bot.send_message(message.chat.id, "Quyidagi avtomobillardan birini tanlang:", reply_markup=keyboard)

# Ranglar menyusi
@bot.message_handler(func=lambda message: message.text == "⚙️ Ranglar")
def show_settings_menu(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(KeyboardButton("⚫️ Qora"), KeyboardButton("⚪️ Oq"),
                 KeyboardButton("🟡 Sariq"), KeyboardButton("🔴 Qizil"),
                 KeyboardButton("🔵 Ko'k"), KeyboardButton("🟢 Yashil"))
    keyboard.row(KeyboardButton("⬅️ Asosiy menuga o'tish "))
    bot.send_message(message.chat.id, "Rangni tanlang yoki orqaga qayting:", reply_markup=keyboard)

# Aloqa bo'limi
@bot.message_handler(func=lambda message: message.text == "📩 Qo'shimcha Ma'lumot uchun raqamlar")
def show_contact_menu(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(KeyboardButton("📞 +998 91 336 20 84"),
                 KeyboardButton("📞 +998 94 827 82 88"),
                 KeyboardButton("📞 +998 99 199 21 08"))
    keyboard.row(KeyboardButton("⬅️ Asosiy menuga o'tish"))
    bot.send_message(message.chat.id, "Qo'shimcha ma'lumot uchun quyidagi raqamlardan birini tanlang yoki qayting:", reply_markup=keyboard)

# "Orqaga" tugmasi bosilganda Start menyusiga qaytish
@bot.message_handler(func=lambda message: message.text == "⬅️ Asosiy menuga o'tish")
def go_back_to_start(message):
    start(message)
## Raqamni tasdiqlash
@bot.message_handler(func=lambda message: message.text in ["📞 +998 91 336 20 84",
                                                           "📞 +998 94 827 82 88",
                                                           "📞 +998 99 199 21 08"])
def confirm_number(message):
    bot.send_message(message.chat.id, f"Siz {message.text} raqamiga ulanishni tanladingiz. Biz bilan bog'lanishingiz mumkin.")

# Rangni tasdiqlash
@bot.message_handler(func=lambda message: message.text in ["⚫️ Qora", "⚪️ Oq",
                                                           "🟡 Sariq","🔴 Qizil",
                                                           "🔵 Ko'k","🟢 Yashil"])
def confirm_color(message):
    bot.send_message(message.chat.id, f"Siz {message.text} rangini tanladingiz.")
# # Rasm yuborish
@bot.message_handler(func=lambda message: message.text == "Mers")
def send_photo(message):
    bot.send_message(message.chat.id, "Mers: Mers - tezlik,qulaylik va innovatsiyani birlashtirgan avtomabil turi.\nNarxi: $1.5 milliard" )
    try:
        # Rasm yo'lini ko'rsating
        with open("C:\\Users\\user\\Pictures\\photo_2025-01-09_13-49-27 (3).jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption="Mana sizga rasm!")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Rasm topilmadi. To'g'ri yo'lni ko'rsating.")


@bot.message_handler(func=lambda message: message.text == "BMW")
def send_photo(message):
    bot.send_message(message.chat.id, "BMW: BMW - tezlik, sport va innovatsiyani birlashtirgan avtomabil turi.\nNarxi: $1.3 milliard")
    try:
        # Rasm yo'lini ko'rsating
        with open("C:\\Users\\user\\Pictures\\photo_2025-01-09_13-49-26 (2).jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption="Mana sizga rasm!")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Rasm topilmadi. To'g'ri yo'lni ko'rsating.")


@bot.message_handler(func=lambda message: message.text == "Audi")
def send_photo(message):
    bot.send_message(message.chat.id, "Audi: Audi - texnologiyalar va zamonaviy dizaynga urg'u beradigan avtomobil.\nNarxi: $100,000")
    try:
        # Rasm yo'lini ko'rsating
        with open("C:\\Users\\user\\Pictures\\photo_2025-01-09_13-49-26.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption="Mana sizga rasm!")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Rasm topilmadi. To'g'ri yo'lni ko'rsating.")

@bot.message_handler(func=lambda message: message.text == "TESLA")
def send_photo(message):
    bot.send_message(message.chat.id, "TESLA: TESLA - Elektro mashina bo'lib, dunyoda mashhur avtomobillardan biridir.\nNarxi: $150,000")
    try:
        # Rasm yo'lini ko'rsating
        with open("C:\\Users\\user\\Pictures\\photo_2025-01-09_13-49-27 (4).jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption="Mana sizga rasm!")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Rasm topilmadi. To'g'ri yo'lni ko'rsating.")

@bot.message_handler(func=lambda message: message.text == "KIA")
def send_photo(message):
    bot.send_message(message.chat.id, "KIA: KIA - zamonaviy texnologiyalar va dizayn bilan mashhur, Koreyada ishlab chiqariladi.\nNarxi: $80,000")
    try:
        # Rasm yo'lini ko'rsating
        with open("C:\\Users\\user\\Pictures\\photo_2025-01-09_13-49-27 (2).jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption="Mana sizga rasm!")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Rasm topilmadi. To'g'ri yo'lni ko'rsating.")

@bot.message_handler(func=lambda message: message.text == "✍️ Izoh qoldirish")
def request_comment(message):
    user_states[message.chat.id] = "awaiting_comment"
    bot.send_message(message.chat.id, "✍️ Iltimos, izohingizni yozib qoldiring:")

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "awaiting_comment")
def receive_comment(message):
    user_states.pop(message.chat.id, None)
    comment = message.text
    admin_message = (
        f"📩 Yangi izoh qoldirildi!\n\n"
        f"👤 Foydalanuvchi: @{message.from_user.username if message.from_user.username else 'No username'}\n"
        f"💬 Izoh: {comment}"
    )
    try:
        bot.send_message(ADMIN_ID, admin_message)
    except Exception as e:
        bot.send_message(message.chat.id, "Admin ID ga ulanishda muammo bor.")
    bot.send_message(message.chat.id, "✅ Izohingiz uchun rahmat! Adminlarimiz uni ko'rib chiqishadi.")


# Botni ishga tushirish
print("Bot ishlayapti....")
bot.polling()
