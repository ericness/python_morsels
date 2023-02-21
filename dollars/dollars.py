import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("value")
    value = float(parser.parse_args().value)
    print(f"${value:.2f}")
