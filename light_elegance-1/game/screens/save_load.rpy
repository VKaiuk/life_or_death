## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load


## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 392
define config.thumbnail_height = 212




screen save():

    tag menu

    #add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use file_slots(_("Save"))


screen load():

    tag menu

    #add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(
        pattern=_("Page {}"), auto=_("Automatic saves"),
        quick=_("Quick saves"))

    use game_menu(title)



    grid 2 2:
        align(0.5, 0.5) xspacing 50 yspacing 25  yoffset 60
        transpose True
        for i in range(4):
            $ slot = i + 1

            hbox:
                style_prefix "slot"

                ##The 3rd and 4th slot should have the save/load/delete buttons on the other side so we reverse the order the hbox is filled in in those cases
                if slot >= 3:
                    box_reverse True

                vbox:


                    ####Save Button
                    ###Not needed in main menu so we hide it
                    if not main_menu:
                        button:
                            add "gui/button/ic_save_load.png": 
                                align(0.5, 0.5) yoffset 3  xoffset 1
                                
                                ###the image is black and transparent so here we color it
                                matrixcolor ColorizeMatrix(mid_accent, mid_accent)
                                at button_fade ### make it slightly transparent when idle
                
                            action FileSave(slot) style "contbutton"


                    ###Load Button
                    button:
                        add "gui/button/ic_save_load.png": 
                            align(0.5, 0.5) yoffset -3 xoffset 1 yzoom -1
                            
                            ###the image is black and transparent so here we color it
                            matrixcolor ColorizeMatrix(mid_accent, mid_accent)
                            at button_fade
                            
                        action FileLoad(slot) style "contbutton"
                        


                    ###Delete button
                    button:
                        add "gui/button/ic_delete.png": 
                            align(0.5, 0.5) yoffset 0 xoffset 0 
                            
                            ###the image is black and transparent so here we color it
                            matrixcolor ColorizeMatrix(mid_accent, mid_accent)
                            at button_fade
                            
                        action FileDelete(slot) style "contbutton"
                        



                ###The Screenshot + Date part of the save slot
                button:
                    text "Empty Slot" align(0.5, 0.5) color mid_accent size 45
                    add AlphaMask(FileScreenshot(slot), "gui/button/save_mask.png") align(0.5, 0.5) yoffset -7
                    add "gui/button/save_border.png" align(0.5, 0.5) yoffset -7

    
                    action NullAction()

                    text FileTime(slot,
                            format=_("{#file_time}%B %d %Y, %H:%M"),
                            empty=_("")):
                                style "slot_time_text"


    

    ####page navigation

    frame:
        style_prefix "page"

        hbox:
            textbutton _("➤") action FilePagePrevious() text_font "DejaVuSans.ttf" text_size 30 yoffset -1 at flip ###no ➤ symbol the other way so we're just transforming it

            if config.has_autosave:
                textbutton _("{#auto_page}A") action FilePage("auto")

            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 10):
                textbutton "[page]" action FilePage(page)

            textbutton _("➤") action FilePageNext() text_font "DejaVuSans.ttf" text_size 30 yoffset -1


    
    ###Sync buttons

    hbox:
        pos(1210, 213)
        button:
            background "gui/button/cloud_bg.png" xysize(119,90)
            add "gui/button/cloud_up.png" align(0.5, 0.5) matrixcolor ColorizeMatrix(light_accent,light_accent) yoffset 1 at button_fade
            action UploadSync()


        button:
            background "gui/button/cloud_bg.png" xysize(119,90)
            add "gui/button/cloud_down.png" align(0.5, 0.5) matrixcolor ColorizeMatrix(light_accent,light_accent) yoffset 1 at button_fade
            action DownloadSync()


transform flip():
    xzoom -1

transform button_fade():
    alpha .5
    on idle:
        alpha 0.5
    on hover:
        alpha 1.0
    on selected:
        alpha .5
style page_frame:
    background Frame("gui/button/page_bg.png", 60, 0, 60, 0)
    ysize 116 padding(60, 34)
    pos(442, 200)
style page_button:
    background None padding(0,0)
    yalign 0.5 
style page_button_text:
    size 34
    idle_color light_accent
    hover_color dark_accent
    selected_color dark_accent
style page_hbox:
    spacing 15
    



style slot_time_text:
    align(0.5, 1.0) yoffset 60
    outlines [ (1, "#2b262609", 0, 0),  (2, "#00000007", 0, 0), (3, "#00000010", 0, 0), (4, "#00000007", 0, 0) ]

    #fixed:
        #xsize 1500 xalign 1.0
        ## This ensures the input will get the enter event before any of the
        ## buttons do.
    #    order_reverse True

        ## The page name, which can be edited by clicking on it.
        ## This can be pretty easily removed if you want.
        ## Don't forget to also remove the `default` at the top if so.
    #    button:
    #        style "page_label"
    #        key_events True
    #        action page_name_value.Toggle()

    #        input:
    #            style "page_label_text"
    #            value page_name_value

        ## The grid of file slots.
    #    grid 3 2:
    #        style_prefix "slot"

    #        for i in range(3*2):
    #            $ slot = i + 1

    #            button:
    #                action FileAction(slot)
    #                has vbox

    #                add FileScreenshot(slot) xalign 0.5

                    ## https://www.fabriziomusacchio.com/blog/2021-08-15-strftime_Cheat_Sheet/
    #                text FileTime(slot,
    #                        format=_("{#file_time}%A, %B %d %Y, %H:%M"),
    #                        empty=_("empty slot")):
    #                    style "slot_time_text"

    #                text FileSaveName(slot) style "slot_name_text"

                    # This means the player can hover this save
                    # slot and hit delete to delete it
    #                key "save_delete" action FileDelete(slot)

        ## Buttons to access other pages.
    #    vbox:
    #        style_prefix "page"
    #        hbox:
    #            textbutton _("<") action FilePagePrevious()

    #           if config.has_autosave:
    #                textbutton _("{#auto_page}A") action FilePage("auto")

    #            if config.has_quicksave:
    #                textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
    #            for page in range(1, 10):
    #                textbutton "[page]" action FilePage(page)

    #            textbutton _(">") action FilePageNext()

    #        if config.has_sync:
    #            if CurrentScreenName() == "save":
    #                textbutton _("Upload Sync"):
    #                    action UploadSync()
    #            else:
    #                textbutton _("Download Sync"):
    #                    action DownloadSync()

style slot_vbox:
    yalign 0.5
    spacing 10
style slot_button:
    background "gui/button/save.png"
    xysize(465,282)

style contbutton:
    background "gui/button/save_btn.png"
    xysize(63, 63)

