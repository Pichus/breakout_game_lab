from pathlib import Path
from typing import override

from pygame import Surface
import pygame

from collision_sprite import CollisionSprite


class Bat(CollisionSprite):
    def __init__(self, x: int, y: int) -> None:
        sprite_resolution = (200, 100)
        texture_path = Path("resources/textures/trampoline.png")
        super().__init__(texture_path, sprite_resolution, x, y)
        self.x_speed: int = 25

    def move_right(self):
        self.x += self.x_speed
        self.rect.x += self.x_speed

    def move_left(self):
        self.x -= self.x_speed
        self.rect.x -= self.x_speed

    @override
    def draw(self, window: Surface):
        super().draw(window)
        pygame.draw.rect(window, (0, 255, 0), self.rect, 2)
