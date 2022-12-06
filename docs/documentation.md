# Documentation:

## File `main.py`:
Just calling 2 functions `initGame()` (as `Start()` in unity) and `tickGame()` (as `Update()` in unity)
````
def main():
    functions.initGame()
    while True:
        functions.tickGame()
````

## File `functions.py`:
This file contains all game checking for draw/input/physics updates

### Functions description:
- `initGame()` - Starts game by creating all necessary variables (controllers / fonts / etc)
- `tickGame()` - Called in `while True` loop, responsible for draw/input/physics updates
- `checkDraw()` - Checks, what should be drawn right now and makes a draw call
- `checkInputs()` - Checks for inputs (mouse click and ESC key)
- `checkPhysics()` - Responsible for moving enemies / ammo / updating tower states / updating `gameController`
- `updateXXXXX()` - Responsible for updating (physics of) XXXXX objects by calling `update()` method (XXXXX - name of object, enemy / tower / etc)
- `checkMouseInGameZone()` - Checks if mouse is placed in game zone (is over tiles)
- `checkClick` - This function is responsible for sending "clickPosition" to right object, it checks if game is running / stopped / etc. and sends "clickPosition" to needed method/function 
- `drawXXXXX()` - Same as `updateXXXXX()` but responsible for displaying object on screen
- `moveEnemies()` - Moves enemies
- `drawSelectedTile()` - Responsible for highlighting tile, over which cursor is placed
- `findClosestTile(mousePos)` - Iterates over tiles and find closest to "mousePos"
- `calculateTiles()` -  Calculates tiles positions on screen
- `generatePath()` - Generates a road for enemies, creates start (red base) and end (blue base) positions, then calls `generatePosts(startTile, endTile)`
- `generatePosts(startTile, endTile)` - Generates "posts" on map, which later will be connected with road
- `calculatePath(start, end, posts)` - Actually calculates the best path between posts by finding "best step" from start to target (post) and then adding that step to posts, and so on till blue base tile
- `getGameZoneBounds()` - Returns bound of game zone :/
- `pause()` - Pauses game :/
- `unpause()` - Unpauses game :/

## File `variables.py`:
This file contains all needed variable for game

### Description of some variables:
- `tiles` - Array of all tiles
- `roadTiles` - Array of all road tiles
- `interfaceController` - UIController responsible for showing interface and menus
- `gameController` - Responsible for spawning enemies win/lose states
- `audioController` - Responsible for sounds

## File `Tile.py`:
This file contains `Tile` class

### Fields:
- `position` - Position of the tile
- `color` - Color of the tile
- `tileResolutionPosition` - Position of the tile according to the tile grid
- `type` - Type of the tile
- `tower` - Optional, will be assigned only if `Tower` will be paled on `Tile`

## File `Tower.py`:
This file contains `Tower` class

### Fields:
- `lvl` - Lvl of tower
- `position` - Position
- `image` - Image of the tower
- `cost of upgrade` - Actually always 25
- `lastShot` - Time of last shot
- `currentShot` - Timer for the next shot


## File `Enemy.py`:
This file contains `Enemy` class

### Fields:
- `hp` - Health points of the enemy
- `speed` - Speed of the enemy
- `road` - Road array
- `roadLength` - Length of road array
- `currentRoadIndex` - Current tile in road array
- `currnetPosition` - Current position of the enemy
- `targetPosition` - Target position of the enemy

## File `Ammo.py`:
This file contains `Ammo` class

### Fields:
- `targetEnemy` - Enemy to fly to
- `speed` - Speed of the bullet
- `damage` - Damage of the bullet
- `position` - Position of the bullet
- `liveTime` - ttl (will be destroyed after `liveTime`)
- `spawnTime` - Time, when bullet was created
- `currentTime` - Current time
- `color` - Color of the bullet

## File `GameController.py`:
This file contains `GameController` class

### Fields:
- `lastSpawnTime` - Time, when last enemy was spawned
- `currentTime` - Timer for spawning next enemy

## File `UIController.py`:
This file contains `UIController` class
Responsible for drawing all elements of the UI and menus

### Fields:
- `needToDrawTowerSelector` - Tells, if it needs to show build menu
- `towerSelectorPos` -  Tells, where to place build menu
- `boundBuildButton` - Bounds of build button
- `boundUpgradeButton` - Bound of upgrade button
- `canUpgrade` - Tells, if it can upgrade
- `canBuild` - Tells, if it can build


## File `AudioController.py`:
This file contains `AudioController` class
Just a dummy class for more comfortable sound-calls


End of documentation :D

![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)
