import pygame, sys
from sprites import BaseSprite

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = True
        # Assuming the first sprite is at position (0, 0) in the sprite sheet
        self.pokemonz = BaseSprite((5, 4))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear screen with black
        self.screen.blit(self.pokemonz.image, self.pokemonz.rect)  # Draw the sprite
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