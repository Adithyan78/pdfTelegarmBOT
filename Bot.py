from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from fpdf import FPDF
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env
TOKEN = os.getenv("BOT_TOKEN")

# Function to remove unsupported chars for latin-1 encoding
def remove_unsupported_chars(text):
    return text.encode('latin-1', errors='ignore').decode('latin-1')

# Function to create PDF from text
def text_to_pdf(text, filename="output.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)
    pdf.output(filename)

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! Send me any text, and I’ll convert it into a PDF for you."
    )

# Handle incoming messages (text to PDF)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = remove_unsupported_chars(update.message.text)  # clean unsupported chars
    file_path = "output.pdf"

    text_to_pdf(user_text, file_path)

    await update.message.reply_document(open(file_path, "rb"))
    os.remove(file_path)  # cleanup

# Main function to start bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))  # Add start command
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # Text messages

    print("Bot is running...")
    app.run_polling()
