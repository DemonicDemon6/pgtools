import pygame
from pgtools.ErrorMessage import ErrorMessage
from pgtools.Color import Color
from typing import Tuple

class Element:
    # Initiate
    def __init__(self, width:int, height:int, pos:Tuple[int,int] = (0, 0), bgColorRGBA:Tuple[int,int,int,int] = Color.named.DEFAULT):
        self.setElementInfo(width, height, pos, bgColorRGBA)

    def __str__(self) -> str:
        element = self.getElementInfo()
        return f"Element: ({', '.join([f'{key}: {value}' for key, value in element.items()])})"

    def __repr__(self) -> str:
        element = self.getElementInfo()
        return f"Element: ({', '.join([f'{value}' for _, value in element.items()])})"

    # Get methods
    def getElementInfo(self) -> dict:
        return {"size":self.size, "pos":self.pos, "backgroundColorRGBA":self.backgroundColorRGBA}

    def getWidth(self) -> int:
        return self.size[0]

    def getHeight(self) -> int:
        return self.size[1]

    def getSize(self) -> Tuple[int, int]:
        return self.size

    def getCoordX(self) -> int:
        return self.pos[0]

    def getCoordY(self) -> int:
        return self.pos[1]

    def getPos(self) -> Tuple[int,int]:
        return self.pos

    def getBackgroundColor(self) -> Tuple[int,int,int,int]:
        return self.backgroundColorRGBA

    # Set methods
    def setElementInfo(self, width:int, height:int, pos:Tuple[int,int] = (0, 0), bgColorRGBA:Tuple[int,int,int,int] = Color.named.DEFAULT):
        self.size = (0,0)
        self.pos = (0,0)
        self.setSize(width, height)
        self.setPos(pos)
        self.setBackgroundColor(bgColorRGBA)

    def setWidth(self, width:int):
        if not isinstance(width, int):
            ErrorMessage.TypeError('width', int, type(width))
        self.size = (width, self.size[1])
        self.surface = None

    def setHeight(self, height:int):
        if not isinstance(height, int):
            ErrorMessage.TypeError('height', int, type(height))
        self.size = (self.size[0], height)
        self.surface = None

    def setSize(self, width:int, height:int):
        self.setWidth(width)
        self.setHeight(height)

    def setCoordX(self, x:int):
        if not isinstance(x, int):
            ErrorMessage.TypeError('X Coordinate', int, type(x))
        self.pos = (x, self.pos[1])
        self.surface = None

    def setCoordY(self, y:int):
        if not isinstance(y, int):
            ErrorMessage.TypeError('Y Coordinate', int, type(y))
        self.pos = (self.pos[0], y)
        self.surface = None

    def setPos(self, pos:Tuple[int,int]):
        if not isinstance(pos, (tuple,list)):
            ErrorMessage.TypeError('pos', tuple, type(tuple))
        if not len(pos) == 2:
            ErrorMessage.LengthError('pos', 2, len(pos))
        x, y = pos
        self.setCoordX(x)
        self.setCoordY(y)

    def setBackgroundColor(self, backgroundColorRGBA:Tuple[int,int,int,int]):
        if not isinstance(backgroundColorRGBA, (tuple,list)):
            ErrorMessage.TypeError('backgroundColorRGBA', tuple, type(backgroundColorRGBA))
        if len(backgroundColorRGBA) == 3:
            backgroundColorRGBA = backgroundColorRGBA[:3] + (255,)
        if not len(backgroundColorRGBA) == 4:
            ErrorMessage.LengthError('backgroundColorRGBA', 4, len(backgroundColorRGBA))
        self.backgroundColorRGBA = Color.rgba(*backgroundColorRGBA)
        self.surface = None

    # Display methods
    def display(self, screen:pygame.surface.Surface):
        if self.surface == None:
            self.updateSurface()
        screen.blit(self.surface, self.pos)

    def updateSurface(self):
        surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        pygame.draw.rect(surface, self.backgroundColorRGBA, self.rect)
        self.surface = surface