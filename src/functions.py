import random
import sys
import pygame
import variables
import math
import Tile
import UIController
import GameController
import AudioContoller
import numpy as np


# Start of program:
def initGame():
    pygame.display.set_caption("pyTowerDefence")
    pygame.font.init()
    variables.font = pygame.font.SysFont('arial', 23)
    variables.window = pygame.display.set_mode((variables.WIDTH, variables.HEIGHT))
    variables.window.fill(variables.gridColor)
    variables.clock = pygame.time.Clock()
    calculateTiles()
    drawGrid()
    generatePath()
    getGameZoneBounds()
    variables.interfaceController = UIController.UIController()
    variables.gameController = GameController.GameController()
    variables.audioController = AudioContoller.AudioController()
    variables.audioController.playBg()


# Call every frame (unity update analog)
def tickGame():
    variables.clock.tick(variables.FPS)
    checkInputs()
    checkPhysics()
    checkDraw()
    variables.passedTime = pygame.time.get_ticks()/1000

def checkDraw():
    drawGrid()
    drawSelectedTile()
    drawEnemies()
    drawTowers()
    drawAmos()
    variables.interfaceController.updateUI()
    pygame.display.update()


# Check for user inputs
def checkInputs():
    checkMouseInGameZone()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            checkClick(pygame.mouse.get_pos())
        elif event.type == pygame.constants.KEYDOWN:
            if event.key == pygame.constants.K_ESCAPE:
                if not variables.stopped:
                    pause()
                else:
                    unpause()



def checkPhysics():
    if not variables.stopped:
        moveEnemies()
        updateTowers()
        updateAmos()
        variables.gameController.update()

def updateAmos():
    for ammo in variables.ammos:
        ammo.update()
def updateTowers():
    for tower in variables.towers:
        tower.update()

def checkMouseInGameZone():
    mousePos = pygame.mouse.get_pos()
    variables.mouseInGameZone = mousePos[0] < variables.gameZoneBounds[0] and mousePos[1] < variables.gameZoneBounds[1]


def checkClick(clickPos):
    if variables.mouseInGameZone and variables.tilesAreSelectable and not variables.stopped:
        x = variables.selectedTile.getPosition()[0]
        y = variables.selectedTile.getPosition()[1] - variables.TILE_SIZE
        variables.interfaceController.setTowerSelectorPos(x, y)
        variables.interfaceController.setNeedToDrawTowerSelector(True)
        typeOfSelectedTile = variables.selectedTile.getType()

        if typeOfSelectedTile == Tile.TileType.Ground:
            variables.interfaceController.setCanBuild(True)
            variables.interfaceController.setCanUpgrade(False)
        elif typeOfSelectedTile == Tile.TileType.Tower:
            variables.interfaceController.setCanBuild(False)
            variables.interfaceController.setCanUpgrade(True)
        else:
            variables.interfaceController.setCanBuild(False)
            variables.interfaceController.setCanUpgrade(False)

        variables.audioController.playSelection()
        variables.tilesAreSelectable = False
    elif not variables.tilesAreSelectable:
        variables.interfaceController.checkMouseInput(clickPos)
    else:
        pass


def drawAmos():
    for ammo in variables.ammos:
        ammo.draw(variables.window)

def drawTowers():
    for tower in variables.towers:
        tower.draw(variables.window)


def drawEnemies():
    for enemy in variables.enemies:
        enemy.draw(variables.window)


def moveEnemies():
    for enemy in variables.enemies:
        enemy.move()


# Check mouse position and craw selected tile
def drawSelectedTile():
    if variables.mouseInGameZone and variables.tilesAreSelectable:
        mousePosition = pygame.mouse.get_pos()
        closestTile = findClosestTile(mousePosition)
        selectedTile = pygame.Rect(closestTile.getPosition()[0] - variables.TILE_SIZE / 2 + 1,
                                   closestTile.getPosition()[1] - variables.TILE_SIZE / 2 + 1, variables.TILE_SIZE - 2,
                                   variables.TILE_SIZE - 2)
        selectionColor = np.clip(np.add(closestTile.getColor(), variables.selectedTileColorShift), 0, 255)
        pygame.draw.rect(variables.window, (selectionColor[0], selectionColor[1], selectionColor[2]), selectedTile,
                         variables.TILE_SIZE)


# Find the closest tile to mouse position by iterating through array with tiles
def findClosestTile(mousePos):
    result = variables.tiles[0]
    selectedTilePos = result.getPosition()
    for tile in variables.tiles:
        coordinates = tile.getPosition()
        if math.dist(coordinates, mousePos) < math.dist(selectedTilePos, mousePos):
            selectedTilePos = coordinates
            result = tile
    variables.selectedTile = result
    return result


