import array

# Window settings
FPS = 60
WIDTH, HEIGHT = 600, 600
clock = None
window = None

# GameField
TILE_SIZE = 30
tiles = []
roadTiles = []
tileResolutionX = 0
tileResolutionY = 0
pathPostShift = 5

# Colors
bgColor = (60, 127, 60)
selectedTileColorShift = (50, 50, 50)
roadColor = (125, 70, 70)
baseColor = (0, 0, 255)
redColor = (255, 0, 0)
gridColor = (60, 60, 60)
