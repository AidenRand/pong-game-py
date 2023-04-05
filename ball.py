import pygame


class Ball:
    def __init__(self, screen, screen_height, moving_ball, x_speed, y_speed, color):
        self.screen = screen
        self.screen_height = screen_height
        self.moving_ball = moving_ball
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.color = color

    def reset_ball(self):
        self.moving_ball = pygame.Rect(494, 290, 10, 10)
        pygame.draw.rect(self.screen, self.color, self.moving_ball)

    def draw_ball(self):
        pygame.draw.rect(self.screen, self.color, self.moving_ball)

    def move_ball(self):
        print(self.y_speed)
        self.moving_ball.x += self.x_speed
        self.moving_ball.y += self.y_speed
