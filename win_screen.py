from pathlib import Path

import pygame
from pygame.font import Font


class WinScreen:
    def __init__(self, screen_width: int, screen_height: int) -> None:
        self._font: Font = Font(pygame.font.get_default_font(), 120)
        original_image = pygame.image.load(
            Path("./resources/textures/win_screen.png")
        ).convert_alpha()
        scaled_image = pygame.transform.scale(
            original_image, (screen_width, screen_height)
        )
        self.image: pygame.Surface = scaled_image

    def draw(self, screen: pygame.Surface, score: int):
        game_over_text_surface = self._font.render(f"+{score}", True, "white")

        _ = screen.blit(self.image, (0, 0))

        _ = screen.blit(
            game_over_text_surface,
            (
                500,
                200,
            ),
        )
