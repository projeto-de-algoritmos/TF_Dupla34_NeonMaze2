from maze_generator import *
from random import randrange

# classe do baseadão (diminui a velocidade a velocidade de queda do tempo)
class baseadao(object):
    def __init__(self,game_surface):
        self.img = pygame.image.load('img/baseadao.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
        self.rect = self.img.get_rect()
        self.game_surface = game_surface
        self.set_pos()

    def set_pos(self):
        self.rect.topleft = randrange(cols) * TILE + 5, randrange(rows) * TILE + 5

    def draw(self):
        self.game_surface.blit(self.img, self.rect)

    def whoami(self):
        return (type(self).__name__)     

# class relógio (aumenta o tempo de jogo)
class watch(object):
    def __init__(self,game_surface):
        self.img = pygame.image.load('img/watch.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
        self.rect = self.img.get_rect()
        self.game_surface = game_surface
        self.set_pos()

    def set_pos(self):
        self.rect.topleft = randrange(cols) * TILE + 5, randrange(rows) * TILE + 5

    def draw(self):
        self.game_surface.blit(self.img, self.rect)

    def whoami(self):
        return (type(self).__name__)

# class gasolina (aumenta a velocidade do jogador)
class gasolina(object):
    def __init__(self,game_surface):
        self.img = pygame.image.load('img/gasolina.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
        self.rect = self.img.get_rect()
        self.game_surface = game_surface
        self.set_pos()

    def set_pos(self):
        self.rect.topleft = randrange(cols) * TILE + 5, randrange(rows) * TILE + 5

    def draw(self):
        self.game_surface.blit(self.img, self.rect)

    def whoami(self):
        return (type(self).__name__)
