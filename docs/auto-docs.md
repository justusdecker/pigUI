# Automatic-Documentator by Justus Decker

# ./pig_ui/app.py

# ./pig_ui/constants.py

# ./pig_ui/events.py

# ./pig_ui/modules.py

# ./pig_ui/pygame_reps.py

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

## set_subs
Format:
    {
        'title': "title",
        'ltext': [],
        'lcom': []
    }

# ./pig_ui/ui/ui_sidebar.py

# ./pig_ui/ui/ui_spinbox.py

# ./pig_ui/ui/ui_textinput.py

## SpecialKeyStates
These States determine in Special how to manage the key

## UITextInput
A Default TextInput

## type_check
        

# ./pig_ui/ui/ux_element.py

## UXParameterError


## set_mode
(0) normal
(1) hover
(2) click
(3) disabled

