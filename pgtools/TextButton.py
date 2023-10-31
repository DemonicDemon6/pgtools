from pgtools.Button import Button

class TextButton(Button):
    def __init__(self, text, color, background=0):
        super()
        self.text = text
        self.color = color
        self.background = background

    def __str__(self):
        return f'TextButton: text=\'{self.text}\' font={self.font} color={self.color} pos=({self.x},{self.y}), size=({self.w},{self.h})'

    def setFont(self, font):
        pass

    def setFontFromFile(self, location, size=1):
        pass
    
    def setText(self, text, color, background=0):
        pass