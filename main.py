import sys

import pygame

WINDOW_HEIGHT, WINDOW_WIDTH = 600, 600

window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit(0)