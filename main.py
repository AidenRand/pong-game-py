import pygame
import math

background_color = (1, 1, 1)
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Pong")
screen.fill(background_color)

white = (255, 255, 255)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    def draw_dotted_line():
        for i in range(32, 590, 5):
            if i % 2 == 0:
                pygame.draw.line(screen, (255, 255, 255), (499, i - 10), (499, i), 5)
            if i % 2 != 0:
                pygame.draw.line(screen, (0, 0, 0), (499, i - 10), (499, i), 5)

    draw_dotted_line()

    pygame.display.flip()
