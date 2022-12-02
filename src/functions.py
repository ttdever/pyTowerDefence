import sys
import pygame
import variables
import math


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
    closestTilePosition = findClosestTile(mousePosition)
    selectedTile = pygame.Rect(closestTilePosition[0] - variables.TILE_SIZE / 2 + 1,
                               closestTilePosition[1] - variables.TILE_SIZE / 2 + 1, variables.TILE_SIZE - 2,
                               variables.TILE_SIZE - 2)
    pygame.draw.rect(variables.window, variables.selectedTileColor, selectedTile, 30)


# Find the closest tile to mouse position by iterating through array with tiles
def findClosestTile(mousePos):
    result = variables.tiles[0]
    for coordinates in variables.tiles:
        if math.dist(coordinates, mousePos) < math.dist(result, mousePos):
            result = coordinates
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
            variables.tiles.append((x + variables.TILE_SIZE / 2, y + variables.TILE_SIZE / 2))