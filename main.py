import time
from Board import Board
from Location import Location
from Destination import Destination
from FileHandler import FileHandler
from Button import Button
import Constants as Cons
import pygame


FPS = 60
WIN = pygame.display.set_mode((Cons.WIDTH, Cons.HEIGHT))
pygame.display.set_caption('Peg Solitaire')
load_file_image = pygame.image.load('assets/load.png').convert_alpha()
restart_game_image = pygame.image.load('assets/restart.png').convert_alpha()
restart_btn = Button(Cons.WIDTH - Cons.XMARGIN,
                     Cons.HEIGHT - Cons.YMARGIN,
                     restart_game_image)
load_btn = Button(Cons.WIDTH - Cons.XMARGIN,
                  Cons.HEIGHT - Cons.YMARGIN * 2,
                  load_file_image)


def main():
    run = True
    pygame.init()
    clock = pygame.time.Clock()
    moves = []
    is_loc = True
    loc = Location(4, 4)
    des = Destination(4, 4)
    board = Board()
    board.show_board()
    board.draw_board(WIN, load_btn, restart_btn)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if len(moves) > 0:
                    FileHandler().log_game(moves)
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if load_btn.rect.collidepoint((x, y)):
                    my_moves = FileHandler().get_moves_from_file()
                    for m in my_moves:
                        time.sleep(0.5)
                        board_x, board_y = board.calculate_board_pos(m.x, m.y)
                        if is_loc:
                            loc = m
                            if board.is_peg(loc):
                                moves.append(loc)
                                pygame.draw.circle(WIN, Cons.ORANGE, (board_x, board_y),
                                                   Cons.RADIUS)
                                pygame.display.update()
                            else:
                                is_loc = not is_loc
                        else:
                            des = m
                            moves.append(des)
                            board.move_peg(loc, des, WIN, load_btn, restart_btn)
                        is_loc = not is_loc
                if restart_btn.rect.collidepoint((x, y)):
                    if len(moves) > 0:
                        print(len(moves))
                        FileHandler().log_game(moves)
                    moves = []
                    is_loc = True
                    board.number_of_pegs = 32
                    board.set_board()
                    board.show_board()
                    board.draw_board(WIN, load_btn, restart_btn)
                if Cons.XMARGIN < x < Cons.SQUARESIZE * Cons.COLUMNS + Cons.XMARGIN \
                        and Cons.YMARGIN < y < Cons.SQUARESIZE * Cons.ROWS + Cons.YMARGIN:
                    col, row = board.calculate_array_pos(x, y)
                    if not (col == 0 and row == 0):
                        board_x, board_y = board.calculate_board_pos(col, row)
                        if is_loc:
                            loc = Location(col, row)
                            if board.is_peg(loc):
                                moves.append(loc)
                                pygame.draw.circle(WIN, Cons.ORANGE, (board_x, board_y),
                                                   Cons.RADIUS)
                                pygame.display.update()
                            else:
                                is_loc = not is_loc
                        else:
                            des = Destination(col, row)
                            moves.append(des)
                            board.move_peg(loc, des, WIN, load_btn, restart_btn)
                        is_loc = not is_loc
    pygame.quit()


if __name__ == "__main__":
    main()
