from pathlib import Path
from typing import override
from pygame import Rect, Surface
from sprite import Sprite


class Brick(Sprite):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        texture_path = Path("resources/textures/brick.png")
        sprite_resolution = (150, 50)

        super().__init__(texture_path, sprite_resolution, x, y)

    @override
    def draw(self, window: Surface) -> Rect:
        return window.blit(self.image, (self.x, self.y))
