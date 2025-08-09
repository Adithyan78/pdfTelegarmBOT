# Telegram Text-to-PDF Bot

A simple Telegram bot that converts any plain text message you send into a downloadable PDF file instantly. Perfect for quick note-taking, sharing documents, or saving text as PDFs on the go.

---

## Features

- Converts plain text to PDF in seconds
- Supports multiline text and paragraphs
- Sends the PDF file directly in Telegram chat
- Easy to deploy locally or on cloud platforms like Render or Railway
- Environment variables support for secure token management

---

## Prerequisites

- Python 3.7 or higher  
- Telegram bot token from [BotFather](https://t.me/BotFather)  
- Git (optional, for cloning repo)  
- (Optional) Node.js & npm if you want to use Railway CLI  

---

## Installation & Setup

### Clone repository and setup environment

```bash
git clone https://github.com/Adithyan78/pdfTelegarmBOT.git
cd pdfTelegarmBOT

# Create virtual environment
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create and activate a virtual environment
Windows (PowerShell):
powershell
Copy
Edit
python -m venv venv
.\venv\Scripts\activate
macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
# Create a .env file
Create a .env file in the project root folder with this content:
BOT_TOKEN=your_telegram_bot_token_here
Replace your_telegram_bot_token_here with your actual Telegram bot token.

# Run the bot locally

python Bot.py
