
## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"


    vbox:
        align(0.5, 0.5) spacing 10

        frame:
            background Frame("gui/input_prompt.png", 50, 0, 50, 0) xysize(None, 128) xalign 0.5 padding(70, 0)
            text prompt style "input_prompt" color mid_accent align(0.5, 0.5)

        frame:
            background "gui/input_bg.png" xysize(1234,222) xalign 0.5
            input id "input" size 40: #### if you're planning to have only shorter input answers (names, words etc.) you can inscrease the text size. 48 works fine
                yalign 0.5
                outlines [ (1, "#2b262609", 0, 0),  (2, "#00000007", 0, 0), (3, "#00000010", 0, 0), (4, "#00000007", 0, 0) ]

style input_prompt:
    xalign 0.0
    size 42

style input:
    xalign 0.5
    xmaximum 1116



