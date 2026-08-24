# ===== ASSESSMENT =====
# Logika 3 metode asesmen

class AssessmentManager:
    def __init__(self, session_manager, question_bank):
        self.session_manager = session_manager
        self.question_bank = question_bank
        self.metode = None
        self.assessment_data = {}
    
    def set_metode(self, metode):
        if metode in ["berbasis_materi", "pola_terpadu", "berbasis_evaluasi"]:
            self.metode = metode
            return True
        return False
    
    def get_metode(self):
        return self.metode
    
    def get_metode_label(self):
        labels = {
            "berbasis_materi": "Asesmen Berbasis Materi",
            "pola_terpadu": "Asesmen Pola Terpadu",
            "berbasis_evaluasi": "Asesmen Berbasis Evaluasi"
        }
        return labels.get(self.metode, "Tidak Diketahui")
    
    def start_session(self, user_id, jenis, config, kategori_data, ahli):
        session_id = self.session_manager.create_session(user_id, jenis, config, kategori_data, ahli)
        session = self.session_manager.get_session(session_id)
        
        topic = kategori_data.get("Topik", "Umum")
        sub_topic = kategori_data.get("Sub-Topik", "Umum")
        tahap = config.get("tahap", 1)
        difficulty = config.get("tingkat_kesulitan", "Sedang")
        count = config.get("total_soal", 10)
        
        questions = self.question_bank.select_questions(topic, sub_topic, tahap, difficulty, count)
        session["questions"] = questions
        session["topic"] = topic
        session["sub_topic"] = sub_topic
        
        return session_id, questions
    
    def process_answer(self, session_id, soal_index, jawaban, waktu):
        session = self.session_manager.get_session(session_id)
        if not session:
            return None
        
        questions = session.get("questions", [])
        if soal_index >= len(questions):
            return None
        
        question = questions[soal_index]
        correct = question.get("correct_answer", "")
        benar = jawaban.upper() == correct
        
        self.session_manager.record_answer(session_id, soal_index, jawaban, benar, waktu)
        
        result = {
            "benar": benar,
            "jawaban_benar": correct,
            "jawaban_user": jawaban
        }
        
        if self.metode == "berbasis_materi":
            result["pembahasan"] = question.get("pembahasan", "")
            result["materi"] = question.get("materi_detail", "")
            result["alasan_salah"] = question.get("alasan_salah", {})
        elif self.metode == "pola_terpadu":
            result["pembahasan"] = question.get("pembahasan", "")
            result["materi"] = question.get("materi_singkat", "")
        else:
            result["pembahasan"] = question.get("pembahasan", "")
        
        return result
    
    def get_final_evaluation(self, session_id):
        session = self.session_manager.get_session(session_id)
        if not session:
            return None
        
        score_data = self.session_manager.calculate_score(session_id)
        questions = session.get("questions", [])
        
        konsep_kuasai = []
        konsep_lemah = []
        
        for i, q in enumerate(questions):
            if i in session.get("jawaban", {}):
                jawaban = session["jawaban"][i]
                if jawaban.get("benar"):
                    konsep_kuasai.append(q.get("konsep", f"Soal {i+1}"))
                else:
                    konsep_lemah.append(q.get("konsep", f"Soal {i+1}"))
        
        return {
            "benar": score_data.get("benar", 0),
            "salah": score_data.get("salah", 0),
            "tidak_dijawab": score_data.get("tidak_dijawab", 0),
            "jumlah_soal": score_data.get("total", 0),
            "nilai": score_data.get("nilai", 0),
            "poin_penguasaan": score_data.get("poin_penguasaan", 0),
            "waktu": score_data.get("waktu", 0),
            "konsep_kuasai": list(set(konsep_kuasai)) if konsep_kuasai else ["-"],
            "konsep_lemah": list(set(konsep_lemah)) if konsep_lemah else ["-"],
            "metode": self.get_metode_label()
        }