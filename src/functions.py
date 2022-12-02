import sys
import pygame
import variables
import math
import classes
import numpy as np


# Start of program:
def initGame():
    variables.window = pygame.display.set_mode((variables.WIDTH, variables.HEIGHT))
    variables.clock = pygame.time.Clock()
    drawGrid()
    calculateTiles()


# Call every frame (unity update analog)
def tickGame():
    variables.clock.tick(variables.FPS)
    checkInputs()
    checkPhysics()
    checkDraw()
    pygame.display.update()


def checkDraw():
    drawGrid()
    drawSelectedTile()


def checkInputs():
    checkExit()


def checkPhysics():
    pass


# Check mouse position :|
def drawSelectedTile():
    mousePosition = pygame.mouse.get_pos()
    closestTile = findClosestTile(mousePosition)
    selectedTile = pygame.Rect(closestTile.getPosition()[0] - variables.TILE_SIZE / 2 + 1,
                               closestTile.getPosition()[1] - variables.TILE_SIZE / 2 + 1, variables.TILE_SIZE - 2,
                               variables.TILE_SIZE - 2)
    selectionColor = np.add(closestTile.getColor(), variables.selectedTileColorShift)
    pygame.draw.rect(variables.window, (selectionColor[0], selectionColor[1], selectionColor[2]), selectedTile, 30)


# Find the closest tile to mouse position by iterating through array with tiles
def findClosestTile(mousePos):
    result = variables.tiles[0]
    selectedTilePos = result.getPosition()
    for tile in variables.tiles:
        coordinates = tile.getPosition()
        if math.dist(coordinates, mousePos) < math.dist(selectedTilePos, mousePos):
            selectedTilePos = coordinates
            result = tile
    return result


# Checks for exit input
def checkExit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)


# Creates tiles and writes tile centers to "variables.tiles"
def drawGrid():
    variables.window.fill(variables.bgColor)
    for x in range(0, variables.WIDTH, variables.TILE_SIZE):
        for y in range(0, variables.HEIGHT, variables.TILE_SIZE):
            rect = pygame.Rect(x, y, variables.TILE_SIZE, variables.TILE_SIZE)
            pygame.draw.rect(variables.window, variables.gridColor, rect, 1)


def calculateTiles():
    for x in range(0, variables.WIDTH, variables.TILE_SIZE):
        for y in range(0, variables.HEIGHT, variables.TILE_SIZE):
            variables.tiles.append(
                classes.Tile((x + variables.TILE_SIZE / 2, y + variables.TILE_SIZE / 2),
                             variables.bgColor,
                             classes.TileType.Ground))
