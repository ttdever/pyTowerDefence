import time

import pygame
import variables


class Enemy:
    def __init__(self, hp, speed, road):
        self.hp = hp
        self.speed = speed
        self.road = road
        self.roadLength = len(road) - 1
        self.currentRoadIndex = 1
        self.currentPosition = road[0].getPosition()
        self.targetPosition = road[1].getPosition()
        self.prevTime = 0

    def draw(self, window):
        pygame.draw.circle(window, (0, 0, 0), self.currentPosition, 2)

    def move(self):
        vectorX, vectorY = (self.targetPosition[0] - self.currentPosition[0], self.targetPosition[1] - self.currentPosition[1])
        stepY = stepX = 0

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
