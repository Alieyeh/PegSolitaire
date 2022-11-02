from Board import Board


class Solver:

    def __init__(self):
        self.count = 0

    def solve_dfs(self, board: Board, moves: list):
        if board.check_win():
            return moves


