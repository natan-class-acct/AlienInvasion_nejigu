
**Alien Invasion Game**

Alien Invasion is a beginner‑friendly Python game inspired by the project from Python Crash Course, 3rd Edition by Eric Matthes. In this game, the player controls a spaceship that fires upward at waves of incoming aliens. The objective is to eliminate each wave before the aliens reach the ship or break through the bottom of the screen.

This project helps me practice essential programming concepts such as classes, user input handling, game object updates, collision detection, and game loop management using the Pygame library. I will continue improving both the game and this README as I progress through the project milestones.

**Track Decision — Track 2: Custom Game Assets**

I’ve chosen Track 2, which focuses on creating a custom visual theme and designing a non‑rectangular alien fleet formation. I’m keeping the classic bottom‑of‑screen ship movement (instead of Track 1’s directional changes) and building a unique art style for the game.

**Note**: These plans are part of the milestone nudge assignment and may evolve as development continues.

**Milestone 1 — Custom Core Assets (Ship, Laser, Background)**
Plan: Use free, properly licensed CC0 assets to maintain a consistent visual style.

Ship Sprite: A spaceship sprite from Space Shooter Remastered  
Source: https://kenney.nl/assets/space-shooter-remastered

Laser/Bullet Sprite: A matching laser bolt from the same pack for visual consistency.

Background: A starfield background from Kenney’s Planets pack or another CC0 space texture.
Source: https://kenney.nl/assets/planets

All assets will be .png files with transparency, loaded using pathlib for cross‑platform compatibility.

Proper attribution (asset name, author, link) will be included in code docstrings as required.

**Milestone 2 — Custom Alien Sprite and Fleet Formation**
Alien Sprite: A themed alien/enemy sprite from the Space Shooter Remastered pack to match the ship and background style.

Fleet Formation: A V‑shaped (wedge) formation, where aliens are arranged in narrowing rows that converge toward a point. This satisfies the requirement for a non‑rectangular formation.

Collision logic (laser–alien, alien–ship) will be updated to work correctly with the new sprites and formation.

**Notes / Open Questions**
The fleet formation may change (e.g., circle, diamond, or another shape**) depending on how it looks and plays once implemented.

Final asset choices may change if I find better‑fitting art before Milestone 2 or the final submission.
