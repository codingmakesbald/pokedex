import pygame

from config import POKEMONZ

TILE_WIDTH = 64
TILE_HEIGHT = 64

WHITE = "white"
BLACK = "black"

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

def draw_pokemon_list(screen, selected_index):
    font = pygame.font.Font(None, 30)
    
    # Calculate the start_y position to center the selected Pokémon
    center_y = 400 // 2
    pokemon_height = 40  # Assuming each Pokémon's name takes up about 40 pixels in height
    start_y = center_y - selected_index * pokemon_height
    
    for i, pokemon in enumerate(POKEMONZ):
        titre = font.render("POKEDEX", True, 'black', "white")
        screen.blit(titre, (0,0))
        # Highlight the selected Pokémon
        if i == selected_index:
            text_surf = font.render(f"No: {i+1}. {pokemon}", True, "BLACK")
            rectangle = BaseSprite((i%16,i//16)).rect.inflate(10, 10) # Add some padding around the text
            rectangle.centerx = 400//4
            rectangle.centery = 200
            screen.blit(BaseSprite((i%16,i//16)).image, rectangle)
            pygame.draw.rect(screen, BLACK, rectangle, 1)  # 1 is the border thickness
        else:
            text_surf = font.render(pokemon, True, "grey")
        
        # Adjust the y position for each Pokémon based on its index
        text_rect = text_surf.get_rect(center=(400 // 1.2, start_y + i * pokemon_height))
        screen.blit(text_surf, text_rect)