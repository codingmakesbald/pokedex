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
    font = pygame.font.Font(None, 30)
    center_y = 200 // 2
    pokemon_height = 40  # Assuming each Pokémon's name takes up about 40 pixels in height
    start_y = center_y - selected_index * pokemon_height
    # Define the subsurface area
    subsurface_rect = pygame.Rect(SCREEN_WIDTH - INFO_WIDTH, 100, INFO_WIDTH-10, INFO_WIDTH)
    info_surface = screen.subsurface(subsurface_rect)
    info_surface.fill(white)  # Assuming 'red' is defined somewhere, e.g., red = (255, 0, 0)

    x,y = screen.get_size()
        # Draw border around the subsurface
    pygame.draw.rect(screen, 'black', subsurface_rect, 4, 8)

    for i, pokemon in enumerate(POKEMONZ):
        titre = font.render("Kanto Pokédex", True, 'black')
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
        Create_box(screen)
    dialog_box = DialogBox(screen, (50, 50), (200, 100), bgcolor=(255, 255, 255), border_color=(0, 0, 0), border_radius=10, border_width=4)
    dialog_box.draw("hello madafaka")


def Create_box(screen, X_position=0, Y_position=0, surface_size=[100, 100], bgcolor="yellow"):
    Width, Height = screen.get_size()
    # Define the rectangle area for the box
    box_rect = pygame.Rect(X_position, Y_position, surface_size[0], surface_size[1])
    info = screen.subsurface(box_rect)

    # Draw border around the box with rounded corners
    border_color = (0, 0, 0)  # Black color as RGB
    border_width = 4  # Thickness of the border
    border_radius = 8  # Radius of the border corners

    pygame.draw.rect(screen, bgcolor, box_rect)
    pygame.draw.rect(screen, border_color, box_rect, border_width, border_radius)


class DialogBox:
    def __init__(self, screen, position, size, bgcolor=(255, 255, 255), border_color=(0, 0, 0), border_radius=8, border_width=2):
        self.screen = screen
        self.position = position
        self.size = size
        self.bgcolor = bgcolor
        self.border_color = border_color
        self.border_radius = border_radius
        self.border_width = border_width
        self.font = pygame.font.Font(None, 30)  # Adjust font size as needed
        self.text_color = (0, 0, 0)  # Default text color
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.subsurface = self.screen.subsurface(self.rect)

    def draw(self, text):
        # Fill the background
        self.subsurface.fill(self.bgcolor)
        
        # Draw the border around the dialog box
        pygame.draw.rect(self.screen, self.border_color, self.rect, self.border_width, self.border_radius)
        
        # Render the text
        text_surface = self.font.render(text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.size[0] // 2, self.size[1] // 2))
        
        # Blit the text surface onto the subsurface at the calculated position
        self.subsurface.blit(text_surface, text_rect)