import pygame, sys
from config import POKEMONZ, SCREEN_HEIGHT, SCREEN_WIDTH
from sprites import BaseSprite, draw_pokemon_list

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = True
        # Assuming the first sprite is at position (0, 0) in the sprite sheet
        self.pokemonz = BaseSprite((5, 4))
        self.current_index = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
              if event.key == pygame.K_DOWN and self.current_index < len(POKEMONZ) - 1:
                self.current_index += 1
              elif event.key == pygame.K_UP and self.current_index > 0:
                self.current_index -= 1

    def draw(self):
        self.screen.fill('#EFEFEF')  # Clear screen with black
        # self.screen.blit(self.pokemonz.image, self.pokemonz.rect)  # Draw the sprite
        draw_pokemon_list(self.screen, self.current_index)
        pygame.display.flip()
        self.clock.tick(60)

    def main(self):
        while self.playing:
            self.draw()
            self.events()

g = Game()
while g.running:
    g.main()

pygame.quit()
sys.exit()