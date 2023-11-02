from pgtools.ErrorMessage import ErrorMessage
from pgtools.Color import Color
from pgtools.Element import Element
from typing import Union, Tuple
import pygame

class Styles():
    # Calling
    def __call__(cls, *args, **kwargs):
        ErrorMessage.InitiateError(cls.__name__)

    # Get methods
    def getStyleInfo(self) -> dict:
        return {"padding": self.padding, "border": self.border, "borderColorRGBA": self.borderColorRGBA}
    
    def getPaddingTop(self) -> int:
        return self.padding[0]
    
    def getPaddingBottom(self) -> int:
        return self.padding[1]

    def getPaddingLeft(self) -> int:
        return self.padding[2]
    
    def getPaddingRight(self) -> int:
        return self.padding[3]
    
    def getPaddingAll(self) -> Tuple[int,int,int,int]:
        return self.padding
    
    def getBorderTop(self) -> int:
        return self.border[0]
    
    def getBorderBottom(self) -> int:
        return self.border[1]

    def getBorderLeft(self) -> int:
        return self.border[2]
    
    def getBorderRight(self) -> int:
        return self.border[3]
    
    def getBorderAll(self) -> Tuple[int,int,int,int]:
        return self.border
    
    def getBorderColor(self) -> Tuple[int,int,int,int]:
        return self.borderColorRGBA

    # Set methods
    def setStyleInfo(self, padding:Tuple[int,int,int,int]=(0,0,0,0), border:Tuple[int,int,int,int]=(0,0,0,0), borderColorRGB:Tuple[int,int,int,int]=Color.named.TRANSPARENT):
        self.padding = (0,0,0,0)
        self.border = (0,0,0,0)
        self.setBorderColor(borderColorRGB)
        self.setPaddingAll(*padding)
        self.setBorderAll(*border)

    def setPaddingTop(self, top:int=0):
        if not isinstance(top, int):
            ErrorMessage.TypeError('top', int, type(top))
        if top < 0:
            ErrorMessage.RangeError('top', 0, float('inf'), top)
        self.padding = (top, self.padding[1], self.padding[2], self.padding[3])

    def setPaddingBottom(self, bottom:int=0):
        if not isinstance(bottom, int):
            ErrorMessage.TypeError('bottom', int, type(bottom))
        if bottom < 0:
            ErrorMessage.RangeError('bottom', 0, float('inf'), bottom)
        self.padding = (self.padding[0], bottom, self.padding[2], self.padding[3])

    def setPaddingLeft(self, left:int=0):
        if not isinstance(left, int):
            ErrorMessage.TypeError('left', int, type(left))
        if left < 0:
            ErrorMessage.RangeError('left', 0, float('inf'), left)
        self.padding = (self.padding[0], self.padding[1], left, self.padding[3])

    def setPaddingRight(self, right:int=0):
        if not isinstance(right, int):
            ErrorMessage.TypeError('right', int, type(right))
        if right < 0:
            ErrorMessage.RangeError('right', 0, float('inf'), right)
        self.padding = (self.padding[0], self.padding[1], self.padding[2], right)

    def setPaddingAll(self, top:int, bottom:int, left:int, right:int):
        self.setPaddingTop(top)
        self.setPaddingBottom(bottom)
        self.setPaddingLeft(left)
        self.setPaddingRight(right)

    def setPadding(self, padding:int):
        self.setPaddingAll(padding, padding, padding, padding)

    def setBorderTop(self, top:int=0):
        if not isinstance(top, int):
            ErrorMessage.TypeError('top', int, type(top))
        if top < 0:
            ErrorMessage.RangeError('top', 0, float('inf'), top)
        self.border = (top, self.border[1], self.border[2], self.border[3])

    def setBorderBottom(self, bottom:int=0):
        if not isinstance(bottom, int):
            ErrorMessage.TypeError('bottom', int, type(bottom))
        if bottom < 0:
            ErrorMessage.RangeError('bottom', 0, float('inf'), bottom)
        self.border = (self.border[0], bottom, self.border[2], self.border[3])

    def setBorderLeft(self, left:int=0):
        if not isinstance(left, int):
            ErrorMessage.TypeError('left', int, type(left))
        if left < 0:
            ErrorMessage.RangeError('left', 0, float('inf'), left)
        self.border = (self.border[0], self.border[1], left, self.border[3])

    def setBorderRight(self, right:int=0):
        if not isinstance(right, int):
            ErrorMessage.TypeError('right', int, type(right))
        if right < 0:
            ErrorMessage.RangeError('right', 0, float('inf'), right)
        self.border = (self.border[0], self.border[1], self.border[2], right)

    def setBorderAll(self, top:int, bottom:int, left:int, right:int):
        self.setBorderTop(top)
        self.setBorderBottom(bottom)
        self.setBorderLeft(left)
        self.setBorderRight(right)

    def setBorder(self, border:int, colorRGBA:Tuple[int,int,int,int]):
        self.setBorderAll(border, border, border, border)
        self.setBorderColor(colorRGBA)

    def setBorderColor(self, colorRGBA:Tuple[int,int,int,int]):
        if not isinstance(colorRGBA, (tuple,list)):
            ErrorMessage.TypeError('colorRGBA', tuple, type(colorRGBA))
        if len(colorRGBA) == 3:
            colorRGBA = colorRGBA[:3] + (255,)
        if not len(colorRGBA) == 4:
            ErrorMessage.LengthError('colorRGBA', 4, len(colorRGBA))
        self.borderColorRGBA = Color.rgba(*colorRGBA)

    # Display methods
    def calcBorder(self, width:int, height:int) -> Union[pygame.Surface, Union[Tuple[int, int], Tuple[int, int]]]:
        # Create border surface
        top, bottom, left, right = self.border
        trueWidth = width + left + right
        trueHeight = height + top + bottom

        # Create border
        surface = pygame.Surface((trueWidth, trueHeight), pygame.SRCALPHA)
        colorRGBA = self.borderColorRGBA
        
        # Draw rects
        topRect = pygame.Rect(0, 0, trueWidth, top)
        bottomRect = pygame.Rect(0, trueHeight - bottom, trueWidth, bottom)
        leftRect = pygame.Rect(0, top, left, trueHeight)
        rightRect = pygame.Rect(trueWidth - right, top, right, trueHeight)

        pygame.draw.rect(surface, colorRGBA, topRect)
        pygame.draw.rect(surface, colorRGBA, bottomRect)
        pygame.draw.rect(surface, colorRGBA, leftRect)
        pygame.draw.rect(surface, colorRGBA, rightRect)

        # Return
        return surface, (trueWidth, trueHeight), (left, top)
    
    def calcPadding(self, width:int, height:int, render:pygame.surface.Surface, renderWidth:int, renderHeight:int, contentSurface:pygame.Surface) -> pygame.Surface:
        # Calculate content area size
        contentWidth = width - (self.padding[2] + self.padding[3])
        contentHeight = height - (self.padding[0] + self.padding[1])

        # Align text within the content area
        contentX = (contentWidth - renderWidth) // 2 + self.padding[2]
        contentY = (contentHeight - renderHeight) // 2 + self.padding[0]

        # Display the text on the content area
        contentSurface.blit(render, (contentX, contentY))

        return contentSurface