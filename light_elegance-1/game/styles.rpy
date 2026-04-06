################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    gui.init(1920, 1080)

define config.check_conflicting_properties = True

################################################################################
## GUI Configuration Variables
################################################################################
## Some choice gui values have been left in, to make them
## easier to adjust for accessibility purposes e.g. to allow
## players to change the default text font or size by rebuilding the gui.
## You may add more back if you need to adjust them, or find-and-replace
## any instances where they are used directly with their value.

# The text font for dialogue and choice menus
define gui.text_font = "fonts/Nunito-VariableFont_wght.ttf"
# The text font for buttons
define gui.interface_text_font = gui.preference("interface_font", "fonts/Jost-Light.ttf")
# The default size of in-game text
define gui.text_size = gui.preference("size", 35)
# The font for character names
define gui.name_text_font = gui.preference("interface_font", "fonts/Jost-Light.ttf")
# The size for character names
define gui.name_text_size = gui.preference("name_size", 40)


###Colors

define light_accent = u"#EDEDED"
define dark_accent = u"#323F5F"
define mid_accent = u"#836F4A"

## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at
## https://www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Style Initialization
################################################################################

init offset = -1

################################################################################
## Styles
################################################################################

style default:
    font gui.text_font
    size gui.text_size
    language gui.language

style input:
    adjust_spacing False

style hyperlink_text:
    hover_underline True
    color mid_accent

style gui_text:
    color '#ffffff'
    size gui.text_size
    font gui.interface_text_font

style button:
    xysize (None, None)
    background Frame("gui/button_bg.png", 45, 49, 45, 49, tile=False)
    padding (48, 27, 48, 30)

style button_text:
    is gui_text
    yalign 0.5
    xalign 0.0
    

    idle_color light_accent 
    hover_color dark_accent
    selected_color light_accent
    insensitive_color u"#9999"

style label_text:
    is gui_text
    size 36
    color light_accent


style bar:
    ysize 33
    base_bar Frame("gui/options/slider.png", 20, 6, 20, 6, tile=False)
    thumb "gui/options/slider_thumb.png"

style vbar:
    xsize 33
    base_bar Frame("gui/options/vslider.png", 20, 6, 20, 6, tile=False)
    thumb "gui/options/slider_thumb.png"

style scrollbar:
    ysize 37
    base_bar None
    thumb Frame("gui/hscrollbar.png", 0, 30, 0, 30, tile=False)
    unscrollable 'hide'

style vscrollbar:
    xsize 37
    base_bar None
    thumb Frame("gui/scrollbar.png", 0, 30, 0, 30, tile=False)
    unscrollable 'hide'

style slider:
    ysize 33
    base_bar Frame("gui/options/slider.png", 20, 6, 20, 6, tile=False)
    thumb "gui/options/slider_thumb.png"

style vslider:
    xsize 33
    base_bar Frame("gui/options/vslider.png", 20, 6, 20, 6, tile=False)
    thumb "gui/options/slider_thumb.png"


style frame:
    padding (6, 6, 6, 6)
    background Frame("gui/frame.png", 6, 6, 6, 6, tile=False)
