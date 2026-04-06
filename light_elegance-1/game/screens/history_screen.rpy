
## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

define config.history_length = 250

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False


    use game_menu(_("History"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical" yinitial 1.0
        align(0.5, 0.5)

        has vbox

        style_prefix "history"

        for h in _history_list:

            frame:
                has vbox
                if h.who:
                    hbox:
                        label h.who style 'history_name':
                            substitute False
                        frame style "histdiv"
                else:
                    frame style "histdiv"
                    null height 10


                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }

style histdiv:
    background Solid("#ededed7e") xysize(None, 2) yalign 0.5 yoffset 5


style history_frame:
    xsize 1200
    ysize None
    background None
    xoffset 50

style history_hbox:
    spacing 20

style history_vbox:
    spacing 20

style history_name:
    xalign 0.0

style history_name_text:
    textalign 0.0
    align (1.0, 0.0)
    color light_accent
    outlines [ (1, "#2b262609", 0, 0),  (2, "#00000007", 0, 0), (3, "#00000010", 0, 0), (4, "#00000007", 0, 0), (2, mid_accent, 0, 0) ]
    font gui.name_text_font
    size 80

style history_text:
    textalign 0.0
    justify True
    xpos 100 xsize 1100
    outlines [ (1, "#2b262609", 0, 0),  (2, "#00000007", 0, 0), (3, "#00000010", 0, 0), (4, "#00000007", 0, 0) ]

style history_label:
    xfill True

style history_label_text:
    xalign 0.0
