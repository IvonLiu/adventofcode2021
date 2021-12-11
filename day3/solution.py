import argparse
from collections import defaultdict


def _bit_not(n, numbits=8):
    return (1 << numbits) - 1 - n


def _get_bits(input_path):
    counts = defaultdict(int)
    line_count = 0
    with open(input_path) as f:
        for line in f:
            line_count += 1
            for pos, c in enumerate(line.rstrip()):
                counts[pos] += int(c)

    gamma = 0
    print(counts, line_count)
    for pos, count in counts.items():
        gamma = (gamma << 1) | (count >= (line_count - count))

    numbits = len(counts)
    epsilon = _bit_not(
        gamma,
        numbits=numbits
    )
    return gamma, epsilon, numbits


def part1(input_path):
    gamma, epsilon, numbits = _get_bits(input_path)
    print(f"{gamma:0{numbits}b}")
    print(f"{epsilon:0{numbits}b}")
    print(gamma * epsilon) 


def _apply_bit_filter(nums, numbits, comp_fn):
    counts = [0, 0]
    for num in nums:
        leftmost = num >> (numbits - 1)
        counts[leftmost] += 1
    selected = 1 << (numbits - 1) if comp_fn(counts[1], counts[0]) else 0
    mask = _bit_not(0, numbits - 1)
    return selected, [
        num & mask for num in nums
        if num & (1 << numbits - 1) == selected
    ]

def _get_rating(nums, numbits, comp_fn):
    rating = 0
    while len(nums) > 1:
        selected, nums = _apply_bit_filter(nums, numbits, comp_fn)
        rating |= selected
        numbits -= 1
    rating |= nums[0]
    return rating


def part2(input_path):
    numbits = -1
    nums = []
    with open(input_path) as f:
        for line in f:
            line = line.rstrip()
            if numbits == -1:
                numbits = len(line)
            else:
                assert len(line) == numbits
            nums.append(int(line, 2))

    oxy_rating = _get_rating(nums, numbits, lambda x, y: x >= y)
    co2_rating = _get_rating(nums, numbits, lambda x, y: x < y)

    print(f"{oxy_rating:0{numbits}b}")
    print(f"{co2_rating:0{numbits}b}")
    print(oxy_rating * co2_rating) 
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-path", type=str, required=True)
    parser.add_argument("fn", type=str)
    args = parser.parse_args()
    globals()[args.fn](args.input_path)
