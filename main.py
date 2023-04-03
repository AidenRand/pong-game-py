import pygame
import ball
import paddle1
import paddle2

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
def make_paddle1():
    global p1, player_paddle1
    new_paddle1 = paddle1.Paddle1(
        screen, player_paddle1, p1, 10, 50, screen_height, white
    )
    new_paddle1.draw_paddle1()
    new_paddle1.stop_paddle1()


# make player two paddle
def make_paddle2():
    global p2, player_paddle2
    new_paddle2 = paddle2.Paddle2(
        screen, player_paddle2, p2, 10, 50, screen_height, white
    )
    new_paddle2.draw_paddle2()
    new_paddle2.stop_paddle2()


p1 = 20
p2 = 20
player_paddle1 = pygame.Rect(10, p1, 10, 40)
player_paddle2 = pygame.Rect(980, p2, 10, 40)


# Make ball move
def move_ball():
    global x_speed, y_speed

    new_ball = ball.Ball(screen, screen_height, moving_ball, x_speed, y_speed, white)
    new_ball.draw_ball()
    new_ball.move_ball()
    if moving_ball.bottom >= screen_height:
        y_speed -= 4

    elif moving_ball.top <= 0:
        y_speed += 4


moving_ball = pygame.Rect(494, 290, 10, 10)
x_speed, y_speed = 4, 4


def game_logic():
    if moving_ball.left > screen_width:
        print("passed on left")

    if moving_ball.right < 0:
        print("passed on right")


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
        player_paddle1.y -= 10
    if key_input1[pygame.K_s]:
        player_paddle1.y += 10

    # Control the second player paddle with up and down arrows
    key_input2 = pygame.key.get_pressed()
    if key_input2[pygame.K_UP]:
        player_paddle2.y -= 10
    if key_input2[pygame.K_DOWN]:
        player_paddle2.y += 10

        # Reverse direction when ball collides with paddle1
    collision_tolerance = 10
    if moving_ball.colliderect(player_paddle1):
        if abs(player_paddle1.right - moving_ball.left) < collision_tolerance:
            x_speed *= -1

    if moving_ball.colliderect(player_paddle2):
        if abs(player_paddle2.left - moving_ball.right) < collision_tolerance:
            x_speed *= -1

    draw_dotted_line()
    move_ball()
    make_paddle1()
    make_paddle2()
    game_logic()
    clock.tick(60)
    pygame.display.flip()
