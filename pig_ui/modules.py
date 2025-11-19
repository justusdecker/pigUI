import json, os
import random
from typing import Callable
from time import time

try:
    import pygame as pg
    from pygame import Rect, Vector2, Surface, Color
    from pygame.surfarray import make_surface
    PG = pg
except:
    def Color(*C): ...
    def Rect(*RV): ...
    def Vector2(*V): ...
    def Surface(*P): ...
    PG = None
