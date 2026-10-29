from pathlib import Path
import pygame
from pygame import Rect, Surface


class Sprite(pygame.sprite.Sprite):
    def __init__(
        self, texture_path: Path, sprite_resolution: tuple[int, int], x: int, y: int
    ) -> None:
        super().__init__()

        self.x: int = x
        self.y: int = y

        original_image: Surface = pygame.image.load(texture_path).convert_alpha()
        scaled_image: Surface = pygame.transform.scale(
            original_image, sprite_resolution
        )
        self.image: Surface = scaled_image

    def draw(self, window: Surface) -> Rect:
        return window.blit(self.image, (self.x, self.y))
