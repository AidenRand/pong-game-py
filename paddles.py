import pygame


class Paddles:
    def __init__(
        self, screen, left_paddle, right_paddle, p1, width, height, screen_height, color
    ):
        self.screen = screen
        self.left_paddle = left_paddle
        self.right_paddle = right_paddle
        self.p1 = p1
        self.width = width
        self.height = height
        self.screen_height = screen_height
        self.color = color

    def draw_paddles(self):
        pygame.draw.rect(self.screen, self.color, self.left_paddle)
        pygame.draw.rect(self.screen, self.color, self.right_paddle)

    def stop_paddles(self):
        # Left paddle collision with top and bottom of screen
        if self.left_paddle.bottom >= self.screen_height:
            self.left_paddle.y -= 10
        elif self.left_paddle.top <= 0:
            self.left_paddle.y += 10

        # Right paddle collision with top and bottom of screen
        if self.right_paddle.bottom >= self.screen_height:
            self.right_paddle.y -= 10
        elif self.right_paddle.top <= 0:
            self.right_paddle.y += 10
