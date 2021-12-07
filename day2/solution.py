import argparse

def part1(input_path):
    h_pos = 0
    depth = 0
    with open(input_path) as f:
        for line in f:
            direction, val = line.rstrip().split(" ")
            val = int(val)
            if direction == "forward":
                h_pos += val
            elif direction == "down":
                depth += val
            elif direction == "up":
                depth -= val
    print(h_pos * depth)

def part2(input_path):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-path", type=str, required=True)
    parser.add_argument("fn", type=str)
    args = parser.parse_args()
    globals()[args.fn](args.input_path)
