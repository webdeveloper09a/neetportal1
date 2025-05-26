import os
import json
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
    ConversationHandler,
)
import logging
from datetime import datetime

# Logging for debugging
logging.basicConfig(level=logging.INFO)

# Replace with your actual admin Telegram user ID
ADMIN_USER_ID =7796598050  # 👈 update this!

# Telegram Bot Token (use Railway → Variables tab or set here directly)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# States for ConversationHandler
BATCH, CATEGORY, FILE = range(3)

BASE_DIR = os.path.join(os.path.dirname(__file__), "Website")
TESTS_JSON = os.path.join(BASE_DIR, "data", "tests.json")
PDF_DIR = os.path.join(BASE_DIR, "pdfs")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_USER_ID:
        await update.message.reply_text("You are not authorized to use this bot.")
        return ConversationHandler.END

    reply_keyboard = [["rm", "tym", "oym"]]
    await update.message.reply_text(
        "Welcome! Please select the batch:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return BATCH


async def batch_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["batch"] = update.message.text.lower()
    batch = context.user_data["batch"]

    if batch == "rm":
        categories = ["fts", "aiats"]
    else:
        categories = ["pt", "aiats", "te", "nrt"]

    reply_keyboard = [categories]
    await update.message.reply_text(
        f"Selected batch: {batch.upper()}\nNow choose the test category:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return CATEGORY


async def category_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["category"] = update.message.text.lower()
    await update.message.reply_text("Now send the PDF file:")
    return FILE


async def save_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.document.mime_type != "application/pdf":
        await update.message.reply_text("Please send a valid PDF file.")
        return FILE

    batch = context.user_data["batch"]
    category = context.user_data["category"]
    pdf_file = update.message.document

    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{batch.upper()}_{category.upper()}_{date_str}.pdf"

    folder_path = os.path.join(PDF_DIR, batch, category)
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, filename)
    await pdf_file.get_file().download_to_drive(file_path)

    # Update tests.json
    with open(TESTS_JSON, "r") as f:
        data = json.load(f)

    data.setdefault(batch, {}).setdefault(category, []).insert(0, filename)

    with open(TESTS_JSON, "w") as f:
        json.dump(data, f, indent=2)

    await update.message.reply_text("✅ PDF uploaded and record saved.")
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Operation cancelled.")
    return ConversationHandler.END


# Entry point to run the bot
if __name__ == "__main__":
    import asyncio

    async def main():
        application = Application.builder().token(BOT_TOKEN).build()

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", start)],
            states={
                BATCH: [MessageHandler(filters.TEXT & ~filters.COMMAND, batch_selection)],
                CATEGORY: [MessageHandler(filters.TEXT & ~filters.COMMAND, category_selection)],
                FILE: [MessageHandler(filters.Document.PDF, save_pdf)],
            },
            fallbacks=[CommandHandler("cancel", cancel)],
        )

        application.add_handler(conv_handler)

        # Start the bot
        await application.run_polling()

    asyncio.run(main())
