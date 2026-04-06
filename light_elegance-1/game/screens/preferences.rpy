
## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"
        align(0.5, 0.5)

        vbox:
            xalign 0.5 xfill True spacing -30

            ###TEXT SPEED BUTTON
            button:
                style_prefix "options"
                hbox:
                    xfill True yfill True
                    label "Text Speed"
                    bar value Preference("text speed"):
                        yalign 0.5 xsize 554 xalign 1.0 xoffset -30

            ###DISPLAY button
            button:
                style_prefix "options"
                hbox:
                    xfill True yfill True
                    label "Display"
                    frame:
                        style "switch"

                        hbox:
                            style "switch_box"
                            text "➤" font "DejaVuSans.ttf" at flip:
                                if preferences.fullscreen == True:
                                    color u"#999" #### just a visual indicator to show there are options to choose
                            if preferences.fullscreen == True:
                                text "Fullscreen" at button_fade
                            else:
                                text "Windowed" at button_fade
                                    
                            text "➤" font "DejaVuSans.ttf":
                                if preferences.fullscreen == False:
                                    color u"#999"

                ####the actual preference button
                action Preference("display", "toggle")


            ###AUDIO SLIDERES
            button:
                style_prefix "options"
                hbox:
                    xfill True yfill True
                    label "Music"
                    bar value Preference("music volume"):
                        yalign 0.5 xsize 554 xalign 1.0 xoffset -30

            button:
                style_prefix "options"
                hbox:
                    xfill True yfill True
                    label "Sound"
                    bar value Preference("sound volume"):
                        yalign 0.5 xsize 554 xalign 1.0 xoffset -30



            
            ####SKIP STUFF

            ###Skip transitions
            button:
                style_prefix "options"
                hbox:
                    xfill True yfill True
                    label "Transitions"
                    frame:
                        style "switch"

                        hbox:
                            style "switch_box"
                            text "➤" font "DejaVuSans.ttf" at flip:
                                if preferences.transitions == 2:
                                    color u"#999" #### just a visual indicator to show there are options to choose
                            if preferences.transitions == 2:
                                text "On" at button_fade
                            else:
                                text "Off" at button_fade
                                    
                            text "➤" font "DejaVuSans.ttf":
                                if preferences.transitions == 0:
                                    color u"#999"

                ####the actual preference button
                action Preference("transitions", "toggle")

            ###Skip unseen text
            button:
                style_prefix "options"
                hbox:
                    xfill True yfill True
                    label "Skip Unseen Text"
                    frame:
                        style "switch"

                        hbox:
                            style "switch_box"
                            text "➤" font "DejaVuSans.ttf" at flip:
                                if preferences.skip_unseen  == True:
                                    color u"#999" #### just a visual indicator to show there are options to choose
                            if preferences.skip_unseen  == True:
                                text "On" at button_fade
                            else:
                                text "Off" at button_fade
                                    
                            text "➤" font "DejaVuSans.ttf":
                                if preferences.skip_unseen  == False:
                                    color u"#999"

                ####the actual preference button
                action Preference("skip", "toggle")

            ###Skip after choices
            button:
                style_prefix "options"
                hbox:
                    xfill True yfill True
                    label "Skip After Choices"
                    frame:
                        style "switch"

                        hbox:
                            style "switch_box"
                            text "➤" font "DejaVuSans.ttf" at flip:
                                if preferences.skip_after_choices  == True:
                                    color u"#999" #### just a visual indicator to show there are options to choose
                            if preferences.skip_after_choices  == True:
                                text "On" at button_fade
                            else:
                                text "Off" at button_fade
                                    
                            text "➤" font "DejaVuSans.ttf":
                                if preferences.skip_after_choices  == False:
                                    color u"#999"

                ####the actual preference button
                action Preference("after choices", "toggle") 


            ###AUTO FORWARD SPEED
            button:
                style_prefix "options"
                hbox:
                    xfill True yfill True
                    label "Auto-Forward Speed"
                    bar value Preference("auto-forward time"):
                        yalign 0.5 xsize 554 xalign 1.0 xoffset -30


style switch_box:
    xalign 0.5 spacing 40 yoffset 2
style switch:
    background Frame("gui/options/switch_bg.png", 50, 0, 50, 0) xysize(532,70)
    xalign 1.0 yalign 0.5 yoffset 2
style game_menu_viewport:
    xysize(1345, 608)
    yoffset 40
style game_menu_vscrollbar:
    yoffset 40

style options_button:
    background "gui/options/frame.png"
    xysize(1228,182)
    right_padding 57 left_padding 130
    xalign 0.5

style options_label:
    yalign 0.5
style options_label_text:
    color dark_accent
    size 44
style options_text:
    yalign 0.5 xalign 0.5
    size 44

#style opslider:
#    xsize 554