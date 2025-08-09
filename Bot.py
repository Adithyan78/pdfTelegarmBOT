
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from fpdf import FPDF
import os


from dotenv import load_dotenv

load_dotenv()  # Load variables from .env
TOKEN = os.getenv("BOT_TOKEN")


# Function to create PDF from text
def text_to_pdf(text, filename="output.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)
    pdf.output(filename)

# Handle incoming messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    file_path = "output.pdf"
    
    text_to_pdf(user_text, file_path)
    
    await update.message.reply_document(open(file_path, "rb"))
    os.remove(file_path)  # cleanup

# Main function to start bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot is running...")
    app.run_polling()
