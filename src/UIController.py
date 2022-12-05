import variables
import pygame
import pygame.freetype

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
    def __init__(self):
        self.needToDrawTowerSelector = False
        self.towerSelectorPos = (0, 0)
        self.boundBuildButton = (0, 0)
        self.boundUpgradeButton = (0, 0)
        self.canUpgrade = False
        self.canBuild = False

    def updateUI(self):
        self.updateBg()
        self.updateAmmo()
        self.updateHP()
        self.updateCoins()
        self.updateEnemiesLeft()
        self.updateTowerSelector()

    def updateAmmo(self):
        pass

    def updateTowerSelector(self):
        if self.needToDrawTowerSelector:
            colorUpgrade = colorBuild = (120, 120, 120)
            if not self.canUpgrade:
                colorUpgrade = (60, 60, 60)
            if not self.canBuild:
                colorBuild = (60, 60, 60)

            if self.towerSelectorPos[0] + variables.TILE_SIZE * 2 > variables.WIDTH:
                self.towerSelectorPos = (self.towerSelectorPos[0] - variables.TILE_SIZE * 2, self.towerSelectorPos[1])
            if self.towerSelectorPos[1] - variables.TILE_SIZE/2 < 0:
                self.towerSelectorPos = (self.towerSelectorPos[0], self.towerSelectorPos[1] + variables.TILE_SIZE/2)

            bgTowerSelector = pygame.Rect(self.towerSelectorPos[0], self.towerSelectorPos[1], variables.TILE_SIZE * 2,
                                          variables.TILE_SIZE)
            buildButton = pygame.Rect(self.towerSelectorPos[0] + 2.5, self.towerSelectorPos[1] + 2.5,
                                      variables.TILE_SIZE - 5, variables.TILE_SIZE - 5)
            upgradeButton = pygame.Rect(self.towerSelectorPos[0] + 2.5 + variables.TILE_SIZE,
                                        self.towerSelectorPos[1] + 2.5, variables.TILE_SIZE - 5,
                                        variables.TILE_SIZE - 5)
            textBuild = variables.font.render('B', True, (200, 200, 200), None)
            textUpgrade = variables.font.render('U', True, (200, 200, 200), None)

            pygame.draw.rect(variables.window, variables.gridColor, bgTowerSelector, variables.TILE_SIZE)

            pygame.draw.rect(variables.window, colorBuild, buildButton, variables.TILE_SIZE)
            variables.window.blit(textBuild, (self.towerSelectorPos[0] + 8, self.towerSelectorPos[1]))
            pygame.draw.rect(variables.window, colorUpgrade, upgradeButton, variables.TILE_SIZE)
            variables.window.blit(textUpgrade,
                                  (self.towerSelectorPos[0] + 8 + variables.TILE_SIZE, self.towerSelectorPos[1]))

            self.boundBuildButton = (self.towerSelectorPos[0] + 2.5, self.towerSelectorPos[1] + 2.5)
            self.boundUpgradeButton = (
                self.towerSelectorPos[0] + 2.5 + variables.TILE_SIZE, self.towerSelectorPos[1] + 2.5)

            pygame.draw.circle(variables.window, variables.redColor, variables.selectedTile.getPosition(), variables.towerRange, 4)
    def updateHP(self):
        variables.window.blit(heartImage, heartPos)
        text = variables.font.render(str(variables.baseHp), True, variables.redColor)
        variables.window.blit(text, heartTextPos)

    def updateCoins(self):
        variables.window.blit(coinImage, coinPos)
        text = variables.font.render(str(variables.money), True, variables.yellowColor)
        variables.window.blit(text, coinTextPos)

    def updateEnemiesLeft(self):
        text = variables.font.render(str(variables.numberOfEnemiesLeft), True, (255, 255, 255))
        variables.window.blit(text, enemiesLeftPos)

    def updateBg(self):
        rectToDraw = pygame.Rect(uiDownPos[0], uiDownPos[1], 600, 60)
        pygame.draw.rect(variables.window, variables.roadColor, rectToDraw, 5)

    def setTowerSelectorPos(self, x, y):
        self.towerSelectorPos = (x, y)

    def setNeedToDrawTowerSelector(self, boolean):
        self.needToDrawTowerSelector = boolean

    def setCanBuild(self, boolean):
        self.canBuild = boolean

    def setCanUpgrade(self, boolean):
        self.canUpgrade = boolean

    def checkMouseInput(self, clickPos):
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
    def drawMenu(self):
        pass
