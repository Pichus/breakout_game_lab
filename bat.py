from pathlib import Path
from typing import override

from pygame import Rect, Surface, Vector2
import pygame

from collision_sprite import CollisionSprite


class Bat(CollisionSprite):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        sprite_resolution = (200, 100)
        texture_path = Path("resources/textures/trampoline.png")
        super().__init__(texture_path, sprite_resolution, x, y)
        self.x_speed: int = 800
        self.dt: float = 0

    def change_position(self, position: Vector2):
        self.x = self.rect.x = round(position.x)
        self.y = self.rect.y = round(position.y)

    @override
    def update(self, dt: float):
        self.dt = dt

    def move(self, direction: Vector2, screen_width: int):
        self.x += round(direction.x * self.x_speed * self.dt)
        self.rect.x = self.x

        is_colliding_with_right_screen_border = self.x >= screen_width - self.rect.width
        is_colliding_with_left_screen_border = self.x <= 0

        if is_colliding_with_right_screen_border:
            self.x = screen_width - self.rect.width
            self.rect.right = screen_width

        if is_colliding_with_left_screen_border:
            self.x = self.rect.left = 0

    @override
    def draw(self, window: Surface) -> Rect:
        rect = super().draw(window)
        _ = pygame.draw.rect(window, (0, 255, 0), self.rect, 2)
        return rect
