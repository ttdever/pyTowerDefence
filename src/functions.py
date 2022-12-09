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


# Start of program (as Start() in unity):
def initGame():
    pygame.display.set_caption("pyTowerDefence")                                    # set window name
    pygame.font.init()                                                              # ini font
    variables.font = pygame.font.SysFont('arial', 23)                               # load font
    variables.window = pygame.display.set_mode((variables.WIDTH, variables.HEIGHT)) # create window
    variables.window.fill(variables.gridColor)                                      # fill window
    variables.clock = pygame.time.Clock()                                           # get timer
    calculateTiles()                                                                # calculate tile grid
    drawGrid()                                                                      # draw tile grid
    generatePath()                                                                  # generate road tiles
    getGameZoneBounds()                                                             # get bounds of game thone
    variables.interfaceController = UIController.UIController()                     # init UIController
    variables.gameController = GameController.GameController()                      # init gameController
    variables.audioController = AudioContoller.AudioController()                    # init Audiocontroller



# Call every frame (unity update)
def tickGame():
    variables.timerStart = pygame.time.get_ticks()  # start of the tick time
    variables.clock.tick(variables.FPS)             # set FPS
    checkInputs()                                   # check player inputs
    checkPhysics()                                  # check physics
    checkDraw()                                     # check, what should be drawn
    variables.timerEnd = pygame.time.get_ticks()    # end of the tick time

    timerDelta = variables.timerEnd - variables.timerStart  # calculate delta time (Time.deltaTime in unity)
    if variables.needToCountTimer:                          # If need to count timer -> add delta time to passedTime
        variables.passedTime += timerDelta/1000

def checkDraw():   #Check what should be drawn
    if not variables.startedPlay:   # If player is not playing -> draw main menu
        variables.interfaceController.drawMainMenu()
    elif variables.win and variables.stopped:   # If player won and game is halted -> draw win screen
        variables.interfaceController.drawWinScreen()
    elif variables.loose and variables.stopped: # If player lost and game is halted -> draw win screen
        variables.interfaceController.drawLostScreen()
    else:
        if variables.stopped:   # if game is paused -> draw pause-menu
            variables.interfaceController.drawMenu()
        else:   # else -> draw game
            drawGrid()  # draw grid
            drawSelectedTile()  # draw selected tile
            drawEnemies()       # draw enemies
            drawTowers()        # draw towers
            drawAmos()          # draw bullets
            variables.interfaceController.updateUI()    # update interface
    pygame.display.update()


# Check for user inputs
def checkInputs():
    checkMouseInGameZone()  # check if mouse is in game zone
    for event in pygame.event.get():   # che events
        if event.type == pygame.QUIT: # if quit -> quit game
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # if LMB clicked -> check where clicked
            checkClick(pygame.mouse.get_pos())
        elif event.type == pygame.constants.KEYDOWN: # if ESC pressed -> pause or unpause:
            if event.key == pygame.constants.K_ESCAPE:
                if not variables.stopped:
                    pause()
                else:
                    unpause()


# Check physics every frame:
def checkPhysics():
    if not variables.stopped and variables.startedPlay: # If game was started and not halted:
        moveEnemies()   # Move enemies
        updateTowers()  # Update towers states
        updateAmos()    # Update ammos state
        variables.gameController.update()   # Update gameController

def updateAmos():   # Update ammos
    for ammo in variables.ammos:
        ammo.update()
def updateTowers(): # Update towers
    for tower in variables.towers:
        tower.update()

def checkMouseInGameZone(): # check if mouse in game zone
    mousePos = pygame.mouse.get_pos() # get mouse position
    variables.mouseInGameZone = mousePos[0] < variables.gameZoneBounds[0] and mousePos[1] < variables.gameZoneBounds[1] # check

