import pygame
import random
from pygame.sprite import Sprite

from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60
    Y_POS = 0
    X_POS_RANGE = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    MOVES = { 0: 'left', 1: 'right' }

    def __init__(self, image, speed_on_x, speed_on_y):
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect(midtop = (random.choice(self.X_POS_RANGE), self.Y_POS))
        self.direction = self.MOVES[random.randint(0, 1)]
        self.movement_count = 0
        self.moves_before_change = random.randint(20, 50)
        self.speed_on_x = speed_on_x
        self.speed_on_y = speed_on_y

    def update(self, enemies):
        self.rect.y += self.speed_on_y

        if self.direction == self.MOVES[0]:
            self.rect.x -= self.speed_on_x
        elif self.direction == self.MOVES[1]:
            self.rect.x += self.speed_on_x

        self.handle_direction()

        if self.rect.top > SCREEN_HEIGHT:
            enemies.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_direction(self):
        self.movement_count += 1

        if (self.movement_count >= self.moves_before_change and self.direction == self.MOVES[1]) or self.rect.right >= SCREEN_WIDTH:
            self.direction = self.MOVES[0]
        elif self.movement_count >= self.moves_before_change and self.direction == self.MOVES[0] or self.rect.left <= 0:
            self.direction = self.MOVES[1]
        
        if (self.movement_count >= self.moves_before_change):
            self.movement_count = 0
