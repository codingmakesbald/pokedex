import pygame

TILE_WIDTH = 64
TILE_HEIGHT = 64

class BaseSprite(pygame.sprite.Sprite):
    __slots__ = ('value')
    def __init__(self, value):
        super().__init__()
        self.sheet = pygame.image.load("Image-Article.png").convert_alpha()
        self.value = tuple(value)
        self.image = self.get_sprite()
        self.rect = self.image.get_rect()

    def get_sprite(self):
      sprite = pygame.Surface((TILE_WIDTH, TILE_HEIGHT), pygame.SRCALPHA)
      sprite.blit(self.sheet, (0, 0), (self.value[0]* TILE_WIDTH, self.value[1]* TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
      return sprite