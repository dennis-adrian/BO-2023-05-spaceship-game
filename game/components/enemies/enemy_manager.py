import random

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.enemy_images = [ENEMY_1, ENEMY_2, ENEMY_3]
    
    def update(self):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 2:
            image = random.choice(self.enemy_images)
            speed_on_x = random.randint(10, 20)
            speed_on_y = random.randint(1, 5)

            enemy = Enemy(image, speed_on_x, speed_on_y)
            self.enemies.append(enemy)