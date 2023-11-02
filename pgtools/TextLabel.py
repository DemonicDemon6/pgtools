from pgtools.Color import Color
from pgtools.Element import Element
from pgtools.Styles import Styles
from pgtools.ErrorMessage import ErrorMessage
from typing import Tuple
import pygame

class TextLabel(Styles, Element):
    # Inherited from Elements:
    # Get methods: getElementInfo(), getWidth(), getHeight(), getSize(), getCoordX(), getCoordY(), getPos(), getBackgroundColor()
    # Set methods: setElementInfo(), setWidth(), setHeight(), setSize(), setCoordX(), setCoordY(), setPos(), setBackgroundColor()
    
    # Inherited from Styles:
    # Get methods: getPaddingTop(), getPaddingBottom(), getPaddingLeft(), getPaddingRight(), getPaddingAll()
    #              getBorderTop(), getBorderBottom(), getBorderLeft(), getBorderRight(), getBorderAll(), getBorderColor()
    #              getStyleInfo()
    # 
    # Set methods: setPaddingTop(), setPaddingBottom(), setPaddingLeft(), setPaddingRight(), setPaddingAll()
    #              setBorderTop(), setBorderBottom(), setBorderLeft(), setBorderRight(), setBorderAll(), setBorderColor()
    #              setStyleInfo()
    #
    # Display methods: calcBorder(), calcPadding()

    # Initiate instance
    def __init__(self, text:str, font:pygame.font.Font, colorRGB:Tuple[int,int,int] = Color.named.DEFAULT, width:int = 0, height:int = 0, pos:Tuple[int,int]=(0,0), bgColorRGBA:Tuple[int,int,int] = Color.named.TRANSPARENT):
        super().__init__(width, height, pos, bgColorRGBA)
        self.setLabelInfo(text, font, colorRGB)
        self.setStyleInfo(borderColorRGB=Color.named.TRANSPARENT)
        self.surface = None

    def __str__(self):
        label = self.getLabelInfo()
        element = self.getElementInfo()
        style = self.getStyleInfo()
        return f"TextLabel: ({', '.join([f'{key}:{value}' for key, value in label.items()])})\n - inherits Element: ({', '.join([f'{key}: {value}' for key, value in element.items()])})\n - inherits Styles: ({', '.join([f'{key}: {value}' for key, value in style.items()])})"

    def __repr__(self) -> str:
        label = self.getLabelInfo()
        element = self.getElementInfo()
        style = self.getStyleInfo()
        return f"TextLabel: ({', '.join([f'{value}' for _, value in label.items()])})\n - inherits Element: ({', '.join([f'{value}' for _, value in element.items()])})\n - inherits Styles: ({', '.join([f'{value}' for _, value in style.items()])})"

    # Get methods
    def getLabelInfo(self)-> dict:
        return {"text":self.text, "font":self.font, "colorRGB":self.colorRGB}

    def getText(self) -> str:
        return self.text

    def getFont(self) -> pygame.font.Font:
        return self.font

    def getColor(self) -> Tuple[int,int,int]:
        return self.colorRGB

    # Set methods
    def setLabelInfo(self, text:str, font:pygame.font.Font, colorRGB:Tuple[int,int,int] = Color.named.DEFAULT):
        self.setText(text)
        self.setFont(font)
        self.setColor(colorRGB)
        self.padding = (0,0,0,0)
        
    def setText(self, text:str):
        if not isinstance(text, str):
            ErrorMessage.TypeError('text', str, type(text))
        self.text = text
        self.surface = None

    def setFont(self, font:pygame.font.Font):
        if not isinstance(font, pygame.font.Font):
            ErrorMessage.TypeError('font', pygame.font.Font, type(font))
        self.font = font
        self.surface = None

    def setColor(self, colorRGB:Tuple[int,int,int]):
        if not isinstance(colorRGB, (tuple,list)):
            ErrorMessage.TypeError('colorRGB', tuple, type(colorRGB))
        if not len(colorRGB) == 3:
            ErrorMessage.LengthError('colorRGB', 3, len(colorRGB))
        self.colorRGB = Color.rgb(*colorRGB)
        self.surface = None

    # Display methods
    def display(self, screen):
        if self.surface == None:
            self.updateSurface()
        screen.blit(self.surface, self.pos)

    def updateSurface(self) -> pygame.surface.Surface:
        # Auto adjust height and width if needed
        renderText = self.font.render(self.text, True, self.colorRGB)
        textWidth, textHeight = renderText.get_size()[0], renderText.get_size()[1]
        if self.getWidth() == 0:
            self.setWidth(textWidth)
        if self.getHeight() == 0:
            self.setHeight(textHeight)

        # Get border | borderSurface:pygame.Surface, borderSize:tuple (width, height), borderLT:tuple (left, top)
        borderSurface, borderSize, borderLT = self.calcBorder(self.getWidth(), self.getHeight())

        # Get content surface with acount of padding | contentSurface:pygame.Surface
        contentSurface = pygame.Surface((self.getWidth(), self.getHeight()), pygame.SRCALPHA)
        contentSurface.fill(self.backgroundColorRGBA)
        contentSurface = self.calcPadding(self.getWidth(), self.getHeight(), renderText, textWidth, textHeight, contentSurface)

        # Combine the content and border surfaces
        combinedSurface = pygame.Surface((borderSize[0], borderSize[1]), pygame.SRCALPHA)
        combinedSurface.blit(borderSurface, (0, 0))
        combinedSurface.blit(contentSurface, (borderLT[0], borderLT[1]))

        # Store in self.surface
        self.surface = combinedSurface
        self.rect = pygame.Rect(self.pos[0], self.pos[1], combinedSurface.get_size()[0], combinedSurface.get_size()[1])