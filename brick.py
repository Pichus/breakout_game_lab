from pathlib import Path

import pygame
from pygame import Surface

from sprite import Sprite


class Brick(Sprite):
    def __init__(self, x: int, y: int) -> None:
        texture_path = Path("resources/textures/brick.png")
        sprite_resolution = (150, 50)

        super().__init__(texture_path, sprite_resolution, x, y)

    def draw(self, window: Surface):
        window.blit(self.image, (self.x, self.y))
