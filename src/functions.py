import random
import sys
import pygame
import variables
import math
import classes
import numpy as np


# Start of program:
def initGame():
    variables.window = pygame.display.set_mode((variables.WIDTH, variables.HEIGHT))
    variables.window.fill(variables.gridColor)
    variables.clock = pygame.time.Clock()
    calculateTiles()
    drawGrid()
    generatePath()


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


# Check mouse position and craw selected tile
def drawSelectedTile():
    mousePosition = pygame.mouse.get_pos()
    closestTile = findClosestTile(mousePosition)
    selectedTile = pygame.Rect(closestTile.getPosition()[0] - variables.TILE_SIZE / 2 + 1,
                               closestTile.getPosition()[1] - variables.TILE_SIZE / 2 + 1, variables.TILE_SIZE - 2,
                               variables.TILE_SIZE - 2)
    selectionColor = np.clip(np.add(closestTile.getColor(), variables.selectedTileColorShift), 0, 255)
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
    for tile in variables.tiles:
        coordinatesToDraw = tile.getPosition()
        x = coordinatesToDraw[0] - variables.TILE_SIZE / 2 + 1
        y = coordinatesToDraw[1] - variables.TILE_SIZE / 2 + 1
        size = variables.TILE_SIZE - 2
        rectToDraw = pygame.Rect(x, y, size, size)
        pygame.draw.rect(variables.window, tile.getColor(), rectToDraw, 20)


def calculateTiles():
    for x in range(0, variables.WIDTH, variables.TILE_SIZE):
        for y in range(0, variables.HEIGHT, variables.TILE_SIZE):
            variables.tiles.append(
                classes.Tile((x + variables.TILE_SIZE / 2, y + variables.TILE_SIZE / 2),
                             variables.bgColor,
                             (int(x / variables.TILE_SIZE), int(y / variables.TILE_SIZE)),
                             classes.TileType.Ground))
    variables.tileResolutionY = y / variables.TILE_SIZE + 1
    variables.tileResolutionX = x / variables.TILE_SIZE + 1


def generatePath():
    allowedStartPositions = []
    allowedEndPositions = []
    for tile in variables.tiles:
        resolutionPosition = tile.getTileResolutionPosition()
        if resolutionPosition[0] == 0 and resolutionPosition[1] in range(1, 14):
            allowedStartPositions.append(tile)
            tile.setColor(variables.roadColor)
        elif resolutionPosition[0] == 14 and resolutionPosition[1] in range(1, 14):
            allowedEndPositions.append(tile)
            tile.setColor(variables.baseColor)

