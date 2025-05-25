import os
import json
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    filters, ConversationHandler, ContextTypes
)

# === CONFIGURATION ===
ADMIN_ID = 123456789  # 🔐 Replace with your Telegram User ID
BASE_DIR = "Website/pdfs"
JSON_PATH = "Website/data/tests.json"

BATCHES = {
    "RM": ["FTS", "AIATS"],
    "OYM": ["PT", "AIATS", "TE", "NRT"],
    "TYM": ["PT", "AIATS", "TE", "NRT"]
}

# === STATES ===
SELECT_BATCH, SELECT_CATEGORY, GET_PDF, GET_FILENAME = range(4)

# === HELPERS ===
def save_to_json(batch, category, filename):
    with open(JSON_PATH, 'r') as f:
        data = json.load(f)

    if batch.lower() not in data:
        data[batch.lower()] = {}

    if category not in data[batch.lower()]:
        data[batch.lower()][category] = []

    if filename not in data[batch.lower()][category]:
        data[batch.lower()][category].append(filename)

    with open(JSON_PATH, 'w') as f:
        json.dump(data, f, indent=2)

# === CONVERSATION FLOW ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ You're not authorized to use this bot.")
        return ConversationHandler.END

    reply_keyboard = [[b] for b in BATCHES.keys()]
    await update.message.reply_text(
        "Select Batch:", reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return SELECT_BATCH

async def select_batch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    batch = update.message.text
    if batch not in BATCHES:
        await update.message.reply_text("Invalid batch. Try again.")
        return ConversationHandler.END

    context.user_data["batch"] = batch
    categories = BATCHES[batch]
    reply_keyboard = [[c] for c in categories]
    await update.message.reply_text(
        "Select Category:", reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return SELECT_CATEGORY

async def select_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    category = update.message.text
    context.user_data["category"] = category
    await update.message.reply_text("Now send the PDF file.")
    return GET_PDF

async def get_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.document or not update.message.document.file_name.endswith(".pdf"):
        await update.message.reply_text("Please send a valid PDF file.")
        return GET_PDF

    context.user_data["file"] = update.message.document
    await update.message.reply_text("What should be the filename? (Example: AIATS-05.pdf)")
    return GET_FILENAME

async def get_filename(update: Update, context: ContextTypes.DEFAULT_TYPE):
    filename = update.message.text
    file = context.user_data["file"]
    batch = context.user_data["batch"]
    category = context.user_data["category"]

    folder_path = os.path.join(BASE_DIR, batch.lower(), category)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)

    file_data = await file.get_file()
    await file_data.download_to_drive(file_path)

    save_to_json(batch, category, filename)

    await update.message.reply_text(f"✅ Uploaded and saved as {filename}")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Cancelled.")
    return ConversationHandler.END

# === MAIN ===
def main():
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN_HERE").build()  # 🔐 Replace with your bot token

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            SELECT_BATCH: [MessageHandler(filters.TEXT & ~filters.COMMAND, select_batch)],
            SELECT_CATEGORY: [MessageHandler(filters.TEXT & ~filters.COMMAND, select_category)],
            GET_PDF: [MessageHandler(filters.Document.PDF, get_pdf)],
            GET_FILENAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_filename)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv_handler)
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
