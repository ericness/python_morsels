import argparse
import csv
from typing import List, Tuple


def determine_delimiter(lines: List[str]) -> Tuple[str, str]:
    """Determine the delimiter used in the data file"""
    dialect = csv.Sniffer().sniff("\n".join(lines[: max(len(lines), 5)]))
    return str(dialect.delimiter), str(dialect.quotechar)


def process_line(line: str, delimiter: str, quote: str) -> str:
    """Process a line in the CSV file"""
    elements = line.rstrip().split(delimiter)
    quoted_elements = [
        f'"{e}"' if delimiter in e else e for e in elements
    ]
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
    parser.add_argument("--in-quote", type=str)

    args = parser.parse_args()

    lines = read_file(args.input_csv)

    delimiter, quote = determine_delimiter(lines)
    delimiter = args.in_delimiter if args.in_delimiter else delimiter
    quote = args.in_quote if args.in_quote else quote

    processed_lines = [process_line(line, delimiter, quote) for line in lines]
    write_file(processed_lines, args.output_csv)
