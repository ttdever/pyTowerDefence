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
    iter_x = iter_y = 0
    for x in range(0, variables.WIDTH, variables.TILE_SIZE):
        iter_x += 1
        for y in range(0, variables.HEIGHT, variables.TILE_SIZE):
            iter_y += 1
            rect = pygame.Rect(x, y, variables.TILE_SIZE, variables.TILE_SIZE)
            pygame.draw.rect(variables.window, variables.gridColor, rect, 1)
            variables.tiles[iter_x][iter_y] = (x, y)

