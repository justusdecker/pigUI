from pig_ui.constants import *
from pig_ui.ui.ux_element import UXWrapper, UXText, UXRect
from pig_ui.ui.ui_element import UIElement

class SpecialKeyStates:
    """
    These States determine in Special how to manage the key
    """
    IDLE = 0
    WAITING_FOR_DELAY = 1
    REPEATING = 2
    
class SpecialKey:
    """
    A Workaround for keypresses in pygame.
    
    Supports repeating keys
    """
    DELAY = 0
    REPEAT = 0
    def __init__(self, delay_ms: int, repeat_ms: int):
        self.REPEAT_MS = repeat_ms
        self.DELAY_MS = delay_ms
        self.last_press_time = 0.0
        self.last_repeat_time = 0.0
        self.state = SpecialKeyStates.IDLE
        self.pressed = False
        
    def reset(self):
        """
        Sets unpressed & State -> IDLE
        """
        self.state = SpecialKeyStates.IDLE
        self.pressed = False
        
    def update(self):
        """
        Updates the KeyState.
        Checks for repeating keys, single presses & idle
        """
        self.pressed = False
        if self.state == SpecialKeyStates.IDLE: 
            self.state = SpecialKeyStates.WAITING_FOR_DELAY
            self.pressed = True
            self.last_press_time = time()
            self.last_repeat_time = time()
            
        elif self.state == SpecialKeyStates.WAITING_FOR_DELAY: 
            time_since = (time() - self.last_press_time) * 1000
            if time_since >= self.DELAY_MS:
                self.state = SpecialKeyStates.REPEATING
                self.last_repeat_time = time()
                
        elif self.state == SpecialKeyStates.REPEATING: 
            time_since = (time() - self.last_repeat_time) * 1000
            if time_since >= self.REPEAT_MS:
                self.pressed = True
                self.last_repeat_time = time()

class UITextInput(UIElement):

    """
    A TextInput.
    
    The user can write something into it.
    
    * **type**: Should be (1=int,2=float,3=hex-color,other=no-check)
    * **multiline**: enables/disables multiple lines
    * **max_length**: sets the max length for the `self.text` var.
    
    Has some flaws:
    * out of bounds write
    """
    def __init__(self, app, pos, size, ux = None, draggable = False, multiline: bool = False, max_length: int = -1, type: int = 2, **kwargs):

        kwargs['cb_lclick'] = self.set_edit
        kwargs['cb_unclick'] = self.reset
        if ux is None:
            
            UIELEMENT_TEXT = [
            [UXRect(-1,Color('#242424'),size=size),
                UXText(color=Color('#969696'),text_get_callback=self.get_text)],
            [UXRect(-1,Color('#242424'),size=size),
                UXText(color=Color('#ffffff'),text_get_callback=self.get_text)],
            [UXRect(-1,Color('#242424'),size=size),
                UXText(color=Color('#ffffff'),text_get_callback=self.get_text)],
            [UXRect(-1,Color('#242424'),size=size),
                UXText(color=Color('#000000'),text_get_callback=self.get_text)]
        ]
            ux = UXWrapper(UIELEMENT_TEXT)
        super().__init__(app, pos, size, ux, draggable, **kwargs)
        
        self.text = 'abc'
        self.is_editing = False
        self.pressed_keys = set()
        self.multiline = multiline
        self.max_length = max_length
        self.type = type
        self.special_keys: dict[str, SpecialKey] = {}
        
        self.set_special_key_state(PG.K_RETURN)
        self.set_special_key_state(PG.K_BACKSPACE)
        
    def get_text(self) -> str:
        """
        Gets the text, normally called by the UXText Lambda.
        """
        return self.text
    
    def set_edit(self,*_):
        """
        Should only be called by Self.
        """
        self.is_editing = True
        
    @property
    def delete(self) -> bool:
        """
        Has the user pressed the BACKSPACE key?
        """
        return PG.K_BACKSPACE in self.event.KEYS
    
    @property
    def _return(self) -> bool:
        """
        Has the user pressed the RETURN key?
        """
        return PG.K_RETURN in self.event.KEYS
    
    @property
    def shift(self) -> bool:
        """
        Has the user pressed the shift key?
        #! Unused
        """
        return PG.K_LSHIFT in self.event.KEYS or PG.K_RSHIFT in self.event.KEYS
    
    def set_used_keys(self):
        """
        #! Unused
        """
        for key in self.event.KEYS:
            self.pressed_keys.add(key)
    
    def type_check(self, text: str) -> str:
        """
        Checks selected type:
        - 1: decimal
        - 2: float | int
        - 3: hex color
        - default: str
        
        Only adds text if type_check is okay
        """
        match self.type:
            case 1: 
                if text.isdecimal(): return text
                return ''
            case 2:
                try:
                    if self.text + text == '-':
                        return text
                    
                    float(self.text + text)
                    return text
                except:
                    return ''
            case 3:
                return text #! will be changed later
            case _: return text
    
    def set_special_key_state(self, key: int): 
        """
        key: int -> pygame.Key
        Creates a new instance of the SpecialKey Class and stores this in the `self.special_keys` dict.
        """
        if key not in self.special_keys:
            self.special_keys[key] = SpecialKey(500,50)
            
    def update_special_key_state(self, key: int):
        """
        key: int -> pygame.Key
        Updates(if key in ev.KEYS) / Resets(else) the an instance of the SpecialKey Class.
        """
        if key in self.event.KEYS:
            self.special_keys[key].update()
        else:
            self.special_keys[key].reset()

    def get_special_key_state(self, key: int):
        """
        key: int -> pygame.Key
        Returns the `pressed` attr of an instance of the SpecialKey Class.
        """
        return self.special_keys[key].pressed
    
    def reset(self,*_):
        """
        Disables editing, should only be called by Self
        """
        self.is_editing = False
        
    def keyboard_interaction(self):
        """
        Updates text, special_keys etc.
        Should only be called by Self
        """
        if not self.is_editing: return
        self.update_special_key_state(PG.K_RETURN)
        self.update_special_key_state(PG.K_BACKSPACE)
        
        if self.get_special_key_state(PG.K_BACKSPACE):
            self.text = self.text[:-1] if self.text else ''
            return
        
        text = self.event.TEXTINPUT
        if self.max_length != -1 and len(self.text) + len(text) > self.max_length: 
            return
        text = self.type_check(text)
        if text:
            self.text += text
        if self.multiline and self.get_special_key_state(PG.K_RETURN):
            self.text += '\n'
