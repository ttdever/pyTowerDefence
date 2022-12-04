import math
import numpy as np
from enum import Enum

class TileType(Enum):
    Ground = 1
    Road = 2
    Tower = 3
    Base = 4

class Tile:
    def __init__(self, position, color, tileResolutionPosition, type):
        self.position = position
        self.color = color
        self.tileResolutionPosition = tileResolutionPosition
        self.type = type

    def getPosition(self):
        return self.position

    def getColor(self):
        return self.color

    def setColor(self, newColor):
        self.color = newColor

    def getTileResolutionPosition(self):
        return self.tileResolutionPosition

    def distanceTo(self, anotherTile):
        return math.dist(self.getTileResolutionPosition(), anotherTile.getTileResolutionPosition())

    def getNeighbours(self, tileGridList):
        neighbours = []
        selfPosition = self.getTileResolutionPosition()
        for tile in tileGridList:
            tilePosition = tile.getTileResolutionPosition()
            checkOnX = (tilePosition[0] == selfPosition[0] and abs(tilePosition[1] - selfPosition[1])) == 1
            checkOnY = (tilePosition[1] == selfPosition[1] and abs(tilePosition[0] - selfPosition[0])) == 1
            if checkOnX or checkOnY:
                neighbours.append(tile)
        return neighbours

    def getType(self):
        return self.type

    def setType(self, typeOfTile):
        self.type = typeOfTile
