from Board import Board
from Destination import Destination
from Location import Location
from FileHandler import FileHandler
import re


def main():
    print_intro()
    moves = []
    is_loc = True
    loc = Location(4, 4)
    des = Destination(4, 4)
    board = Board()
    board.show_board()
    while True:
        inp = input('enter coordinates of peg:')
        if inp == 'q' or inp == 'Q':
            FileHandler().log_game(moves)
            break
        elif inp == 'r' or inp == 'R':
            my_moves = FileHandler().get_moves_from_file()
            for m in my_moves:
                if is_loc:
                    loc = m
                    moves.append(loc)
                else:
                    des = m
                    moves.append(des)
                    board.move_peg(loc, des)
                is_loc = not is_loc
        else:
            if re.match('^[0-7],[0-7]$', inp):
                coordinates = re.findall('\d+', inp)
                x = int(coordinates[0])
                y = int(coordinates[1])
                if is_loc:
                    loc = Location(x, y)
                    moves.append(loc)
                else:
                    des = Destination(x, y)
                    moves.append(des)
                    board.move_peg(loc, des)
                is_loc = not is_loc
            else:
                print("incorrect input")
                continue


def print_intro():
    print("\n" + "Welcome to Peg Solitaire!" + "\n")
    print("-Enter q to exit the game")
    print("-Enter r to read the solution file")
    print("-Enter peg coordinates in this format to play: x,y" + "\n")
    print("First choose which peg to move and enter and"
          " then choose destination")
    print("If move is rejected choose what peg to move again")
    print("If input is incorrect choose from where you left off")
    print("The solution file must have complete moves" + "\n")


if __name__ == "__main__":
    main()
