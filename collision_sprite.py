from typing import override

from pygame import Rect, Vector2
from sprite import Sprite


class CollisionSprite(Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.rect: Rect = self.image.get_rect(topleft=(x, y))

    @override
    def change_position(self, position: Vector2):
        super().change_position(position)
        self.rect.x = round(position.x)
        self.rect.y = round(position.y)
