from abc import ABC
from typing import override

from pygame import Rect
from screen_border import ScreenBorder
from sprite import Sprite


class CollisionSprite(Sprite, ABC):
    _rect: Rect

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self._rect = self.image.get_rect(topleft=(x, y))

    @property
    def rect(self) -> Rect:
        return self._rect

    @override
    def change_position(self, x: int | None = None, y: int | None = None):
        super().change_position(x, y)
        if x is not None:
            self._rect.x = x
        if y is not None:
            self._rect.y = y

    def _check_screen_border_collision(
        self, screen_width: int, screen_height: int
    ) -> ScreenBorder | None:
        is_colliding_with_left_side_of_screen = self._rect.left < 0
        if is_colliding_with_left_side_of_screen:
            return ScreenBorder.LEFT

        is_colliding_with_right_side_of_screen = self._rect.right > screen_width
        if is_colliding_with_right_side_of_screen:
            return ScreenBorder.RIGHT

        is_colliding_with_top_of_screen = self._rect.top <= 0
        if is_colliding_with_top_of_screen:
            return ScreenBorder.UPPER

        is_colliding_with_bottom_of_screen = self._rect.bottom >= screen_height
        if is_colliding_with_bottom_of_screen:
            return ScreenBorder.BOTTOM

        return None
