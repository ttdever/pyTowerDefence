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


End of documentation :D

![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)
