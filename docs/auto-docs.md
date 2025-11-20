# Automatic-Documentator by Justus Decker

# ./pig_ui/app.py

## App
The Main Application that calls all necessary functions used for:
- BackgroundCleaning
- EventTracing
- UIInteraction
- Drawing
- DisplayUpdates

Contains the basic pygame loop combined with pigUI

## run
Runs:
- BackgroundCleaning
- EventTracing
- UIInteraction
- Drawing
- DisplayUpdates

## update
Ticks the pygame Clock

## draw
updates the display & draw debug elements

For the debugging state(will be added later):
    Draws Circles for LeftClick & DoubleClicks.

## event_handler
Checks all events and set the `self.is_running` to false

## destroy
        
        

# ./pig_ui/constants.py

# ./pig_ui/events.py

## Events
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

## __set_mouse_btn
Sets the event->mouse-button

## recv_events
Process all events.
More info in the Events.docstring

# ./pig_ui/modules.py

# ./pig_ui/__init__.py

# ./pig_ui/ui/bezier.py

## draw_beziere
Draws a smooth cubic Bezier curve onto the specified screen surface.

## compute_bezier_points
Computes a set of discrete points along a cubic Bezier curve.

# ./pig_ui/ui/constants.py

# ./pig_ui/ui/ui_colorpicker.py

## convert_hsv_to_rgb
Converts HSV to RGB

## color_rect_array
Gives a pixel_array of a color_palette based of the hue, used for the colorpicker

This is not optimized:
    - only drawing pixels needed, not all & convert

## color_rect
Gives a Surface of a color_palette based of the hue, used for the colorpicker

## color_line
Gives a pixel_array of a color_line for selecting the hue of the color_rect, used for the colorpicker

This is not optimized:
    - only drawing pixels needed, not all & convert

# ./pig_ui/ui/ui_dropdown.py

# ./pig_ui/ui/ui_element.py

## UIElement
The Base-Class for all UIElements
***
A UIElement supports by default the following events & its corresponding callbacks:
|key|callback name|
|---|---|
|cb_lclick|left click|
|cb_dclick|double click|
|cb_rclick|right click|
|cb_unclick|release|
|cb_hover|hover|
|cb_unhover|unhover|
|cb_drag|drag|
|cb_wheel|scroll|
|cb_keypress|keypress|

## Params
#### app
The UI Element needs this to:
- blit to the window
- retreive events

#### pos
This is the Offset to the parent. If no parent is given, use pos+(0,0) as start.

#### size
Used to determine the Default UXElement size & the bounding box

> [!NOTE]
> You should not change the size in the lifetime, only in the init state.
> You must change the UXElement sizes manually!

#### ux
Must be a UXWrapper Object.

`ux` is used for styling the UIElement, for more info: look into the UXElement Docs.

### kwargs

#### group
A Group is used to update / draw only a specific    

event

layer
o_layer
visible
anchor
parent
draggable
blocked
click_offset
uid
 
## Attributes

## rect
Returns the Rect from this UI Object.

## image
Returns the current Image for this UIElement.
Will be a blank 1 by 1 Surface if nothing set!

## anchor_offset
Calculates the offset for the anchor: Center, LEFT etc.

## parent_offset
Calculates the parent offset to the `regular` position of the `UIElement`

## abs_offset
The absolute offset: anchor + parents + pos

## root_parent
Gets the main / root parent of this object.
Can only be None if the first upper parent is None.

# ./pig_ui/ui/ui_manager.py

## add_to_queue
This adds a ``UIElement`` to the render queue.

## remove_from_queue
Removes the given ``UIElement`` from the QUEUE.

## stick_on_top
Takes the selected Object, if its exists in QUEUE and
remove it from its old layer and re:adds it on the end of the set 

## __get_ordered_by_layers
HUD LAYER = 1
BG LAYER = 2

## get_skip_unwanted_groups
Skip unwanted groups & not visible uie's

## get_dead_uie
We encountered a softlock after:
    Pressing a button that makes itself invisbile
This is a fix/workaround for this

# ./pig_ui/ui/ui_menu.py

## UIMenuBar
A graphical element at the top-left of the screen that provides a collection of commands and options for the application.

