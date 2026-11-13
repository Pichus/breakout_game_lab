from abc import ABC, abstractmethod
from pathlib import Path

import pygame
from pygame import Rect, Surface

from constants import DEBUG


class Sprite(pygame.sprite.Sprite, ABC):
    _x: int
    _y: int
    image: Surface

    def __init__(self, x: int, y: int) -> None:
        super().__init__()

        self._x = x
        self._y = y

        self._set_image()

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @abstractmethod
    def _set_image(self):
        pass

    def _load_and_scale_image(
        self, texture_path: Path, sprite_resolution: tuple[int, int]
    ) -> Surface:

        original_image: Surface = pygame.image.load(texture_path).convert_alpha()
        scaled_image: Surface = pygame.transform.scale(
            original_image, sprite_resolution
        )
        return scaled_image

    def draw(self, window: Surface) -> Rect:
        drawn_rect = window.blit(self.image, (self._x, self._y))

        if DEBUG:
            return pygame.draw.rect(window, "green", drawn_rect, 5)

        return drawn_rect

    def change_position(self, x: int | None = None, y: int | None = None):
        if x is not None:
            self._x = x
        if y is not None:
            self._y = y
