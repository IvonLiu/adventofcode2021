import argparse
from collections import defaultdict


def part1(input_path):
    counts = defaultdict(int)
    line_count = 0
    with open(input_path) as f:
        for line in f:
            line_count += 1
            for pos, c in enumerate(line.rstrip()):
                counts[pos] += int(c)

    gamma = 0
    epsilon = 0
    for pos, count in counts.items():
        if count > line_count - count:
            gamma = (gamma << 1) | 1
            epsilon = epsilon << 1
        else:
            gamma = gamma << 1
            epsilon = (epsilon << 1) | 1

    print(f"{gamma:b}")
    print(f"{epsilon:b}")
    print(f"{gamma * epsilon}")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-path", type=str, required=True)
    parser.add_argument("fn", type=str)
    args = parser.parse_args()
    globals()[args.fn](args.input_path)