import pygame
import variables
import Tile
import Tower
import Enemy

tower1Image = pygame.transform.scale(pygame.image.load("materials/towers/tower1.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))
tower2Image = pygame.transform.scale(pygame.image.load("materials/towers/tower2.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))
tower3Image = pygame.transform.scale(pygame.image.load("materials/towers/tower3.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))
tower4Image = pygame.transform.scale(pygame.image.load("materials/towers/tower4.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))
tower5Image = pygame.transform.scale(pygame.image.load("materials/towers/tower5.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))
tower6Image = pygame.transform.scale(pygame.image.load("materials/towers/tower6.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))

class GameController:
    def __init__(self):
        self.lastSpawnTime = pygame.time.get_ticks()
        self.currentTime = pygame.time.get_ticks()

    def placeTower(self, tile):
        positionToPlace = tile.getPosition()
        if tile.getType() == Tile.TileType.Ground and variables.money >= variables.costOfTower:
            towerToAdd = Tower.Tower(1, positionToPlace, tower1Image)
            variables.towers.append(towerToAdd)
            tile.setType(Tile.TileType.Tower)
            tile.setTower(towerToAdd)
            variables.money -= variables.costOfTower


    def upgradeTower(self, tile):
        if tile.getType() == Tile.TileType.Tower and variables.money >= variables.costOfTower:
            tower = tile.getTower()
            towerLvl = tower.getLvl()
            if towerLvl == 1:
                tower.upgrade(tower2Image)
            elif towerLvl == 2:
                tower.upgrade(tower3Image)
            elif towerLvl == 3:
                tower.upgrade(tower4Image)
            elif towerLvl == 4:
                tower.upgrade(tower5Image)
            elif towerLvl == 5:
                tower.upgrade(tower6Image)
            elif towerLvl == 6:
                return
            variables.money -= variables.costOfTower

    def update(self):
        self.currentTime = pygame.time.get_ticks()
        if self.checkIfSpawnEnemies():
            self.spawnEnemy()
        elif variables.numberOfEnemiesLeft <= 0:
            self.win()

    def checkIfSpawnEnemies(self):
        if self.currentTime - self.lastSpawnTime > variables.enemySpawnDelay and variables.numberOfEnemiesLeft > 0:
            self.lastSpawnTime = self.currentTime
            if variables.enemySpawnDelay < 1:
                variables.enemySpawnDelay = 1
            else:
                variables.enemySpawnDelay -= variables.passedTime/20
            return True
        else:
            return False

    def spawnEnemy(self):
        enemyToSpawn = Enemy.Enemy(10 + variables.passedTime/2.5, 50 + variables.passedTime/50, variables.roadTiles)
        variables.enemies.append(enemyToSpawn)
        variables.numberOfEnemiesLeft -= 1


    def getPlayerDamage(self):
        variables.baseHp -= 1
        if variables.baseHp <= 0:
            self.loose()
        pass

    def loose(self):
        print("Game over")

    def win(self):
        print("Wint")

    def stopGame(self):
        pass

    def continueGame(self):
        pass

