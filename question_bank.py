# ===== QUESTION BANK =====
# Mengelola bank soal

class QuestionBank:
    def __init__(self):
        self.questions = []
        self.used_questions = []
        self.current_questions = []
    
    def add_question(self, question):
        self.questions.append(question)
    
    def get_questions(self, topic, sub_topic, tahap, difficulty, count=10):
        filtered = []
        for q in self.questions:
            if (q.get("topic") == topic and 
                q.get("sub_topic") == sub_topic and
                q.get("tahap") == tahap and
                q.get("difficulty") == difficulty and
                q not in self.used_questions):
                filtered.append(q)
        return filtered[:count]
    
    def select_questions(self, topic, sub_topic, tahap, difficulty, count=10):
        selected = self.get_questions(topic, sub_topic, tahap, difficulty, count)
        if len(selected) < count:
            expanded = self.get_questions(topic, sub_topic, tahap, None, count)
            if len(expanded) >= count:
                selected = expanded[:count]
        
        for q in selected:
            self.used_questions.append(q)
            if q in self.questions:
                self.questions.remove(q)
        
        self.current_questions = selected
        return selected
    
    def get_current_question(self, index):
        if 0 <= index < len(self.current_questions):
            return self.current_questions[index]
        return None
    
    def get_current_questions(self):
        return self.current_questions
    
    def format_question(self, question, session_num, question_num, total):
        status = question.get("status", "MANDIRI")
        kisi = question.get("kisi_kisi", "-")
        
        formatted = f"""Sesi {session_num} - {question_num}/{total}
Status : {status}
Kisi-kisi : {kisi}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{question.get('text', '')}

A. {question.get('options', {}).get('A', '')}

B. {question.get('options', {}).get('B', '')}

C. {question.get('options', {}).get('C', '')}

D. {question.get('options', {}).get('D', '')}

E. {question.get('options', {}).get('E', '')}

Materi : {question.get('materi', '-')}
Sumber : {question.get('sumber', '-')}
Link : {question.get('link', '-')}"""
        return formatted