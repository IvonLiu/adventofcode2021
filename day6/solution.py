import argparse
from typing import List


def _parse_input(input_path) -> List[int]:
    with open(input_path) as f:
        line = next(f).rstrip()
        return [int(n) for n in line.split(",")]


def _solve(input_path, num_days):
    counts = [0] * 9
    for n in _parse_input(input_path):
        counts[n] += 1

    for _ in range(num_days):
        new_fish = counts[0]
        for group in range(8):
            counts[group] = counts[group + 1]
        counts[8] = new_fish
        counts[6] += new_fish

    print(sum(counts))


def part1(input_path):
    _solve(input_path, num_days=80)


def part2(input_path):
    _solve(input_path, num_days=256)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-path", type=str, required=True)
    parser.add_argument("fn", type=str)
    args = parser.parse_args()
    globals()[args.fn](args.input_path)
