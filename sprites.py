import pygame

from config import *


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

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400  # Assuming these are your screen dimensions
INFO_WIDTH = 200  # Width of the info subsurface

def draw_pokemon_list(screen, selected_index):
    font = pygame.font.Font(None, 30)
    center_y = 200 // 2
    pokemon_height = 40  # Assuming each Pokémon's name takes up about 40 pixels in height
    start_y = center_y - selected_index * pokemon_height
    info_surface = screen.subsurface((SCREEN_WIDTH - INFO_WIDTH, 100, INFO_WIDTH, INFO_WIDTH))
    info_surface.fill("lightgreen")  # F
    
    for i, pokemon in enumerate(POKEMONZ):
        titre = font.render("POKEDEX", True, 'black')
        titreR = titre.get_rect()
        titreR.centerx = 200
        screen.blit(titre, (titreR.x,0))

        # Highlight the selected Pokémon
        if i == selected_index:
            sprite = BaseSprite((i%16,i//16)).image
            # Scale the sprite to be 1.5 times bigger
            scaled_sprite = pygame.transform.scale(sprite, (int(TILE_WIDTH * 1.5), int(TILE_HEIGHT * 1.5)))
            text_surf = font.render(f"No:{i+1}  {pokemon}", True, "BLACK")
            rectangle = scaled_sprite.get_rect()  # Get the rect of the scaled sprite
            rectangle.centerx = 400 // 4
            rectangle.centery = 200
            screen.blit(scaled_sprite, rectangle.topleft)  # Blit the scaled sprite

        else:
            text_surf = font.render(pokemon, True, "grey")

        # Adjust the y position for each Pokémon based on its index
        text_rect = text_surf.get_rect(center=(200 // 2, start_y + i * pokemon_height))
        info_surface.blit(text_surf, text_rect)