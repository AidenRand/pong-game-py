import pygame
import main

p2 = 10
player_paddle = pygame.draw.rect(main.screen, (main.white), (10, p2, 10, 30))


def move_paddle():
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_UP]:
        p2 -= 5
    if key_input[pygame.K_DOWN]:
        p2 += 5
