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

INFO_WIDTH = 200  # Width of the info subsurface

def draw_pokemon_list(screen, selected_index):
    lltz= PokemonListDrawer(screen, POKEMONZ, selected_index)
    lltz.draw()



class PokemonListDrawer:
    INFO_WIDTH = 200  # Width of the info subsurface

    def __init__(self, screen, pokemon_list, selected_index):
        self.screen = screen
        self.pokemon_list = pokemon_list
        self.selected_index = selected_index
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        center_y = 200 // 2
        pokemon_height = 40  # Assuming each Pokémon's name takes up about 40 pixels in height
        start_y = center_y - self.selected_index * pokemon_height

        # Define the subsurface area
        subsurface_rect = pygame.Rect(SCREEN_WIDTH - self.INFO_WIDTH, 100, self.INFO_WIDTH - 10, self.INFO_WIDTH)
        info_surface = self.screen.subsurface(subsurface_rect)
        info_surface.fill(white)  # Assuming 'white' is defined somewhere, e.g., white = (255, 255, 255)

        # Draw border around the subsurface
        pygame.draw.rect(self.screen, 'black', subsurface_rect, 4, 8)

        for i, pokemon in enumerate(self.pokemon_list):
            titre = self.font.render("Kanto Pokédex", True, 'black')
            titreR = titre.get_rect()
            titreR.centerx = 200
            self.screen.blit(titre, (titreR.x, 0))

            # Highlight the selected Pokémon
            if i == self.selected_index:
                sprite = BaseSprite((i % 16, i // 16)).image
                # Scale the sprite to be 1.5 times bigger
                scaled_sprite = pygame.transform.scale(sprite, (int(TILE_WIDTH * 1.5), int(TILE_HEIGHT * 1.5)))
                text_surf = self.font.render(f"No:{i + 1}  {pokemon}", True, "BLACK")
                rectangle = scaled_sprite.get_rect()
                rectangle.centerx = 400 // 4
                rectangle.centery = 200
                self.screen.blit(scaled_sprite, rectangle.topleft)
            else:
                text_surf = self.font.render(pokemon, True, "grey")

            # Adjust the y position for each Pokémon based on its index
            text_rect = text_surf.get_rect(center=(200 // 2, start_y + i * pokemon_height))
            info_surface.blit(text_surf, text_rect)