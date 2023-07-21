import pygame

from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    SCREEN_HALF_HEIGHT = SCREEN_HEIGHT / 2
    SCREEN_HALF_WIDTH = SCREEN_WIDTH / 2

    def __init__(self, screen, message):
        self.reset_screen(screen)
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, False, "Black")
        self.rect = self.text.get_rect(center = (self.SCREEN_HALF_WIDTH, self.SCREEN_HALF_HEIGHT))
    
    def update(self, game):
        pygame.display.update()
        self.handle_events(game)

    def draw(self, screen):
        screen.blit(self.text, self.rect)
    
    def handle_events(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            if event.type == pygame.KEYDOWN:
                game.run()
    
    def reset_screen(self, screen):
        screen.fill('White')
    
    def update_message(self, message):
        self.text = self.font.render(message, False, 'Black')
        self.rect = self.text.get_rect(center = (self.SCREEN_HALF_WIDTH, self.SCREEN_HALF_HEIGHT))