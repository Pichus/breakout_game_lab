from pathlib import Path
from typing import Callable, override
from pygame import Rect, Surface, Vector2
from collision_sprite import CollisionSprite


class Brick(CollisionSprite):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__(x, y)
        self.image: Surface
        self.x: int
        self.y: int

        self.health: int = 1
        self.points: int = 1
        self._on_zero_health_handler: Callable[[int], None]

    @override
    def set_image(self):
        texture_path = Path("resources/textures/brick.png")
        sprite_resolution = (150, 50)
        self.image = self.load_and_scale_image(texture_path, sprite_resolution)

    @override
    def draw(self, window: Surface) -> Rect:
        return window.blit(self.image, (self.x, self.y))

    @override
    def update(self, health: int):
        if health <= 0:
            self._on_zero_health_handler(self.points)

        self.health = health

    def on_zero_health(self, handler: Callable[[int], None]):
        self._on_zero_health_handler = handler

    def change_position(self, position: Vector2):
        self.x = self.rect.x = round(position.x)
        self.y = self.rect.y = round(position.y)
