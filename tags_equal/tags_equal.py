from typing import Dict, Tuple


def process_tag(tag: str) -> Tuple[str, Dict[str, str]]:
    """Extract attributes and values from HTML tag.

    Args:
        tag (str): HTML tag with attributes

    Returns:
        Dict[str, str]: Dict of attribute name and value pairs
    """
    opening_tag: str = ""
    attributes: Dict[str, str] = {}

    for index, element in enumerate(map(str.lower, tag.split(" "))):
        if index == 0:
            opening_tag = element.lstrip("<")
        elif "=" in element:
            attribute, value = element.rstrip(">").split("=")
            attributes[attribute] = value
    
    return opening_tag, attributes
        


def tags_equal(tag1: str, tag2: str) -> bool:
    """Determine if the attributes of the two tags are equal.

    Args:
        tag1 (str): First HTML tag
        tag2 (str): Second HTML tag

    Returns:
        bool: Are tag attributes equal
    """
    return process_tag(tag1) == process_tag(tag2)
