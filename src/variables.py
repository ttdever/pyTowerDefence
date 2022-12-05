import pygame.freetype

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
selectedTile = None
gameZoneBounds = (0, 0)
mouseInGameZone = False
tilesAreSelectable = True
interfaceController = None
gameController = None

# Colors
bgColor = (60, 127, 60)
selectedTileColorShift = (50, 50, 50)
roadColor = (125, 70, 70)
baseColor = (0, 0, 255)
redColor = (255, 0, 0)
yellowColor = (255, 255, 0)
gridColor = (60, 60, 60)
buttonBgColor = (120, 120, 120)

# Game objects:
enemies = []
towers = []
guns = []
ammos = []

# Game rules:
numberOfEnemiesToBeSpawned = 10
numberOfEnemiesLeft = 10
enemyHp = 10
moneyPerEnemy = 5
enemySpawnDelay = 2000

baseDamage = 5
baseHp = 5
money = 50
point = 0
costOfTower = 25
towerRange = 100
ammoSpeed = 100
ammoDamage = 10
towerShootDelay = 4000

# Fonts:
font = None