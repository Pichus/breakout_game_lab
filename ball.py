from pathlib import Path
from typing import Callable, override

from pygame import Rect, Surface
import pygame
from pygame.math import Vector2
from collision_sprite import CollisionSprite
from bat import Bat


class Ball(CollisionSprite):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        texture_path = Path("resources/textures/hedgehog_ball.png")
        sprite_resolution = (100, 100)
        super().__init__(texture_path, sprite_resolution, x, y)

        self.x_speed: int = 600
        self.y_speed: int = 600
        self.radius: int = round(self.rect.height / 2)
        self.on_bottom_screen_collision_function: Callable[[], None]

    def change_position(self, position: Vector2):
        self.x = self.rect.x = round(position.x)
        self.y = self.rect.y = round(position.y)

    def on_bottom_screen_collision(self, function: Callable[[], None]):
        self.on_bottom_screen_collision_function = function

    @override
    def update(self, screen: Surface, dt: float, bat: Bat):
        self.x += round(self.x_speed * dt)
        self.rect.x = self.x

        is_colliding_with_trampoline = self.rect.colliderect(bat.rect)
        is_colliding_with_sides_of_screen = (
            self.rect.left < 0 or self.rect.right >= screen.get_width()
        )

        if is_colliding_with_trampoline:
            if self.x_speed < 0:
                self.rect.x = bat.rect.right + 10
            if self.x_speed > 0:
                self.rect.x = bat.rect.left - 10
            self.x_speed = -self.x_speed

        if is_colliding_with_sides_of_screen:
            self.x_speed = -self.x_speed

        self.y += round(self.y_speed * dt)
        self.rect.y = self.y

        is_colliding_with_top_of_screen = self.rect.top <= 0
        is_colliding_with_bottom_of_screen = self.rect.bottom >= screen.get_height()
        is_colliding_with_trampoline = self.rect.colliderect(bat.rect)

        if is_colliding_with_trampoline:
            self.rect.bottom = bat.rect.top
            self.y = bat.rect.top - bat.rect.height
            self.y_speed = -self.y_speed

        if is_colliding_with_top_of_screen:
            self.y_speed = -self.y_speed

        if is_colliding_with_bottom_of_screen:
            self.on_bottom_screen_collision_function()

    @override
    def draw(self, window: Surface) -> Rect:
        rect = super().draw(window)
        _ = pygame.draw.rect(window, (255, 0, 0), rect, 2)
        return rect
