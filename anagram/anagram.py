import collections
import re

LETTER_REGEX = r"[a-z]"


def build_counter(val: str) -> collections.Counter:
    """Build a counter from a string"""
    clean_val = re.findall(LETTER_REGEX, val.lower())
    return collections.Counter(clean_val)


def is_anagram(a: str, b: str) -> bool:
    """Determine if a and b are anagrams"""
    counter_a = build_counter(a)
    counter_b = build_counter(b)
    return counter_a == counter_b
