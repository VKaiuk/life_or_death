
image placeholder = "gui/gallery/placeholder.png"
image placeholder_thumb = "gui/gallery/placeholder_thumb.png"

init python:
    g = Gallery()


    ###transition used when clicking on image
    g.transition = dissolve

    # A button that contains an image that automatically unlocks.
    g.button("test_1")
    g.image("placeholder")
    g.unlock("placeholder")


    # A button with an image that is always unlocked.
    g.button("test_2")
    g.image("placeholder")



default max_gallery_pages = 3  ### the number of gallery pages. Increase if needed just add the extra screens too

screen gallery:

    tag menu

    use game_menu(_("History"))

    default gallery_page = 1


    frame:
        style_prefix "page"
        yoffset 25 xoffset -145

        hbox:
            textbutton _("➤") action SetScreenVariable("gallery_page", gallery_page-1), SensitiveIf(gallery_page != 1): 
                text_font "DejaVuSans.ttf" text_size 30 yoffset -1 at flip ###no ➤ symbol the other way so we're just transforming it

            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, max_gallery_pages+1):
                textbutton "[page]" action [SetScreenVariable("gallery_page", page)]

            textbutton _("➤") action SetScreenVariable("gallery_page", gallery_page+1), SensitiveIf(gallery_page != max_gallery_pages) text_font "DejaVuSans.ttf" text_size 30 yoffset -1


    use expression ("gallery_page_" + str(gallery_page))



###Make the buttons here in different screens for each page
screen gallery_page_1():


    hbox:
        style_prefix "gallery"

        ###Add max 6 buttons
        add g.make_button("test_2", "placeholder_thumb",style="gbtn")
        add g.make_button("test_1", "placeholder_thumb",style="gbtn")
        add g.make_button("test_1", "placeholder_thumb",style="gbtn")

        add g.make_button("test_2", "placeholder_thumb",style="gbtn")
        add g.make_button("test_1", "placeholder_thumb",style="gbtn")
        add g.make_button("test_2", "placeholder_thumb",style="gbtn")


screen gallery_page_2():


    hbox:
        style_prefix "gallery"

        ###Add max 6 buttons
        add g.make_button("test_1", "placeholder_thumb",style="gbtn")
        add g.make_button("test_1", "placeholder_thumb",style="gbtn")
        add g.make_button("test_1", "placeholder_thumb",style="gbtn")

        add g.make_button("test_1", "placeholder_thumb",style="gbtn")
        add g.make_button("test_1", "placeholder_thumb",style="gbtn")
        add g.make_button("test_1", "placeholder_thumb",style="gbtn")

screen gallery_page_3():


    hbox:
        style_prefix "gallery"

        ###Add max 6 buttons
        add g.make_button("test_2", "placeholder_thumb",style="gbtn")
        add g.make_button("test_2", "placeholder_thumb",style="gbtn")
        add g.make_button("test_2", "placeholder_thumb",style="gbtn")

        add g.make_button("test_2", "placeholder_thumb",style="gbtn")
        add g.make_button("test_2", "placeholder_thumb",style="gbtn")
        add g.make_button("test_2", "placeholder_thumb",style="gbtn")



style gbtn:
    xysize(187,540)
    background "gui/gallery/bg.png"
    foreground "gui/gallery/border.png"
    insensitive_foreground "gui/gallery/locked.png"

style gallery_hbox:
    spacing 30
    align(0.5, 0.5) yoffset 60