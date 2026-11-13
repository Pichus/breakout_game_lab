from typing import Callable

import pygame
from pygame.font import Font


class GameBoard:
    _score: int
    _lives: int
    _font: Font
    _on_lost_all_lives_handler: Callable[[], None] | None

    def __init__(self) -> None:
        self._score = 0
        self._lives = 3
        self._font = Font(pygame.font.get_default_font(), 36)
        self._on_lost_all_lives_handler = None

    @property
    def score(self) -> int:
        return self._score

    @property
    def lives(self) -> int:
        return self._lives

    def on_lost_all_lives(self, function: Callable[[], None]):
        self._on_lost_all_lives_handler = function

    def update(self, score: int = 0, lives: int = 3):
        self._score = score

        if lives == 0 and self._on_lost_all_lives_handler:
            self._on_lost_all_lives_handler()
        self._lives = lives

    def draw(self, screen: pygame.Surface):
        lives_text_surface = self._font.render(f"Lives: {self._lives}", True, "red")
        score_text_surface = self._font.render(f"Score: {self._score}", True, "blue")

        _ = screen.blit(lives_text_surface, (0, 0))
        _ = screen.blit(
            score_text_surface, (screen.get_width() - score_text_surface.get_width(), 0)
        )
