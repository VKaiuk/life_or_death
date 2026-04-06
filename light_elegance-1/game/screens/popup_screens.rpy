
## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action=None):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "#0008" # You can replace this with your own overlay image

    frame:
        has vbox

        label "Attention" text_font gui.name_text_font text_size 70 xalign 0.5

        label _(message) style "confirm_prompt"

        hbox:

            textbutton _("Confirm") action yes_action
            # Modified so you can just have a confirmation prompt
            if no_action is not None:
                textbutton _("Cancel") action no_action

    ## Right-click and escape answer "no".
    if no_action is not None:
        key "game_menu" action no_action
    else:
        key "game_menu" action yes_action

style confirm_frame:
    background Frame("gui/frame.png", 118, 180, 114, 138)
    padding (70, 85, 70, 110)
    xalign 0.5
    yalign 0.5
    xsize 900

style confirm_vbox:
    align (0.5, 0.5)
    spacing 45

style confirm_prompt:
    xalign 0.5

style confirm_prompt_text:
    textalign 0.5
    align (0.5, 0.5)
    layout "subtitle"
    color mid_accent
    size 41
    line_spacing -10

style confirm_hbox:
    xalign 0.5
    spacing 150

style confirm_button:
    xalign 0.5
    background "gui/confirm_bg.png"
    xysize(249, 74)

style confirm_button_text:
    textalign 0.5
    align(0.5, 0.5)
    idle_color light_accent
    hover_color mid_accent
    size 35


####Sync frame styles

style sync_frame:
    background Frame("gui/sync_bg.png", 118, 180, 114, 138)
    padding (70, 0, 70, 200)

    #ysize 450
    xalign 0.5
    yalign 0.5
    xsize 900

style sync_vbox:
    align (0.5, 0.5)
    spacing 45

style sync_label_text:
    xalign 0.5
    size 70

style sync_input:
    color mid_accent
    size 35

style sync_text:
    textalign 0.5
    align (0.5, 0.5)
    layout "subtitle"
    color mid_accent
    size 41
    line_spacing -10

style sync_hbox:
    xalign 0.5
    spacing 150

style sync_button:
    xalign 0.5 yoffset -20
    background "gui/confirm_bg.png"
    xysize(249, 74)

style sync_button_text:
    textalign 0.5
    align(0.5, 0.5)
    idle_color light_accent
    hover_color mid_accent
    size 35


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:
        has hbox

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_hbox:
    spacing 9

style skip_frame:
    is empty
    ypos 15
    xpos -20
    background Frame("gui/skip.png", 24, 40, 100, 40, tile=False)
    padding (50, 25, 75, 25)

style skip_text:
    size 30
    color mid_accent

style skip_triangle:
    is skip_text
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"
    yoffset 5

## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame:
    is empty
    ypos 100
    xoffset -20

    background Frame("gui/notify.png", 20, 43, 45, 40)
    padding (50, 25, 60, 25)

style notify_text:
    size 35



