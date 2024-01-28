import re

def normalize_phone(phone_number):
    return re.sub(r"[\+]?[3]?[8]?[0]", r"+380", re.sub(r"[^0-9]", r"", phone_number), 1)