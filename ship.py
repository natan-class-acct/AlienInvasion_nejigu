"""
Program Name: ship.py
Author: Natan Ejigu
Purpose: Manages the player's ship for Track 1 (Custom Game
         Mechanics). The ship is drawn as a simple placeholder
         shape and positioned at the TOP center of the screen
         (instead of the bottom, as in the base book tutorial).
Starter code: Ship class structure based on Python Crash Course. Ship image loading replaced with
    a drawn placeholder shape, and starting position changed from
    midbottom to midtop, per Track 1 requirements.
Date: July 25, 2026
"""

import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Build a simple placeholder ship image: a downward-pointing triangle it
        # can be swapped for a real image later using pathlib, e.g.:
        # self.image = pygame.image.load(Path('images/ship.bmp'))
        self.width = 40
        self.height = 30
        self.image = pygame.Surface(
            (self.width, self.height), pygame.SRCALPHA)
        pygame.draw.polygon(
            self.image,
            (60, 60, 60),
            [(0, 0), (self.width, 0), (self.width // 2, self.height)],
        )
        self.rect = self.image.get_rect()

        # Start each new ship at the TOP center of the screen.
        self.rect.midtop = self.screen_rect.midtop

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)