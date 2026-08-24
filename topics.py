# ===== TOPICS =====
# Manajemen input kategori dan topik

def get_category_input_fields():
    return [
        "Kategori",
        "Bidang Studi",
        "Program Studi",
        "Metode Penentuan Topik dan Sub-Topik",
        "Topik",
        "Sub-Topik",
        "Cakupan Materi",
        "Kisi-kisi",
        "Sumber Referensi",
        "Prioritas Tahun"
    ]

def get_category_options():
    return {
        "A": "CPNS",
        "B": "PPPK",
        "C": "Mata Kuliah",
        "D": "Mata Pelajaran"
    }

def get_bidang_studi_options():
    return {
        "A": "Sains",
        "B": "Sosial",
        "C": "Bahasa",
        "D": "Lainnya"
    }

def get_program_studi_options():
    return {
        "A": "Fisika",
        "B": "Kimia",
        "C": "Biologi",
        "D": "Lainnya"
    }

def get_topik_options():
    return {
        "A": "Topik 1",
        "B": "Topik 2",
        "C": "Topik 3",
        "D": "Topik 4"
    }

def get_sub_topik_options():
    return {
        "A": "Sub-Topik 1",
        "B": "Sub-Topik 2",
        "C": "Sub-Topik 3",
        "D": "Sub-Topik 4"
    }