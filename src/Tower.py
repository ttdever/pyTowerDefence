import variables
import pygame

gun1Image = pygame.transform.scale(pygame.image.load("materials/weapons/guns/gun1.png"), (variables.TILE_SIZE - 5, variables.TILE_SIZE - 5))

class Tower:
    def __init__(self, lvl, position, image, costOfUpgrade=20):
        self.lvl = lvl
        realPos = (position[0] - variables.TILE_SIZE / 2 + 2.5, position[1] - variables.TILE_SIZE / 2)
        self.position = realPos
        self.image = image
        self.costOfUpgrade = costOfUpgrade

    def getPosition(self):
        return self.position

    def draw(self, window):
        window.blit(self.image, self.position)

    def upgrade(self, picture):
        self.lvl += 1
        self.image = picture

