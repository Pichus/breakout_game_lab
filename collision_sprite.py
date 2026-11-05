from pygame import Rect
from sprite import Sprite


class CollisionSprite(Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.rect: Rect = self.image.get_rect(topleft=(x, y))
