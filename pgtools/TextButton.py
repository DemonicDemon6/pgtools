from pgtools.Button import Button
from pgtools.Color import Color
from pgtools.Element import Element
from pgtools.ErrorMessage import ErrorMessage
from pgtools.TextLabel import TextLabel
from typing import Tuple
import pygame

class TextButton(TextLabel, Button):
    # Inherited from Elements:
    # Get methods: getElementInfo(), getWidth(), getHeight(), getSize(), getCoordX(), getCoordY(), getPos(), getBackgroundColor()
    # Set methods: setElementInfo(), setWidth(), setHeight(), setSize(), setCoordX(), setCoordY(), setPos(), setBackgroundColor()
    
    # Inherits from Button:
    # Display methods: isHovered(), isClicked(), isLeftClicked(), isRightClicked()

    # Inherits from TextLabel
    # Get methods: getText(), getFont(), getColor(), getLabelInfo()
    # Set methods: setText(), setFont(), setColor(), setLabelInfo()
    # Display methods: display(), updateSurface()

    # Inherited from Styles:
    # Get methods: getPaddingTop(), getPaddingBottom(), getPaddingLeft(), getPaddingRight(), getPaddingAll()
    #              getBorderTop(), getBorderBottom(), getBorderLeft(), getBorderRight(), getBorderAll(), getBorderColor()
    #              getStyleInfo()
    # 
    # Set methods: setPaddingTop(), setPaddingBottom(), setPaddingLeft(), setPaddingRight(), setPaddingAll()
    #              setBorderTop(), setBorderBottom(), setBorderLeft(), setBorderRight(), setBorderAll(), setBorderColor()
    #              setStyleInfo()
    #
    # Display methods: createBorder()

    # Initiate instance
    def __init__(self, text:str, font:pygame.font.Font, colorRGB:Tuple[int,int,int], width:int = 0, height:int = 0, pos:Tuple[int,int] = (0,0), bgColorRGBA:Tuple[int,int,int,int] = Color.named.DEFAULT):
        super().__init__(text, font, colorRGB, width, height, pos, bgColorRGBA)

    def __str__(self) -> str:
        label = self.getLabelInfo()
        button = self.getElementInfo() # Button == Clickable Element
        style = self.getStyleInfo()
        return f"TextButton({', '.join([f'{key}:{value}' for key, value in label.items()])})\n - inherits Button: ({', '.join([f'{key}: {value}' for key, value in button.items()])})\n - inherits Styles: ({', '.join([f'{key}: {value}' for key, value in style.items()])})"
    
    def __repr__(self) -> str:
        label = self.getLabelInfo()
        button = self.getElementInfo() # Button == Clickable Element
        style = self.getStyleInfo()
        return f"TextButton: ({', '.join([f'{value}' for _, value in label.items()])})\n - inherits Button: ({', '.join([f'{value}' for _, value in button.items()])})\n - inherits Styles: ({', '.join([f'{value}' for _, value in style.items()])})"
    
    # Display method
    def display(self, screen):
        if self.surface is None:
            self.updateSurface()
        super().display(screen)