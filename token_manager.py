# ===== TOKEN MANAGER =====
# Mengelola saldo token pengguna

user_tokens = {}

# Paket token
PACKAGES = {
    "100": {"token": 100, "price": 10000, "label": "100 Token = Rp 10.000"},
    "200": {"token": 200, "price": 20000, "label": "200 Token = Rp 20.000"},
    "300": {"token": 300, "price": 30000, "label": "300 Token = Rp 30.000"},
    "400": {"token": 400, "price": 40000, "label": "400 Token = Rp 40.000"},
    "500": {"token": 500, "price": 45000, "label": "500 Token = Rp 45.000 (Hemat!)"},
}

def get_balance(user_id):
    return user_tokens.get(user_id, 0)

def add_tokens(user_id, amount):
    user_tokens[user_id] = user_tokens.get(user_id, 0) + amount
    return user_tokens[user_id]

def deduct_token(user_id, cost=1):
    if user_tokens.get(user_id, 0) >= cost:
        user_tokens[user_id] -= cost
        return True, cost
    return False, cost

def has_enough_tokens(user_id, cost=1):
    return user_tokens.get(user_id, 0) >= cost

def get_packages():
    return PACKAGES