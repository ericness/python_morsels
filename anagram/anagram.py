import collections


def is_anagram(a: str, b: str) -> bool:
    """Determine if a and b are anagrams"""
    counter_a = collections.Counter(a.lower())
    counter_b = collections.Counter(b.lower())
    return counter_a == counter_b
