from pathlib import Path
from typing import Callable, override

from pygame import Rect, Surface
import pygame
from pygame.sprite import Group
from brick import Brick
from collision_sprite import CollisionSprite
from bat import Bat


class Ball(CollisionSprite):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__(x, y)
        self.image: Surface
        self.x: int
        self.y: int

        self.x_speed: int = 600
        self.y_speed: int = 600
        self.damage: int = 1

        self._on_bottom_screen_collision_handler: Callable[[], None]

    @override
    def set_image(self):
        texture_path = Path("resources/textures/hedgehog_ball.png")
        sprite_resolution = (100, 100)
        self.image = self.load_and_scale_image(texture_path, sprite_resolution)

    def on_bottom_screen_collision(self, handler: Callable[[], None]):
        self._on_bottom_screen_collision_handler = handler

    def _handle_brick_collision(self, bricks: list[Brick]):
        for brick in bricks:
            brick.update(brick.health - self.damage)

    @override
    def update(self, screen: Surface, dt: float, bat: Bat, bricks: Group[Brick]):  # pyright: ignore[reportInvalidTypeArguments]
        self.x += round(self.x_speed * dt)
        self.rect.x = self.x

        is_colliding_with_trampoline = self.rect.colliderect(bat.rect)
        is_colliding_with_left_side_of_screen = self.rect.left < 0
        is_colliding_with_right_side_of_screen = self.rect.right > screen.get_width()
        bricks_ball_collides_with = pygame.sprite.spritecollide(self, bricks, False)  # pyright: ignore[reportArgumentType]
        is_colliding_with_bricks = len(bricks_ball_collides_with) > 0

        if is_colliding_with_bricks:
            self.x_speed = -self.x_speed
            self._handle_brick_collision(bricks_ball_collides_with)

        if is_colliding_with_trampoline:
            if self.x_speed < 0:
                self.rect.right = bat.rect.right + 1
                self.x = self.rect.right + self.rect.width + 1
            if self.x_speed > 0:
                self.rect.left = bat.rect.left - 1
                self.x = self.rect.left - self.rect.width - 1
            self.x_speed = -self.x_speed

        if is_colliding_with_left_side_of_screen:
            self.rect.left = 1
            self.x = 1
            self.x_speed = -self.x_speed

        if is_colliding_with_right_side_of_screen:
            self.rect.right = screen.get_width() - 1
            self.x = screen.get_width() - self.rect.width - 1
            self.x_speed = -self.x_speed

        self.y += round(self.y_speed * dt)
        self.rect.y = self.y

        is_colliding_with_top_of_screen = self.rect.top <= 0
        is_colliding_with_bottom_of_screen = self.rect.bottom >= screen.get_height()
        is_colliding_with_trampoline = self.rect.colliderect(bat.rect)
        bricks_ball_collides_with = pygame.sprite.spritecollide(self, bricks, False)  # pyright: ignore[reportArgumentType]
        is_colliding_with_bricks = len(bricks_ball_collides_with) > 0

        if is_colliding_with_bricks:
            self.y_speed = -self.y_speed
            self._handle_brick_collision(bricks_ball_collides_with)

        if is_colliding_with_trampoline:
            self.rect.bottom = bat.rect.top - 1
            self.y = bat.rect.top - bat.rect.height - 1
            self.y_speed = -self.y_speed

        if is_colliding_with_top_of_screen:
            self.rect.top = 1
            self.y = 1
            self.y_speed = -self.y_speed

        if is_colliding_with_bottom_of_screen:
            self._on_bottom_screen_collision_handler()
