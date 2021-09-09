import collections
import re
import unicodedata

LETTER_REGEX = r"[a-z]"


def build_counter(val: str) -> collections.Counter:
    """Build a counter from a string"""
    ascii_val = unicodedata.normalize("NFKD", val)
    clean_val = re.findall(LETTER_REGEX, ascii_val.lower())
    return collections.Counter(clean_val)


def is_anagram(a: str, b: str) -> bool:
    """Determine if a and b are anagrams"""
    counter_a = build_counter(a)
    counter_b = build_counter(b)
    return counter_a == counter_b
