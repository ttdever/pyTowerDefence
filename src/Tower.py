import variables
class Tower:
    def __init__(self, lvl, position, image):
        self.lvl = lvl
        realPos = (position[0] - variables.TILE_SIZE / 2 + 2.5, position[1] - variables.TILE_SIZE - 12.5)
        self.position = realPos
        self.image = image

    def getPosition(self):
        return self.position

    def draw(self, window):
        window.blit(self.image, self.position)
