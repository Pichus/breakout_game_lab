import pygame

from ball import Ball
from brick import Brick
import constants
from bat import Bat

pygame.init()

display_info = pygame.display.Info()
display_width = display_info.current_w
display_height = display_info.current_h

screen = pygame.display.set_mode(
    (display_width, display_height), pygame.FULLSCREEN | pygame.SCALED
)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        # elif event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        #        trampoline.move_left()
        #    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        #        trampoline.move_right()

    screen.fill("purple")

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        trampoline.move_left()
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        trampoline.move_right()

    brick.draw(screen)

    trampoline.draw(screen)

    ball.update(screen, clock, trampoline)
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(constants.FPS)
