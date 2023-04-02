import pygame
import ball

pygame.init()
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")
background = (5, 5, 5)
screen.fill(background)

white = (200, 200, 200)


def stop_paddle():
    global p1, p2, player_paddle1, player_paddle2
    pygame.draw.rect(screen, white, player_paddle1)
    pygame.draw.rect(screen, white, player_paddle2)

    # Paddle collision with top and bottom of window
    if player_paddle1.bottom >= screen_height:
        player_paddle1.y -= 10
    elif player_paddle1.top <= 0:
        player_paddle1.y += 10

    if player_paddle2.bottom >= screen_height:
        player_paddle2.y -= 10
    elif player_paddle2.top <= 0:
        player_paddle2.y = 10


p1 = 20
p2 = 20
player_paddle1 = pygame.Rect(10, p1, 10, 40)
player_paddle2 = pygame.Rect(980, p2, 10, 40)


# Make ball move
def move_ball():
    global x_speed, y_speed
    moving_ball.x += x_speed
    moving_ball.y += y_speed

    # Collision with top and bottom screen
    if moving_ball.bottom >= screen_height:
        y_speed -= 4

    elif moving_ball.top <= 0:
        y_speed += 4

    if moving_ball.left >= screen_width:
        x_speed -= 5
    elif moving_ball.right <= 0:
        x_speed += 5

    pygame.draw.rect(screen, white, moving_ball)


moving_ball = pygame.Rect(494, 290, 10, 10)
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
    stop_paddle()
    clock.tick(60)
    pygame.display.flip()
