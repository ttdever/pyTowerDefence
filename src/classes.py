from enum import Enum

class TileType(Enum):
    Ground = 1
    Road = 2
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

    def getTileResolutionPosition(self):
        return self.tileResolutionPosition

    def setColor(self, newColor):
        self.color = newColor