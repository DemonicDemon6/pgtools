import pygame
from pgtools.Color import Color
from pgtools.Element import Element
from typing import Tuple

class Button(Element):
    # Inherited from Elements:
    # Get methods: getElementInfo(), getWidth(), getHeight(), getSize(), getCoordX(), getCoordY(), getPos(), getBackgroundColor()
    # Set methods: setElementInfo(), setWidth(), setHeight(), setSize(), setCoordX(), setCoordY(), setPos(), setBackgroundColor()
    # Display methods: display(), updateSurface()

    # Initiate instances
    def __init__(self, width:int, height:int, pos:Tuple[int,int] = (0,0), bgColorRGBA:Tuple[int,int,int,int] = Color.named.GREEN):
        super().__init__(width, height, pos, bgColorRGBA)
        self.held = False

    def __str__(self) -> str:
        element = self.getElementInfo()
        return f"Button: ({', '.join([f'{key}: {value}' for key, value in element.items()])})"
    
    def __repr__(self) -> str:
        element = self.getElementInfo()
        return f"Button: ({', '.join([f'{value}' for _, value in element.items()])})"
    
    # Display methods
    def isHovered(self) -> bool:
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def isClicked(self) -> bool:
        return self.isHovered() and (pygame.mouse.get_pressed()[0] == 1 or pygame.mouse.get_pressed()[2] == 1)

    def isLeftClicked(self) -> bool:
        return self.isClicked() and pygame.mouse.get_pressed()[0] == 1

    def isRightClicked(self) -> bool:
        return self.isClicked() and pygame.mouse.get_pressed()[2] == 1