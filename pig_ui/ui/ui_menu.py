from pig_ui.ui.ui_element import UIElement
from pig_ui.ui.ui_dropdown import UIDropDown
from pig_ui.constants import *
from pig_ui.ui.ux_element import UXWrapper, UXText, UXRect
from pig_ui.ui.ui_manager import UIM
class UIMenuBar(UIElement):
    """
    A graphical element at the top-left of the screen that provides a collection of commands and options for the application.
    
    Basically a set of DropDown-Elements
    
    > [!ATTENTION]
    > You should not use multiple of this!
    """
    def __init__(self, app, pos, size, ux = None, draggable = False, **kwargs):
        kwargs['visible'] = False
        kwargs['anchor'] = 'tl'
        super().__init__(app, pos, size, ux, draggable, **kwargs)
        self.sub = []
    def set_subs(self, subs: list[dict]):
        """
        Sets the sub-elements of the UIMenu
        subs:
        * **title**: the title of the element(Is the title of a DropDown).
        * **ltext**: a list of titles for the sub-elements of the DropDown.
        * **lcom**: a list of callbacks for the sub-elements.(None will set each to lambda)
        
        Format:
        ```json
        {
            'title': "title",
            'ltext': [],
            'lcom': []
        }
        ```
        """
        
        for i, dd in enumerate(subs):
            uidd = UIDropDown(
                self.app, 
                Vector2(i*self.size.x, 0),
                self.size,
                parent=self,
                anchor= 'tl',
                title = dd['title'],
                draggable=False,
                )
            
            uidd.set_subs(dd['ltext'], dd['lcom'])
            self.sub.append(uidd)