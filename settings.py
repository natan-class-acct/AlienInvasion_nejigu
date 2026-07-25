"""
Program Name: settings.py
Author: Natan Ejigu
Purpose: A module to store all settings for the Alien Invasion game in one place, so they can
         be changed easily as the project grows.
Starter code: Based on the Alien Invasion project from Python Crash
    Course, 3rd Edition, by Eric Matthes.
Date: July 25, 2026
"""


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)