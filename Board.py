from Location import Location
from Destination import Destination


class Board:

    def __init__(self):
        self.b = [[' ', ' ', 1, 1, 1, ' ', ' '], [' ', ' ', 1, 1, 1, ' ', ' '],
                  [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1], [' ', ' ', 1, 1, 1, ' ', ' '],
                  [' ', ' ', 1, 1, 1, ' ', ' ']]
        self.number_of_pegs = 32

    def not_in_board(self, loc: Location):
        if loc.x < 2 and loc.y < 2:
            return True
        elif loc.x > 4 and loc.y < 2:
            return True
        elif loc.x < 2 and loc.y > 4:
            return True
        elif loc.x > 4 and loc.y > 4:
            return True
        else:
            return False

    def is_full(self, x: int, y: int):
        if self.b[x][y] == 1:
            return True
        else:
            return False

    def set_board(self):
        self.b = [[' ', ' ', 1, 1, 1, ' ', ' '], [' ', ' ', 1, 1, 1, ' ', ' '],
                  [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1], [' ', ' ', 1, 1, 1, ' ', ' '],
                  [' ', ' ', 1, 1, 1, ' ', ' ']]

    def move_peg(self, my_loc: Location, des: Destination):
        if self.is_legal(my_loc, des):
            self.b[my_loc.x][my_loc.y] = 0
            self.b[des.x][des.y] = 1
            if des.is_left(my_loc):
                self.b[des.x + 1][des.y] = 0
            elif des.is_right(my_loc):
                self.b[des.x - 1][des.y] = 0
            elif des.is_up(my_loc):
                self.b[des.x][des.y + 1] = 0
            elif des.is_down(my_loc):
                self.b[des.x][des.y - 1] = 0
            self.show_board()
            self.decrement_number_of_pegs()
            if self.check_win():
                print('Game won!')
        else:
            print('Move not allowed')

    def is_legal(self, loc: Location, des: Destination):
        if des.x == loc.x and des.y == loc.y:
            print("Destination same as location")
            return False
        elif self.not_in_board(des):
            print("Destination not in board")
            return False
        elif self.is_full(des.x, des.y):
            print("Destination is full")
            return False
        elif des.is_left(loc) and self.is_full(des.x + 1, des.y):
            return True
        elif des.is_right(loc) and self.is_full(des.x - 1, des.y):
            return True
        elif des.is_up(loc) and self.is_full(des.x, des.y + 1):
            return True
        elif des.is_down(loc) and self.is_full(des.x, des.y - 1):
            return True
        else:
            return False

    def show_board(self):
        print("  0  1  2  3  4  5  6  X")
        for i in range(0, 7):
            print(i, end='')
            for j in range(0, 7):
                if self.b[j][i] == 1:
                    print(' . ', end='')
                elif self.b[j][i] == 0:
                    print(' o ', end='')
                else:
                    print('   ', end='')
            print('\t')
        print("Y")

    def check_win(self):
        return self.b == [[' ', ' ', 0, 0, 0, ' ', ' '],
                          [' ', ' ', 0, 0, 0, ' ', ' '],
                          [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0], [' ', ' ', 0, 0, 0, ' ', ' '],
                          [' ', ' ', 0, 0, 0, ' ', ' ']]

    def decrement_number_of_pegs(self):
        self.number_of_pegs = self.number_of_pegs - 1
        print(str(self.number_of_pegs) + " pegs left")
