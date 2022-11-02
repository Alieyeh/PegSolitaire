from Location import Location
from Destination import Destination
import Constants as Cons
import pygame


class Board:

    def __init__(self):
        self.b = [[' ', ' ', 1, 1, 1, ' ', ' '], [' ', ' ', 1, 1, 1, ' ', ' '],
                  [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1], [' ', ' ', 1, 1, 1, ' ', ' '],
                  [' ', ' ', 1, 1, 1, ' ', ' ']]
        self.number_of_pegs = 32
        self.error_message = ''
        self.my_font = pygame.font.SysFont('Times New Roman', 25)

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

    def move_peg(self, my_loc: Location, des: Destination, win, load_btn, restart_btn):
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
            self.draw_board(win, load_btn, restart_btn)
            if self.check_win():
                text_surface = self.my_font.render('Game Won!', False, Cons.WHITE)
                win.blit(text_surface, (Cons.XMARGIN, 0))
                pygame.display.flip()
                print('Game won!')
        else:
            self.draw_board(win, load_btn, restart_btn)
            text_surface = self.my_font.render('Move not allowed ' +
                                               self.error_message, False, Cons.ORANGE)
            win.blit(text_surface, (Cons.XMARGIN, Cons.YMARGIN // 2))
            pygame.display.flip()
            print('Move not allowed')
            self.error_message = ''

    def is_legal(self, loc: Location, des: Destination):
        if des.x == loc.x and des.y == loc.y:
            self.error_message = "Destination same as location"
            print("Destination same as location")
            return False
        elif self.not_in_board(des):
            self.error_message = "Destination not in board"
            print("Destination not in board")
            return False
        elif self.is_full(des.x, des.y):
            self.error_message = "Destination is full"
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

    def calculate_board_pos(self, row, col):
        peg_x = row * Cons.SQUARESIZE + Cons.XMARGIN + Cons.RADIUS + 2
        peg_y = col * Cons.SQUARESIZE + Cons.YMARGIN + Cons.RADIUS + 2

        return peg_x, peg_y

    def calculate_array_pos(self, x, y):
        for row in range(Cons.ROWS):
            for col in range(Cons.COLUMNS):
                if self.b[row][col] != ' ':
                    x_marg = (row * Cons.SQUARESIZE) + Cons.XMARGIN
                    y_marg = (col * Cons.SQUARESIZE) + Cons.YMARGIN
                    if (x_marg <= x < x_marg + Cons.SQUARESIZE and
                            y_marg <= y < y_marg + Cons.SQUARESIZE):
                        return row, col
        return 0, 0

    def is_peg(self, loc: Location):
        if self.b[loc.x][loc.y] == 1:
            return True
        else:
            return False

    def draw_empty_board(self, win):
        win.fill(Cons.BLACK)
        for row in range(Cons.ROWS):
            for col in range(row % 2, Cons.ROWS, 2):
                if self.b[row][col] != ' ':
                    pygame.draw.rect(win, Cons.GREEN, (
                        (row * Cons.SQUARESIZE) + Cons.XMARGIN,
                        (col * Cons.SQUARESIZE) + Cons.YMARGIN,
                        Cons.SQUARESIZE, Cons.SQUARESIZE))

    def draw_pegs(self, win):
        for row in range(Cons.ROWS):
            for col in range(Cons.COLUMNS):
                if self.b[col][row] == 1:
                    pygame.draw.circle(win, Cons.PURPLE, (self.calculate_board_pos(col, row)),
                                       Cons.RADIUS)

    def draw_board(self, win, load_btn, restart_btn):
        self.draw_empty_board(win)
        self.draw_pegs(win)
        self.show_number_of_pegs(win)
        load_btn.draw(win)
        restart_btn.draw(win)
        pygame.display.update()

    def show_board(self):
        print("  0  1  2  3  4  5  6  X")
        for row in range(Cons.ROWS):
            print(row, end='')
            for col in range(Cons.COLUMNS):
                if self.b[col][row] == 1:
                    print(' . ', end='')
                elif self.b[col][row] == 0:
                    print(' o ', end='')
                else:
                    print('   ', end='')
            print('\t')
        print("Y")

    def check_win(self):
        if self.number_of_pegs == 1 and self.b[3][3] == 1:
            return True
        else:
            return False

    def show_number_of_pegs(self, win):
        text_surface = self.my_font.render(str(self.number_of_pegs)
                                           + " pegs left", False, Cons.BLUE)
        win.blit(text_surface, (Cons.XMARGIN // 2, Cons.HEIGHT - Cons.YMARGIN))

    def decrement_number_of_pegs(self):
        self.number_of_pegs = self.number_of_pegs - 1
        print(str(self.number_of_pegs) + " pegs left")
