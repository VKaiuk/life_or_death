## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the title and navigation.
##
## This screen no longer includes a background, and it no longer transcludes
## its contents. It is intended to be easily removable from any given menu
## screen and thus you are required to do some of the heavy lifting for
## setting up containers for the contents of your menu screens.
##

screen game_menu(title):

    if main_menu:
        add "main_menu_image"

    style_prefix "game_menu"

    add "gui/game_menu/game_menu.png" align(0.5, 0.5) yoffset 50

    frame:
        background Frame("gui/game_menu/nav_bg.png", 80, 0, 80, 0) ysize 79 left_padding 60 right_padding 100
        pos(118, 75)

        hbox:
            
            if not main_menu:
                textbutton "Save" action ShowMenu("save")
            else:
                textbutton "Load" action ShowMenu("load")
            frame style "framediv" ### a vertical line to act as divider
            textbutton "Options" action ShowMenu("preferences")
            frame style "framediv"
            textbutton "History" action ShowMenu("history")
            frame style "framediv"
            # textbutton "Gallery" action ShowMenu("gallery")
            # frame style "framediv"
            textbutton "About" action ShowMenu("about")
            frame style "framediv"
            textbutton "Help" action ShowMenu("help")
            frame style "framediv"
            textbutton "Quit" action Quit()

            ###you may add additional menus here


    
    ###return button

    textbutton "Return" action Return():
        ysize 99 
        text_yoffset -2 text_idle_color light_accent text_hover_color dark_accent
        background Frame("gui/namebox.png", 40, 0, 40, 0, tile=False, xalign=0.5)
        padding (100, 5, 100, 5)

        xalign 0.5 ypos 987

style game_menu_hbox:
    yalign 0.5 spacing 15
style framediv:
    xysize(2, 47)
    background Solid("#ededed33")
    yalign 0.5
style game_menu_button:
    background None
    hover_background Frame("gui/game_menu/nav_select.png", 20, 20, 20, 20) 
    selected_background Frame("gui/game_menu/nav_select.png", 20, 20, 20, 20) 
    padding(10,0)
    yalign 0.5
style game_menu_button_text:
    size 44
    color light_accent

