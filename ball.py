import pygame
import main


# Make ball move
def move_ball():
    global x_speed, y_speed
    moving_ball.x += x_speed
    moving_ball.y += y_speed

    # Collision with top and bottom screen
    if moving_ball.bottom >= main.screen_height or moving_ball.top <= 0:
        y_speed *= -1

    if moving_ball.left >= main.screen_width or moving_ball.right <= 0:
        x_speed *= -1

    pygame.draw.rect(main.screen, main.white, moving_ball)


moving_ball = pygame.Rect(494, 290, 10, 10)
x_speed, y_speed = 6, 5
