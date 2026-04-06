
## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
EasyRenPyGui is made by {a=https://github.com/shawna-p}Feniks{/a} {a=https://feniksdev.com/}@feniksdev.com{/a}
""")


screen about():

    tag menu


    use game_menu(_("About"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"
        align(0.5, 0.5)

        has vbox
        style_prefix "about"

        label "[config.name!t]"
        text _("Version [config.version!t]\n") xalign 0.5

        if gui.about:
            text "[gui.about!t]\n"

        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label_text:
    size 90
    font gui.name_text_font
    outlines [ (1, "#2b262609", 0, 0),  (2, "#00000007", 0, 0), (3, "#00000010", 0, 0), (4, "#00000007", 0, 0), (2, mid_accent, 0, 0) ]
style about_label:
    xalign 0.5
style about_vbox:
    xfill True
style about_text:
    outlines [ (1, "#2b262609", 0, 0),  (2, "#00000007", 0, 0), (3, "#00000010", 0, 0), (4, "#00000007", 0, 0) ]


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"))

    frame:
        style_prefix "page"
        xalign 0.5 left_padding 100 right_padding 100 yoffset 50
        hbox:
            yoffset -1
            textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
            frame style "framediv" ysize 30 ###simple little divider. Style defined in game_menu.rpy
            textbutton _("Mouse") action SetScreenVariable("device", "mouse")
            frame style "framediv" ysize 30
            if GamepadExists():
                textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

    viewport:
        #style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"
        align(0.5, 0.5) yoffset 100 xysize(1345, 508)

        has vbox
        style_prefix "help"
        spacing 23

       

        if device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help
        elif device == "gamepad":
            use gamepad_help


screen keyboard_help():

    vbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    vbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    vbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    vbox:
        label _("Escape")
        text _("Accesses the game menu.")

    vbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    vbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    vbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    vbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    vbox:
        label "H"
        text _("Hides the user interface.")

    vbox:
        label "S"
        text _("Takes a screenshot.")

    vbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    vbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    vbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    vbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    vbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    vbox:
        label _("Mouse Wheel Up / Click Rollback Side")
        text _("Rolls back to earlier dialogue.")

    vbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    vbox:
        label _("Right Trigger / A/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    vbox:
        label _("Left Trigger / Left Shoulder")
        text _("Rolls back to earlier dialogue.")

    vbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    vbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    vbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    vbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate() xalign 0.5 padding(100, 35)  xoffset 10



style help_label:
    xalign 0.5

style help_label_text:
    xalign 0.5
    textalign 0.5
    font gui.name_text_font
    size 47
    outlines [ (1, "#2b262609", 0, 0),  (2, "#00000007", 0, 0), (3, "#00000010", 0, 0), (4, "#00000007", 0, 0), (2, mid_accent, 0, 0) ]

style help_text:
    xalign 0.5
    textalign 0.5
    outlines [ (1, "#2b262609", 0, 0),  (2, "#00000007", 0, 0), (3, "#00000010", 0, 0), (4, "#00000007", 0, 0) ]

style help_vbox:
    xfill True
    xalign 0.5


