from pgtools.ErrorMessage import ErrorMessage
from typing import Tuple

class Color:
    def __call__(cls, *args, **kwargs):
        ErrorMessage.InitiateError(cls.__name__)
    
    # Named colors
    class named:
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        PURPLE = (128, 0, 128)
        ORANGE = (255, 165, 0)
        YELLOW = (251, 236, 93)
        AQUA = (0, 255, 255)
        GRAY = (128, 128, 128)
        LIGHT_GRAY = (211, 211, 211)
        DEFAULT = (39, 205, 227)
        TRANSPARENT = (255, 255, 255, 0)

    @staticmethod
    def rgb(r:int, g:int, b:int) -> Tuple[int,int,int]:
        rgb = (r, g, b)
        if not all(isinstance(val, int) for val in rgb):
            ErrorMessage.TypeError("RGB", int, (type(r),type(g),type(b)))
        if not all(0 <= val <= 255 for val in rgb):
            ErrorMessage.RangeError("RGB", 0, 255, (r, g, b))
        return (r, g, b)

    @staticmethod
    def rgba(r:int, g:int, b:int, a:int) -> Tuple[int,int,int,int]:
        rgba = (r, g, b, a)
        if not all(isinstance(val, int) for val in rgba):
            ErrorMessage.TypeError("RGBA", int, (type(r),type(g),type(b),type(a)))
        if not all(0 <= val <= 255 for val in rgba):
            ErrorMessage.RangeError("RGB", 0, 255, (r, g, b, a))
        return (r, g, b, a)

    @staticmethod
    def hex(hexCode:str) -> Tuple[int,int,int,int]:
        if hexCode[0] == "#":
            hexCode = hexCode[1:]
        valid = "0123456789ABCDEF"
        if all(char.upper() in valid for char in hexCode) and (len(hexCode) == 3 or len(hexCode) == 6):
            return tuple(int(hexCode[i:i+2], 16) for i in (0, 2, 4))
        else:
            ErrorMessage.FormatError('hexcode', '#ffffff or #fff', hexCode)