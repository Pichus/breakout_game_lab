from abc import ABC, abstractmethod
from pathlib import Path

import pygame
from pygame import Rect, Surface

from constants import DEBUG


class Sprite(pygame.sprite.Sprite, ABC):
    x: int
    y: int
    image: Surface

    def __init__(self, x: int, y: int) -> None:
        super().__init__()

        self.x = x
        self.y = y

        self.set_image()

    @abstractmethod
    def set_image(self):
        pass

    def load_and_scale_image(
        self, texture_path: Path, sprite_resolution: tuple[int, int]
    ) -> Surface:

        original_image: Surface = pygame.image.load(texture_path).convert_alpha()
        scaled_image: Surface = pygame.transform.scale(
            original_image, sprite_resolution
        )
        return scaled_image

    def draw(self, window: Surface) -> Rect:
        drawn_rect = window.blit(self.image, (self.x, self.y))

        if DEBUG:
            return pygame.draw.rect(window, "green", drawn_rect, 5)

        return drawn_rect

    def change_position(self, x: int | None = None, y: int | None = None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
