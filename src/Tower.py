import variables
import pygame
import math
import Ammo

ammoColors = [(127, 255, 212), (227, 207, 87), (0, 0, 255), (152, 245, 255), (255, 97, 3), (220, 20, 60)]

class Tower:
    # Constructor
    def __init__(self, lvl, position, image, costOfUpgrade=20):
        self.lvl = lvl  # Tower lvl
        realPos = (position[0] - variables.TILE_SIZE / 2 + 2.5, position[1] - variables.TILE_SIZE / 2) #Real pos on window
        self.position = realPos # positon
        self.image = image #iamge of tower
        self.costOfUpgrade = costOfUpgrade # cost Of upgrade
        self.lastShot = pygame.time.get_ticks() # last shot time
        self.currentShot = self.lastShot # timer

    def getPosition(self): # return position
        return self.position

    def draw(self, window): # draw tower
        window.blit(self.image, self.position)

    def update(self): # update physics
        self.currentShot = pygame.time.get_ticks() # update timer
        closestEnemy = self.findClosestEnemy() # find closest enemy

        if not closestEnemy == None and self.currentShot - self.lastShot > variables.towerShootDelay: # if enemy exists and enough time passed:
            checkMinDistance = math.dist(self.position, closestEnemy.getPosition()) <= variables.towerRange # if enemy in range
            if checkMinDistance:
                self.shoot(closestEnemy) # shoot
                self.lastShot = self.currentShot # update last shoot time

    def upgrade(self, picture): # upgrade tower
        self.lvl += 1
        self.image = picture

    def getLvl(self): # get level
        return self.lvl

    def shoot(self, enemy):
        multi = self.lvl / 2 # upgrade multiplier
        if multi < 1:
            multi = 1
        # create bullet:
        ammoToCreate = Ammo.Ammo(self.position, enemy, variables.ammoSpeed * multi + 1, variables.ammoDamage * multi + 1, ammoColors[self.lvl - 1])
        # add bullet to ammos[] array:
        variables.ammos.append(ammoToCreate)

    def findClosestEnemy(self):
        if len(variables.enemies) > 0: # if enemies are on map
            bestEnemy = variables.enemies[0] # get first
            for enemy in variables.enemies: # iterate
                # if closest enemy exists -> replace current
                if math.dist(bestEnemy.getPosition(), self.position) > math.dist(enemy.getPosition(), self.position):
                    bestEnemy = enemy
            return bestEnemy # return enemy
        else:
            return None