Basically a set of DropDown-Elements

> [!ATTENTION]
> You should not use multiple of this!

## set_subs
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

# ./pig_ui/ui/ui_sidebar.py

## UISideBar
The SideBar is used for e.g.:
* Settings
* Menus

Only LeftBound!

## roll_in
Closes the sidebar.

## roll_out
Opens the sidebar.

# ./pig_ui/ui/ui_spinbox.py

## UISpinBox
A SpinBox, simply a TextInput with two Buttons, one for incrementing the current number & the other for decrementing it. 

## get_n
Get the `self.inp.text` if int | float compatible
Otherwise returns 0

## inc_num
Calling this function will increment the number stored in `self.inp`

## dec_num
Calling this function will decrement the number stored in `self.inp`

# ./pig_ui/ui/ui_textinput.py

## SpecialKeyStates
These States determine in Special how to manage the key

## SpecialKey
A Workaround for keypresses in pygame.

Supports repeating keys

## UITextInput
A TextInput.

The user can write something into it.

* **type**: Should be (1=int,2=float,3=hex-color,other=no-check)
* **multiline**: enables/disables multiple lines
* **max_length**: sets the max length for the `self.text` var.

Has some flaws:
* out of bounds write

## reset
Sets unpressed & State -> IDLE

## update
Updates the KeyState.
Checks for repeating keys, single presses & idle

## get_text
Gets the text, normally called by the UXText Lambda.

## set_edit
Should only be called by Self.

## delete
Has the user pressed the BACKSPACE key?

## _return
Has the user pressed the RETURN key?

## shift
Has the user pressed the shift key?
#! Unused

## set_used_keys
#! Unused

## type_check
Checks selected type:
- 1: decimal
- 2: float | int
- 3: hex color
- default: str

Only adds text if type_check is okay

## set_special_key_state
key: int -> pygame.Key
Creates a new instance of the SpecialKey Class and stores this in the `self.special_keys` dict.

## update_special_key_state
key: int -> pygame.Key
Updates(if key in ev.KEYS) / Resets(else) the an instance of the SpecialKey Class.

## get_special_key_state
key: int -> pygame.Key
Returns the `pressed` attr of an instance of the SpecialKey Class.

## reset
Disables editing, should only be called by Self

## keyboard_interaction
Updates text, special_keys etc.
Should only be called by Self

# ./pig_ui/ui/ux_element.py

## UX4Param
A Parameter Object used to determine rect-boundings

*options -> must be 4 Parameters

## UXElement
A UXElement is used to style the UI

## UXRect
A Rectangle Object, will be rendered by calling draw.

Uses the same options as pygame.draw.rect

## UXCircle
A Circle Object, will be rendered by calling draw.

Uses the same options as pygame.draw.circle

## UXLine
A Line Object, will be rendered by calling draw.

Uses the same options as pygame.draw.line

## UXPolygon
A Polygon Object, will be rendered by calling draw.

Uses the same options as pygame.draw.polygon

## UXImage
A Image Object, this is different to the other UX.

* **path**: Can be a string or Surface.(If string loads the image from the path else takes the image)

## UXText
A Text Object.
Uses pygame.font to draw text

* **anchor**: Should be (0=left,1=center,2=right)
* **color**: Must be a color-like & pygame-compatible
* **text_get_callback**: Can be str or a function(Used to change text on the fly, if necessary)

Missing / Future:
Add a snap point for x & y, so the text will not go outside the element!

## UXWrapper
Wraps up the UX for UI Usage.

## draw
Draws the object based on the options

## draw
Draws a rectangle based on the options

## draw
Draws a circle based on the options

## draw
Draws a line based on the options

## draw
Draws a polygon based on the options

## update
Updates the image, should be the same resolution as before!

## draw
Draws the object based on the options

## anchor_offset
Returns the anchor offset based on `self.anchor`
Can be:
* 0: left
* 0.5: center
* 1: right

## draw
Renders the text(extremly inefficient) & draws it based on the options to the screen.

## draw
Draws the UX for the selected mode

## set_mode
sets the mode, usually called by the UIElement.
*0: normal
*1: hover
*2: click
*3: disabled(unused currently)

