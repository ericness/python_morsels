import argparse
from typing import List


def process_line(line: str) -> str:
    """Process a line in the CSV file"""
    elements = line.rstrip().split("|")
    quoted_elements = [f"\"{e}\"" if "," in e else e for e in elements]
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

    args = parser.parse_args()

    lines = read_file(args.input_csv)
    processed_lines = [process_line(line) for line in lines]
    write_file(processed_lines, args.output_csv)
