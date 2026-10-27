from pathlib import Path
from pygame import Rect
from sprite import Sprite


class CollisionSprite(Sprite):
    def __init__(
        self, texture_path: Path, sprite_resolution: tuple[int, int], x: int, y: int
    ) -> None:
        super().__init__(texture_path, sprite_resolution, x, y)
        self.rect: Rect = self.image.get_rect(topleft=(x, y))
