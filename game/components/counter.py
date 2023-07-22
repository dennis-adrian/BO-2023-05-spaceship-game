import pygame
from game.utils.constants import FONT_STYLE

class Counter:
    def __init__(self):
        self.counter = 0
        self.font = pygame.font.Font(FONT_STYLE, 30)

    def update(self):
        self.counter += 1

    def draw(self, screen, message, pos_x, pos_y, color='Black'):
        self.text = self.font.render(message, False, color)
        self.rect = self.text.get_rect(center = (pos_x, pos_y))
        screen.blit(self.text, self.rect)

    def set_value(self, value):
        self.counter = value

    def reset(self):
        self.counter = 0