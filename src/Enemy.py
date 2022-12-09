import variables
import pygame
import variables

enemyColors = [(252, 230, 201), (205, 173, 0), (0, 128, 0), (205, 92, 92), (205, 205, 193), (240, 128, 128)]


# Enemy class:
class Enemy:
    def __init__(self, hp, speed, road): #Constructor
        self.hp = hp                                    # Hp of the enemy
        self.speed = speed                              # Speed of the enemy
        self.road = road                                # Tiles of the road
        self.roadLength = len(road) - 1                 # Last tile index
        self.currentRoadIndex = 1                       # Current tile index
        self.currentPosition = road[0].getPosition()    # Current position
        self.targetPosition = road[1].getPosition()     # Target position

    def draw(self, window):     # Draw to call every draw-frame

        #Calculate color:
        if 10 <= self.hp < 20:
            color = enemyColors[0]
        elif 20 <= self.hp < 30:
            color = enemyColors[1]
        elif 30 <= self.hp < 40:
            color = enemyColors[2]
        elif 40 <= self.hp < 50:
            color = enemyColors[3]
        elif 50 <= self.hp < 60:
            color = enemyColors[4]
        elif self.hp >= 60:
            color = enemyColors[5]
        else:
            color = (255, 255, 255)

        # Draw enemy
        pygame.draw.circle(window, (0, 0, 0), self.currentPosition, 6)
        pygame.draw.circle(window, color, self.currentPosition, 5)

    def move(self):
        # Calculate vector
        vectorX, vectorY = (
        self.targetPosition[0] - self.currentPosition[0], self.targetPosition[1] - self.currentPosition[1])

        # Normalize vector:
        if vectorY < 0:
            stepY = (-1 * self.speed) / variables.FPS
        else:
            stepY = (1 * self.speed) / variables.FPS
        if vectorX < 0:
            stepX = (-1 * self.speed) / variables.FPS
        else:
            stepX = (1 * self.speed) / variables.FPS

        # Update position:
        self.currentPosition = (self.currentPosition[0] + stepX, self.currentPosition[1] + stepY)

        # Check min distance to next tile
        checkMinDistance = abs(self.currentPosition[0] - self.targetPosition[0]) < 7 and abs(
            self.currentPosition[1] - self.targetPosition[1]) < 7

        # If near next tile -> switch to next tile + 1
        if checkMinDistance:
            # if current tile index < size of tile array:
            if self.currentRoadIndex < self.roadLength:
                self.currentRoadIndex += 1
                self.targetPosition = self.road[self.currentRoadIndex].getPosition()
            # else (means that enemy is at last tile (base tile)) -> damage player base
            else:
                variables.gameController.getPlayerDamage()
                variables.audioController.playBaseHit()
                variables.enemies.remove(self)

    # Function to get damage from bullets
    def getDamage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()

    def die(self):
        try:
            # Play death sound remove itself from enemies[] array and add money to player
            variables.audioController.playEnemyHit()
            variables.enemies.remove(self)
            variables.money += variables.moneyPerEnemy
        except Exception as e:
            pass

    # Return enemies position:
    def getPosition(self):
        return self.currentPosition
