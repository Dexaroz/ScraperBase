import re
import unicodedata

def clean_text(text):
    return re.sub(r'\s+', ' ', text)

def remove_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')