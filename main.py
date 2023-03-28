import pygame

background_color = (1, 1, 1)
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Pong")
screen.fill(background_color)
pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
