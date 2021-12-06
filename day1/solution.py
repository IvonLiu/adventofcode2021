import argparse
from collections import deque

def part1(input_path):
    increased_count = 0
    prev = None
    with open(input_path, "r") as f:
        for line in f:
            curr = int(line)
            if prev is not None:
                if curr > prev:
                    increased_count += 1
            prev = curr
    print(increased_count)


def part2(input_path):
    increased_count = 0
    queue = deque()
    with open(input_path, "r") as f:
        for line in f:
            curr = int(line)
            if len(queue) == 3:
                if curr > queue.popleft():
                    increased_count += 1
            queue.append(curr)
    print(increased_count)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-path", type=str, required=True)
    parser.add_argument("fn", type=str)
    args = parser.parse_args()
    globals()[args.fn](args.input_path)
