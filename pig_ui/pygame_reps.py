def Color(*args) -> tuple[int, int, int, int]:
    r, g, b, a = 0, 0, 0, 255
    if len(args) == 1:
            arg = args[0]
            if isinstance(arg, str):
                hex_str = arg.lstrip('#')
                if len(hex_str) == 6: #252525
                    r = int(hex_str[0:2], 16)
                    g = int(hex_str[2:4], 16)
                    b = int(hex_str[4:6], 16)
                elif len(hex_str) == 8: #252525ff
                    r = int(hex_str[0:2], 16)
                    g = int(hex_str[2:4], 16)
                    b = int(hex_str[4:6], 16)
                    a = int(hex_str[6:8], 16)
                    
            elif isinstance(arg, (tuple, list)):
                if len(arg) >= 3:
                    r, g, b = arg[0], arg[1], arg[2]
                if len(arg) == 4:
                    a = arg[3]
    elif len(args) >= 3:
        r, g, b = args[0], args[1], args[2]
        if len(args) == 4:
            a = args[3]
            
    return (r,g,b,a)
from pygame import Vector2
type VectorLike = int | float | tuple | Vector2
class Vector2: ...
class Vector2:
    def __init__(self, x: float | int, y: float | int):
        self.x, self.y = x, y
    
    @property
    def xx(self) -> Vector2:
        return Vector2(self.x, self.x)
    @property
    def yy(self) -> Vector2:
        return Vector2(self.y, self.y)
    @property
    def yx(self) -> Vector2:
        return Vector2(self.y, self.x)
    @property
    def xy(self) -> Vector2:
        return Vector2(self.x, self.y)
    
    def __add__(self, val: VectorLike) -> Vector2:
        if isinstance(val, (int, float)):
            return Vector2(self.x + val, self.y + val)
        elif isinstance(val, tuple):
            return Vector2(self.x + val[0], self.y + val[1])
        elif isinstance(val, Vector2):
            return Vector2(self.x + val.x, self.y + val.y)
    
    def __sub__(self, val: VectorLike) -> Vector2:
        if isinstance(val, (int, float)):
            return Vector2(self.x - val, self.y - val)
        elif isinstance(val, tuple):
            return Vector2(self.x - val[0], self.y - val[1])
        elif isinstance(val, Vector2):
            return Vector2(self.x - val.x, self.y - val.y)
    
    def __mul__(self, val: VectorLike) -> Vector2:
        if isinstance(val, (int, float)):
            return Vector2(self.x * val, self.y * val)
        elif isinstance(val, tuple):
            return Vector2(self.x * val[0], self.y * val[1])
        elif isinstance(val, Vector2):
            return Vector2(self.x * val.x, self.y * val.y)

    def __truediv__(self, val: VectorLike) -> Vector2:
        if isinstance(val, (int, float)):
            return Vector2(self.x / val, self.y / val)
        elif isinstance(val, tuple):
            return Vector2(self.x / val[0], self.y / val[1])
        elif isinstance(val, Vector2):
            return Vector2(self.x / val.x, self.y / val.y)
    
    def __floordiv__(self, val: VectorLike) -> Vector2:
        if isinstance(val, (int, float)):
            return Vector2(self.x // val, self.y // val)
        elif isinstance(val, tuple):
            return Vector2(self.x // val[0], self.y // val[1])
        elif isinstance(val, Vector2):
            return Vector2(self.x // val.x, self.y // val.y)
    
    def __repr__(self) -> str:
        return f'Vector2<x={self.x},y={self.y}>'
    
    def as_tuple(self) -> tuple:
        return (self.x, self.y)