# Handle click event:
def checkClick(clickPos):
    # If mouse in game zone and tiles are selectable and game not stopped and was started ->
    # -> tell UIController to update build/update menu position and tell that it needs to be drawn
    if variables.mouseInGameZone and variables.tilesAreSelectable and not variables.stopped and variables.startedPlay:
        x = variables.selectedTile.getPosition()[0]
        y = variables.selectedTile.getPosition()[1] - variables.TILE_SIZE
        variables.interfaceController.setTowerSelectorPos(x, y)
        variables.interfaceController.setNeedToDrawTowerSelector(True)
        typeOfSelectedTile = variables.selectedTile.getType()

        if typeOfSelectedTile == Tile.TileType.Ground:  # if ground -> set can build | can't upgrade
            variables.interfaceController.setCanBuild(True)
            variables.interfaceController.setCanUpgrade(False)
        elif typeOfSelectedTile == Tile.TileType.Tower: # if tower -> set can't build | can upgrade
            variables.interfaceController.setCanBuild(False)
            variables.interfaceController.setCanUpgrade(True)
        else:                                           # else -> set can't build | can't upgrade
            variables.interfaceController.setCanBuild(False)
            variables.interfaceController.setCanUpgrade(False)

        variables.audioController.playSelection()       # play selection sound
        variables.tilesAreSelectable = False            # tell program not to update selected tile
    elif not variables.tilesAreSelectable:              # check for player click (build or update button)
        variables.interfaceController.checkMouseInput(clickPos)
    elif variables.stopped and variables.startedPlay and not variables.win and not variables.loose:
        variables.interfaceController.checkQuitButton(clickPos) # check for pause-menu input
    elif not variables.startedPlay:
        variables.interfaceController.checkMainMenuButtons(clickPos) # check for main-menu input
    elif variables.win and variables.stopped:
        variables.interfaceController.checkWinScreen(clickPos) # check for win-menu input
    elif variables.loose and variables.stopped:
        variables.interfaceController.checkLostScreen(clickPos) # check for lost-screen input

# draw ammos:
def drawAmos():
    for ammo in variables.ammos:
        ammo.draw(variables.window)

# draw towers:
def drawTowers():
    for tower in variables.towers:
        tower.draw(variables.window)

# draw enemies:
def drawEnemies():
    for enemy in variables.enemies:
        enemy.draw(variables.window)

# move enemies:
def moveEnemies():
    for enemy in variables.enemies:
        enemy.move()


# Check mouse position and craw selected tile
def drawSelectedTile():
    if variables.mouseInGameZone and variables.tilesAreSelectable:
        mousePosition = pygame.mouse.get_pos() # Get mouse position
        closestTile = findClosestTile(mousePosition) # Get closest tile
        selectedTile = pygame.Rect(closestTile.getPosition()[0] - variables.TILE_SIZE / 2 + 1,
                                   closestTile.getPosition()[1] - variables.TILE_SIZE / 2 + 1, variables.TILE_SIZE - 2,
                                   variables.TILE_SIZE - 2) # create tile to draw on top
        selectionColor = np.clip(np.add(closestTile.getColor(), variables.selectedTileColorShift), 0, 255) # calculate new color with boumds (0, 255)
        pygame.draw.rect(variables.window, (selectionColor[0], selectionColor[1], selectionColor[2]), selectedTile,
                         variables.TILE_SIZE) # draw new tile


# Find the closest tile to mouse position by iterating through array with tiles
def findClosestTile(mousePos):
    result = variables.tiles[0] # get first tile
    selectedTilePos = result.getPosition() # get its position
    for tile in variables.tiles: # iterate over tiles
        coordinates = tile.getPosition() # get next tile position
        if math.dist(coordinates, mousePos) < math.dist(selectedTilePos, mousePos): # if next tile closer to mouse pos -> override coordinates and result tile
            selectedTilePos = coordinates
            result = tile
    variables.selectedTile = result # write selected tile
    return result # return selected tile


# Creates tiles and writes tile centers to "variables.tiles"
def drawGrid():
    variables.window.fill(variables.gridColor) # fill window
    for tile in variables.tiles: # iterate over tiles array:
        coordinatesToDraw = tile.getPosition() # het coordinates to draw:
        x = coordinatesToDraw[0] - variables.TILE_SIZE / 2 + 1  # coordinates are center of tile
        y = coordinatesToDraw[1] - variables.TILE_SIZE / 2 + 1  # and we need left upper corner
        size = variables.TILE_SIZE - 2  # size of tile (-2 for grid effect)
        rectToDraw = pygame.Rect(x, y, size, size) # create rect
        pygame.draw.rect(variables.window, tile.getColor(), rectToDraw, variables.TILE_SIZE) # draw rect

# Calculate tiles positions:
def calculateTiles():
    for x in range(0, variables.WIDTH, variables.TILE_SIZE): # Iterate over window width with step TILE_SIZE
        for y in range(0, variables.HEIGHT - int(variables.HEIGHT / 10), variables.TILE_SIZE): # Same for height, but give space for UI
            variables.tiles.append(
                Tile.Tile((x + variables.TILE_SIZE / 2, y + variables.TILE_SIZE / 2),
                          variables.bgColor,
                          (int(x / variables.TILE_SIZE), int(y / variables.TILE_SIZE)),
                          Tile.TileType.Ground)) # Create new tile and add it to tile array
    variables.tileResolutionY = y / variables.TILE_SIZE + 1 #Calculate tile resolution
    variables.tileResolutionX = x / variables.TILE_SIZE + 1


