import pygame.draw

import variables
class Ammo:
    def __init__(self, instancePos, targetEnemy, speed, damage):
        self.targetEnemy = targetEnemy
        self.speed = speed
        self.damage = damage
        self.position = instancePos

    def update(self):
        self.moveTowardsEnemy()

    def moveTowardsEnemy(self):
        vectorX, vectorY = (
        self.targetEnemy.getPosition()[0] - self.position[0], self.targetEnemy.getPosition()[1] - self.position[1])

        if vectorY < 0:
            stepY = (-1 * self.speed) / variables.FPS
        else:
            stepY = (1 * self.speed) / variables.FPS
        if vectorX < 0:
            stepX = (-1 * self.speed) / variables.FPS
        else:
            stepX = (1 * self.speed) / variables.FPS

        self.position = (self.position[0] + stepX, self.position[1] + stepY)
        checkMinDistance = abs(self.position[0] - self.targetEnemy.getPosition()[0]) < 7 and abs(
            self.position[1] - self.targetEnemy.getPosition()[1]) < 2
        if checkMinDistance:
            self.targetEnemy.getDamage(self.damage)
            variables.ammos.remove(self)
    def draw(self, window):
        pygame.draw.circle(window, (0, 125, 200), self.position, 4, 4)
