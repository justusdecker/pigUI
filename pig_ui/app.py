from pig_ui.constants import *
from pig_ui.events import Events
from pig_ui.ui.ui_element import UIM

class App:
    """
    The Main Application that calls all necessary functions used for:
    - BackgroundCleaning
    - EventTracing
    - UIInteraction
    - Drawing
    - DisplayUpdates
    
    Contains the basic pygame loop combined with pigUI
    """
    def __init__(self, title: str = 'pigUI'):
        self.is_running = True
        self.window = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        PG.display.set_caption(title)
        self.clock = PG.time.Clock()
        self.events = Events()

    def run(self):
        """
        Runs:
        - BackgroundCleaning
        - EventTracing
        - UIInteraction
        - Drawing
        - DisplayUpdates
        """
        while self.is_running:
            self.window.fill((25,25,25))
            self.update()
            UIM.update()
            self.draw()
            self.event_handler()
            
        self.destroy()
    
    def update(self):
        """
        Ticks the pygame Clock
        """
        self.clock.tick(60)
        
    def draw(self):
        """
        updates the display & draw debug elements
        
        For the debugging state(will be added later):
            Draws Circles for LeftClick & DoubleClicks.
        """
        if self.events.MOUSE_LEFT:
            PG.draw.circle(self.window,(128,128,0),self.events.MOUSE_POS,8,3)
        if self.events.DOUBLE_CLICK:
            PG.draw.circle(self.window,(0,128,128),self.events.MOUSE_POS,16,3)
        PG.display.update()
        
    def event_handler(self):
        """
        Checks all events and set the `self.is_running` to false
        """
        self.events.recv_events()
        if self.events.QUIT:
            self.is_running = False
            
    def destroy(self):
        """
        
        """
        self.is_running = False