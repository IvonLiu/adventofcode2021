import argparse


def _parse_input(input_path, ignore_diagonal=True):
    with open(input_path) as f:
        for line in f:
            line = line.rstrip()
            points = line.split(" -> ")
            start = [int(n) for n in points[0].split(",")]
            end = [int(n) for n in points[1].split(",")]
            if not ignore_diagonal or (
                start[0] == end[0] or start[1] == end[1]
            ):
                yield (start, end)


def _sign(n):
    assert n != 0
    return n / abs(n)


def part1(input_path):
    points = set()
    danger = set()
    lines = _parse_input(input_path)

    def check(x, y):
        if (x, y) in danger:
            return
        if (x, y) in points:
            danger.add((x, y))
        else:
            points.add((x, y))

    for start, end in lines:
        if start[0] == end[0]:
            d = (0, _sign(end[1] - start[1]))
        elif start[1] == end[1]:
            d = (_sign(end[0] - start[0]), 0)
        else:
            raise ValueError(f"({start}, {end}) is a diagonal")

        x, y = start
        while x != end[0] or y != end[1]:
            check(x, y)
            x += d[0]
            y += d[1]
        check(*end)

    print(len(danger))


def part2(input_path):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-path", type=str, required=True)
    parser.add_argument("fn", type=str)
    args = parser.parse_args()
    globals()[args.fn](args.input_path)
