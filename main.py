import pygame
import ball

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


def move_paddle():
    global p1
    player_paddle = pygame.Rect(10, p1, 10, 40)
    pygame.draw.rect(screen, white, player_paddle)

    # Paddle collision with top and bottom of window
    if player_paddle.bottom >= screen_height:
        p1 += -10
    elif player_paddle.top <= 0:
        p1 -= -10

    # Control paddle with up and down arrows
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_UP]:
        p1 -= 10
    if key_input[pygame.K_DOWN]:
        p1 += 10


p1 = 20


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
    ball.move_ball()
    move_paddle()
    clock.tick(60)
    pygame.display.flip()
