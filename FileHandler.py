from Destination import Destination
from Location import Location
from datetime import datetime
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
        destination).
        """
        self.is_loc = True
        self.file_name = 'partial_solution.txt'

    def get_moves_from_file(self):
        """
        Reads file of moves and returns the moves as a list
        of locations and destinations. If file has an issue it
        will return an empty list.

        Returns:
        --------
        list
        """
        my_moves = []
        choose_file = input("Would you like to choose file? (Y/N)")
        if choose_file == 'y' or choose_file == 'Y':
            self.file_name = input("Enter file path and name: ")
        elif choose_file == 'n' or choose_file == 'N':
            pass
        else:
            print("Did not choose, will load partial_solution.txt")
        try:
            with open(self.file_name) as f:
                entries = f.read().split()

                # If the number of coordinates is odd it's
                # likely to be due to an incomplete move so
                # the last set of coordinates will be removed.
                if len(entries) % 2 != 0:
                    print("incomplete move in file")
                    entries.pop()

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
                        print("file content is incorrect")
                        return []
        except IOError:
            print("Could not open/read/find file")
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
