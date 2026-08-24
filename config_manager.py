# ===== CONFIG MANAGER =====
# Mengelola konfigurasi dan preset

class ConfigManager:
    def __init__(self):
        self.configs = {
            "latihan": {},
            "evaluasi_sub_topik": {},
            "uji_kompetensi": {},
            "komprehensif": {}
        }
        self.active_config = None
        self.active_jenis = None
        
        self.defaults = {
            "tahap": 1,
            "kemampuan_diuji": "Pemahaman",
            "sub_kemampuan": "Berpikir Analitis",
            "jenis_soal": "Pilihan Ganda",
            "cara_penyajian": "Satu per Satu",
            "tingkat_kesulitan": "Sedang",
            "adaptasi_kesulitan": "Tidak",
            "sistem_penilaian": "Langsung",
            "jumlah_soal_per_sesi": 10,
            "jumlah_sesi": 1,
            "total_soal": 10
        }
        
        self.presets = {
            "standar_1": {
                "tahap": 1,
                "kemampuan_diuji": "Pemahaman",
                "sub_kemampuan": "Berpikir Analitis",
                "jenis_soal": "Pilihan Ganda",
                "cara_penyajian": "Satu per Satu",
                "tingkat_kesulitan": "Sedang",
                "adaptasi_kesulitan": "Tidak",
                "sistem_penilaian": "Langsung",
                "jumlah_soal_per_sesi": 10,
                "jumlah_sesi": 1,
                "total_soal": 10
            },
            "standar_2": {
                "tahap": 3,
                "kemampuan_diuji": "Penerapan",
                "sub_kemampuan": "Berpikir Konvergen",
                "jenis_soal": "Pilihan Ganda",
                "cara_penyajian": "Satu per Satu",
                "tingkat_kesulitan": "Sedang-Sulit",
                "adaptasi_kesulitan": "Tidak",
                "sistem_penilaian": "Langsung",
                "jumlah_soal_per_sesi": 15,
                "jumlah_sesi": 2,
                "total_soal": 30
            }
        }
    
    def get_config(self, jenis):
        return self.configs.get(jenis, {})
    
    def set_config(self, jenis, params):
        self.configs[jenis] = params
        self.active_config = params
        self.active_jenis = jenis
    
    def get_preset(self, nama):
        return self.presets.get(nama, {})
    
    def apply_preset(self, jenis, nama_preset):
        preset = self.get_preset(nama_preset)
        if preset:
            self.set_config(jenis, preset)
            return True
        return False
    
    def get_parameter_list(self):
        return [
            "Tahap Pembelajaran",
            "Kemampuan yang Diuji",
            "Sub-Kemampuan Berpikir",
            "Jenis Soal",
            "Cara Penyajian Soal",
            "Tingkat Kesulitan",
            "Adaptasi Kesulitan",
            "Sistem Penilaian",
            "Jumlah Soal per Sesi",
            "Jumlah Sesi",
            "Total Soal"
        ]
    
    def get_parameter_options(self, param):
        options = {
            "Tahap Pembelajaran": [str(i) for i in range(1, 10)],
            "Kemampuan yang Diuji": ["Hafalan", "Pemahaman", "Penerapan", "Analisis", "Evaluasi", "Penalaran", "Pemecahan Masalah", "HOTS", "Campuran"],
            "Sub-Kemampuan Berpikir": ["Berpikir Logis", "Berpikir Deduktif", "Berpikir Induktif", "Berpikir Analitis", "Berpikir Kritis", "Berpikir Evaluatif", "Berpikir Konvergen", "Berpikir Kreatif", "Berpikir Divergen", "Berpikir Lateral", "Berpikir Sistemik", "Berpikir Holistik", "Berpikir Probabilistik", "Berpikir Inferensial", "Pengambilan Keputusan", "Pemecahan Masalah", "Berpikir Strategis", "Penalaran Moral", "Berpikir Reflektif", "Metakognisi", "Berpikir Adaptif"],
            "Jenis Soal": ["Pilihan Ganda", "Esai", "Campuran"],
            "Cara Penyajian Soal": ["Satu per Satu", "Sekaligus"],
            "Tingkat Kesulitan": ["Mudah", "Mudah-Sedang", "Sedang", "Sedang-Sulit", "Sulit", "HOTS", "Mudah + HOTS", "Sedang + HOTS", "Sulit + HOTS", "Sesuai Tahap", "Adaptif"],
            "Adaptasi Kesulitan": ["Ya", "Tidak"],
            "Sistem Penilaian": ["Langsung", "Akhir Sesi"],
            "Jumlah Soal per Sesi": ["5", "10", "15", "20", "25", "30"],
            "Jumlah Sesi": ["1", "2", "3", "4", "5"],
        }
        return options.get(param, [])