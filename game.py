from pygame import Surface, Vector2
import pygame
from pygame.key import ScancodeWrapper
from pygame.sprite import Group

from ball import Ball
from brick import Brick
from bat import Bat


class Game:
    def __init__(self) -> None:
        # self.ball: Ball = Ball(700, 300)

        self.ball: Ball = Ball(0, 0)

        self.bricks: Group[Brick] = Group()  # pyright: ignore[reportInvalidTypeArguments]
        self.bricks.add(Brick(0, 0))

        self.bat: Bat = Bat(
            200,
            0,
        )

        self.bat.y = 1000 - self.bat.rect.height
        self.bat.rect.y = self.bat.y
        pass

    def move_sprites_to_initial_positions(self, screen_width: int, screen_height: int):
        self.ball.change_position(Vector2(700, 300))
        self.bat.change_position(
            Vector2(screen_width // 2, screen_height - self.bat.rect.height)
        )

    def update(self, screen: Surface, dt: float):
        self.ball.update(screen, dt, self.bat)
        self.bat.update(dt)

    def draw_frame(self, screen: Surface):
        _ = self.bat.draw(screen)
        _ = self.ball.draw(screen)

    def on_key_press(self, keys_pressed: ScancodeWrapper):
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            self.bat.move_left()
        elif keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            self.bat.move_right()
