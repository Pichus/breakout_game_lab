from pathlib import Path
from typing import Callable, override

from pygame import Surface, Vector2
import pygame
from pygame.sprite import Group
from brick import Brick
from collision_sprite import CollisionSprite
from bat import Bat
from screen_border import ScreenBorder


class Ball(CollisionSprite):
    image: Surface
    x: int
    y: int

    _speed: Vector2
    _direction: Vector2
    _damage: int
    _on_bottom_screen_collision_handler: Callable[[], None] | None

    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__(x, y)

        self._speed = Vector2(600, 600)
        self._direction = Vector2(1, 1)
        self._damage = 1
        self._on_bottom_screen_collision_handler = None

    @property
    def damage(self) -> int:
        return self._damage

    @override
    def set_image(self):
        texture_path = Path("resources/textures/hedgehog_ball.png")
        sprite_resolution = (100, 100)
        self.image = self.load_and_scale_image(texture_path, sprite_resolution)

    def on_bottom_screen_collision(self, handler: Callable[[], None]):
        self._on_bottom_screen_collision_handler = handler

    def _handle_brick_collision(self, bricks: list[Brick]):
        for brick in bricks:
            brick.update(brick.health - self._damage)

    def _is_colliding_with_bat(self, bat: Bat) -> bool:
        return self.rect.colliderect(bat.rect)

    def _check_brick_collisions(self, bricks: Group[Brick]) -> list[Brick]:  # pyright: ignore[reportInvalidTypeArguments]
        bricks_ball_collides_with = pygame.sprite.spritecollide(self, bricks, False)  # pyright: ignore[reportArgumentType, reportUnknownVariableType]
        return bricks_ball_collides_with  # pyright: ignore[reportUnknownVariableType]

    def _update_on_x_axis(
        self,
        dt: float,
        screen_width: int,
        screen_height: int,
        bat: Bat,
        bricks: Group[Brick],  # pyright: ignore[reportInvalidTypeArguments]
    ):
        self.change_position(x=self.x + round(self._speed.x * self._direction.x * dt))

        screen_border_collision = self._check_screen_border_collision(
            screen_width, screen_height
        )
        brick_collisions = self._check_brick_collisions(bricks)

        if brick_collisions:
            self._direction.x *= -1
            self._handle_brick_collision(brick_collisions)

        if self._is_colliding_with_bat(bat):
            is_ball_moving_in_right_direction = self._speed.x < 0
            if is_ball_moving_in_right_direction:
                self.change_position(x=(self.rect.right + self.rect.width + 1))

            is_ball_moving_in_right_direction = self._speed.x > 0
            if is_ball_moving_in_right_direction:
                self.change_position(x=(self.rect.left - self.rect.width - 1))

            self._direction.x *= -1

        if screen_border_collision:
            if screen_border_collision == ScreenBorder.LEFT:
                self.change_position(x=1)
                self._direction.x *= -1

            if screen_border_collision == ScreenBorder.RIGHT:
                self.change_position(x=(screen_width - self.rect.width - 1))
                self._direction.x *= -1

    def _update_on_y_axis(
        self,
        dt: float,
        screen_width: int,
        screen_height: int,
        bat: Bat,
        bricks: Group[Brick],  # pyright: ignore[reportInvalidTypeArguments]
    ):
        self.change_position(y=(self.y + round(self._speed.y * self._direction.y * dt)))

        screen_border_collision = self._check_screen_border_collision(
            screen_width, screen_height
        )
        brick_collisions = self._check_brick_collisions(bricks)

        if brick_collisions:
            self._direction.y *= -1
            self._handle_brick_collision(brick_collisions)

        if self._is_colliding_with_bat(bat):
            self.change_position(y=(bat.rect.top - bat.rect.height - 1))
            self._direction.y *= -1

        if screen_border_collision:
            if screen_border_collision == ScreenBorder.UPPER:
                self.change_position(y=1)
                self._direction.y *= -1

            if (
                screen_border_collision == ScreenBorder.BOTTOM
                and self._on_bottom_screen_collision_handler
            ):
                self._on_bottom_screen_collision_handler()

    @override
    def update(
        self,
        screen_width: int,
        screen_height: int,
        dt: float,
        bat: Bat,
        bricks: Group[Brick],  # pyright: ignore[reportInvalidTypeArguments]
    ):
        self._update_on_x_axis(dt, screen_width, screen_height, bat, bricks)
        self._update_on_y_axis(dt, screen_width, screen_height, bat, bricks)
