from pygame import Surface
import pygame
from pygame.font import Font


class GameOverScreen:
    def __init__(self) -> None:
        self._font: Font = Font(pygame.font.get_default_font(), 72)

    def draw(self, screen: Surface, score: int):
        game_over_text_surface = self._font.render(
            f"Game over! Score: {score}", True, "red"
        )

        _ = screen.fill("black")

        _ = screen.blit(
            game_over_text_surface,
            (
                (screen.get_width() // 2) - (game_over_text_surface.get_width() // 2),
                (screen.get_height() // 2) - (game_over_text_surface.get_height() // 2),
            ),
        )
