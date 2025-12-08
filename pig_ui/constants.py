from pig_ui.modules import *
class Anchors:
    TOP_LEFT = 'tl'
    TOP_CENTER = 'tc'
    TOP_RIGHT = 'tr'
    
    CCENTER = 'cc'
    CENTER_LEFT = 'cl'
    CENTER_RIGHT = 'cr'
    
    BOTTOM_LEFT = 'bl'
    BOTTOM_RIGHT = 'br'
    BOTTOM_CENTER = 'bc'
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

FONT_NAME = 'Consolas'
FONT_SIZE_BASE = 13
FONT_MIN_SIZE_DRAW = 10
SAVE_FILE = "nodes_save.json"
CULL_PADDING = 50 
DATA_TYPES = {
    "str":      Color('#FFA500'),    
    "int":      Color('#0096C8'),    
    "float":    Color('#00C8C8'),    
    "bool":     Color('#ff0000'),      
    "list":     Color('#9600C8'),    
    "any":      Color('#646464'),  
}
DEFAULT_SOCKET_COLOR = Color('#C86400')
try:
    from pygame.font import SysFont, init
    init()
    NORM_FONT = SysFont('Consolas',FONT_SIZE_BASE)
except:
    NORM_FONT = None
