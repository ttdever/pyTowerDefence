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

enemiesLeftPos = (570, 543)
uiDownPos = (0, 540)

tower1Image = pygame.transform.scale(pygame.image.load("materials/towers/tower1.png"), (25, 25))
tower2Image = pygame.transform.scale(pygame.image.load("materials/towers/tower2.png"), (25, 25))
tower3Image = pygame.transform.scale(pygame.image.load("materials/towers/tower3.png"), (25, 25))
tower4Image = pygame.transform.scale(pygame.image.load("materials/towers/tower4.png"), (25, 25))
tower5Image = pygame.transform.scale(pygame.image.load("materials/towers/tower5.png"), (25, 25))
tower6Image = pygame.transform.scale(pygame.image.load("materials/towers/tower6.png"), (25, 25))

class UIController:
    def __init__(self):
        self.needToDrawTowerSelector = False
        self.towerSelectorPos = (0, 0)
        self.boundBuildButton = (0, 0)
        self.boundUpdateButton = (0, 0)
        self.canUpdate = False
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
            bgTowerSelector = pygame.Rect(self.towerSelectorPos[0], self.towerSelectorPos[1], variables.TILE_SIZE * 2, variables.TILE_SIZE)
            buildButton = pygame.Rect(self.towerSelectorPos[0] + 2.5, self.towerSelectorPos[1] + 2.5, variables.TILE_SIZE - 5, variables.TILE_SIZE - 5)
            upgradeButton = pygame.Rect(self.towerSelectorPos[0] + 2.5 + variables.TILE_SIZE, self.towerSelectorPos[1] + 2.5, variables.TILE_SIZE - 5, variables.TILE_SIZE - 5)
            textBuild = variables.font.render('B', True, (200, 200, 200), None)
            textUpgrade = variables.font.render('U', True, (200, 200, 200), None)

            pygame.draw.rect(variables.window, variables.gridColor, bgTowerSelector, variables.TILE_SIZE)
            pygame.draw.rect(variables.window, variables.buttonBgColor, buildButton, variables.TILE_SIZE)
            variables.window.blit(textBuild, (self.towerSelectorPos[0] + 8, self.towerSelectorPos[1]))

            pygame.draw.rect(variables.window, variables.buttonBgColor, upgradeButton, variables.TILE_SIZE)
            variables.window.blit(textUpgrade, (self.towerSelectorPos[0] + 8 + variables.TILE_SIZE, self.towerSelectorPos[1]))

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

    def setCanUpdate(self, boolean):
        self.canUpdate = boolean

