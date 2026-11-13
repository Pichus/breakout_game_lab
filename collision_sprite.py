from abc import ABC
from typing import override

from pygame import Rect
from screen_border import ScreenBorder
from sprite import Sprite


class CollisionSprite(Sprite, ABC):
    rect: Rect

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.rect = self.image.get_rect(topleft=(x, y))

    @override
    def change_position(self, x: int | None = None, y: int | None = None):
        super().change_position(x, y)
        if x is not None:
            self.rect.x = x
        if y is not None:
            self.rect.y = y

    def _check_screen_border_collision(
        self, screen_width: int, screen_height: int
    ) -> ScreenBorder | None:
        is_colliding_with_left_side_of_screen = self.rect.left < 0
        if is_colliding_with_left_side_of_screen:
            return ScreenBorder.LEFT

        is_colliding_with_right_side_of_screen = self.rect.right > screen_width
        if is_colliding_with_right_side_of_screen:
            return ScreenBorder.RIGHT

        is_colliding_with_top_of_screen = self.rect.top <= 0
        if is_colliding_with_top_of_screen:
            return ScreenBorder.UPPER

        is_colliding_with_bottom_of_screen = self.rect.bottom >= screen_height
        if is_colliding_with_bottom_of_screen:
            return ScreenBorder.BOTTOM

        return None
