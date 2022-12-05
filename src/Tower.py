import variables
import pygame
import math
import Ammo

ammoColors = [(127, 255, 212), (227, 207, 87), (0, 0, 255), (152, 245, 255), (255, 97, 3), (220, 20, 60)]

class Tower:
    def __init__(self, lvl, position, image, costOfUpgrade=20):
        self.lvl = lvl
        realPos = (position[0] - variables.TILE_SIZE / 2 + 2.5, position[1] - variables.TILE_SIZE / 2)
        self.position = realPos
        self.image = image
        self.costOfUpgrade = costOfUpgrade
        self.lastShot = pygame.time.get_ticks()
        self.currentShot = self.lastShot

    def getPosition(self):
        return self.position

    def draw(self, window):
        window.blit(self.image, self.position)

    def update(self):
        self.currentShot = pygame.time.get_ticks()
        closestEnemy = self.findClosestEnemy()

        if not closestEnemy == None and self.currentShot - self.lastShot > variables.towerShootDelay:
            checkMinDistance = math.dist(self.position, closestEnemy.getPosition()) <= variables.towerRange
            if checkMinDistance:
                self.shoot(closestEnemy)
                self.lastShot = self.currentShot

    def upgrade(self, picture):
        self.lvl += 1
        self.image = picture

    def getLvl(self):
        return self.lvl

    def shoot(self, enemy):
        multi = self.lvl / 2
        if multi < 1:
            multi = 1
        ammoToCreate = Ammo.Ammo(self.position, enemy, variables.ammoSpeed * multi + 1, variables.ammoDamage * multi + 1, ammoColors[self.lvl - 1])
        variables.ammos.append(ammoToCreate)

    def findClosestEnemy(self):
        if len(variables.enemies) > 0:
            bestEnemy = variables.enemies[0]
            for enemy in variables.enemies:
                if math.dist(bestEnemy.getPosition(), self.position) > math.dist(enemy.getPosition(), self.position):
                    bestEnemy = enemy
            return bestEnemy
        else:
            return None

        pass
