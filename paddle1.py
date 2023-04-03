import pygame


class Paddle1:
    def __init__(self, screen, player_paddle1, p1, width, height, screen_height, color):
        self.screen = screen
        self.player_paddle1 = player_paddle1
        self.p1 = p1
        self.width = width
        self.height = height
        self.screen_height = screen_height
        self.color = color

    def draw_paddle1(self):
        pygame.draw.rect(self.screen, self.color, self.player_paddle1)

    def stop_paddle1(self):
        # Paddle collision with top and bottom of window
        if self.player_paddle1.bottom >= self.screen_height:
            self.player_paddle1.y -= 10
        elif self.player_paddle1.top <= 0:
            self.player_paddle1.y += 10
