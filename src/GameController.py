import pygame
import variables
import Tile
import Tower

tower1Image = pygame.transform.scale(pygame.image.load("materials/towers/tower1.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))
tower2Image = pygame.transform.scale(pygame.image.load("materials/towers/tower2.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))
tower3Image = pygame.transform.scale(pygame.image.load("materials/towers/tower3.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))
tower4Image = pygame.transform.scale(pygame.image.load("materials/towers/tower4.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))
tower5Image = pygame.transform.scale(pygame.image.load("materials/towers/tower5.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))
tower6Image = pygame.transform.scale(pygame.image.load("materials/towers/tower6.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))

class GameController:
    def __init__(self):
        pass

    def placeTower(self, tile):
        positionToPlace = tile.getPosition()
        if tile.getType() == Tile.TileType.Ground and variables.money >= variables.costOfTower:
            towerToAdd = Tower.Tower(1, positionToPlace, tower1Image)
            variables.towers.append(towerToAdd)
            tile.setType(Tile.TileType.Tower)
            variables.money -= variables.costOfTower


    def upgradeTower(self):
        pass

    def loadNextLvl(self):
        pass

    def stopGame(self):
        pass

    def continueGame(self):
        pass

