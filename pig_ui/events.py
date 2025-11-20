from pig_ui.constants import *
class Events:
    """
    A Custom Pygame Event Wrapper
    ***
    The Events you can use:
    |name|type|description|
    |---|---|---|
    |WHEEL|int|Can be -1, 0 & 1|
    |MOUSE_LEFT|bool|-|
    |MOUSE_RIGHT|bool|-|
    |MOUSE_MIDDLE|bool|-|
    |MOUSE_4|bool|-|
    |MOUSE_5|bool|-|
    |QUIT|bool|alias: pygame.QUIT|
    |MOUSE_POS|tuple[int, int]|(x, y)|
    |KEYS|list[int]|[pygame.K_a...]|
    |KEYDOWN|bool|unused|
    |DOUBLE_CLICK|bool|-|
    |TEXTINPUT|str|-|
    """
    def __init__(self):
        self.WHEEL = False
        self.MOUSE_LEFT = False
        self.MOUSE_MIDDLE = False
        self.MOUSE_RIGHT = False
        self.MOUSE_4 = False
        self.MOUSE_5 = False
        self.QUIT = False
        self.MOUSE_POS = PG.mouse.get_pos()
        self.KEYDOWN = False
        self.KEYS = set()
        self.DOUBLE_CLICK = False
        self.TEXTINPUT = ''
        self.last_click = 0
        self.keys_to_control = [
            PG.K_a, # Add a new Node
            PG.K_s, # Saves the configuration
            PG.K_l, # Loads the configuration
        ]
        
    def __set_mouse_btn(self, event_btn: int, i: bool):
        """
        Sets the event->mouse-button
        """
        match event_btn:
            case 1: self.MOUSE_LEFT = i
            case 2: self.MOUSE_MIDDLE = i
            case 3: self.MOUSE_RIGHT = i
            case 4: self.MOUSE_4 = i
            case 5: self.MOUSE_5 = i
            
    def recv_events(self) -> None:
        """
        Process all events.
        More info in the Events.docstring
        """
        self.WHEEL = 0 # Resets the Wheel, because pygame will not do this
        self.DOUBLE_CLICK = False
        self.MOUSE_POS = PG.mouse.get_pos()
        self.TEXTINPUT = ''
        for event in PG.event.get():
            match event.type:
                case PG.MOUSEBUTTONDOWN | PG.MOUSEBUTTONUP:
                    i = event.type == PG.MOUSEBUTTONDOWN
                    self.__set_mouse_btn(event.button,i)
                    if time() - self.last_click <= 0.5 and i: # using the windows-default double-click speed
                        self.DOUBLE_CLICK = True
                        self.last_click = 0
                    if event.button == 1 and i:
                        self.last_click = time()
                case PG.MOUSEWHEEL:
                    self.WHEEL = event.y
                case PG.KEYDOWN:
                    self.KEYS.add(event.key)
                case PG.KEYUP:
                    self.KEYS.remove(event.key)
                case PG.TEXTINPUT:
                    self.TEXTINPUT = event.text
                case PG.QUIT:
                    self.QUIT = True
       