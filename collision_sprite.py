from typing import override

from pygame import Rect, Vector2
from sprite import Sprite


class CollisionSprite(Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.rect: Rect = self.image.get_rect(topleft=(x, y))

    @override
    def change_position(self, x: int | None = None, y: int | None = None):
        super().change_position(x, y)
        if x is not None:
            self.rect.x = x
        if y is not None:
            self.rect.y = y
