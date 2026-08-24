# ===== KEYBOARDS =====
# Semua tombol untuk bot

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from token_manager import get_balance, get_packages
from ahli import get_all_ahli
from topics import (
    get_category_options, get_bidang_studi_options,
    get_program_studi_options, get_topik_options,
    get_sub_topik_options
)

# ===== MENU UTAMA =====
def main_menu(user_id=None):
    saldo = get_balance(user_id) if user_id else 0
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📚 Input Kategori", callback_data="input_kategori")],
        [InlineKeyboardButton("🧠 Pilih Metode Asesmen", callback_data="metode_asesmen")],
        [InlineKeyboardButton("⚙️ Pilih Ahli", callback_data="pilih_ahli")],
        [InlineKeyboardButton(f"💰 {saldo} token", callback_data="cek_saldo")],
        [InlineKeyboardButton("🛒 Beli Token", callback_data="beli_token")],
        [InlineKeyboardButton("❓ Bantuan", callback_data="bantuan")],
    ])

# ===== KATEGORI =====
def kategori_menu():
    options = get_category_options()
    keyboard = []
    for key, value in options.items():
        keyboard.append([InlineKeyboardButton(f"{key}. {value}", callback_data=f"kategori_{key}")])
    keyboard.append([InlineKeyboardButton("Y. Lainnya (Tuliskan)", callback_data="kategori_lain")])
    keyboard.append([InlineKeyboardButton("Z. Kembali", callback_data="back")])
    return InlineKeyboardMarkup(keyboard)

# ===== BIDANG STUDI =====
def bidang_studi_menu():
    options = get_bidang_studi_options()
    keyboard = []
    for key, value in options.items():
        keyboard.append([InlineKeyboardButton(f"{key}. {value}", callback_data=f"bidang_{key}")])
    keyboard.append([InlineKeyboardButton("Y. Lainnya (Tuliskan)", callback_data="bidang_lain")])
    keyboard.append([InlineKeyboardButton("Z. Kembali", callback_data="back_kategori")])
    return InlineKeyboardMarkup(keyboard)

# ===== PROGRAM STUDI =====
def program_studi_menu():
    options = get_program_studi_options()
    keyboard = []
    for key, value in options.items():
        keyboard.append([InlineKeyboardButton(f"{key}. {value}", callback_data=f"program_{key}")])
    keyboard.append([InlineKeyboardButton("Y. Lainnya (Tuliskan)", callback_data="program_lain")])
    keyboard.append([InlineKeyboardButton("Z. Kembali", callback_data="back_bidang")])
    return InlineKeyboardMarkup(keyboard)

# ===== METODE PENENTUAN TOPIK =====
def metode_topik_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("A. Tampilkan Otomatis", callback_data="metode_otomatis")],
        [InlineKeyboardButton("B. Isi Mandiri", callback_data="metode_mandiri")],
        [InlineKeyboardButton("Y. Lainnya (Tuliskan)", callback_data="metode_lain")],
        [InlineKeyboardButton("Z. Kembali", callback_data="back_program")],
    ])

# ===== TOPIK =====
def topik_menu():
    options = get_topik_options()
    keyboard = []
    for key, value in options.items():
        keyboard.append([InlineKeyboardButton(f"{key}. {value}", callback_data=f"topik_{key}")])
    keyboard.append([InlineKeyboardButton("Y. Lainnya (Tuliskan)", callback_data="topik_lain")])
    keyboard.append([InlineKeyboardButton("Z. Kembali", callback_data="back_metode")])
    return InlineKeyboardMarkup(keyboard)

# ===== SUB-TOPIK =====
def sub_topik_menu():
    options = get_sub_topik_options()
    keyboard = []
    for key, value in options.items():
        keyboard.append([InlineKeyboardButton(f"{key}. {value}", callback_data=f"sub_{key}")])
    keyboard.append([InlineKeyboardButton("Y. Lainnya (Tuliskan)", callback_data="sub_lain")])
    keyboard.append([InlineKeyboardButton("Z. Kembali", callback_data="back_topik")])
    return InlineKeyboardMarkup(keyboard)