# Creates tiles and writes tile centers to "variables.tiles"
def drawGrid():
    variables.window.fill(variables.gridColor)
    for tile in variables.tiles:
        coordinatesToDraw = tile.getPosition()
        x = coordinatesToDraw[0] - variables.TILE_SIZE / 2 + 1
        y = coordinatesToDraw[1] - variables.TILE_SIZE / 2 + 1
        size = variables.TILE_SIZE - 2
        rectToDraw = pygame.Rect(x, y, size, size)
        pygame.draw.rect(variables.window, tile.getColor(), rectToDraw, variables.TILE_SIZE)


def calculateTiles():
    for x in range(0, variables.WIDTH, variables.TILE_SIZE):
        for y in range(0, variables.HEIGHT - int(variables.HEIGHT / 10), variables.TILE_SIZE):
            variables.tiles.append(
                Tile.Tile((x + variables.TILE_SIZE / 2, y + variables.TILE_SIZE / 2),
                          variables.bgColor,
                          (int(x / variables.TILE_SIZE), int(y / variables.TILE_SIZE)),
                          Tile.TileType.Ground))
    variables.tileResolutionY = y / variables.TILE_SIZE + 1
    variables.tileResolutionX = x / variables.TILE_SIZE + 1


# Generates path between enemy spawn and base:
def generatePath():
    allowedStartPositions = []
    allowedEndPositions = []
    for tile in variables.tiles:
        resolutionPosition = tile.getTileResolutionPosition()
        x = resolutionPosition[0]
        y = resolutionPosition[1]
        if x == 0 and resolutionPosition[1] in range(1, int(variables.tileResolutionX - 1)):
            allowedStartPositions.append(tile)
        elif x == int(variables.tileResolutionX - 1) and y in range(1, int(variables.tileResolutionX - 1)):
            allowedEndPositions.append(tile)

    startTile = allowedStartPositions[random.randrange(0, len(allowedStartPositions))]
    endTile = allowedEndPositions[random.randrange(0, len(allowedEndPositions))]
    startTile.setColor(variables.roadColor)
    endTile.setColor(variables.baseColor)
    posts = generatePosts(startTile, endTile)
    variables.roadTiles = calculatePath(startTile, endTile, posts)


# Calculate path:
def generatePosts(startTile, endTile):
    allowedTiles = []
    for tile in variables.tiles:
        resolutionPos = tile.getTileResolutionPosition()
        x = resolutionPos[0]
        y = resolutionPos[1]
        if x != 0 and x != variables.tileResolutionX - 1 and y != 0 and y != variables.tileResolutionY - 1:
            if x % 5 == 0 and x + 2 != endTile.getTileResolutionPosition()[0] and x - 1 != \
                    startTile.getTileResolutionPosition()[0]:
                allowedTiles.append(tile)

    x = allowedTiles[len(allowedTiles) - 1].getTileResolutionPosition()[0]
    y = allowedTiles[len(allowedTiles) - 1].getTileResolutionPosition()[1]
    allowedTiles = np.reshape(allowedTiles, (int(x / 5), y))

    selectedPosts = []
    for i in range(len(allowedTiles)):
        selectedPosts.append(allowedTiles[i][random.randrange(0, len(allowedTiles[i]) - 1)])
    for post in selectedPosts:
        post.setColor(variables.roadColor)

    return selectedPosts


def calculatePath(start, end, posts):
    start.setColor(variables.redColor)
    start.setType(Tile.TileType.Road)
    end.setType(Tile.TileType.Road)
    posts.insert(0, start)
    posts.append(end)
    i = 0

    while i < len(posts):
        neighbours = posts[i].getNeighbours(variables.tiles)
        bestNeighbour = neighbours[0]
        for neighbour in neighbours:
            if bestNeighbour.distanceTo(posts[i + 1]) > neighbour.distanceTo(posts[i + 1]):
                bestNeighbour = neighbour
        if bestNeighbour.getTileResolutionPosition() == end.getTileResolutionPosition():
            break
        elif posts.__contains__(bestNeighbour):
            i += 1
            continue
        else:
            bestNeighbour.setColor(variables.roadColor)
            bestNeighbour.setType(Tile.TileType.Road)
            posts.insert(i + 1, bestNeighbour)
            i += 1
    return posts


def getGameZoneBounds():
    lastTile = variables.tiles[len(variables.tiles) - 1]
    variables.gameZoneBounds = (
        lastTile.getPosition()[0] + variables.TILE_SIZE / 2, lastTile.getPosition()[1] + variables.TILE_SIZE / 2)

def pause():
    variables.stopped = True


def unpause():
    variables.stopped = False

