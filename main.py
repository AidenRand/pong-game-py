import pygame
import time
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


def make_borders():
    top_border = pygame.Rect(0, 0, 1000, 5)
    bottom_border = pygame.Rect(0, 595, 1000, 5)
    pygame.draw.rect(screen, white, top_border)
    pygame.draw.rect(screen, white, bottom_border)


# Make paddles
def make_paddles():
    global p1, left_paddle, right_paddle
    new_paddle1 = paddles.Paddles(
        screen, left_paddle, right_paddle, p1, 10, 50, screen_height, white
    )
    new_paddle1.draw_paddles()
    new_paddle1.stop_paddles()


p1 = 280
p2 = 280
# Create left and right paddle
left_paddle = pygame.Rect(10, p1, 10, 40)
right_paddle = pygame.Rect(980, p2, 10, 40)

text_font = pygame.font.Font("fonts/8_bit_party/8_bit_party.ttf", 50)


def draw_left_score(text, font, text_col, x, y):
    left_text = font.render(text, True, text_col)
    screen.blit(left_text, (x, y))


def draw_right_score(text, font, text_col, x, y):
    right_text = font.render(text, True, text_col)
    screen.blit(right_text, (x, y))


# Make ball move
def make_ball():
    global x_speed, y_speed, x, y, left_score, right_score
    start_time = time.time()

    new_ball = ball.Ball(
        screen, screen_height, moving_ball, x_speed, y_speed, x, y, white
    )

    if moving_ball.bottom >= 595:
        y_speed = -3

    elif moving_ball.top <= 5:
        y_speed = 3

    # Reset the ball if it goes off screen
    if moving_ball.right >= 1050:
        # new_ball.reset_ball()
        left_score += 1
        time.sleep(2)
        moving_ball.x = x
        moving_ball.y = y
        start_input = pygame.key.get_pressed()
        if start_input[pygame.K_SPACE]:
            moving_ball.x = x
            moving_ball.y = y

    if moving_ball.left <= -50:
        # new_ball.reset_ball()
        right_score += 1
        time.sleep(2)
        moving_ball.x = x
        moving_ball.y = y
        start_input = pygame.key.get_pressed()
        if start_input[pygame.K_SPACE]:
            moving_ball.x = x
            moving_ball.y = y

    new_ball.draw_ball()
    new_ball.move_ball()


x, y = 494, 290
moving_ball = pygame.Rect(x, y, 10, 10)
x_speed, y_speed = 10, 3

left_score = 0
right_score = 0


# Draw vertical dotted line in center of screen
def draw_dotted_line():
    for i in range(32, 590, 5):
        if i % 2 == 0:
            pygame.draw.line(screen, white, (499, i - 10), (499, i), 3)
        if i % 2 != 0:
            pygame.draw.line(screen, (5, 5, 5), (499, i - 10), (499, i), 3)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((5, 5, 5))

    draw_left_score(str(left_score), text_font, white, 390, 20)
    draw_right_score(str(right_score), text_font, white, 580, 20)

    # Control the first player paddle with w and s
    key_input1 = pygame.key.get_pressed()
    if key_input1[pygame.K_w]:
        left_paddle.y -= 13
    if key_input1[pygame.K_s]:
        left_paddle.y += 13

    # Control the second player paddle with up and down arrows
    key_input2 = pygame.key.get_pressed()
    if key_input2[pygame.K_UP]:
        right_paddle.y -= 13
    if key_input2[pygame.K_DOWN]:
        right_paddle.y += 13

    # Reverse direction when ball collides with paddle1
    collision_tolerance = 10
    if moving_ball.colliderect(left_paddle):
        if abs(left_paddle.right - moving_ball.left) < collision_tolerance:
            x_speed *= -1

    collision_tolerance = 10
    if moving_ball.colliderect(left_paddle):
        if abs(left_paddle.top - moving_ball.bottom) < collision_tolerance:
            x_speed *= -1

    collision_tolerance = 10
    if moving_ball.colliderect(left_paddle):
        if abs(left_paddle.bottom - moving_ball.top) < collision_tolerance:
            y_speed *= -1

    # Reverse direction when ball collides with paddle 2
    if moving_ball.colliderect(right_paddle):
        if abs(right_paddle.left - moving_ball.right) < collision_tolerance:
            x_speed *= -1

    if moving_ball.colliderect(right_paddle):
        if abs(right_paddle.top - moving_ball.bottom) < collision_tolerance:
            y_speed *= -1

    if moving_ball.colliderect(right_paddle):
        if abs(right_paddle.bottom - moving_ball.top) < collision_tolerance:
            y_speed *= -1

    make_borders()
    draw_dotted_line()
    make_ball()
    make_paddles()
    clock.tick(60)
    pygame.display.flip()
