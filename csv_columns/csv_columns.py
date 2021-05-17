from collections import defaultdict
import csv
from typing import TextIO, Dict


def csv_columns(file: TextIO) -> Dict:
    """Map column headers to lists of values"""
    values = defaultdict(list)
    csv_reader = csv.reader(file)
    for i, row in enumerate(csv_reader):
        if i == 0:
            keys = row
        else:
            for j, value in enumerate(row):
                values[j].append(value)

    return {k: v for k, v in zip(keys, values.values())}
