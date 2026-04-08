import re

def extract_nit(text: str):
    match = re.search(r"\b\d{9,10}\b", text)
    return match.group(0) if match else None