import re


def clean_text(text: str) -> str:
    """Normalize text for dedup."""
    text = text.strip()
    text = text.casefold()
    text = re.sub(r"\s+", " ", text)  # collapse whitespace
    text = re.sub(r"[^\w\s]", " ", text)  # replace punctuation
    return text
