import variables
import pygame
import pygame.freetype
import sys
import functions

# UI ELEMENT POSITIONS:
heartImage = pygame.image.load('materials/UI/heart.png')
heartImage = pygame.transform.scale(heartImage, (20, 20))
heartPos = (10, 548)
heartTextPos = (40, 543)

coinImage = pygame.image.load('materials/UI/coin.png')
coinImage = pygame.transform.scale(coinImage, (20, 20))
coinPos = (10, 570)
coinTextPos = (40, 566)

enemiesLeftPos = (560, 543)
uiDownPos = (0, 540)


class UIController:

    # Constructor:
    def __init__(self):
        self.needToDrawTowerSelector = False #Need to draw build/upgrade selector
        self.towerSelectorPos = (0, 0) # Selector position
        self.boundBuildButton = (0, 0) # bounds of "build" button
        self.boundUpgradeButton = (0, 0) # bound of "upgrade" button
        self.canUpgrade = False
        self.canBuild = False

    def updateUI(self):
        self.updateBg() # Update UI background
        self.updateHP() # update hp count
        self.updateCoins() # update money count
        self.updateEnemiesLeft() # update enemies left number
        self.updateTowerSelector() # update tower selector

    def updateTowerSelector(self):
        if self.needToDrawTowerSelector:    # if must traw selector
            colorUpgrade = colorBuild = (120, 120, 120) # color when button is active
            if not self.canUpgrade:
                colorUpgrade = (60, 60, 60) # color if button not active
            if not self.canBuild:
                colorBuild = (60, 60, 60)

            # Check if selector is out of screen:
            if self.towerSelectorPos[0] + variables.TILE_SIZE * 2 > variables.WIDTH:
                self.towerSelectorPos = (self.towerSelectorPos[0] - variables.TILE_SIZE * 2, self.towerSelectorPos[1])
            if self.towerSelectorPos[1] - variables.TILE_SIZE/2 < 0:
                self.towerSelectorPos = (self.towerSelectorPos[0], self.towerSelectorPos[1] + variables.TILE_SIZE/2)

            # create bg for selector
            bgTowerSelector = pygame.Rect(self.towerSelectorPos[0], self.towerSelectorPos[1], variables.TILE_SIZE * 2,
                                          variables.TILE_SIZE)

            # create buttons for selector:
            buildButton = pygame.Rect(self.towerSelectorPos[0] + 2.5, self.towerSelectorPos[1] + 2.5,
                                      variables.TILE_SIZE - 5, variables.TILE_SIZE - 5)
            upgradeButton = pygame.Rect(self.towerSelectorPos[0] + 2.5 + variables.TILE_SIZE,
                                        self.towerSelectorPos[1] + 2.5, variables.TILE_SIZE - 5,
                                        variables.TILE_SIZE - 5)

            # create text for selector
            textBuild = variables.font.render('B', True, (200, 200, 200), None)
            textUpgrade = variables.font.render('U', True, (200, 200, 200), None)

            pygame.draw.rect(variables.window, variables.gridColor, bgTowerSelector, variables.TILE_SIZE)

            # Draw slelector:
            pygame.draw.rect(variables.window, colorBuild, buildButton, variables.TILE_SIZE)
            variables.window.blit(textBuild, (self.towerSelectorPos[0] + 8, self.towerSelectorPos[1]))
            pygame.draw.rect(variables.window, colorUpgrade, upgradeButton, variables.TILE_SIZE)
            variables.window.blit(textUpgrade,
                                  (self.towerSelectorPos[0] + 8 + variables.TILE_SIZE, self.towerSelectorPos[1]))

            self.boundBuildButton = (self.towerSelectorPos[0] + 2.5, self.towerSelectorPos[1] + 2.5)
            self.boundUpgradeButton = (
                self.towerSelectorPos[0] + 2.5 + variables.TILE_SIZE, self.towerSelectorPos[1] + 2.5)

            # draw tower range
            pygame.draw.circle(variables.window, variables.redColor, variables.selectedTile.getPosition(), variables.towerRange, 4)
    def updateHP(self): # update hp count
        variables.window.blit(heartImage, heartPos)
        text = variables.font.render(str(variables.baseHp), True, variables.redColor)
        variables.window.blit(text, heartTextPos)

    def updateCoins(self): # update money count
        variables.window.blit(coinImage, coinPos)
        text = variables.font.render(str(variables.money), True, variables.yellowColor)
        variables.window.blit(text, coinTextPos)

    def updateEnemiesLeft(self): # update enemies left count
        text = variables.font.render(str(variables.numberOfEnemiesLeft), True, (255, 255, 255))
        variables.window.blit(text, enemiesLeftPos)

    def updateBg(self): # update background
        rectToDraw = pygame.Rect(uiDownPos[0], uiDownPos[1], 600, 60)
        pygame.draw.rect(variables.window, variables.roadColor, rectToDraw, 5)

    def setTowerSelectorPos(self, x, y): # set build/upgrade selector position
        self.towerSelectorPos = (x, y)

    def setNeedToDrawTowerSelector(self, boolean): # set, if need to draw selector
        self.needToDrawTowerSelector = boolean

    def setCanBuild(self, boolean): # can build
        self.canBuild = boolean

    def setCanUpgrade(self, boolean): # can upgrade
        self.canUpgrade = boolean

    def checkMouseInput(self, clickPos):    # check mouse input for build / upgrade selector:
        inBoundsBuild = (clickPos[0] > self.boundBuildButton[0] and clickPos[1] > self.boundBuildButton[1]) and \
                        (clickPos[0] < self.boundBuildButton[0] + variables.TILE_SIZE - 5 and clickPos[1] <
                         self.boundBuildButton[1] + variables.TILE_SIZE - 5) \
                        and self.canBuild
        inBoundsUpgrade = (clickPos[0] > self.boundUpgradeButton[0] and clickPos[1] > self.boundUpgradeButton[1]) and \
                          (clickPos[0] < self.boundUpgradeButton[0] + variables.TILE_SIZE - 5 and clickPos[1] <
                           self.boundUpgradeButton[1] + variables.TILE_SIZE - 5) \
                          and self.canUpgrade
        if inBoundsBuild:
            variables.gameController.placeTower(variables.selectedTile)
        elif inBoundsUpgrade:
            variables.gameController.upgradeTower(variables.selectedTile)

        variables.tilesAreSelectable = True
        self.needToDrawTowerSelector = False
    def drawMenu(self): # draw pause-menu:
        variables.window.fill((80, 80, 80))
        quitButton = pygame.Rect(200,200,200,50)
        quitButtonBlack = pygame.Rect(195, 195, 210, 60)
        pygame.draw.rect(variables.window, (0,0,0), quitButtonBlack, 25, 25)
        pygame.draw.rect(variables.window, variables.buttonBgColor, quitButton, 25, 25)
        text = variables.font.render("Quit", True, (200, 200, 200), None)
        variables.window.blit(text, (280, 210))

        text = variables.font.render("Or press esc to continue", True, (200, 200, 200), None)
        variables.window.blit(text, (200, 310))

    def checkQuitButton(self, clickPos): # check quit button
        if 200 <= clickPos[0] <= 400 and 200 <= clickPos[1] <= 250:
            pygame.quit()
            sys.exit(0)

    def drawMainMenu(self): # DRAW MAIN MENU
        variables.window.fill((60, 120, 60))
        quitButton = pygame.Rect(200, 200, 200, 50)
        quitButtonBlack = pygame.Rect(195, 195, 210, 60)
        pygame.draw.rect(variables.window, (0, 0, 0), quitButtonBlack, 25, 25)
        pygame.draw.rect(variables.window, variables.buttonBgColor, quitButton, 25, 25)
        text = variables.font.render("Start", True, (200, 200, 200), None)
        variables.window.blit(text, (280, 210))

    def checkMainMenuButtons(self, clickPos): # check main menu input
        if 200 <= clickPos[0] <= 400 and 200 <= clickPos[1] <= 250:
            variables.startedPlay = True
            variables.passedTime = 0
            variables.audioController.playBg()
            variables.enemySpawnDelay = 2000

    def drawWinScreen(self): # draw win screen
        variables.window.fill((60, 120, 60))
        quitButton = pygame.Rect(200, 200, 200, 50)
        quitButtonBlack = pygame.Rect(195, 195, 210, 60)
        pygame.draw.rect(variables.window, (0, 0, 0), quitButtonBlack, 25, 25)
        pygame.draw.rect(variables.window, variables.buttonBgColor, quitButton, 25, 25)
        text = variables.font.render("Next", True, (200, 200, 200), None)
        variables.window.blit(text, (280, 210))
        text = variables.font.render("You won press next to continue", True, (200, 200, 200), None)
        variables.window.blit(text, (180, 310))

    def checkWinScreen(self, clickPos): # check win screen input
        if 200 <= clickPos[0] <= 400 and 200 <= clickPos[1] <= 250:
            variables.numberOfEnemiesToBeSpawned *= 2
            variables.numberOfEnemiesLeft = variables.numberOfEnemiesToBeSpawned
            variables.baseHp = 5
            variables.money = 50
            variables.enemies = []
            variables.towers = []
            variables.ammos = []
            variables.enemySpawnDelay = 2000
            variables.tiles = []
            functions.initGame()
            variables.passedTime = 0
            variables.stopped = False
            variables.win = False

    def drawLostScreen(self): # draw lost screen
        variables.window.fill((60,120,60))
        quitButton = pygame.Rect(200,200,200,50)
        quitButtonBlack = pygame.Rect(195, 195, 210, 60)
        pygame.draw.rect(variables.window, (0,0,0), quitButtonBlack, 25, 25)
        pygame.draw.rect(variables.window, variables.buttonBgColor, quitButton, 25, 25)
        text = variables.font.render("Again", True, (200, 200, 200), None)
        variables.window.blit(text, (280, 210))
        text = variables.font.render("You lost press again to restart", True, (200, 200, 200), None)
        variables.window.blit(text, (175, 310))

    def checkLostScreen(self, clickPos): # check lost screen input
        if 200 <= clickPos[0] <= 400 and 200 <= clickPos[1] <= 250:
            variables.numberOfEnemiesToBeSpawned = 50
            variables.numberOfEnemiesLeft = variables.numberOfEnemiesToBeSpawned
            variables.baseHp = 5
            variables.money = 50
            variables.enemies = []
            variables.towers = []
            variables.enemySpawnDelay = 2000
            variables.ammos = []
            variables.tiles = []
            variables.passedTime = 0
            functions.initGame()
            variables.stopped = False
            variables.win = False




