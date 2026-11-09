from pygame import Surface, Vector2
import pygame
from pygame.font import Font
from pygame.key import ScancodeWrapper
from pygame.sprite import Group

from ball import Ball
from brick import Brick
from bat import Bat
from brick_type import BrickType
from game_board import GameBoard
from game_over_screen import GameOverScreen
from game_status import GameStatus
from stronger_brick import StrongerBrick


class Game:
    def __init__(self, screen_width: int, screen_height: int) -> None:
        self.screen_width: int = screen_width
        self.screen_height: int = screen_height

        self.game_over_screen: GameOverScreen = GameOverScreen()

        self.game_status: GameStatus = GameStatus.RUNNING

        self.game_board: GameBoard = GameBoard()
        self.game_board.on_lost_all_lives(lambda: self.on_lost_all_lives_handler())

        self.ball: Ball = Ball()
        self.ball.on_bottom_screen_collision(
            lambda: self.on_bottom_screen_collision_handler()
        )

        self.bat: Bat = Bat()

        self.bricks: Group[Brick] = Group()  # pyright: ignore[reportInvalidTypeArguments]

        for brick in self.bricks:
            brick.on_zero_health(
                lambda points: self.on_brick_zero_health_handler(points)
            )

        self.font: Font = Font(pygame.font.get_default_font(), 36)

        self.brick_layout: list[list[BrickType]] = [
            [
                BrickType.STRONGER,
                BrickType.STRONGER,
                BrickType.STRONGER,
                BrickType.BASIC,
                BrickType.BASIC,
                BrickType.STRONGER,
                BrickType.STRONGER,
                BrickType.STRONGER,
            ],
            [
                BrickType.STRONGER,
                BrickType.STRONGER,
                BrickType.BASIC,
                BrickType.BASIC,
                BrickType.BASIC,
                BrickType.BASIC,
                BrickType.STRONGER,
                BrickType.STRONGER,
            ],
            [
                BrickType.STRONGER,
                BrickType.BASIC,
                BrickType.BASIC,
                BrickType.BASIC,
                BrickType.BASIC,
                BrickType.BASIC,
                BrickType.BASIC,
                BrickType.STRONGER,
            ],
        ]

    def on_brick_zero_health_handler(self, points: int):
        self.game_board.update(self.game_board.score + points, self.game_board.lives)

    def move_sprites_to_initial_positions(self):
        self.move_ball_to_initial_position()
        self.move_bat_to_initial_position()
        self.position_bricks()

    def position_bricks(self):
        basic_brick = Brick()

        brick_height = basic_brick.rect.height
        brick_width = basic_brick.rect.width
        horizontal_margin_between_bricks = 20
        vertical_margin_between_bricks = 10
        bricks_per_row = len(self.brick_layout[0])

        row_width = (bricks_per_row * brick_width) + (
            (bricks_per_row - 1) * horizontal_margin_between_bricks
        )

        starting_x_coordinate = (self.screen_width - row_width) // 2
        starting_y_coordingate = 50

        for row in range(0, len(self.brick_layout)):
            for col in range(0, len(self.brick_layout[row])):
                x_coordinate = starting_x_coordinate
                if col > 0:
                    x_coordinate += (col * brick_width) + (
                        col * horizontal_margin_between_bricks
                    )

                y_coordinate = starting_y_coordingate

                if row > 0:
                    y_coordinate += (row * brick_height) + (
                        row * vertical_margin_between_bricks
                    )

                brick: Brick = Brick()
                current_brick_type = self.brick_layout[row][col]

                if current_brick_type == BrickType.STRONGER:
                    brick = StrongerBrick()

                brick.change_position(Vector2(x_coordinate, y_coordinate))

                self.bricks.add(brick)

    def move_ball_to_initial_position(self):
        self.ball.change_position(
            Vector2(
                (self.screen_width // 2) - (self.ball.rect.width // 2),
                self.screen_height // 2,
            )
        )

    def on_bottom_screen_collision_handler(self):
        self.game_board.update(self.game_board.score, self.game_board.lives - 1)
        self.move_ball_to_initial_position()
        self.move_bat_to_initial_position()

    def on_lost_all_lives_handler(self):
        self.game_status = GameStatus.GAME_OVER

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

        for brick in self.bricks:
            _ = brick.draw(screen)

    def on_key_press(self, keys_pressed: ScancodeWrapper):
        left_direction = Vector2(-1, 0)
        right_direction = Vector2(1, 0)

        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            self.bat.move(left_direction, self.screen_width)
        elif keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            self.bat.move(right_direction, self.screen_width)
