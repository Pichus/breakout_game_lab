import pygame
from pygame.font import Font


class GameBoard:
    def __init__(self) -> None:
        self.score: int = 0
        self.lives: int = 3
        self.font: Font = Font(pygame.font.get_default_font(), 36)

    def update(self, score: int = 0, lives: int = 3):
        self.score = score
        self.lives = lives

    def draw(self, screen: pygame.Surface):
        lives_text_surface = self.font.render(f"Lives: {self.lives}", True, "red")
        score_text_surface = self.font.render(f"Score: {self.score}", True, "blue")

        _ = screen.blit(lives_text_surface, (0, 0))
        _ = screen.blit(
            score_text_surface, (screen.get_width() - score_text_surface.get_width(), 0)
        )
