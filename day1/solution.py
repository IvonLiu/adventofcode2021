import argparse

def part1(input_path):
    increased_count = 0
    prev = None
    with open (input_path, "r") as f:
        for line in f:
            curr = int(line)
            if prev is not None:
                if curr > prev:
                    increased_count += 1
            prev = curr
    print(increased_count)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-path", type=str, required=True)
    args = parser.parse_args()
    part1(args.input_path)
