from pig_ui.constants import *

class UX4Param:
    """
    A Parameter Object used to determine rect-boundings
    
    *options -> must be 4 Parameters
    """
    def __init__(self,*options):
        self.options = options

class UXElement:
    """
    A UXElement is used to style the UI
    """
    def draw(self):
        """
        Draws the object based on the options
        """

class UXRect(UXElement):
    """
    A Rectangle Object, will be rendered by calling draw.
    
    Uses the same options as pygame.draw.rect
    """
    def __init__(self,
                 border_radius: int | UX4Param = -1,
                 color: Color = Color('#252525'),
                 offset: Vector2 = Vector2(0,0),
                 size: Vector2 = Vector2(1,1),
                 width: int = 0):
        self.border_radius = border_radius
        if isinstance(self.border_radius, int):
            self.border_radius = UX4Param(*[self.border_radius]*4)
        self.color = color
        self.pos = offset
        self.size = size
        self.width = width
        
    def draw(self, surf: Surface, offset: Vector2):
        """
        Draws a rectangle based on the options
        """
        PG.draw.rect(surf, 
                     self.color, 
                     (offset.x + self.pos.x,offset.y + self.pos.y, self.size.x,self.size.y),
                     self.width,
                     border_radius=-1,
                     #*self.border_radius.options
                     )

class UXCircle(UXElement): 
    """
    A Circle Object, will be rendered by calling draw.
    
    Uses the same options as pygame.draw.circle
    """
    def __init__(self,
                 color: Color,
                 center: Vector2,
                 radius: float,
                 width: int,
                 drawing_points: UX4Param):
        self.color = color
        self.center = center
        self.radius = radius
        self.width = width
        self.drawing_points = drawing_points
        
    def draw(self, surf):
        """
        Draws a circle based on the options
        """
        PG.draw.circle(
            surf,
            self.color,
            self.center,
            self.radius,
            self.width,
            *self.drawing_points.options
        )

class UXLine(UXElement):
    """
    A Line Object, will be rendered by calling draw.
    
    Uses the same options as pygame.draw.line
    """
    def __init__(self,
                 color: Color,
                 start: Vector2,
                 end: Vector2,
                 width: int):
        self.color = color
        self.start = start
        self.end = end
        self.width = width
        
    def draw(self, surf):
        """
        Draws a line based on the options
        """
        PG.draw.line(
            surf,
            self.color,
            self.start,
            self.end,
            self.width
        )

class UXPolygon(UXElement):
    """
    A Polygon Object, will be rendered by calling draw.
    
    Uses the same options as pygame.draw.polygon
    """
    def __init__(self,
                 color: Color,
                 points: list[Vector2],
                 width: int):
        self.color = color
        self.points = points
        self.width = width
    def draw(self, surf):
        """
        Draws a polygon based on the options
        """
        PG.draw.polygon(
            surf,
            self.color,
            self.points,
            self.width
        )

class UXImage(UXElement):
    """
    A Image Object, this is different to the other UX.
    
    * **path**: Can be a string or Surface.(If string loads the image from the path else takes the image)
    """
    def __init__(self,
                 pos: Vector2,
                 path: str | Surface,
                 alpha: bool):
        self.pos = pos
        if isinstance(path, str):
            self.image = PG.image.load(path)
        elif isinstance(path, Surface):
            self.image = path
            
        self.alpha = alpha
        
    def update(self, surf: Surface):
        """
        Updates the image, should be the same resolution as before!
        """
        self.image = surf
        
    def draw(self, surf, offset):
        """
        Draws the object based on the options
        """
        surf.blit(self.image, self.pos+offset)

class UXText(UXElement):
    """
    A Text Object.
    Uses pygame.font to draw text
    
    * **anchor**: Should be (0=left,1=center,2=right)
    * **color**: Must be a color-like & pygame-compatible
    * **text_get_callback**: Can be str or a function(Used to change text on the fly, if necessary)
    
    Missing / Future:
    Add a snap point for x & y, so the text will not go outside the element!
    """
    def __init__(self, pos: Vector2 = Vector2(0,0), color: Color = Color('#dddddd'), anchor = 0,text_get_callback: Callable | str = lambda: ""):
        self.anchor = anchor
        self.pos = pos
        self.text_get_callback = text_get_callback
        self.color = color
        super().__init__()
        
    @property
    def anchor_offset(self) -> Vector2:
        """
        Returns the anchor offset based on `self.anchor`
        Can be:
        * 0: left
        * 0.5: center
        * 1: right
        """
        return [0,0.5,1][self.anchor]
    
    def draw(self, surf: Surface, offset: Vector2):
        """
        Renders the text(extremly inefficient) & draws it based on the options to the screen.
        """
        text = self.text_get_callback() if not isinstance(self.text_get_callback, str) else self.text_get_callback
        rendered = NORM_FONT.render(text, True, self.color)
        size = Vector2(*rendered.get_size())
        surf.blit(rendered, self.pos + offset - (size * self.anchor_offset))
        
        

UIELEMENT_DEFAULT = [
    [UXRect(-1,Color('#484848'),size=Vector2(15,15))],
    [UXRect(-1,Color('#969696'),size=Vector2(15,15))],
    [UXRect(-1,Color('#ffffff'),size=Vector2(15,15))],
    [UXRect(-1,Color('#000000'),size=Vector2(15,15))]
]


UIELEMENT_TEXT = [
    [UXText(color=Color('#484848'))],
    [UXText(color=Color('#969696'))],
    [UXText(color=Color('#ffffff'))],
    [UXText(color=Color('#000000'))]
]
            
class UXWrapper:
    """
    Wraps up the UX for UI Usage.
    """
    def __init__(self, ux: list[list[UXElement]]):
        
        self.ux = ux
        self.set_mode(0)
    
    def draw(self,surf: Surface, offset: Vector2):
        """
        Draws the UX for the selected mode
        """
        for ux in self.ux[self.selected]:
            ux.draw(surf, offset)
        
    def set_mode(self,type: int):
        """
        sets the mode, usually called by the UIElement.
        *0: normal
        *1: hover
        *2: click
        *3: disabled(unused currently)
        """
        self.selected = type
        
        
