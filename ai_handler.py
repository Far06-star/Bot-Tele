# ===== AI HANDLER =====

import os
import logging
import google.generativeai as genai
from groq import Groq
import openai

logger = logging.getLogger(__name__)

# ===== KUOTA HARIAN =====
DAILY_QUOTA = {
    "gemini": 1500,
    "groq": 14400,
    "openrouter": 50
}

usage_counter = {
    "gemini": 0,
    "groq": 0,
    "openrouter": 0
}

# ===== SETUP AI =====
def setup_ai():
    GEMINI_API_KEY = "AQ.Ab8RN6IPsKF27K9lxNhxCRq3lmhhUgKMA3u3bjageX_OpJZLfQ"
    GROQ_API_KEY = "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"
    OPENROUTER_API_KEY = "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"
    
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel('gemini-pro')
    groq_client = Groq(api_key=GROQ_API_KEY)
    openrouter_client = openai.OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY
    )
    
    return gemini_model, groq_client, openrouter_client

gemini_model, groq_client, openrouter_client = setup_ai()

# ===== FUNGSI PANGGIL AI =====
async def ask_ai(prompt, provider="gemini", topic="umum"):
    system_prompt = f"Kamu adalah guru {topic}. Jawab dengan jelas dan ramah."
    
    try:
        if provider == "gemini":
            full = f"{system_prompt}\n\nPertanyaan: {prompt}"
            response = gemini_model.generate_content(full)
            return response.text
        elif provider == "groq":
            response = groq_client.chat.completions.create(
                model="mixtral-8x7b-32768",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        elif provider == "openrouter":
            response = openrouter_client.chat.completions.create(
                model="meta-llama/llama-3-8b-instruct:free",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        else:
            return "❌ Provider tidak dikenal."
    except Exception as e:
        logger.error(f"AI Error: {e}")
        return "⚠️ Maaf, saya sedang tidak bisa menjawab. Coba lagi nanti."

# ===== CEK KUOTA =====
def check_quota(provider):
    if provider == "gemini" and usage_counter["gemini"] >= DAILY_QUOTA["gemini"]:
        return False, "Gemini"
    elif provider == "groq" and usage_counter["groq"] >= DAILY_QUOTA["groq"]:
        return False, "Groq"
    elif provider == "openrouter" and usage_counter["openrouter"] >= DAILY_QUOTA["openrouter"]:
        return False, "OpenRouter"
    return True, None

def get_available_provider():
    if usage_counter["gemini"] < DAILY_QUOTA["gemini"]:
        return "gemini"
    elif usage_counter["groq"] < DAILY_QUOTA["groq"]:
        return "groq"
    elif usage_counter["openrouter"] < DAILY_QUOTA["openrouter"]:
        return "openrouter"
    return None

# ===== AHLI 1 =====
async def ahli_1(prompt, topic="umum"):
    provider = get_available_provider()
    if provider is None:
        return "⚠️ Maaf, semua asisten sedang sibuk. Coba besok."
    
    response = await ask_ai(prompt, provider, topic)
    usage_counter[provider] += 1
    return response

# ===== AHLI 2 =====
async def ahli_2(prompt, topic="umum"):
    if usage_counter["gemini"] < DAILY_QUOTA["gemini"]:
        response = await ask_ai(prompt, "gemini", topic)
        usage_counter["gemini"] += 1
        return response
    elif usage_counter["groq"] < DAILY_QUOTA["groq"]:
        response = await ask_ai(prompt, "groq", topic)
        usage_counter["groq"] += 1
        return response
    else:
        return "⚠️ Maaf, asisten sedang sibuk. Coba besok."

# ===== AHLI 3 =====
async def ahli_3(prompt, topic="umum"):
    if usage_counter["groq"] < DAILY_QUOTA["groq"]:
        response = await ask_ai(prompt, "groq", topic)
        usage_counter["groq"] += 1
        return response
    elif usage_counter["gemini"] < DAILY_QUOTA["gemini"]:
        response = await ask_ai(prompt, "gemini", topic)
        usage_counter["gemini"] += 1
        return response
    else:
        return "⚠️ Maaf, asisten sedang sibuk. Coba besok."

# ===== AHLI 4 =====
async def ahli_4(prompt, topic="umum", siklus_ke=0):
    if siklus_ke < 30:
        if usage_counter["gemini"] < DAILY_QUOTA["gemini"]:
            response = await ask_ai(prompt, "gemini", topic)
            usage_counter["gemini"] += 1
            return response
        else:
            if usage_counter["groq"] < DAILY_QUOTA["groq"]:
                response = await ask_ai(prompt, "groq", topic)
                usage_counter["groq"] += 1
                return response
    else:
        if usage_counter["groq"] < DAILY_QUOTA["groq"]:
            response = await ask_ai(prompt, "groq", topic)
            usage_counter["groq"] += 1
            return response
    
    return "⚠️ Maaf, asisten sedang sibuk. Coba besok."

# ===== AHLI 5 =====
async def ahli_5(prompt, topic="umum"):
    if usage_counter["groq"] < DAILY_QUOTA["groq"]:
        response = await ask_ai(prompt, "groq", topic)
        usage_counter["groq"] += 1
        return response
    else:
        return "⚠️ Maaf, asisten sedang sibuk. Coba besok."

# ===== AHLI 6 =====
async def ahli_6(prompt, topic="umum"):
    if usage_counter["openrouter"] < DAILY_QUOTA["openrouter"]:
        response = await ask_ai(prompt, "openrouter", topic)
        usage_counter["openrouter"] += 1
        return response
    else:
        return "⚠️ Maaf, semua asisten sedang sibuk. Coba besok."

# ===== GET AHLI FUNCTION =====
def get_ahli_function(ahli_id):
    ahli_map = {
        "ahli_1": ahli_1,
        "ahli_2": ahli_2,
        "ahli_3": ahli_3,
        "ahli_4": ahli_4,
        "ahli_5": ahli_5,
        "ahli_6": ahli_6
    }
    return ahli_map.get(ahli_id, ahli_1)