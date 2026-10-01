from pygame import surface
import random
import pygame


class Anvil:
    def __init__(self, screen_width):
        self.screen_width = screen_width
        self.width = 40
        self.height = 32
        self.x = random.randint(20, screen_width - self.width - 20)
        self.y = -self.height
        self.speed = random.uniform(4.5, 7.0)

    def update(self):
        self.y += self.speed

    def is_off_screen(self, screen_height):
        return self.y > screen_height + 10

    @property
    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)

    def render(self, surface):
        # Change anvil color based on falling speed
        if self.speed >= 6.5:
            top_color = (220, 60, 50)      # Red
            base_color = (170, 40, 35)
        elif self.speed >= 5.5:
            top_color = (230, 140, 50)     # Orange
            base_color = (190, 95, 35)
        else:
            top_color = (120, 120, 130)    # Normal gray
            base_color = (80, 80, 90)

        top_rect = pygame.Rect(
        int(self.x) + 4,
        int(self.y),
        self.width - 8,
        14)
        pygame.draw.rect(
        surface,
        top_color,
        top_rect,
        border_radius=2)

        base_rect = pygame.Rect(
        int(self.x),
        int(self.y) + 14,
        self.width,
        18)
        pygame.draw.rect(
        surface,
        base_color,
        base_rect,
        border_radius=3)

        pygame.draw.rect(
        surface,
        (200, 200, 210),
        base_rect,
        width=1,
        border_radius=3)