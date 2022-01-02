import argparse
from typing import Dict, List, Set, Tuple

import attr


@attr.s
class Board:

    row_sets: List[Set[int]] = attr.ib()
    col_sets: List[Set[int]] = attr.ib()
    numbers: Dict[int, Tuple[int, int]] = attr.ib()
    won: bool = attr.ib(default=False)

    def draw(self, num: int) -> bool:
        if num not in self.numbers:
            return False

        row, col = self.numbers[num]
        self.row_sets[row].remove(num)
        self.col_sets[col].remove(num)
        if not self.row_sets[row] or not self.col_sets[col]:
            self.won = True
            return True

        return False


    def score(self, last: int) -> int:
        unmarked_sum = sum(
            (sum(row_set) for row_set in self.row_sets)
        )
        return unmarked_sum * last


    @classmethod
    def from_matrix(cls, mat: List[List[int]]) -> "Board":

        n = len(mat)
        row_sets = [set() for _ in range(n)]
        col_sets = [set() for _ in range(n)]
        numbers = {}

        for row in range(n):
            for col in range(n):
                num = mat[row][col]
                row_sets[row].add(num)
                col_sets[col].add(num)
                assert num not in numbers
                numbers[num] = (row, col)

        return cls(
            row_sets=row_sets,
            col_sets=col_sets,
            numbers=numbers,
        )


def _parse_input(input_path: str) -> Tuple[List[int], List[Board]]:

    boards = []

    with open(input_path) as f:
        drawn_numbers = next(f).rstrip()
        drawn_numbers = [int(n) for n in drawn_numbers.split(",")]

        mat = []

        for line in f:
            line = line.rstrip()

            if not line:
                if mat:
                    boards.append(Board.from_matrix(mat))
                mat = []
                continue
            
            mat.append(
                [int(n) for n in line.split(" ") if n]
            )

    return drawn_numbers, boards


def part1(input_path):
    drawn_numbers, boards = _parse_input(input_path)
    for num in drawn_numbers:
        for board in boards:
            if board.draw(num):
                print(board.score(last=num))
                return


def part2(input_path):
    drawn_numbers, boards = _parse_input(input_path)
    last_score = 0
    for num in drawn_numbers:
        for board in boards:
            if not board.won:
                if board.draw(num):
                    last_score = board.score(last=num)
    print(last_score)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-path", type=str, required=True)
    parser.add_argument("fn", type=str)
    args = parser.parse_args()
    globals()[args.fn](args.input_path)
