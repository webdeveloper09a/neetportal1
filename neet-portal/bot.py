import os
import json
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes
from telegram.ext import CallbackContext

BOT_TOKEN = os.environ["BOT_TOKEN"]
ADMIN_ID = int(os.environ["ADMIN_ID"])

UPLOAD_CATEGORY, UPLOAD_SUBCATEGORY, UPLOAD_FILE = range(3)
CATEGORY_MAP = {
    "rm": ["FTS", "AIATS"],
    "tym": ["PT", "AIATS", "TE", "NRT"],
    "oym": ["PT", "AIATS", "TE", "NRT"]
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ You are not authorized to use this bot.")
        return ConversationHandler.END
    await update.message.reply_text("📂 Enter category (rm/tym/oym):")
    return UPLOAD_CATEGORY

async def get_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cat = update.message.text.strip().lower()
    if cat not in CATEGORY_MAP:
        await update.message.reply_text("❗ Invalid category. Use rm, tym, or oym.")
        return ConversationHandler.END
    context.user_data["category"] = cat
    await update.message.reply_text(f"📁 Enter subcategory {CATEGORY_MAP[cat]}:")
    return UPLOAD_SUBCATEGORY

async def get_subcategory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subcat = update.message.text.strip().upper()
    cat = context.user_data["category"]
    if subcat not in CATEGORY_MAP[cat]:
        await update.message.reply_text(f"❗ Invalid subcategory for {cat}.")
        return ConversationHandler.END
    context.user_data["subcategory"] = subcat
    await update.message.reply_text("📄 Now send the PDF file:")
    return UPLOAD_FILE

async def handle_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    document = update.message.document
    if not document or not document.file_name.endswith(".pdf"):
        await update.message.reply_text("❗ Please send a valid PDF.")
        return UPLOAD_FILE

    cat = context.user_data["category"]
    subcat = context.user_data["subcategory"]
    filename = document.file_name
    save_path = f"Website/pdfs/{cat}/{subcat}/{filename}"

    file = await context.bot.get_file(document.file_id)
    await file.download_to_drive(save_path)

    # Update tests.json
    with open("Website/data/tests.json", "r") as f:
        data = json.load(f)
    if cat not in data:
        data[cat] = {}
    if subcat not in data[cat]:
        data[cat][subcat] = []
    data[cat][subcat].append(filename)
    with open("Website/data/tests.json", "w") as f:
        json.dump(data, f, indent=4)

    await update.message.reply_text("✅ Uploaded successfully.")
    return ConversationHandler.END

app = Application.builder().token(BOT_TOKEN).build()

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("upload", start)],
    states={
        UPLOAD_CATEGORY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_category)],
        UPLOAD_SUBCATEGORY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_subcategory)],
        UPLOAD_FILE: [MessageHandler(filters.Document.PDF, handle_pdf)],
    },
    fallbacks=[],
)
app.add_handler(conv_handler)

if __name__ == "__main__":
    print("🤖 Bot is running...")
    app.run_polling()
