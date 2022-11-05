from Destination import Destination
from Location import Location
from datetime import datetime
import Constants as Cons
import pygame
import re


class FileHandler:
    """
    Handles the logging and reading of moves from and to
    text file.
    """

    def __init__(self):
        """
        Initialises the FileHandler class by assigning the values
        of file name (the default solution file) and is_loc (shows
        if the location being read is the peg's current location or
        destination) as well as message (what will be written to the
        screen) and my_font.
        """
        self.is_loc = True
        self.file_name = 'partial_solution.txt'
        self.message = ''
        self.my_font = pygame.font.SysFont('Times New Roman', 25)

    def get_moves_from_file(self, file_name: str, win: pygame.display):
        """
        Reads file of moves and returns the moves as a list
        of locations and destinations. If file name is empty
        it will load the partial solution file. If file has
        an issue it will return an empty list.

        Params:
        --------
        file_name: string, mandatory.
            Name and address of the file that will be read.

        win: pygame.display, mandatory.
            The main window (screen) of the game.

        Returns:
        --------
        list
        """
        my_moves = []
        if file_name != '':
            self.file_name = file_name
        else:
            print("Did not choose, will load partial_solution.txt")
        try:
            with open(self.file_name) as f:
                entries = f.read().split()

                # If the number of coordinates is odd it's
                # likely to be due to an incomplete move so
                # the last set of coordinates will be removed.
                if len(entries) % 2 != 0:
                    entries.pop()
                    print("incomplete move in file")

                # Checks if entries match the correct format,
                # lets user know if not and appends as location
                # or destination if it does.
                for entry in entries:
                    if re.match('^[0-7],[0-7]$', entry):
                        line = entry.split(',')
                        if self.is_loc:
                            my_moves.append(Location(int(line[0]), int(line[1])))
                        else:
                            my_moves.append(Destination(int(line[0]), int(line[1])))
                        self.is_loc = not self.is_loc
                    else:
                        self.message = "file content is incorrect"
                        self.write_message(win)
                        return []
        except IOError:
            self.message = "Could not open/read/find file"
            self.write_message(win)
        return my_moves

    def log_game(self, moves: list):
        """
        Logs the moves made in the game to a text file in board
        coordinate format.

        Params:
        ------

        moves: list, mandatory
            List of moves to log.
        """
        filename = 'gameLog_' + datetime.now().strftime("%Y%m%d-%H%M%S")
        try:
            with open('logs/' + filename, 'w') as f:
                mov = " ".join(str(m.x) + "," + str(m.y) for m in moves)
                print(type(mov))
                print(mov)
                f.write(mov)
        except FileNotFoundError:
            print("file not found")

    def write_message(self, win):
        """
        Writes a message to the screen.

        Params:
        ------

        win: pygame.display, mandatory.
            The main window (screen) of the game.
        """
        text_surface = self.my_font.render(self.message,
                                           False, Cons.ORANGE)
        win.blit(text_surface, (Cons.X_MARGIN // 2, Cons.Y_MARGIN // 2))
        pygame.display.flip()
        print(self.message)
        self.message = ''