# ===== METODE ASESMEN =====
def metode_asesmen_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("A. Asesmen Berbasis Materi", callback_data="asesmen_materi")],
        [InlineKeyboardButton("B. Asesmen Pola Terpadu", callback_data="asesmen_terpadu")],
        [InlineKeyboardButton("C. Asesmen Berbasis Evaluasi", callback_data="asesmen_evaluasi")],
        [InlineKeyboardButton("Y. Lainnya (Tuliskan)", callback_data="asesmen_lain")],
        [InlineKeyboardButton("Z. Kembali", callback_data="back")],
    ])

# ===== PRESET MENU =====
def preset_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("A. Standar 1", callback_data="preset_standar1")],
        [InlineKeyboardButton("B. Standar 2", callback_data="preset_standar2")],
        [InlineKeyboardButton("C. Konfigurasi Manual", callback_data="preset_manual")],
        [InlineKeyboardButton("D. Gunakan Konfigurasi Terakhir", callback_data="preset_terakhir")],
        [InlineKeyboardButton("E. Preset lainnya (Tempelkan)", callback_data="preset_lain")],
        [InlineKeyboardButton("Y. Lainnya (Tuliskan)", callback_data="preset_lainnya")],
        [InlineKeyboardButton("Z. Kembali", callback_data="back_asesmen")],
    ])

# ===== PILIH AHLI =====
def ahli_menu():
    ahli_list = get_all_ahli()
    keyboard = []
    for ahli in ahli_list:
        keyboard.append([InlineKeyboardButton(
            f"{ahli['icon']} Ahli {ahli['id'].replace('ahli_', '')} - {ahli['nama']}",
            callback_data=f"ahli_{ahli['id']}"
        )])
    keyboard.append([InlineKeyboardButton("Y. Lainnya (Tuliskan)", callback_data="ahli_lain")])
    keyboard.append([InlineKeyboardButton("Z. Kembali", callback_data="back")])
    return InlineKeyboardMarkup(keyboard)

# ===== RANGKUMAN =====
def konfirmasi_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("A. Konfirmasi", callback_data="konfirmasi")],
        [InlineKeyboardButton("B. Ubah", callback_data="ubah")],
        [InlineKeyboardButton("Y. Lainnya (Tuliskan)", callback_data="konfirmasi_lain")],
        [InlineKeyboardButton("Z. Kembali", callback_data="back_preset")],
    ])

# ===== PAKET TOKEN =====
def token_package_menu():
    packages = get_packages()
    keyboard = []
    for key, value in packages.items():
        keyboard.append([InlineKeyboardButton(value["label"], callback_data=f"buy_{key}")])
    keyboard.append([InlineKeyboardButton("Y. Lainnya (Tuliskan)", callback_data="buy_lain")])
    keyboard.append([InlineKeyboardButton("Z. Kembali", callback_data="back")])
    return InlineKeyboardMarkup(keyboard)

# ===== JAWABAN SOAL =====
def jawaban_menu(soal_index):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("A", callback_data=f"jawab_A_{soal_index}"),
         InlineKeyboardButton("B", callback_data=f"jawab_B_{soal_index}"),
         InlineKeyboardButton("C", callback_data=f"jawab_C_{soal_index}")],
        [InlineKeyboardButton("D", callback_data=f"jawab_D_{soal_index}"),
         InlineKeyboardButton("E", callback_data=f"jawab_E_{soal_index}")],
        [InlineKeyboardButton("⏭️ Lewati", callback_data=f"lewat_{soal_index}")],
    ])

# ===== SETELAH SESI =====
def after_session_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("A. Lanjut", callback_data="lanjut")],
        [InlineKeyboardButton("B. Tunggu", callback_data="tunggu")],
        [InlineKeyboardButton("C. Checkpoint", callback_data="checkpoint")],
        [InlineKeyboardButton("D. Parameter", callback_data="parameter")],
    ])

# ===== CHECKPOINT =====
def checkpoint_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("A. Lanjut", callback_data="cp_lanjut")],
        [InlineKeyboardButton("B. Simpan", callback_data="cp_simpan")],
        [InlineKeyboardButton("Y. Lainnya (Tuliskan)", callback_data="cp_lain")],
        [InlineKeyboardButton("Z. Kembali", callback_data="cp_kembali")],
    ])