# ===== AHLI =====
# Definisi 6 Ahli dengan gelar dan komposisi

AHLI_LIST = [
    {
        "id": "ahli_1",
        "nama": "Sang Maha Guru",
        "semboyan": "Satu Untuk Semua",
        "komposisi": "Gemini (semua)",
        "siklus": 30,
        "icon": "🧠",
        "deskripsi": "Kualitas soal dan penilaian terbaik."
    },
    {
        "id": "ahli_2",
        "nama": "Sang Penggagas",
        "semboyan": "Menggagas Soal, Menuntun Jawaban",
        "komposisi": "Gemini (soal) + Groq (penilaian)",
        "siklus": 30,
        "icon": "📝",
        "deskripsi": "Soal berbobot tinggi dengan penilaian cepat."
    },
    {
        "id": "ahli_3",
        "nama": "Sang Pembedah",
        "semboyan": "Membedah Setiap Jawaban",
        "komposisi": "Groq (soal) + Gemini (penilaian)",
        "siklus": 30,
        "icon": "🔍",
        "deskripsi": "Penilaian mendalam dan analisis tajam."
    },
    {
        "id": "ahli_4",
        "nama": "Sang Petarung",
        "semboyan": "Awal Kuat, Akhir Tangguh",
        "komposisi": "Gemini (30) → Groq (288)",
        "siklus": 318,
        "icon": "⚔️",
        "deskripsi": "30 soal berkualitas + 288 soal cepat."
    },
    {
        "id": "ahli_5",
        "nama": "Sang Pelari",
        "semboyan": "Cepat dan Tepat Sasaran",
        "komposisi": "Groq (semua)",
        "siklus": 288,
        "icon": "⚡",
        "deskripsi": "Kapasitas besar dan respons cepat."
    },
    {
        "id": "ahli_6",
        "nama": "Sang Penjaga",
        "semboyan": "Penjaga di Ujung Jalan",
        "komposisi": "OpenRouter (semua)",
        "siklus": 1,
        "icon": "🛡️",
        "deskripsi": "Cadangan darurat terakhir."
    }
]

def get_ahli(ahli_id):
    for ahli in AHLI_LIST:
        if ahli["id"] == ahli_id:
            return ahli
    return None

def get_all_ahli():
    return AHLI_LIST