# Generates path between enemy spawn and base:
def generatePath():
    allowedStartPositions = []  # Allowed start positions (enemy base)
    allowedEndPositions = []    # Allowed end positions (player base)
    for tile in variables.tiles: # Iterate over tiles
        resolutionPosition = tile.getTileResolutionPosition() # Get tile position on tile grid
        x = resolutionPosition[0]
        y = resolutionPosition[1]
        if x == 0 and resolutionPosition[1] in range(1, int(variables.tileResolutionX - 1)): # If left side of tile grid and not corners -> add to startPositions
            allowedStartPositions.append(tile)
        elif x == int(variables.tileResolutionX - 1) and y in range(1, int(variables.tileResolutionX - 1)): # If right side of tile grid and not corners -> add to endPositions
            allowedEndPositions.append(tile)

    startTile = allowedStartPositions[random.randrange(0, len(allowedStartPositions))] # pickRandom from allowedStartPositions
    endTile = allowedEndPositions[random.randrange(0, len(allowedEndPositions))] # pickRandom from allowedEndPositions
    startTile.setColor(variables.roadColor) # change color of start/end tile
    endTile.setColor(variables.baseColor)
    posts = generatePosts(startTile, endTile) # generate posts
    variables.roadTiles = calculatePath(startTile, endTile, posts) # calculate road between start -> posts -> end


# Generate posts:
def generatePosts(startTile, endTile):
    allowedTiles = []
    for tile in variables.tiles: # iterate over tiles
        resolutionPos = tile.getTileResolutionPosition() # Get tile resolution
        x = resolutionPos[0]
        y = resolutionPos[1]

        # If not left side of tile grid and not last and not upper and not bottom
        if x != 0 and x != variables.tileResolutionX - 1 and y != 0 and y != variables.tileResolutionY - 1:
            # Only for every 5th column and not endX or startX
            if x % 5 == 0 and x + 2 != endTile.getTileResolutionPosition()[0] and x - 1 !=  startTile.getTileResolutionPosition()[0]:
                allowedTiles.append(tile) #Add tile to allowd tiles

    # Get bounds of the allowedTiles array
    x = allowedTiles[len(allowedTiles) - 1].getTileResolutionPosition()[0]
    y = allowedTiles[len(allowedTiles) - 1].getTileResolutionPosition()[1]
    allowedTiles = np.reshape(allowedTiles, (int(x / 5), y)) # reshape array to 2dim array

    #select random posts:
    selectedPosts = []
    for i in range(len(allowedTiles)):
        selectedPosts.append(allowedTiles[i][random.randrange(0, len(allowedTiles[i]) - 1)])
    for post in selectedPosts:
        post.setColor(variables.roadColor)

    return selectedPosts


# calculate road between start -> posts -> end
def calculatePath(start, end, posts):
    start.setColor(variables.redColor) # Set enemy base color -> red
    start.setType(Tile.TileType.Road)   # Set type of tile -> road
    end.setType(Tile.TileType.Road) # Same for end tile
    posts.insert(0, start) # add start and end tiles to posts
    posts.append(end)
    i = 0  # iterator

    while i < len(posts):
        # Get neighbours of the tile
        neighbours = posts[i].getNeighbours(variables.tiles) #Get tile neighbours
        bestNeighbour = neighbours[0]   # pick neighbour
        for neighbour in neighbours: # iterate over neighbours
            if bestNeighbour.distanceTo(posts[i + 1]) > neighbour.distanceTo(posts[i + 1]): # if distance to next post for next neighbour is smaller
                bestNeighbour = neighbour   #Overwrite next neighbour
        if bestNeighbour.getTileResolutionPosition() == end.getTileResolutionPosition(): # if best neighbour is last tile -> break
            break
        elif posts.__contains__(bestNeighbour): # if posts already contains bestNeighbour add 1 to iterator
            i += 1
            continue
        else:
            bestNeighbour.setColor(variables.roadColor) # set color of neighbour to road color
            bestNeighbour.setType(Tile.TileType.Road) # set type to road
            posts.insert(i + 1, bestNeighbour) # insert best neighbour into posts
            i += 1
    return posts # return posts

# get game zone bounds
def getGameZoneBounds():
    # Just get right down tiles -> get its coordinates (center of tile) -> add 1/2 of tile size to coordinates
    lastTile = variables.tiles[len(variables.tiles) - 1]
    variables.gameZoneBounds = (
        lastTile.getPosition()[0] + variables.TILE_SIZE / 2, lastTile.getPosition()[1] + variables.TILE_SIZE / 2)

def pause():
    variables.stopped = True
    variables.needToCountTimer = False

def unpause():
    variables.needToCountTimer = True
    variables.stopped = False

