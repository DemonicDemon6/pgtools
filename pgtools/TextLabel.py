from pgtools.Color import Color
import pygame

class TextLabel:
    # Initiate TextLabel instance
    def __init__(self, text: str, font: pygame.font.Font, color:tuple=(0, 0, 0), pos:tuple=(0, 0)):
        self.setText(text)
        self.setFont(font)
        self.setColor(color)
        self.setPos(pos)

    # str + repr
    def __str__(self):
        return f"Text: {self.text}, Font: {self.font}, Color: {self.color}, Pos: {self.pos}"
    
    def __repr__(self):
        return f"Text('{self.text}', {self.font}, {self.color}, {self.pos})"
    
    # Set methods
    def setText(self, text: str):
        if not isinstance(text, str):
            raise TypeError(f"Expected text as string. Got {type(text)}")
        self.text = text
        self.surface = None
    
    def setFont(self, font: pygame.font.Font):
        if not isinstance(font, pygame.font.Font):
            raise TypeError(f'Font must be a Pygame Font object. Got {type(font)}')
        self.font = font
        self.surface = None

    def setColor(self, color: tuple):
        if not isinstance(color, (tuple,list)):
            raise TypeError(f'Expected color as tuple/list. Got {type(color)}')
        if not len(color) == 3:
            raise ValueError(f'Expected three values in color. Got {len(color)} values')
        r, g, b = color
        self.color = Color.rgb(r, g, b)
        self.surface = None

    def setPos(self, pos: tuple):        
        if not (isinstance(pos, (tuple, list))):
            raise TypeError(f'Expected pos as tuple/list. Got {type(pos)}')
        if not len(pos) == 2:
            raise ValueError(f'Expected two values in pos. Got {len(pos)} values')
        if not all(isinstance(val, int) for val in pos):
            raise TypeError('Expected x,y coordinates as integers')
        self.pos = pos

    # Get methods
    def getText(self):
        return self.text
    
    def getFont(self):
        return self.font
    
    def getColor(self):
        return self.color

    def getPos(self):
        return self.pos
    
    def getSize(self):
        if self.font is not None:
            rect = self.font.render(self.text, True, self.color).get_rect()
            return rect.width, rect.height
        else:
            return (0, 0)
        
    # Display methods
    def display(self, screen: pygame.surface.Surface, antialias:bool=True):
        if self.surface is None:
            self.surface = self.font.render(self.text, antialias, self.color)
        screen.blit(self.surface, self.pos)