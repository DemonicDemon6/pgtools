class Color:
    # Named colors
    class named:
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        PURPLE = (128, 0, 128)
        ORANGE = (255, 165, 0)
        AQUA = (0, 255, 255)
        GRAY = (128, 128, 128)
        LIGHT_GRAY = (211, 211, 211)

    @staticmethod
    def rgb(r: int, g: int, b: int):
        rgb = (r, g, b)
        if not all(isinstance(val, int) for val in rgb):
            raise TypeError(f'Expected RGB as integers.')
        if not all(0 <= val <= 255 for val in rgb):
            raise ValueError(f'RGB values should be between 0-255')
        return (r, g, b)
    
    def rgba(r: int, g: int, b: int, a: int):
        rgba = (r, g, b, a)
        if not all(isinstance(val, int) for val in rgba):
            raise TypeError(f'Expected RGB as integers.')
        if not all(0 <= val <= 255 for val in rgba):
            raise ValueError(f'RGB values should be between 0-255')
        return (r, g, b, a)

    @staticmethod
    def hex(hexCode: str):
        if isValidHexCode(hexCode):
            hexCode = hexCode.lstrip('#')
            return tuple(int(hexCode[i:i+2], 16) for i in (0, 2, 4))
        else:
            raise ValueError("Invalid hex color code. Form: '#ffffff'")

def isValidHexCode(hexCode: str):
    if hexCode[0] == '#':
        hexCode = hexCode[1:]
        valid = '0123456789ABCDEF'
        return all(char.upper() in valid for char in hexCode) and (len(hexCode) == 3 or len(hexCode) == 6)

    return False