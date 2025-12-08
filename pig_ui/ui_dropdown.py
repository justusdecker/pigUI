from pig_ui.constants import *
from pig_ui.ux_element import UXWrapper, UXText, UXRect
from pig_ui.ui_element import UIElement
from pig_ui.ui_manager import UIM
class UIDropDown(UIElement):
    """
    A DropDown Menu.
    
    - * **title**: changes the title of the main element
    """
    def __init__(self, app, pos, size, **kwargs):
        kwargs['cb_lclick'] = self.toggle_dd
        kwargs['anchor'] = "tl"
        ux=UXWrapper(
            ux = [
                [UXRect(-1,Color(col),size=size),
                 UXText(text_get_callback=kwargs.get('title', ''))] for col in ('#484848', '#969696', '#ffffff', '#000000')
            ]
        )
        super().__init__(app, pos, size, ux, **kwargs)
        self.sub = []

    @property
    def text(self) -> str:
        """
        !Unused
        """
        return "test"
    
    def toggle_dd(self,*_):
        """
        Toggles the visibility of all SubElements
        """
        for uie in self.sub:
            uie.visible = not uie.visible
            
    def sub_callbacks(self,obj):
        """
        Runs the corresponding callback for the dropdown subelement.
        Determined by the object
        """
        i = self.sub.index(obj)
        self.sub_cbs[i](obj)
        for uie in self.sub:
            uie.visible = not uie.visible
            
    def set_subs(self, ltext: list[str], lcom: list[Callable] | None = None):
        """
        Set SubElements & Resets existing Subs if exist:
        Format:
        ltext:
        ```json
        [
            "abc",
            "def",
            ...
        ]
        lcom:
        None or
        [
            function,
            lambda x: print(x),
            ...
        ]
        ```
        """
        for uie in self.sub:
            uie: UIElement
            uie.destroy()
        
        self.texts = []
        if lcom is None:
            lcom = [lambda *x: None for i in ltext]
        self.sub_cbs = lcom
        for i, (t, c) in enumerate(zip(ltext, lcom)):
            self.texts.append(t)
            ux = [
                [UXRect(-1,Color(col),size=self.size),
                 UXText(text_get_callback=t)] for col in ('#484848', '#969696', '#ffffff', '#000000')
            ]
            
            uie = UIElement(
                self.app, 
                Vector2(0,(i+1) * self.size.y),
                self.size,
                draggable=False,
                ux=UXWrapper(ux), 
                parent=self,
                anchor="tl",
                cb_lclick=self.sub_callbacks,
                cb_dclick=lambda x: None,
                visible=False
                )
            self.sub.append(uie)