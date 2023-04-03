import pygame


class Paddle2:
    def __init__(self, screen, player_paddle2, p2, width, height, screen_height, color):
        self.screen = screen
        self.player_paddle2 = player_paddle2
        self.p2 = p2
        self.width = width
        self.height = height
        self.screen_height = screen_height
        self.color = color

    def draw_paddle2(self):
        pygame.draw.rect(self.screen, self.color, self.player_paddle2)

    def stop_paddle2(self):
        # Paddle collision with top and bottom of window
        if self.player_paddle2.bottom >= self.screen_height:
            self.player_paddle2.y -= 10
        elif self.player_paddle2.top <= 0:
            self.player_paddle2.y += 10
