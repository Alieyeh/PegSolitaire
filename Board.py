from Location import Location
from Destination import Destination
import Constants as Cons
import pygame


class Board:
    """
    Board class keeps and draws the board state and checks the
    legality of moves.
    """
    def __init__(self):
        """
        Initialises the Board class by assigning values to board
        (start position), number of pegs, error message, and font.
        """
        self.b = [[' ', ' ', 1, 1, 1, ' ', ' '],
                  [' ', ' ', 1, 1, 1, ' ', ' '],
                  [1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 0, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1],
                  [' ', ' ', 1, 1, 1, ' ', ' '],
                  [' ', ' ', 1, 1, 1, ' ', ' ']]
        self.number_of_pegs = 32
        self.error_message = ''
        self.my_font = pygame.font.SysFont('Times New Roman', 25)

    def not_in_board(self, loc: Location):
        """
        Checks to see if the location of the chosen peg is on
        the board or not.

        Params:
        ------

        loc: Location, mandatory.
            The location of the chosen peg on the board.

        Returns:
        --------
        Boolean
        """
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
        """
        Checks to see if the peg destination is full or not.

        Params:
        ------

        x: integer, mandatory.
            X coordinate of peg on board.

        y: integer, mandatory.
            Y coordinate of peg on board.

        Returns:
        --------
        Boolean
        """
        if self.b[x][y] == 1:
            return True
        else:
            return False

    def set_board(self):
        """
        Changes the state of the board to the beginning state.
        """
        self.b = [[' ', ' ', 1, 1, 1, ' ', ' '],
                  [' ', ' ', 1, 1, 1, ' ', ' '],
                  [1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 0, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1],
                  [' ', ' ', 1, 1, 1, ' ', ' '],
                  [' ', ' ', 1, 1, 1, ' ', ' ']]

    def move_peg(self, loc: Location, des: Destination,
                 win, load_btn, restart_btn):
        """
        Checks to see if the move made is legal or not.
        Sets additional error message in the case of
        certain transgressions.

        Params:
        ------

        loc: Location, mandatory.
            Location of the chosen peg on the board.

        des: Destination, mandatory.
            The destination of the chosen peg on the board.

        win: pygame.display, mandatory
            The main window (screen) of the game.

        load_btn: Button, mandatory.
            The load button, used for loading a solution file.

        restart_btn: Button, mandatory.
            The restart button, used for restarting the game.

        """
        # moving peg and removing the one in the middle if move is legal
        if self.is_legal(loc, des):
            self.b[loc.x][loc.y] = 0
            self.b[des.x][des.y] = 1
            if des.is_left(loc):
                self.b[des.x + 1][des.y] = 0
            elif des.is_right(loc):
                self.b[des.x - 1][des.y] = 0
            elif des.is_up(loc):
                self.b[des.x][des.y + 1] = 0
            elif des.is_down(loc):
                self.b[des.x][des.y - 1] = 0

            # Drawing board and decrementing number of pegs left
            self.show_board()
            self.decrement_number_of_pegs()
            self.draw_board(win, load_btn, restart_btn)

            # Checking win condition and showing message if won
            if self.check_win():
                text_surface = self.my_font.render('Game Won!',
                                                   False, Cons.WHITE)
                win.blit(text_surface, (Cons.X_MARGIN, Cons.Y_MARGIN // 2))
                pygame.display.flip()
                print('Game won!✴︎')
        else:

            # Writing error message if move is not legal
            self.draw_board(win, load_btn, restart_btn)
            text_surface = self.my_font.render(self.error_message,
                                               False, Cons.ORANGE)
            win.blit(text_surface, (Cons.X_MARGIN // 2, Cons.Y_MARGIN // 2))
            pygame.display.flip()
            print('Move not allowed')
            self.error_message = ''

    def is_legal(self, loc: Location, des: Destination):
        """
        Checks to see if the move made is legal or not.
        Sets additional error message in the case of
        certain transgressions.

        Params:
        ------

        loc: Location, mandatory.
            Location of the chosen peg on the board.

        des: Destination, mandatory.
            The destination of the chosen peg on the board.

        Returns:
        --------
        Boolean
        """
        if des.x == loc.x and des.y == loc.y:
            self.error_message = "Peg unselected"
            print("Peg unselected")
            return False
        elif self.not_in_board(des):
            self.error_message = "Move not allowed, Destination not in board"
            print("Move not allowed, Destination not in board")
            return False
        elif not self.is_peg(loc):
            self.error_message = "peg location empty"
            print("peg location empty")
            return False
        elif self.is_full(des.x, des.y):
            self.error_message = "Move not allowed, Destination is full"
            print("Move not allowed, Destination is full")
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
            self.error_message = "Move not allowed"
            return False

    def calculate_screen_pos(self, row: int, col: int):
        """
        Calculates the chosen position on the screen based on
        board coordinates.

        Params:
        ------

        row: Integer, mandatory.
            X coordinate of the board for the chosen position.

        col: Integer, mandatory.
            Y coordinate of the board for the chosen position.

        Returns:
        --------
        Integer
        """
        peg_x = row * Cons.SQUARE_SIZE + Cons.X_MARGIN + Cons.RADIUS + 2
        peg_y = col * Cons.SQUARE_SIZE + Cons.Y_MARGIN + Cons.RADIUS + 2

        return peg_x, peg_y

    def calculate_board_pos(self, x: int, y: int):
        """
        Calculates the chosen position on the board based on
        screen coordinates. Return 0,0 if coordinates are not
        on the board.

        Params:
        ------

        x: Integer, mandatory.
            X coordinate of the screen at chosen position.

        y: Integer, mandatory.
            Y coordinate of the screen at chosen position.

        Returns:
        --------
        Integer
        """
        for row in range(Cons.ROWS):
            for col in range(Cons.COLUMNS):
                if self.b[row][col] != ' ':
                    x_marg = (row * Cons.SQUARE_SIZE) + Cons.X_MARGIN
                    y_marg = (col * Cons.SQUARE_SIZE) + Cons.Y_MARGIN
                    if (x_marg <= x < x_marg + Cons.SQUARE_SIZE and
                            y_marg <= y < y_marg + Cons.SQUARE_SIZE):
                        return row, col
        return 0, 0

    def is_peg(self, loc: Location):
        """
        Checks if the chosen location has a peg in it.

        Params:
        ------

        loc: Location, mandatory.
            The location of the chosen peg on the board.

        Returns:
        --------
        Boolean
        """
        if self.b[loc.x][loc.y] == 1:
            return True
        else:
            return False

    def draw_empty_board(self, win: pygame.display):
        """
        Draws the board without the pegs.

        Params:
        ------

        win: pygame.display, mandatory.
            The main window (screen) of the game.
        """
        win.fill(Cons.BLACK)
        for row in range(Cons.ROWS):
            for col in range(row % 2, Cons.ROWS, 2):
                if self.b[row][col] != ' ':
                    pygame.draw.rect(win, Cons.GREEN, (
                        (row * Cons.SQUARE_SIZE) + Cons.X_MARGIN,
                        (col * Cons.SQUARE_SIZE) + Cons.Y_MARGIN,
                        Cons.SQUARE_SIZE, Cons.SQUARE_SIZE))

    def draw_pegs(self, win: pygame.display):
        """
        Draws the pegs to the screen but doesnt update screen.

        Params:
        ------

        win: pygame.display, mandatory.
            The location of the chosen peg on the board.
        """
        for row in range(Cons.ROWS):
            for col in range(Cons.COLUMNS):
                if self.b[col][row] == 1:
                    pygame.draw.circle(win, Cons.PURPLE,
                                       (self.calculate_screen_pos(col, row)),
                                       Cons.RADIUS)

    def draw_board(self, win: pygame.display, load_btn, restart_btn):
        """
        Draws the current board state along with buttons and
        the number of pegs on to the screen and updates screen.

        Params:
        ------

        win: pygame.display, mandatory.
            The location of the chosen peg on the board.

        load_btn: Button, mandatory.
            The load button, used for loading a solution file.

        restart_btn: Button, mandatory.
            The restart button, used for restarting the game.
        """
        self.draw_empty_board(win)
        self.draw_pegs(win)
        self.show_number_of_pegs(win)
        load_btn.draw(win)
        restart_btn.draw(win)
        pygame.display.update()

    def show_board(self):
        """
        Prints the board to the terminal.
        """
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
        """
        Checks to see if the user has won or not (one peg left
        in the correct location).

        Returns:
        --------
        Boolean
        """
        if self.number_of_pegs == 1 and self.b[3][3] == 1:
            return True
        else:
            return False

    def show_number_of_pegs(self, win: pygame.display):
        """
        Draws the number of pegs on to the game screen without
        update updating screen.

        Params:
        ------

        win: pygame.display, mandatory.
            The main window (screen) of the game.
        """
        text_surface = self.my_font.render(str(self.number_of_pegs)
                                           + " pegs left",
                                           False, Cons.BLUE)
        win.blit(text_surface, (Cons.X_MARGIN // 2,
                                Cons.HEIGHT - Cons.Y_MARGIN))

    def decrement_number_of_pegs(self):
        """
        Reduces the number of pegs by one and prints current
        number of pegs.
        """
        self.number_of_pegs = self.number_of_pegs - 1
        print(str(self.number_of_pegs) + " pegs left")
