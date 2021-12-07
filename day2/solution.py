import argparse

def _process_lines(input_path):
    with open(input_path) as f:
        for line in f:
            direction, val = line.rstrip().split(" ")
            val = int(val)
            yield direction, val

def part1(input_path):
    h_pos = 0
    depth = 0
    for direction, val in _process_lines(input_path):
        if direction == "forward":
            h_pos += val
        elif direction == "down":
            depth += val
        elif direction == "up":
            depth -= val
    print(h_pos * depth)


def part2(input_path):
    h_pos = 0
    depth = 0
    aim = 0
    for direction, val in _process_lines(input_path):
        if direction == "forward":
            h_pos += val
            depth += val * aim
        elif direction == "down":
            aim += val
        elif direction == "up":
            aim -= val
    print(h_pos * depth)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-path", type=str, required=True)
    parser.add_argument("fn", type=str)
    args = parser.parse_args()
    globals()[args.fn](args.input_path)
