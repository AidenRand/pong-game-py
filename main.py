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
    global p1, p2
    pygame.draw.rect(screen, (white), (p1, p2, 10, 30))
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        p1 -= 5
    if key_input[pygame.K_RIGHT]:
        p1 += 5
    if key_input[pygame.K_UP]:
        p2 -= 5
    if key_input[pygame.K_DOWN]:
        p2 += 5


p1 = 10
p2 = 10


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
