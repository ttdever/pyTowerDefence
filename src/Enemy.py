import variables
import pygame
import variables

enemyColors = [(252, 230, 201), (205, 173, 0), (0, 128, 0), (205, 92, 92), (205, 205, 193), (240, 128, 128)]


class Enemy:
    def __init__(self, hp, speed, road):
        self.hp = hp
        self.speed = speed
        self.road = road
        self.roadLength = len(road) - 1
        self.currentRoadIndex = 1
        self.currentPosition = road[0].getPosition()
        self.targetPosition = road[1].getPosition()

    def draw(self, window):
        if 10 <= self.hp < 20:
            color = enemyColors[0]
        elif 20 <= self.hp < 30:
            color = enemyColors[1]
        elif 30 <= self.hp < 40:
            color = enemyColors[2]
        elif 40 <= self.hp < 50:
            color = enemyColors[3]
        elif 50 <= self.hp < 60:
            color = enemyColors[4]
        elif self.hp >= 60:
            color = enemyColors[5]
        else:
            color = (255, 255, 255)
        pygame.draw.circle(window, (0, 0, 0), self.currentPosition, 6)
        pygame.draw.circle(window, color, self.currentPosition, 5)

    def move(self):
        vectorX, vectorY = (
        self.targetPosition[0] - self.currentPosition[0], self.targetPosition[1] - self.currentPosition[1])

        if vectorY < 0:
            stepY = (-1 * self.speed) / variables.FPS
        else:
            stepY = (1 * self.speed) / variables.FPS
        if vectorX < 0:
            stepX = (-1 * self.speed) / variables.FPS
        else:
            stepX = (1 * self.speed) / variables.FPS

        self.currentPosition = (self.currentPosition[0] + stepX, self.currentPosition[1] + stepY)
        checkMinDistance = abs(self.currentPosition[0] - self.targetPosition[0]) < 7 and abs(
            self.currentPosition[1] - self.targetPosition[1]) < 7
        if checkMinDistance:
            if self.currentRoadIndex < self.roadLength:
                self.currentRoadIndex += 1
                self.targetPosition = self.road[self.currentRoadIndex].getPosition()
            else:
                variables.gameController.getPlayerDamage()
                variables.audioController.playBaseHit()
                variables.enemies.remove(self)

    def getDamage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()

    def die(self):
        try:
            variables.audioController.playEnemyHit()
            variables.enemies.remove(self)
            variables.money += variables.moneyPerEnemy
        except Exception as e:
            pass

    def getPosition(self):
        return self.currentPosition
