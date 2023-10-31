import pygame as pygame
import pgtools

pygame.init()

# Create screen
width, height = 1100, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PG Tools')
fps = 60

run = True
while run:
    clock = pygame.time.Clock()
    clock.tick(fps)
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    
pygame.quit()