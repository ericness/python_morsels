from collections import defaultdict, OrderedDict
import csv
from typing import TextIO, Dict, List


def csv_columns(file: TextIO, headers: List[str] = None, missing: str = None) -> Dict:
    """Map column headers to lists of values"""
    values = defaultdict(list)
    csv_reader = csv.reader(file)
    for i, row in enumerate(csv_reader):
        if i == 0 and not headers:
            keys = row
        elif i == 0 and headers:
            keys = headers
            row.extend([missing] * (len(keys) - len(row)))
            for j, value in enumerate(row):
                values[j].append(value)
        else:
            row.extend([missing] * (len(keys) - len(row)))
            for j, value in enumerate(row):
                values[j].append(value)

    result = OrderedDict()

    for k, v in zip(keys, values.values()):
        result[k] = v
    return result
