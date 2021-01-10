import argparse
import re
from typing import List

DELIMITER_REGEX = r"[\w\s]+(([\W\S])[\w\s]+)+"


def determine_delimiter(lines: List[str]) -> str:
    """Determine the delimiter used in the data file"""
    result = re.fullmatch(DELIMITER_REGEX, lines[0])
    return "|"


def process_line(line: str, delimiter: str, quote: str) -> str:
    """Process a line in the CSV file"""
    elements = line.rstrip().split(delimiter)
    quoted_elements = [f"{quote}{e}{quote}" if delimiter in e else e for e in elements]
    return ",".join(quoted_elements)


def read_file(filename: str) -> List[str]:
    """Read in CSV file"""
    with open(filename) as f:
        return f.readlines()


def write_file(lines: List[str], filename: str):
    """Write new CSV file"""
    with open(filename, "w") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", type=str, help="Input CSV file")
    parser.add_argument("output_csv", type=str, help="Output CSV file")
    parser.add_argument("--in-delimiter", type=str)
    parser.add_argument("--in-quote", type=str, default="\"")

    args = parser.parse_args()

    lines = read_file(args.input_csv)

    if not args.in_delimiter:
        delimiter = determine_delimiter(lines)
    else:
        delimiter = args.in_delimiter

    processed_lines = [process_line(line, delimiter, args.in_quote) for line in lines]
    write_file(processed_lines, args.output_csv)
