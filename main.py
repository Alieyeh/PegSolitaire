import time
from Board import Board
from Location import Location
from Destination import Destination
from FileHandler import FileHandler
from Button import Button
import Constants as Cons
import pygame

# Initialising global values
FPS = 60
WIN = pygame.display.set_mode((Cons.WIDTH, Cons.HEIGHT))
pygame.display.set_caption('Peg Solitaire')
load_file_image = pygame.image.load('assets/load.png').convert_alpha()
restart_game_image = pygame.image.load('assets/restart.png').convert_alpha()
restart_btn = Button(Cons.WIDTH - Cons.X_MARGIN,
                     Cons.HEIGHT - Cons.Y_MARGIN,
                     restart_game_image)
load_btn = Button(Cons.WIDTH - Cons.X_MARGIN,
                  Cons.HEIGHT - Cons.Y_MARGIN * 2,
                  load_file_image)


def main():
    """
    Game logic. Initializes variables, checks for and handles closing
    screen and clicking screen (checking for and handling button press
    and peg movements) in main game loop.
    """

    # Initialising parameters
    run = True
    pygame.init()
    clock = pygame.time.Clock()
    file_name = ''
    extra = 0
    peg_picked = False
    is_loc = True
    loc = Location(4, 4)
    des = Destination(4, 4)
    board = Board()
    board.show_board()
    board.draw_board(WIN, load_btn, restart_btn)
    my_font = pygame.font.SysFont('FreeMono, Monospace', 17)

    # Main game loop
    while run:
        # Standardize speed
        clock.tick(FPS)

        # handle events
        for event in pygame.event.get():

            # Closes game (ends main loop) and logs moves
            if event.type == pygame.QUIT:
                if len(board.moves) > 0:
                    FileHandler().log_game(board.moves)
                run = False

            # Checks for button press events
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # Loads file and shows moves if load file button was clicked
                if load_btn.rect.collidepoint((x, y)):
                    # checks if peg is selected, only reads from file if it isn't
                    if is_loc:
                        my_moves = FileHandler().get_moves_from_file(file_name, WIN)
                        file_name = ''
                        extra = 0
                        for m in my_moves:
                            time.sleep(0.2)
                            board_x, board_y = board.calculate_screen_pos(m.x, m.y)
                            if is_loc:
                                loc = m
                                if board.is_peg(loc):
                                    peg_picked = True
                                    pygame.draw.circle(WIN, Cons.ORANGE, (board_x, board_y),
                                                       Cons.RADIUS)
                                    pygame.display.update()
                            else:
                                peg_picked = False
                                des = m
                                board.move_peg(loc, des, WIN, load_btn, restart_btn)
                            is_loc = not is_loc

                # Logs previous game and restarts game if restart button was clicked
                if restart_btn.rect.collidepoint((x, y)):
                    if len(board.moves) > 0:
                        print(len(board.moves))
                        FileHandler().log_game(board.moves)
                    is_loc = True
                    peg_picked = False
                    file_name = ''
                    extra = 0
                    board.number_of_pegs = 32
                    board.set_board()
                    board.show_board()
                    board.draw_board(WIN, load_btn, restart_btn)

                # Handles peg movement if a space on the board was clicked
                if Cons.X_MARGIN < x < Cons.SQUARE_SIZE * Cons.COLUMNS + Cons.X_MARGIN \
                        and Cons.Y_MARGIN < y < Cons.SQUARE_SIZE * Cons.ROWS + Cons.Y_MARGIN:
                    col, row = board.calculate_board_pos(x, y)
                    if not (col == 0 and row == 0):
                        board_x, board_y = board.calculate_screen_pos(col, row)
                        if is_loc:
                            loc = Location(col, row)
                            if board.is_peg(loc):
                                pygame.draw.circle(WIN, Cons.ORANGE, (board_x, board_y),
                                                   Cons.RADIUS)
                                pygame.display.update()
                            else:
                                is_loc = not is_loc
                        else:
                            des = Destination(col, row)
                            board.move_peg(loc, des, WIN, load_btn, restart_btn)
                        is_loc = not is_loc

            # Gets file destination/name from typed out user input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    file_name = file_name[:-1]
                    if extra > 0:
                        extra = extra - 1
                elif event.key == pygame.K_SPACE:
                    pass
                else:
                    file_name += event.unicode
                input_rect = pygame.Rect(Cons.WIDTH - Cons.X_MARGIN * 1.6,
                                         Cons.HEIGHT - Cons.Y_MARGIN * 2.5,
                                         Cons.X_MARGIN + 50, Cons.Y_MARGIN - 40)
                pygame.draw.rect(WIN, Cons.BLACK, input_rect)
                pygame.draw.rect(WIN, Cons.GREEN, input_rect, 2)
                if len(file_name) > 18:
                    extra = len(file_name) - 18
                file_surface = my_font.render(file_name[extra:], True,
                                              Cons.WHITE)
                WIN.blit(file_surface, (input_rect.x + 5, input_rect.y + 2))
                if peg_picked:
                    pygame.draw.circle(WIN, Cons.ORANGE, (board_x, board_y),
                                       Cons.RADIUS)
                pygame.display.update()

    # Ends game when main loop has ended
    pygame.quit()


if __name__ == "__main__":
    '''
    calls main function to run game.
    '''
    main()
