from enum import Enum

class TileType(Enum):
    Ground = 1
    Road = 2
class Tile:
    def __init__(self, position, color, type):
        self.position = position
        self.color = color

    def getPosition(self):
        return self.position

    def getColor(self):
        return self.color

    def setColor(self, newColor):
        self.color = newColor