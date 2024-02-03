import pygame
from config import SCREEN_HEIGHT

class DialogBox:
    def __init__(self, screen, position, size, bgcolor=(255, 255, 255), border_color=(0, 0, 0), border_radius=8, border_width=2):
        self.screen = screen
        self.screenWidth, self.screenHeight = screen.get_size()
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



dialog_box = DialogBox(SCREEN_HEIGHT, (50, 50), (200, 100), bgcolor=(255, 255, 255), border_color=(0, 0, 0), border_radius=10, border_width=4)
dialog_box.draw("hello madafaka")
