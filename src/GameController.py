import pygame
import variables
import Tile
import Tower
import Enemy

# Load towers images:
tower1Image = pygame.transform.scale(pygame.image.load("materials/towers/tower1.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))
tower2Image = pygame.transform.scale(pygame.image.load("materials/towers/tower2.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))
tower3Image = pygame.transform.scale(pygame.image.load("materials/towers/tower3.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))
tower4Image = pygame.transform.scale(pygame.image.load("materials/towers/tower4.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))
tower5Image = pygame.transform.scale(pygame.image.load("materials/towers/tower5.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))
tower6Image = pygame.transform.scale(pygame.image.load("materials/towers/tower6.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))

class GameController:
    def __init__(self):
        self.lastSpawnTime = pygame.time.get_ticks() # Last time enemy was spawned
        self.currentTime = pygame.time.get_ticks()  # timer

    # Place tower
    def placeTower(self, tile):
        positionToPlace = tile.getPosition() # Get tile position
        if tile.getType() == Tile.TileType.Ground and variables.money >= variables.costOfTower: # check if allowed tile and player has enough money
            towerToAdd = Tower.Tower(1, positionToPlace, tower1Image) # Create tower
            variables.towers.append(towerToAdd) # add tower to towers array
            tile.setType(Tile.TileType.Tower) # set type of tile to tower
            tile.setTower(towerToAdd) # set tower onto tile
            variables.audioController.playBuild() # play build sound
            variables.money -= variables.costOfTower # get money from player


    def upgradeTower(self, tile):
        #Check if tile type is tower and player got enough money:
        if tile.getType() == Tile.TileType.Tower and variables.money >= variables.costOfTower:
            tower = tile.getTower() # get tower from tile
            towerLvl = tower.getLvl() # get lvl of the tower
            # calculate image:
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
            # play upgrade sound
            variables.audioController.playUpgrade()
            variables.money -= variables.costOfTower # get money from player

    # called every frame
    def update(self):
        self.currentTime = pygame.time.get_ticks()  # Timer
        if self.checkIfSpawnEnemies():  # check if need to spawn enemies:
            self.spawnEnemy()   # spawn if needed
        elif variables.numberOfEnemiesLeft <= 0 and len(variables.enemies) == 0: # if no enemies left -> win
            self.win()

    def checkIfSpawnEnemies(self):
        if self.currentTime - self.lastSpawnTime > variables.enemySpawnDelay and variables.numberOfEnemiesLeft > 0: # if timer - lastSpawnTime > spawnDelay
            self.lastSpawnTime = self.currentTime # assign lastSpawn Time to currentTime
            variables.enemySpawnDelay -= variables.passedTime / 10 # decrease delay
            if variables.enemySpawnDelay < 1:   # if delay < 1 -> delay = 1
                variables.enemySpawnDelay = 1
            return True
        else:
            return False

    def spawnEnemy(self):
        enemyToSpawn = Enemy.Enemy(10 + variables.passedTime/2.5, 50 + variables.passedTime/50, variables.roadTiles) # Create enemy
        variables.enemies.append(enemyToSpawn) # Add enemy to enemies arary
        variables.numberOfEnemiesLeft -= 1 # decrease enemy count


    def getPlayerDamage(self):
        variables.baseHp -= 1       # damage player base
        if variables.baseHp <= 0:
            self.loose()
        pass

    def loose(self):
        variables.loose = True
        variables.enemySpawnDelay = 2000
        variables.stopped = True

    def win(self):
        variables.win = True
        variables.enemySpawnDelay = 2000
        variables.stopped = True

