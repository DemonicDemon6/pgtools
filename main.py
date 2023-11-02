import pygame
import pgtools
from pgtools import Color

pygame.init()

# Create screen
width, height = 1100, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PG Tools')
fps = 60

font = pygame.font.Font(None, 32)


def updateDisplay():
    # element = pgtools.Element(200, 100, (111,111), pgtools.Color.named.GREEN)
    # element.display(screen)

    # btn = pgtools.Button(300, 100, (20,20), pgtools.Color.rgb(255, 255, 255))
    # btn.display(screen)
    # if btn.isClicked():
    #     print('Clicked')

    # text1 = pgtools.TextLabel('Hello!', font, Color.named.WHITE, 200, 100, (525,125), (255, 255, 255, 1))
    # text1.setPaddingTop(20)
    # text1.setPaddingRight(20)
    # text1.setBorder(20, (255,255,255,255))
    # text1.display(screen)

    # textBtn = pgtools.TextButton('Hello!', font, pgtools.Color.named.WHITE, 200, 100, (111,111), pgtools.Color.named.YELLOW)
    # textBtn.setBorder(20, (255, 255, 255, 100))
    # textBtn.display(screen)
    # if textBtn.isLeftClicked():
    #     print("hi")

    # surface = pygame.Surface((500,200), pygame.SRCALPHA)
    # surface.fill((255,255,255,128))
    # text = font.render('Hello hello hello how r u', True, (255,0,0))

    # textX = (surface.get_size()[0] // 2) - (text.get_size()[0] // 2)
    # textY = (surface.get_size()[1] // 2) - (text.get_size()[1] // 2)

    # surface.blit(text, (textX,textY))
    # screen.blit(surface, (50,50))
    pass


run = True
while run:
    clock = pygame.time.Clock()
    clock.tick(fps)
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(Color.named.BLACK)
    updateDisplay()
    pygame.display.flip()

pygame.quit()
