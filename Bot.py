import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("7546233862:AAH9iqJG77PO908kw7kkdBI-Zu_PWYDUdcg")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Aap food design services ke liye yaha contact kar sakte hain.")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Thank you! Hum aapse jaldi contact karenge. 😊")

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    print("Bot started...")
    application.run_polling()

if __name__ == "__main__":
    main()
