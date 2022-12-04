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
pathPostShift = 3

# Colors
bgColor = (60, 127, 60)
selectedTileColorShift = (50, 50, 50)
roadColor = (125, 70, 70)
baseColor = (0, 0, 255)
redColor = (255, 0, 0)
gridColor = (60, 60, 60)

# Game objects:
enemies = []

# Game rules:
numberOfEnemiesToBeSpawned = 10
numberOfEnemiesLeft = 10
enemyHp = 10
damagePerEnemy = 20
moneyPerEnemy = 10


baseDamage = 5
baseHp = 100
money = 50
point = 0
upgradeBaseCost = 25
