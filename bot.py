# ===== BOT UTAMA =====
# Logika utama bot Telegram

import os
import logging
import asyncio
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes
)

# ===== LOAD ENV =====
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# ===== LOGGING =====
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ===== IMPORT MODULES =====
from keyboards import *
from token_manager import get_balance, add_tokens, deduct_token, has_enough_tokens, user_tokens, get_packages
from topics import get_category_input_fields, get_category_options
from ahli import get_ahli, get_all_ahli
from config_manager import ConfigManager
from session_manager import SessionManager
from question_bank import QuestionBank
from assessment import AssessmentManager
from ai_handler import (
    ahli_1, ahli_2, ahli_3, ahli_4, ahli_5, ahli_6,
    usage_counter, DAILY_QUOTA
)

# ===== INISIALISASI =====
config_manager = ConfigManager()
session_manager = SessionManager()
question_bank = QuestionBank()
assessment_manager = AssessmentManager(session_manager, question_bank)

# ===== STATE =====
user_state = {}
user_config = {}
user_metode = {}
user_kategori = {}
user_ahli = {}
user_current_soal = {}

# ===== JEDA =====
JEDA_ANTAR_PESAN = 1

async def send_with_delay(chat_id, text, reply_markup=None, parse_mode=None):
    await asyncio.sleep(JEDA_ANTAR_PESAN)
    return await application.bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=reply_markup,
        parse_mode=parse_mode
    )

# ===== START =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in user_tokens:
        add_tokens(user_id, 500)
    user_state[user_id] = "main_menu"
    await send_with_delay(
        update.effective_chat.id,
        f"👋 Selamat datang di **Sistem Kuis Pembelajaran Bertahap**!\n\n💰 Saldo: {get_balance(user_id)} token",
        reply_markup=main_menu(user_id),
        parse_mode="Markdown"
    )


# ===== MAIN =====
# ===== BUTTON HANDLER =====
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menangani semua tombol yang ditekan"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        f"✅ Tombol ditekan!\n\n"
        f"Kode tombol: {query.data}\n\n"
        f"Untuk memulai, ketik /start"
    )

# ===== MESSAGE HANDLER =====
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menangani semua pesan teks dari pengguna"""
    user_id = update.effective_user.id
    text = update.message.text
    
    # Balas pesan sederhana
    await update.message.reply_text(
        f"✅ Pesanmu diterima!\n\n"
        f"Kamu mengetik: {text}\n\n"
        f"Untuk memulai, ketik /start"
    )
def main():
    global application
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Daftarkan semua handler
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    logger.info("🤖 Bot Kuis Pembelajaran sedang berjalan...")
    application.run_polling()

if __name__ == "__main__":
    main()