import variables
import pygame

heartImage = pygame.image.load('materials/UI/heart.png')
heartImage = pygame.transform.scale(heartImage, (20, 20))
heartPos = (10, 545)
heartTextPos = (40, 540)

coinImage = pygame.image.load('materials/UI/coin.png')
coinImage = pygame.transform.scale(coinImage, (20, 20))
coinPos = (10, 570)
coinTextPos = (40, 566)

enemiesLeftPos = (570, 540)

class UIController:
    def __init__(self):
        pass

    def updateUI(self):
        self.updateAmmo()
        self.updateHP()
        self.updateCoins()
        self.updateEnemiesLeft()
        self.updateBg()

    def updateAmmo(self):
        pass

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
        pass
