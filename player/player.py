import pygame
from player.player_bullet import PlayerBullet
import game_object
from game_object import GameObject
from frame_counter import FrameCounter


# 3 class Cat, Rock, Rain
class Player(GameObject):
    # 1. Create constructor (properties)
    def __init__(self, x, y, input_manager):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load('images/player/player1.png')
        self.input_manager = input_manager
        self.shoot_lock = False
        self.counter = FrameCounter(20)

    # 2. Describe action / method / behavior
    def update(self):
        GameObject.update(self)
        self.move()
        self.shoot()

    def move(self):
        dx = 0
        dy = 0

        if self.input_manager.right_pressed:
            dx += 5
        if self.input_manager.left_pressed:
            dx -= 5
        if self.input_manager.down_pressed:
            dy += 5
        if self.input_manager.up_pressed:
            dy -= 5

        self.x += dx
        self.y += dy

    def shoot(self):
        if self.input_manager.x_pressed and not self.shoot_lock:
            game_object.recycle(PlayerBullet, self.x, self.y - 40)
            self.shoot_lock = True

        if self.shoot_lock:
            self.counter.run()
            if self.counter.expired:
                self.shoot_lock = False
                self.counter.reset()
