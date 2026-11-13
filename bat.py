from pathlib import Path
from typing import override

from pygame import Rect, Surface, Vector2

from collision_sprite import CollisionSprite
from screen_border import ScreenBorder


class Bat(CollisionSprite):
    image: Surface
    _x: int
    _y: int
    _rect: Rect

    _x_speed: int
    _dt: float

    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__(x, y)

        self._x_speed = 1000
        self._dt = 0

    @override
    def _set_image(self):
        sprite_resolution = (200, 100)
        texture_path = Path("resources/textures/trampoline.png")
        self.image = self._load_and_scale_image(texture_path, sprite_resolution)

    @override
    def update(self, dt: float):
        self._dt = dt

    def move(self, direction: Vector2, screen_width: int):
        self.change_position(x=(self.x + round(direction.x * self._x_speed * self._dt)))

        screen_border_collision = self._check_screen_border_collision(screen_width, 0)

        if screen_border_collision:
            if screen_border_collision == ScreenBorder.RIGHT:
                self.change_position(x=(screen_width - self.rect.width))

            if screen_border_collision == ScreenBorder.LEFT:
                self.change_position(x=0)
