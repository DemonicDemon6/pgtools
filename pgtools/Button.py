from pgtools.Color import Color
import pygame

class Button:
    # Initiate Button instance
    def __init__(self, width: int, height: int, background:tuple=(0,0,0,255), pos:tuple=(0,0)):
        self.size = (0,0)
        self.pos = (0,0)
        self.setSize(width, height)
        self.setBackgroundColor(background)
        self.setPos(pos)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    # str + repr
    def __str__(self):
        return f"Button (Width: {self.size[0]}, Height: {self.size[1]}, BackgroundColor: {self.background}, Pos: {self.pos})"

    def __repr__(self):
        return f"Button({self.size[0]}, {self.size[1]}, {self.background}, {self.pos})"

    # Set methods
    def setWidth(self, width: int):
        if not isinstance(width, int):
            raise TypeError(f"Expected width as integer. Got {type(width)}")
        self.size = (width, self.size[1])
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def setHeight(self, height: int):
        if not isinstance(height, int):
            raise TypeError(f"Expected height as integer. Got {type(height)}")
        self.size = (self.size[0], height)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def setSize(self, width: int, height: int):
        self.setWidth(width)
        self.setHeight(height)

    def setBackgroundColor(self, color: tuple):
        if not isinstance(color, (tuple,list)):
            raise TypeError(f"Expected color as tuple/list. Got {type(color)}")
        if not len(color) == 4:
            raise ValueError(f"Expected 4 values in color. Got {len(color)}")
        r, g, b, a = color
        self.background = Color.rgba(r,g,b,a)

    def setPos(self, pos: tuple):
        if not (isinstance(pos, (tuple, list))):
            raise TypeError(f'Expected pos as tuple/list. Got {type(pos)}')
        if not len(pos) == 2:
            raise ValueError(f'Expected two values in pos. Got {len(pos)} values')
        if not all(isinstance(val, int) for val in pos):
            raise TypeError('Expected x,y coordinates as integers')
        self.pos = pos
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    # Get methods
    def getSize(self):
        return self.size

    def getPos(self):
        return self.pos
    
    def getBackgroundColor(self):
        return self.background

    # Display methods
    def display(self, screen: pygame.surface.Surface):
        surface = pygame.Surface(self.size, pygame.SRCALPHA)
        pygame.draw.rect(surface, self.background, (0, 0, self.size[0], self.size[1]))
        screen.blit(surface, self.pos)

    def isHovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def isClicked(self):
        return self.isHovered() and (pygame.mouse.get_pressed()[0] == 1 or pygame.mouse.get_pressed()[2] == 1)

    def isLeftClicked(self):
        return self.isClicked() and pygame.mouse.get_pressed()[0] == 1

    def isRightClicked(self):
        return self.isClicked() and pygame.mouse.get_pressed()[2] == 1