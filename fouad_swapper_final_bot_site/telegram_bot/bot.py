
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8753507918:AAHPxp2ZGNvB_z__PCTt_Fbmt91sJvNKEWA"
ADMIN_ID = 7989922729

gif = "https://media1.giphy.com/media/v1.Y2lkPTZjMDliOTUyaWFmbXN0cWtoNzh0aHR0dnNrMXJ3bTYxNW92ZXNuOHc3dGpzOWx4bSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YmZOBDYBcmWK4/giphy.gif"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    buttons = [
        [KeyboardButton("💳 الاشتراك")],
        [KeyboardButton("📤 إرسال إثبات الدفع")],
        [KeyboardButton("👨‍💻 تواصل مع المطور")]
    ]

    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    await update.message.reply_animation(
        animation=gif,
        caption="🔥 Fouad Swapper Tool\n\nاختر من القائمة",
        reply_markup=keyboard
    )


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "💳 الاشتراك":

        await update.message.reply_text(
"""💰 الاشتراك الشهري: 26$

Binance ID
499796959

البنك العربي
00962795637371

بعد الدفع اضغط
إرسال إثبات الدفع
"""
        )

    elif text == "👨‍💻 تواصل مع المطور":

        await update.message.reply_text(
"تواصل مع المطور\n\n@N0hnnf"
        )

    elif text == "📤 إرسال إثبات الدفع":

        await update.message.reply_text(
"أرسل لقطة شاشة الدفع أو رقم التحويل."
        )


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user

    username = user.username if user.username else "No username"

    caption = f"""
📥 طلب تفعيل جديد

👤 Name: {user.first_name}
🔗 Username: @{username}
🆔 ID: {user.id}
"""

    photo = update.message.photo[-1].file_id

    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=photo,
        caption=caption
    )

    await update.message.reply_text(
"✅ تم إرسال طلبك للمطور، سيتم التحقق وتفعيل الأداة قريباً."
    )


def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    app.run_polling()


if __name__ == "__main__":
    main()
