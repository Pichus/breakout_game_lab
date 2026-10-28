from pygame import Surface
from pygame.time import Clock

from ball import Ball
from brick import Brick
from bat import Bat


class Game:
    def __init__(self) -> None:
        # self.ball: Ball = Ball(700, 300)

        self.ball: Ball = Ball(0, 0)

        # self.bricks: list[Brick] = [Brick(100, 100)]

        self.bricks: list[Brick] = [Brick(0, 0)]

        self.bat: Bat = Bat(0, 0)

        # self.bat: Bat = Bat(screen.get_width() // 2, 0)
        # self.bat.y = screen.get_height() - self.bat.rect.height
        # self.bat.rect.y = self.bat.y
        pass

    def update(self, screen: Surface, clock: Clock):
        self.ball.update(screen, clock, self.bat)
        self.bat.update()
        pass
