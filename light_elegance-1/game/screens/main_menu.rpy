
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu


image main_menu_image = Solid("#9999") ###Define your main menu background here


define game_title = "Game Title" ### Edit the title of the game here
define title_size = 309 ### Adjust the text size here, if it's too big and the title overflows

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu
    style_prefix "main"

    add "main_menu_image"
    add "gui/main_menu/bg.png"

    ##Space included both before and after so the blur doesn't clip
    label " [game_title] " text_color u"#000" at blurry ###this is a blurred copy of the title to create a nice shadow effect
    label " [game_title] " text_color light_accent text_outlines [ (absolute(4), mid_accent, absolute(0), absolute(0)) ]




    hbox:
        xalign 0.5 ypos 680 spacing 30
        textbutton "Continue" action ShowMenu("load"):
            text_size 40 yalign 0.5 left_padding 80 right_padding 80

        textbutton "New Game" action Start():
            background "gui/button_1_bg.png" xysize(448, 136)
            text_size 55 left_padding 70 right_padding 70 text_align(0.5, 0.5) text_yoffset 0

        textbutton "Options" action ShowMenu("preferences"):
            text_size 40 yalign 0.5 left_padding 80 right_padding 80


    frame:
        
        style_prefix "mm_more"

        hbox:
            textbutton "About" action ShowMenu("about")
            text "•" 
            textbutton "Help" action ShowMenu("help")
            text "•" 
            textbutton "Quit" action Quit()

            ###you can add more buttons here if you wish

        
        

###Styles and transforms

transform blurry():
    blur 20

style main_label_text:
    font "fonts/Chomsky.otf" 
    size title_size

style main_label:
    align(0.5, 0.5)
    yoffset -30 

style mm_more_text:
    yalign 0.5 size 20
    font "DejaVuSans.ttf"
style mm_more_button:
    background None padding (0,0)
    yalign 0.5
style mm_more_hbox:
    yalign 0.5
    spacing 10
style mm_more_frame:
    background Frame("gui/main_menu/more_bg.png", 20, 0, 100, 0)
    pos(45, 960) ysize 80 top_padding 15 right_padding 100 left_padding 30


