import pygame

import constants
from game import Game

_ = pygame.init()

display_info = pygame.display.Info()
display_width = display_info.current_w
display_height = display_info.current_h

screen = pygame.display.set_mode(
    (display_width, display_height), pygame.FULLSCREEN | pygame.SCALED
)

clock = pygame.time.Clock()

game = Game(screen.get_width(), screen.get_height())

dt = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    keys = pygame.key.get_pressed()
    game.on_key_press(keys)

    game.update(screen.get_width(), screen.get_height(), dt)
    game.draw_frame(screen)

    pygame.display.flip()

    dt = clock.tick(constants.FPS) / 1000
