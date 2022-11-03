import pygame
import Constants as Cons


class Button:
    """
    The Button class initialises and draws a button.
    """

    def __init__(self, x: int, y: int, image: pygame.image):
        """
        Initialises Button class. Gets x and y coordinates of button
        and the image of the button, and scales the image to the appropriate
        size, creates a rect for the image and sets its coordinates.

        Params:
        ------

        x: int, mandatory
            X coordinate of button (top left corner).

        y: int, mandatory
            Y coordinate of button (top left corner).

        image: pygame.image, mandatory
            Image of button.
        """
        self.image = pygame.transform.scale(image, (Cons.X_MARGIN - 40, Cons.Y_MARGIN - 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, win):
        """
        Draws button to the screen.

        Params:
        ------

        win: pygame.display, mandatory
            The screen that the button will be drawn on.
        """
        win.blit(self.image, (self.rect.x, self.rect.y))
