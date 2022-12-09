import pygame.draw

import variables

# Bullet class:
class Ammo:
    def __init__(self, instancePos, targetEnemy, speed, damage, color): # Constructor
        self.targetEnemy = targetEnemy  # Target to follow
        self.speed = speed  # Speed
        self.damage = damage # Damage of the bullet
        self.position = instancePos # start position
        self.liveTime = 1000    # TTL
        self.spawnTime = pygame.time.get_ticks()   # Time when spawned
        self.currentTime = self.spawnTime   # Timer
        self.color = color # Color of the bullet
        variables.audioController.playShot() # play shot sound

    def update(self):   # Call every physics tick
        self.moveTowardsEnemy() #Move towards enemy
        self.currentTime = pygame.time.get_ticks() # Update timer
        if self.currentTime - self.spawnTime > self.liveTime: # If stuck (lives longer then liveTime -> Destroy)
            self.destroy()  #Destroy itself

    def moveTowardsEnemy(self): # Function to move towards enemy
        vectorX, vectorY = (
        self.targetEnemy.getPosition()[0] - self.position[0], self.targetEnemy.getPosition()[1] - self.position[1]) #Calculate movement vector

        # Normalize vector:
        if vectorY < 0:
            stepY = (-1 * self.speed) / variables.FPS
        else:
            stepY = (1 * self.speed) / variables.FPS
        if vectorX < 0:
            stepX = (-1 * self.speed) / variables.FPS
        else:
            stepX = (1 * self.speed) / variables.FPS

        self.position = (self.position[0] + stepX, self.position[1] + stepY) # Update position

        # Check if close to the enemy:
        checkMinDistance = abs(self.position[0] - self.targetEnemy.getPosition()[0]) < 7 and abs(
            self.position[1] - self.targetEnemy.getPosition()[1]) < 2

        # if close -> damage enemy and destroy itself
        if checkMinDistance:
            self.targetEnemy.getDamage(self.damage)
            self.destroy()

    def destroy(self): # Destroy function
        try:
            variables.ammos.remove(self) # Just remove itself from ammos[] array
        except Exception as e:
            pass

    # Draw itself every draw-frame
    def draw(self, window):
        pygame.draw.circle(window, self.color, self.position, 4, 4)
