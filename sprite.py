from abc import ABC
from pathlib import Path

import pygame
from pygame import Rect, Surface


class Sprite(pygame.sprite.Sprite, ABC):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()

        self.x: int = x
        self.y: int = y

        self.image: Surface
        self.set_image()

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
        return window.blit(self.image, (self.x, self.y))
