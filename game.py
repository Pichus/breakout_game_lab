from pygame import Surface, Vector2
import pygame
from pygame.font import Font
from pygame.key import ScancodeWrapper
from pygame.sprite import Group

from ball import Ball
from brick import Brick
from bat import Bat
from game_board import GameBoard
from game_over_screen import GameOverScreen
from game_status import GameStatus


class Game:
    def __init__(self, screen_width: int, screen_height: int) -> None:
        self.screen_width: int = screen_width
        self.screen_height: int = screen_height

        self.game_over_screen: GameOverScreen = GameOverScreen()

        self.game_status: GameStatus = GameStatus.RUNNING

        def on_lost_all_lives_handler():
            self.game_status = GameStatus.GAME_OVER

        self.game_board: GameBoard = GameBoard()
        self.game_board.on_lost_all_lives(on_lost_all_lives_handler)

        def on_bottom_screen_collision_handler():
            self.game_board.update(self.game_board.score, self.game_board.lives - 1)
            self.move_ball_to_initial_position()
            self.move_bat_to_initial_position()

        self.ball: Ball = Ball()
        self.ball.on_bottom_screen_collision(on_bottom_screen_collision_handler)

        self.bat: Bat = Bat()

        self.bricks: Group[Brick] = Group()  # pyright: ignore[reportInvalidTypeArguments]
        self.bricks.add(Brick())

        self.font: Font = Font(pygame.font.get_default_font(), 36)

    def move_sprites_to_initial_positions(self):
        self.move_ball_to_initial_position()
        self.move_bat_to_initial_position()

    def move_ball_to_initial_position(self):
        self.ball.change_position(
            Vector2(
                (self.screen_width // 2) - (self.ball.rect.width // 2),
                self.screen_height // 2,
            )
        )

    def move_bat_to_initial_position(self):
        self.bat.change_position(
            Vector2(
                (self.screen_width // 2) - (self.bat.rect.width // 2),
                self.screen_height - self.bat.rect.height,
            )
        )

    def update(self, screen: Surface, dt: float):
        if self.game_status == GameStatus.GAME_OVER:
            return

        self.ball.update(screen, dt, self.bat)
        self.bat.update(dt)

    def draw_frame(self, screen: Surface):
        if self.game_status == GameStatus.GAME_OVER:
            self.game_over_screen.draw(screen, self.game_board.score)
            return

        _ = screen.fill("purple")
        _ = self.game_board.draw(screen)
        _ = self.bat.draw(screen)
        _ = self.ball.draw(screen)

    def on_key_press(self, keys_pressed: ScancodeWrapper):
        left_direction = Vector2(-1, 0)
        right_direction = Vector2(1, 0)

        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            self.bat.move(left_direction, self.screen_width)
        elif keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            self.bat.move(right_direction, self.screen_width)
