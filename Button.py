import pygame
import Constants as Cons


class Button:

    def __init__(self, x, y, image: pygame.image):
        self.image = pygame.transform.scale(image, (Cons.XMARGIN - 40, Cons.YMARGIN - 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))
