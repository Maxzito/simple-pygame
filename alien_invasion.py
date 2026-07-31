import sys
import pygame

class AlienInvasion:
    """Overal class to manage game assets behaviour"""

    def __init__(self):
        """Initialize game and create resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Star the main loop"""

        while True:
            # Watch keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Make most recently draw screen visible
            pygame.display.flip()       # Não entendi muito

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game
