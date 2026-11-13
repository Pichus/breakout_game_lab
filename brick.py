from pathlib import Path
from typing import Callable, override
from pygame import Surface
from collision_sprite import CollisionSprite


class Brick(CollisionSprite):
    image: Surface
    _x: int
    _y: int

    _health: int
    _points: int
    _on_zero_health_handler: Callable[[int], None] | None

    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__(x, y)

        self._health = 1
        self._points = 1
        self._on_zero_health_handler = None

    @property
    def health(self) -> int:
        return self._health

    @property
    def points(self) -> int:
        return self._points

    @override
    def _set_image(self):
        texture_path = Path("resources/textures/brick.png")
        sprite_resolution = (150, 50)
        self.image = self._load_and_scale_image(texture_path, sprite_resolution)

    @override
    def update(self, health: int):
        if health <= 0:
            if self._on_zero_health_handler:
                self._on_zero_health_handler(self._points)
            self.kill()

        self._health = health

    def on_zero_health(self, handler: Callable[[int], None]):
        self._on_zero_health_handler = handler
