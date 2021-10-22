import re
from typing import IO, List, Tuple

DATE_REGEX = r"^\d\d\d\d-\d\d-\d\d$"

HTML_REPLACEMENTS = {
    "&nbsp;": " ",
    "&quot;": "\"",
    "&amp;": "&",
}

def replace_html(string: str) -> str:
    result = string
    for code, sub in HTML_REPLACEMENTS.items():
        result = result.replace(code, sub)
    return result


def entries_by_date(diary_file: IO) -> List[Tuple]:
    """Break diary into entries"""
    entries = []
    current_entry = []
    for line in map(replace_html, map(str.strip, diary_file.readlines())):
        if re.match(DATE_REGEX, line):
            if current_entry:
                entries.append((current_entry[0], "\n\n".join(current_entry[1:])))
                current_entry = []
        if line:
            current_entry.append(line)
    
    entries.append((current_entry[0], "\n\n".join(current_entry[1:])))
    return entries
