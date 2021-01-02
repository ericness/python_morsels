import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", type=str, help="Input CSV file")
    parser.add_argument("output_csv", type=str, help="Output CSV file")

    args = parser.parse_args()

    print(args.input_csv)
    print(args.output_csv)
