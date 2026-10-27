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
        max_width = window.get_width() - self.rect.width
        max_height = window.get_height() - self.rect.height

        is_colliding_with_top_of_screen = self.y < 0
        is_colliding_with_bottom_of_screen = self.y >= max_height
        is_colliding_with_sides_of_screen = self.x < 0 or self.x >= max_width
        is_colliding_with_trampoline = self.rect.colliderect(trampoline.rect)

        if is_colliding_with_sides_of_screen:
            self.x_speed = -self.x_speed

        if is_colliding_with_top_of_screen or is_colliding_with_bottom_of_screen:
            self.y_speed = -self.y_speed

        # if is_colliding_with_bottom_of_screen:
        #     self.x_speed = 0
        #     self.y_speed = 0
        #     print("game over")

        if is_colliding_with_trampoline:
            self.y_speed = -self.y_speed
            self.x_speed = -self.x_speed

        delta = clock.tick(constants.FPS) / 1000
        self.x += round(self.x_speed * delta)
        self.y += round(self.y_speed * delta)
        self.rect.x = self.x
        self.rect.y = self.y

    @override
    def draw(self, window: Surface):
        super().draw(window)
        pygame.draw.rect(window, (255, 0, 0), self.rect, 2)
