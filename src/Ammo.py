import pygame.draw

import variables
class Ammo:
    def __init__(self, instancePos, targetEnemy, speed, damage, color):
        self.targetEnemy = targetEnemy
        self.speed = speed
        self.damage = damage
        self.position = instancePos
        self.liveTime = 1000
        self.spawnTime = pygame.time.get_ticks()
        self.currentTime = self.spawnTime
        self.color = color

    def update(self):
        self.moveTowardsEnemy()
        self.currentTime = pygame.time.get_ticks()
        if self.currentTime - self.spawnTime > self.liveTime:
            self.destroy()

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
            self.destroy()

    def destroy(self):
        try:
            variables.ammos.remove(self)
        except Exception as e:
            pass

    def draw(self, window):
        pygame.draw.circle(window, self.color, self.position, 4, 4)
