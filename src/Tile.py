import math
from enum import Enum

#Types of tiles:
class TileType(Enum):
    Ground = 1
    Road = 2
    Tower = 3
    Base = 4

class Tile:

    # Constructor
    def __init__(self, position, color, tileResolutionPosition, type):
        self.position = position    # Tile position
        self.color = color          # Tile color
        self.tileResolutionPosition = tileResolutionPosition    # Tile position on tile grid
        self.type = type    # Tile type
        self.tower = None   # Optional tower

    def getPosition(self):  # return position
        return self.position

    def getColor(self): # return color
        return self.color

    def setColor(self, newColor): # set color
        self.color = newColor

    def getTileResolutionPosition(self): # get position on tile grid
        return self.tileResolutionPosition

    def distanceTo(self, anotherTile):  # Get distance to another tile
        return math.dist(self.getTileResolutionPosition(), anotherTile.getTileResolutionPosition())

    def getNeighbours(self, tileGridList):  # Get neighbours
        neighbours = []
        selfPosition = self.getTileResolutionPosition() # Get tile grid-position
        for tile in tileGridList:
            tilePosition = tile.getTileResolutionPosition()
            checkOnX = (tilePosition[0] == selfPosition[0] and abs(tilePosition[1] - selfPosition[1])) == 1
            checkOnY = (tilePosition[1] == selfPosition[1] and abs(tilePosition[0] - selfPosition[0])) == 1
            if checkOnX or checkOnY: # if sam x and yDelta == 1 -> tile is neighbour (same for y and xDelta)
                neighbours.append(tile) # add to neighbours array
        return neighbours

    def getType(self):  # return type
        return self.type

    def setType(self, typeOfTile): # set type
        self.type = typeOfTile

    def setTower(self, tower): # set tower
        self.tower = tower

    def getTower(self): # get tower
        return self.tower
