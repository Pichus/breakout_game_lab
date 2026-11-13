from pathlib import Path
from typing import override

from pygame import Rect, Surface, Vector2

from collision_sprite import CollisionSprite


class Bat(CollisionSprite):
    image: Surface
    x: int
    y: int
    rect: Rect

    x_speed: int
    dt: float

    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__(x, y)

        self.x_speed = 1000
        self.dt = 0

    @override
    def set_image(self):
        sprite_resolution = (200, 100)
        texture_path = Path("resources/textures/trampoline.png")
        self.image = self.load_and_scale_image(texture_path, sprite_resolution)

    @override
    def update(self, dt: float):
        self.dt = dt

    def move(self, direction: Vector2, screen_width: int):
        self.change_position(x=(self.x + round(direction.x * self.x_speed * self.dt)))

        is_colliding_with_right_screen_border = self.x >= screen_width - self.rect.width
        is_colliding_with_left_screen_border = self.x <= 0

        if is_colliding_with_right_screen_border:
            self.change_position(x=(screen_width - self.rect.width))

        if is_colliding_with_left_screen_border:
            self.change_position(x=0)
