import pygame
from player.player import Player
from enemy.enemy_spawner import EnemySpawner
from input.input_manager import InputManager
import game_object

BG = (255, 0, 0)

# 1. Init pygame
pygame.init()

# 2. Set screen
SIZE = (600, 800)
canvas = pygame.display.set_mode(SIZE)

# 3. Clock
clock = pygame.time.Clock()

loop = True

input_manager = InputManager()

player = Player(400, 580, input_manager)

game_object.add(player)
game_object.add(EnemySpawner())

while loop:
    # 1. Event processing
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            input_manager.update(event)

    game_object.update()

    # 2. Draw
    canvas.fill(BG)

    game_object.render(canvas)

    pygame.display.set_caption('Micro game')

    # 3. Flip
    pygame.display.flip()
    clock.tick(60)