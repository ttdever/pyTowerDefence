import sys
import pygame
import variables
from array import *


# Start of program:
def initGame():
    variables.window = pygame.display.set_mode((variables.WIDTH, variables.HEIGHT))
    variables.window.fill(variables.bgColor)
    drawGrid()


# Call every frame (unity update analog)
def tickGame():
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)


# Creates tiles
def drawGrid():
    variables.tiles.append([])
    iter_x = iter_y = 0
    for x in range(0, variables.WIDTH, variables.TILE_SIZE):
        for y in range(0, variables.HEIGHT, variables.TILE_SIZE):
            rect = pygame.Rect(x, y, variables.TILE_SIZE, variables.TILE_SIZE)
            pygame.draw.rect(variables.window, variables.gridColor, rect, 1)
            pygame.draw.circle(variables.window, (255,0,0), (x + variables.TILE_SIZE/2, y + variables.TILE_SIZE/2), 1, 1)
            variables.tiles.append((x, y))
            iter_y += 1
        iter_y = 0
        iter_x += 1
