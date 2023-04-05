import pygame
import ball
import paddles


pygame.init()
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")
background = (5, 5, 5)
screen.fill(background)

white = (200, 200, 200)


# Make player one paddle
def make_paddles():
    global p1, left_paddle, right_paddle
    new_paddle1 = paddles.Paddles(
        screen, left_paddle, right_paddle, p1, 10, 50, screen_height, white
    )
    new_paddle1.draw_paddles()
    new_paddle1.stop_paddles()


p1 = 20
p2 = 20
left_paddle = pygame.Rect(10, p1, 10, 40)
right_paddle = pygame.Rect(980, p2, 10, 40)


# Make ball move
def move_ball():
    global x_speed, y_speed, x, y
    x = 0
    y = 0

    new_ball = ball.Ball(screen, screen_height, moving_ball, x_speed, y_speed, white)
    new_ball.move_ball()
    new_ball.draw_ball()
    if moving_ball.bottom >= screen_height:
        y_speed -= 4

    elif moving_ball.top <= 0:
        y_speed += 4

    if moving_ball.right >= screen_width:
        x_speed -= 4
        new_ball.reset_ball()

    elif moving_ball.left <= 0:
        x_speed += 4
        new_ball.reset_ball()


def reset_ball(ball):
    moving_ball = pygame.Rect(0, 0, 10, 10)
    return moving_ball


x, y = 494, 290
moving_ball = pygame.Rect(x, y, 10, 10)
x_speed, y_speed = 4, 4


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

    # Control the first player paddle with w and s
    key_input1 = pygame.key.get_pressed()
    if key_input1[pygame.K_w]:
        left_paddle.y -= 10
    if key_input1[pygame.K_s]:
        left_paddle.y += 10

    # Control the second player paddle with up and down arrows
    key_input2 = pygame.key.get_pressed()
    if key_input2[pygame.K_UP]:
        right_paddle.y -= 10
    if key_input2[pygame.K_DOWN]:
        right_paddle.y += 10

        # Reverse direction when ball collides with paddle1
    collision_tolerance = 10
    if moving_ball.colliderect(left_paddle):
        if abs(left_paddle.right - moving_ball.left) < collision_tolerance:
            x_speed *= -1

    if moving_ball.colliderect(right_paddle):
        if abs(right_paddle.left - moving_ball.right) < collision_tolerance:
            x_speed *= -1

    draw_dotted_line()
    move_ball()
    make_paddles()
    clock.tick(60)
    pygame.display.flip()
