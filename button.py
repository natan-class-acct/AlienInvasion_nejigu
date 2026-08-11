"""
Program Name: button.py
Author: Natan Ejigu
Purpose: Defines the Button class used to create a Play button for
         the Alien Invasion game (Track 1: Custom Game Mechanics).
         Handles rendering the button rectangle and label text to
         the screen.
Starter code: Button class based on the Alien Invasion project from
    Python Crash Course, 3rd Edition, by Eric Matthes
Date: August 5 2026
"""

import pygame
import pygame.font
 
 
class Button:
    """A class to build buttons for the game."""
 
    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
 
        # Button dimensions.
        self.width, self.height = 200, 50
 
        # Colors matching the game's theme.
        self.bg_color = (15, 15, 40)
        self.border_color = (255, 200, 0)
        self.text_color = (255, 200, 0)
 
        self.font = pygame.font.SysFont(None, 48)
 
        # Build the button rect and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
 
        self._prep_msg(msg)
 
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center it on the
        button."""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
 
    def draw_button(self):
        """Draw the button border, fill, and label text."""
        # Gold border (2px thick).
        pygame.draw.rect(self.screen, self.border_color, self.rect)
        # Dark navy fill inside the border.
        inner_rect = self.rect.inflate(-4, -4)
        pygame.draw.rect(self.screen, self.bg_color, inner_rect)
        # Gold text label.
        self.screen.blit(self.msg_image, self.msg_image_rect)