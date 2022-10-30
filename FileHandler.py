from Destination import Destination
from Location import Location
from datetime import datetime
import re


class FileHandler:

    def __init__(self):
        self.is_loc = True
        self.file_name = 'partial_solution.txt'

    def get_moves_from_file(self):
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
                if len(entries) % 2 != 0:
                    print("incomplete move in file")
                    entries.pop()
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

    def log_game(self, moves):
        filename = 'gameLog_' + datetime.now().strftime("%Y%m%d-%H%M%S")
        try:
            with open('logs/' + filename, 'w') as f:
                mov = " ".join(str(m.x) + "," + str(m.y) for m in moves)
                print(type(mov))
                print(mov)
                f.write(mov)
        except FileNotFoundError:
            print("file not found")
