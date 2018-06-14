import pygame
from game_object import GameObject


class Enemy(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("images/enemy/bacteria1.png")

    def update(self):
        GameObject.update(self)
        self.y += 3
