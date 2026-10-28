from pathlib import Path
from typing import override

from pygame import Surface
import pygame
from pygame.time import Clock

from collision_sprite import CollisionSprite
import constants
from trampoline import Trampoline


class Ball(CollisionSprite):
    def __init__(self, x: int, y: int) -> None:
        texture_path = Path("resources/textures/hedgehog_ball.png")
        sprite_resolution = (100, 100)
        super().__init__(texture_path, sprite_resolution, x, y)

        self.x_speed: int = 600
        self.y_speed: int = 600
        self.radius: int = round(self.rect.height / 2)

    def update(self, window: Surface, clock: Clock, trampoline: Trampoline):
        delta = clock.tick(constants.FPS) / 1000

        self.x += round(self.x_speed * delta)
        self.rect.x = self.x

        is_colliding_with_trampoline = self.rect.colliderect(trampoline.rect)
        is_colliding_with_sides_of_screen = (
            self.rect.left < 0 or self.rect.right >= window.get_width()
        )

        if is_colliding_with_trampoline:
            if self.x_speed < 0:
                self.rect.x = trampoline.rect.right + 10
            if self.x_speed > 0:
                self.rect.x = trampoline.rect.left - 10
            self.x_speed = -self.x_speed

        if is_colliding_with_sides_of_screen:
            self.x_speed = -self.x_speed

        self.y += round(self.y_speed * delta)
        self.rect.y = self.y

        is_colliding_with_top_of_screen = self.rect.top <= 0
        is_colliding_with_bottom_of_screen = self.rect.bottom >= window.get_height()
        is_colliding_with_trampoline = self.rect.colliderect(trampoline.rect)

        if is_colliding_with_trampoline:
            if self.y_speed > 0:
                self.rect.bottom = trampoline.rect.top
                self.y = trampoline.rect.top - trampoline.rect.height
            if self.y_speed < 0:
                self.rect.top = trampoline.rect.bottom
                self.y = trampoline.rect.bottom + trampoline.rect.height
            self.y_speed = -self.y_speed

        if is_colliding_with_top_of_screen or is_colliding_with_bottom_of_screen:
            self.y_speed = -self.y_speed

    @override
    def draw(self, window: Surface):
        super().draw(window)
        pygame.draw.rect(window, (255, 0, 0), self.rect, 2)
