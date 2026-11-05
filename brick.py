from pathlib import Path
from typing import override
from pygame import Rect, Surface
from sprite import Sprite


class Brick(Sprite):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__(x, y)
        self.image: Surface
        self.x: int
        self.y: int

    @override
    def set_image(self):
        texture_path = Path("resources/textures/brick.png")
        sprite_resolution = (150, 50)
        self.image = self.load_and_scale_image(texture_path, sprite_resolution)

    @override
    def draw(self, window: Surface) -> Rect:
        return window.blit(self.image, (self.x, self.y))
