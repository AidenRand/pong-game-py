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

    if moving_ball.left >= screen_width or moving_ball.right <= 0:
        x_speed *= -1

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
background = (5, 5, 5)
screen.fill(background)

white = (200, 200, 200)


# Draw vertical dotted line in center of screen
def draw_dotted_line():
    for i in range(32, 590, 5):
        if i % 2 == 0:
            pygame.draw.line(screen, white, (499, i - 10), (499, i), 5)
        if i % 2 != 0:
            pygame.draw.line(screen, (5, 5, 5), (499, i - 10), (499, i), 5)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((5, 5, 5))
    draw_dotted_line()
    move_ball()
    clock.tick(60)
    pygame.display.flip()
