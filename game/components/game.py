import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, DEFAULT_TYPE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.counter import Counter

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.menu = Menu(self.screen, 'Press any button to start')
        self.power_up_manager = PowerUpManager()
        self.score = Counter()
        self.death_counter = Counter()
        self.highest_score = Counter()

    def execute(self):
        self.running = True
        while self.running and not self.playing:
            self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.score.reset()
        self.player.reset()
        self.bullet_manager.reset()
        self.enemy_manager.reset()
        self.power_up_manager.reset()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.score.draw(self.screen, f'Score: {self.score.counter}',SCREEN_WIDTH - 100, 50, 'White')
        pygame.display.update()
        # pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        self.menu.draw(self.screen)
        self.menu.update(self)

        self.menu.reset_screen(self.screen)

        if self.death_counter.counter > 0:
            self.menu.update_message('Game Over: Press any button to start')
            self.set_highest_score()

            icon = pygame.transform.scale((ICON), (80, 120))
            self.screen.blit(icon, ((SCREEN_WIDTH / 2) - 40, (SCREEN_HEIGHT / 2) - 150))
            self.score.draw(self.screen, f'Your score: {self.score.counter}', SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) + 50)
            self.highest_score.draw(self.screen, f'Highest Score: {self.highest_score.counter}', SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) + 100)
            self.death_counter.draw(self.screen, f'Total Deaths: {self.death_counter.counter}', SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) + 150)

        self.menu.draw(self.screen)
        self.menu.update(self)

    def set_highest_score(self):
        if self.score.counter > self.highest_score.counter:
            self.highest_score.set_value(self.score.counter)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)

            if time_to_show >= 0:
                power_up_counter = Counter()
                power_up_counter.draw(self.screen, f'{self.player.power_up_type.capitalize()} is enabled for {time_to_show}', SCREEN_WIDTH / 2, 50, 'White')
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()