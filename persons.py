from random import randrange, choice
from maze_generator import *

# Selker normal 
class normalSelkers:
    def __init__(self,game_surface):
        self.img = pygame.image.load('img/2.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
        self.rect = self.img.get_rect()
        self.game_surface = game_surface
        self.set_pos()

    def set_pos(self):
        self.rect.topleft = randrange(cols) * TILE + 5, randrange(rows) * TILE + 5

    def draw(self):
        self.game_surface.blit(self.img, self.rect)
    
# Selker inimigo
class blackSelkers:
    def __init__(self,game_surface):
        self.img = pygame.image.load('img/selkerNegro.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
        self.rect = self.img.get_rect()
        self.game_surface = game_surface
        self.set_pos()

    def set_pos(self):
        self.rect.topleft = randrange(cols) * TILE + 5, randrange(rows) * TILE + 5

    def draw(self):
        self.game_surface.blit(self.img, self.rect)