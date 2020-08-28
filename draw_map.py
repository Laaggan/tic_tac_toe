import pygame
from math import floor
import numpy as np

pygame.init()
grid_size = 16

world_map = np.loadtxt('map.txt')

w = world_map.shape[0]
h = world_map.shape[1]

screen = pygame.display.set_mode((w*grid_size, h*grid_size))
pygame.display.set_caption("Tic Tac Toe")

sprites_img = pygame.image.load('gfx/Overworld.png')

def get_current_tile(current_tile_value):
    if current_tile_value == 0:
        current_tile = sprites_img.subsurface((0*16, 0*16, 16, 16))
    elif current_tile_value == 1:
        current_tile = sprites_img.subsurface((1*16, 0*16, 16, 16))
    elif current_tile_value == 2:
        current_tile = sprites_img.subsurface((0*16, 1*16, 16, 16))
    return  current_tile

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((100, 100, 100))

    for i in range(w):
        for j in range(h):
            current_tile_value = world_map[i, j]
            current_tile = get_current_tile(current_tile_value)
            screen.blit(current_tile, (16*i, 16*j))
    pygame.display.update()