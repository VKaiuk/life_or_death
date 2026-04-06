
## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        at menu_appear
        for i in items:
            textbutton i.caption action i.action



transform menu_appear():
    subpixel True
    alpha 0.0

    on show:
        linear .3 alpha 1
style choice_vbox:
    xalign 0.5
    ypos 430
    yanchor 0.5
    spacing 15

style choice_button:
    is default # This means it doesn't use the usual button styling
    xysize (1280, None)
    idle_background Frame("gui/button/menu_idle.png",
        150, 50, 150, 50, tile=False)
    hover_background Frame("gui/button/menu_hover.png",
        150, 50, 150, 50, tile=False)

    idle_foreground Transform("gui/button/dot_idle.png",yalign=0.5, xalign=0.5, yoffset=-7)
    hover_foreground Transform("gui/button/dot_hover.png",yalign=0.5, xalign=0.5, yoffset=-7)
    padding (100, 30)

style choice_button_text:
    is default # This means it doesn't use the usual button text styling
    xalign 0.5 yalign 0.5 yoffset -7 size 35
    idle_color mid_accent
    hover_color dark_accent
    insensitive_color "#444"
    textalign 0.5
    line_spacing -10