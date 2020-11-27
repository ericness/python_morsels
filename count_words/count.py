from collections import Counter
import re
from typing import Dict


def count_words(text: str) -> Dict[str, int]:
    """Create map of words in text"""
    regex = r"\w(?:\S*\w)*"
    clean_words = re.findall(regex, text)
    words = [word.lower() for word in clean_words]
    return dict(Counter(words))
