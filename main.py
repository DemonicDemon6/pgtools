import pygame as pygame
import pgtools

pygame.init()

# Create screen
width, height = 1100, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PG Tools')
fps = 60

font = pygame.font.Font(None, 32)

def updateDisplay():
    element = pgtools.Element(200, 100, (111,111), pgtools.Color.named.GREEN)
    element.display(screen)

    btn = pgtools.Button(300, 100, (20,20), pgtools.Color.rgb(255, 255, 255))
    # btn.display(screen)
    # if btn.isClicked():
    #     print('Clicked')

    text1 = pgtools.TextLabel('Hello!', font, pgtools.Color.named.WHITE, 200, 100, (111,111), pgtools.Color.named.YELLOW)
    text1.setPaddingLeft(20)
    text1.setBorder(10)
    text1.setBorderColor(pgtools.Color.named.DEFAULT)
    text1.display(screen)
    # textBtn = pgtools.TextButton('Hello!', font, pgtools.Color.named.WHITE, 100, 500, (111,111), pgtools.Color.named.YELLOW)
    # textBtn.display(screen)

run = True
while run:
    clock = pygame.time.Clock()
    clock.tick(fps)
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    updateDisplay()
    pygame.display.update()
    
pygame.quit()