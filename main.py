import sys
import pygame

from settings import Settings

class AlienInvasion:
    """Overal class to manage game assets behaviour"""

    def __init__(self):
        """Initialize game and create resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
                (self.settings.SW, self.settings.SH)
                )

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Star the main loop"""

        while True:
            # Watch keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.BG_COLOR)

            # Make most recently draw screen visible
            pygame.display.flip()       # Não entendi muito
            self.clock.tick(60)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
