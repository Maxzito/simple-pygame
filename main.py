import sys
import pygame

from settings import Settings
from ship import Ship

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
        self.ship = Ship(self)      # Passando self pq esta é uma instancia do game

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Star the main loop"""

        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keys pressed"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
            

    def _update_screen(self):
        """Upddate images on the screen, and flip a new _update_screen"""

        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.BG_COLOR)
        self.ship.blitme()

        # Make most recently draw screen visible
        pygame.display.flip()       # Não entendi muito


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
