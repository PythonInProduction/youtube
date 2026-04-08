import re
import unicodedata


def clean_text(text: str) -> str:
    """Normalize text for dedup."""
    text = unicodedata.normalize("NFKC", text)
    text = text.casefold()
    text = re.sub(r"[^\w\s]", " ", text)  # replace punctuation
    text = re.sub(r"\s+", " ", text)  # collapse whitespace
    text = text.strip()
    return text
