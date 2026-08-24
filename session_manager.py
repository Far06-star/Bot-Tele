# ===== SESSION MANAGER =====
# Mengelola sesi dan progres

class SessionManager:
    def __init__(self):
        self.sessions = {}
        self.current_session = None
        self.progress = {}
    
    def create_session(self, user_id, jenis, config, kategori_data, ahli):
        session_id = f"{user_id}_{jenis}_{len(self.sessions)}"
        self.sessions[session_id] = {
            "user_id": user_id,
            "jenis": jenis,
            "config": config,
            "kategori_data": kategori_data,
            "ahli": ahli,
            "status": "active",
            "current_soal": 0,
            "soal_terjawab": [],
            "jawaban": {},
            "benar": 0,
            "salah": 0,
            "tidak_dijawab": 0,
            "waktu_mulai": None,
            "waktu_selesai": None,
            "total_soal": config.get("total_soal", 10),
            "sesi_ke": 1,
            "total_sesi": config.get("jumlah_sesi", 1),
            "questions": []
        }
        self.current_session = session_id
        return session_id
    
    def get_session(self, session_id):
        return self.sessions.get(session_id)
    
    def get_current_session(self):
        if self.current_session:
            return self.sessions.get(self.current_session)
        return None
    
    def update_progress(self, session_id, data):
        if session_id in self.sessions:
            self.sessions[session_id].update(data)
    
    def record_answer(self, session_id, soal_index, jawaban, benar, waktu):
        session = self.get_session(session_id)
        if not session:
            return False
        
        session["jawaban"][soal_index] = {
            "jawaban": jawaban,
            "benar": benar,
            "waktu": waktu
        }
        
        if jawaban == "Tidak Dijawab":
            session["tidak_dijawab"] += 1
        elif benar:
            session["benar"] += 1
        else:
            session["salah"] += 1
        
        session["soal_terjawab"].append(soal_index)
        session["current_soal"] = soal_index + 1
        
        return True
    
    def calculate_score(self, session_id):
        session = self.get_session(session_id)
        if not session:
            return None
        
        total = session.get("total_soal", 10)
        benar = session.get("benar", 0)
        poin = round((benar / total) * 100) if total > 0 else 0
        
        return {
            "benar": benar,
            "salah": session.get("salah", 0),
            "tidak_dijawab": session.get("tidak_dijawab", 0),
            "total": total,
            "nilai": poin,
            "poin_penguasaan": poin,
            "waktu": session.get("waktu_selesai") - session.get("waktu_mulai") if session.get("waktu_mulai") else None
        }
    
    def get_checkpoint_data(self, session_id):
        session = self.get_session(session_id)
        if not session:
            return None
        
        return {
            "jenis": session.get("jenis"),
            "sesi": session.get("sesi_ke"),
            "soal": session.get("current_soal"),
            "total_soal": session.get("total_soal"),
            "total_sesi": session.get("total_sesi"),
            "soal_terjawab": session.get("soal_terjawab"),
            "nilai": session.get("benar"),
            "penguasaan": round((session.get("benar", 0) / session.get("total_soal", 1)) * 100, 1)
        }