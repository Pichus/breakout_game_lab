from pathlib import Path
from typing import override

from pygame import Surface
from brick import Brick


class StrongerBrick(Brick):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__(x, y)
        self.x: int
        self.y: int
        self.image: Surface
        self.health: int

        self.health = 2

    @override
    def set_image(self):
        texture_path = Path("resources/textures/stronger_brick.png")
        sprite_resolution = (150, 50)
        self.image = self.load_and_scale_image(texture_path, sprite_resolution)
