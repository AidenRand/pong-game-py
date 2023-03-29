import pygame
import ball


# Make ball move
def move_ball():
    global x_speed, y_speed
    moving_ball.x += x_speed
    moving_ball.y += y_speed

    # Collision with top and bottom screen
    if moving_ball.bottom >= screen_height or moving_ball.top <= 0:
        y_speed *= -1

    pygame.draw.rect(screen, white, moving_ball)


moving_ball = ball.moving_ball
x_speed = ball.x_speed
y_speed = ball.y_speed

pygame.init()
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")
screen.fill((5, 5, 5))

white = (200, 200, 200)


# Draw vertical dotted line in center of screen
def draw_dotted_line():
    for i in range(32, 590, 5):
        if i % 2 == 0:
            pygame.draw.line(screen, white, (499, i - 10), (499, i), 5)
        if i % 2 != 0:
            pygame.draw.line(screen, (5, 5, 5), (499, i - 10), (499, i), 5)


draw_dotted_line()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    move_ball()
    pygame.display.flip()
    clock.tick(60)
