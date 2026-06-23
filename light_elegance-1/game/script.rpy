# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default first_name = "?"
default last_name = "?"
define q = Character("????")
define k = Character("Ivy")
define s = Character("Kaori")
define u = Character("[first_name]")
define i = Character("Echo") 
define c = Character("Cashier")
define t = Character("Kaori & Ivy")

image sakura normal = Transform("images/images/Sakura/normal.png", zoom=0.24, ypos=1.06)
image sakura panick = Transform("images/images/Sakura/panick.png", zoom=0.24, ypos=1.06)
image sakura sad = Transform("images/images/Sakura/sad.png", zoom=0.24, ypos=1.06)
image sakura blush = Transform("images/images/Sakura/blush.png", zoom=0.24, ypos=1.06)
image sakura serious = Transform("images/images/Sakura/serious.png", zoom=0.24, ypos=1.06)

image kaori normal = Transform("images/images/Kaori/normal.png", zoom=0.24, ypos=1.06)
image kaori happy = Transform("images/images/Kaori/happy.png", zoom=0.24, ypos=1.06)
image kaori sad = Transform("images/images/Kaori/sad.png", zoom=0.24, ypos=1.06)
image kaori serious = Transform("images/images/Kaori/serious.png", zoom=0.24, ypos=1.06)
image kaori blush = Transform("images/images/Kaori/blush.png", zoom=0.24, ypos=1.06)

image cashier = Transform("images/Side_Pack_1/Maid_A/Maid_A_Casual_Frown.png",zoom=1.1, ypos=1.45)

default time_left = 300
# 600

default first_kaori = False
default first_sakura = False

default asked_q1 = False
default asked_q2 = False
default asked_q3 = False

default asked_qq1 = False
default asked_qq2 = False
default asked_qq3 = False

default talked_kaori = False
default talked_sakura = False
default is_riverbank = False

default offensive = False
default normal = False

default current_ending = None
default persistent.seen_ivy_ending_note = False
default persistent.seen_kaori_ending_note = False
default persistent.seen_refuse_ending_note = False


transform left_char: 
    zoom 0.25
    xpos 0.25
    ypos 1.3
    anchor (0.5, 1.0) 

transform right_kaori:
    xpos 0.70
    ypos 1.53
    
transform blur_bg:
    blur 5

transform center_pos:
    xalign 0.5
    yanchor 1.0

transform enter_from_left:
    xalign 0.5
    xoffset -1200
    yanchor 1.0
    linear 0.8 xoffset 0

transform enter_from_right:
    xalign 0.5
    yanchor 1.0
    xoffset 1200
    linear 0.8 xoffset 0
    
transform exit_to_left:
    linear 0.8 xoffset -1200

transform exit_to_right:
    linear 0.8 xoffset 1200

transform slight_zoom_up:
    linear 0.25 zoom 1.25 ypos 1.3

transform face_zoom:
    linear 0.25 zoom 1.8 ypos 1.85

transform walk_bob:
    yoffset 0
    xoffset 0
    linear 0.15 yoffset -4 xoffset 2
    linear 0.15 yoffset 0 xoffset 0
    linear 0.15 yoffset -4 xoffset -2
    linear 0.15 yoffset 0 xoffset 0
    repeat

transform slight_zoom_down:
    linear 0.25 zoom 0.95

transform slight_zoom_bounce:
    linear 0.25 zoom 1.25 ypos 1.3
    linear 0.25 zoom 1.0 ypos 1.05

# The game starts here.

#region Start
label start:
    define playlist = [
        "audio/sound3.mp3",
        "audio/sound3.mp3",
        "audio/sound3.mp3",
        "audio/sound3.mp3",
        "audio/sound2.ogg",
        "audio/sound4.ogg",
        "audio/end.mp3",
        "audio/sound4.mp3",
        "audio/sound1.mp3",
        "audio/mystery.mp3",
    ]

    # jump ending
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # play music "audio/TownTheme.mp3" volume 1.5 fadein 1.0
    stop music fadeout 1.0
    play music playlist loop
    pause 1.5
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.R
    # jump ending
    "BEEP! BEEP! BEEP!"
    scene bedroom
    i "Hmhm... "
    i "It's time to wake up."
    u "Ugh..."
    u "Damn it. I forgot you people had this creepy side of yours. Who thought putting a speaker in my room was a good idea?"
    i "You did. It was included in the documents you signed."
    u "And here I thought I read them carefully."
    i "You remember the rules, right?"
    i "You can't speak to the main suspects once you enter the school building."
    i "You'll have four breaks to find the real culprit."
    i "Only during those four breaks will you have the opportunity to speak with the suspects."
    i "At the end of the day, you'll make a choice that can't be changed."
    i "Hey! Are you listening!?"
    u "Ha? Yeah, I'm listening."
    i "..."
    i "Please confirm your understanding by stating your first and last name."
    $ first_name = 'Sol'
    $ last_name = 'Paver'
    u "[first_name] [last_name]. Ahhh..."
    # label ask_name:
    #     $ first_name = renpy.input("Enter the first name: ", length=32).strip()
    #     if first_name == "":
    #         "First name is required."
    #         jump ask_name
    #     jump last_name

    # label last_name:
    #     $ last_name = renpy.input("Enter the last name: ", length=32).strip()
    #     if last_name == "":
    #         "Last name is required."
    #         jump last_name


    i "Thank you for your confirmation."
    i "Please remember that you will be the one carrying out the execution."
    i "I advise you to prepare yourself."
    i "[first_name] [last_name], We wish you luck."

    u "..."

    "Meiyaku Academy. A place unlike any ordinary school. It was specifically designed to raise the finest detective... at least, that’s what they say."

    "If a crime is committed and it involves me in any way, I am the one responsible for the investigation."
    "Nothing leaves this institution. Every case is resolved within its walls."
    "And once the culprit is found..."
    "They face the death penalty."

    "And yesterday... My best friend's body was found."
    "As his closest friend, it falls to me to find the person responsible. And today is the day I must make my decision." 
    "There are two people considered as the primary suspects."
    "My childhood friend..."
    "And someone I truly care about."
    "Who should I believe? Who should I trust?"
    "As an aspiring detective, I should let go of my emotions, especially in moments like this."
    "But how do I..."
    "How do I choose who lives or dies?"

    pause 1.0

    scene store_day with fade

    pause 1.0
    "On my way to school, I see a girl running toward me. She’s wearing a school uniform, holding a pink school hoodie in her hands."
    "She waves one hand in the air, calling out to me from a distance. I can’t really hear her, but I can already guess who it is."
    show kaori happy at enter_from_left, walk_bob
    pause 0.8
    hide kaori
    show kaori happy

    q "Hey [first_name]! I've been calling you forever! Why didn't you wait for me?"
    "Her name's Ivy and she’s my childhood friend. Our parents work together, and somewhere along the way, we naturally became close."
    "There's always a smile on her face. I’ve never seen her sad or devastated before. Even today..."
    k "It's been a while. How are you?"
    u "I'm fine... You seem awfully cheerful for a day like this."
    show kaori normal with dissolve
    k "Why shouldn't I?"
    u "A boy from our class died two weeks ago."
    "I think his name was Ronn."
    "His girlfriend killed him. According to her, he was the one who murdered her best friend."
    "There's a rumor she only did it because he cheated on her."
    "..."
    "Yeah."
    "I think I've just developed a lifelong fear of cheating."
    u "Doesn't that scare you?"
    k "A little. But not as much as it should."

    k "I know you're capable of finding the real culprit."
    k "So I choose to believe in you."
    u "You sure are confident about me. But don’t expect me to go easy on you just because we’re friends."
    show kaori happy with dissolve
    k "Haha... Don’t worry. I know how serious you are when it comes to things like this."
    u "Are you really okay?"

    show kaori serious with dissolve
    k "Yeah... Honestly, I’m more worried about you. A lot has happened these past few days."
    k "I don’t think anyone could handle all of this alone."
    "I rub my neck, trying to organize my thoughts."
    u "I think I'm sad. I think I should be."
    u "But I don't know..."
    u "The more I think about his death, the less I seem to care."
    u "Do you think it's normal?"
    k "..."
    k "I think you still don’t fully understand what’s happening right now."
    k "It’s normal to feel lost when you lose someone close."
    u "..."
    show kaori normal with dissolve
    k "So if you need anything... talk to me. I’ll always be there for you."
    u "Yeah. Thanks... Ivy."

    "We continued our walk to school in silence."

    scene front_school_day with fade
    show kaori normal with dissolve
    k "So... who do you think the real culprit is? Between me and Kaori."
    u "I don't think I should answer."
    k "Why? If you tell me now, you can see later whether you had good intuition."
    k "That's an important trait for a great detective."
    menu:
        "Ivy":
            u "Between the two of you, I think it’s you."
            show kaori serious with dissolve
            "She stops and crosses her arms with a huff."
            k "What? Why?"
            u "I mean... I don't think Kaori's capable of it."
            k "Oh... so you think I am?"
            u "Well..."
            q "Of course you are."

            "I turn my head to the left. It’s Kaori."
            "The person I... I feel something deeper for than friendship."
            show kaori serious
            show kaori serious:
                linear 0.2 xpos 0.70

            show sakura normal 
            show sakura normal:
                linear 0.2 xpos 0.25 
            
            s "Look at your face. It practically screams, 'I'm the killer.'"
            u "K-Kaori..."
            k "Ugh... why are you here?"
        "Kaori":
            u "Between the two of you, I think it’s Kaori."
            q "Why?"
            u "I don’t know her as well as I know you."
            "I turn my head to the left, expecting to see Ivy, but I see Kaori instead."
            "The person I... I feel something deeper for than friendship."
            show kaori serious
            show kaori serious:
                linear 0.2 xpos 0.70

            show sakura normal
            show sakura normal:
                linear 0.2 xpos 0.25 
            u "S-Kaori!? What are you doing here?"
            u "I'm sorry... I-"
            s "No, I understand. That’s how this works."
            show sakura normal with dissolve
        "None of you":
            u "I don’t think it was either of you."
            k "Why is that?"
            u "I don’t think Kaori's capable of it."
            u "And you... I’ve known you for a long time, so I know it wasn’t you."
            q "So who do you think it was?"
            "I turn my head to the left. It’s Kaori."
            "The person I... I feel something deeper for than friendship."
            show kaori serious
            show kaori serious:
                linear 0.2 xpos 0.70

            show sakura normal
            show sakura normal:
                linear 0.2 xpos 0.25 

            u "K-Kaori!? What are you doing here?"
            s "So?"
            u "I-I don't know. I haven't even read the report."
            u "For all I know, the killer could be the janitor."
            s "Hmm..."

    show sakura normal at slight_zoom_up
    s "You two seem... happy this morning. And you're walking to school together."
    s "Didn't you only meet because of today's situation? You never used to do that."
    show sakura serious at slight_zoom_bounce

    show kaori serious at slight_zoom_up
    k "N-No, that's not true."
    k "We're childhood friends. I don't think it's strange for friends to walk to school together."

    k "What about you? Are you worried he'll choose you today? Is that why you came looking for him?"
    show kaori serious at slight_zoom_bounce

    show sakura serious at slight_zoom_up
    s "No... I’m not. Why would I be... I haven’t done anything wrong."
    show sakura serious at slight_zoom_bounce

    "Right... the two of them weren't on good terms. To be honest, I never knew why."
    "A long sigh escapes my lips."
    u "Let’s calm down, both of you..."
    "An awkward silence settles between us."
    "As we continue walking, I notice how cold it is today. Goosebumps run down my arms."
    show sakura normal at slight_zoom_up
    s "What’s wrong, [first_name]? Are you cold?"
    show sakura normal at slight_zoom_bounce
    
    show kaori happy at slight_zoom_up
    k "Do you have a hoodie or something?"
    show kaori happy at slight_zoom_bounce

    u "I’m fine. And no, I don’t."
    u "I lost mine somewhere."
    show sakura normal at slight_zoom_up
    show kaori happy at slight_zoom_up
    with vpunch

    t "Here. Take mine!"
    "Kaori and Ivy both hold out their hoodies toward me at the same time."
    show sakura serious with dissolve
    show kaori normal with dissolve
    k "What are you doing?"
    s "I was about to ask you the same thing."
    u "Stop it. I’m not taking either of them."
    u "They’re pink."
    t "Hmph."
    "Both of them turn their heads away at the same time."
    u "Haha."
    "Still, it feels like Kaori came here for a reason."
    u "You wanted to tell us something, Kaori?"

    show sakura normal at slight_zoom_up
    show kaori normal at slight_zoom_down
    s "Mmm... yes, right."

    s "You’ve already been informed about the rules, haven’t you?"
    u "Yes, I was."
    s "Then, Ivy, you and I are not allowed to speak to each other once we enter the building."

    show kaori normal with dissolve
    k "Phew... I wasn't planning to."
    u "Ivy..."
    k "...What?"
    s "Oh... and the case report, along with all information found is on your desk."


    show sakura normal at slight_zoom_bounce
    s "That's everything from me." 
    s "And [first_name]... I wish you luck."

    show sakura normal at exit_to_left, walk_bob
    pause 0.8
    hide sakura

    show kaori normal at exit_to_left, walk_bob
    pause 0.8
    hide kaori
    
    "Kaori turns and walks into the school. Ivy follows after her, but pauses and glances back at me."

    show kaori happy with dissolve

    k "Just wait and see, [first_name]. I'll prove I had nothing to do with it, haha."
    show kaori happy at exit_to_right, walk_bob
    pause 0.8
    hide kaori happy

    "Ivy is different from others. Even though her life may be on the line, she wears a pure smile, as if none of this frightens her at all."
    "Kaori though, seems anxious. Her eyes are full of sadness, even when she tries to hide that."

    scene class with fade
    "I walk into the classroom, and every student’s gaze is fixed on me. Well... it’s different from what usually happens."
    "I make my way to my desk, and just like Kaori mentioned, the report case is already there."
    jump test

    return
#endregion

#region Choice System
label test:
    scene class with fade

    # $ talked_kaori = True
    # $ talked_sakura = True
    if not talked_kaori and not talked_sakura:
        $ report = """
        {size=+12}Case No. 234{/size}
        Summary 

        Victim's Full Name: Hiro Tanaka
        Body discovered: 03:40 AM
        Location: Riverbank, Mizunagi Street
        Estimated time of death: Around 11:00 PM 

        Body Evidence:
            1. Skin appears pale and wrinkled.
            2. Bruising present around the neck.
            3. Victim's blood found beneath his fingernails.

        {color=#ff0000}{i}*INFORMATION DISCLOSED TO INVESTIGATOR*{/i}{/color}
        
        Ivy Lee

        {i}Relationship to victim: Friend / Classmate{/i}
        - Ivy Lee was the last person seen with the victim after school, around 6:00 PM on the day of his death. 
        - She was added to the list of suspects as a secondary person of interest.

        Kaori Ito

        {i}Relationship to victim: Friend / Classmate{/i}
        - According to the anonymous witness, Kaori was seen speaking with the victim near the school at
        approximately 10:40PM. The two remained there for some time.
        - The content of their conversation is unknown.
        - At around 10:50 PM, the victim left the area. Kaori reportedly walked in the same direction a few
        minutes later. 

        {color=#ff0000}All events described above were confirmed by the principal using security camera footage.{/color}
        """
    elif talked_sakura and not talked_kaori:
        $ report = """
        {size=+12}Case No. 234{/size}
        Summary
        Victim's Full Name: Hiro Tanaka
        Body discovered: 03:40 AM
        Location: Riverbank, Mizunagi Street
        Estimated time of death: Around 11:00 PM 

        Body Evidence:
            1. Skin appears pale and wrinkled.
            2. Bruising present around the neck.
            3. Victim's blood found beneath his fingernails.

        {color=#ff0000}{i}*INFORMATION DISCLOSED TO INVESTIGATOR*{/i}{/color}
        
        Ivy Lee

        {i}Relationship to victim: Friend / Classmate{/i}
        - Ivy Lee was the last person seen with the victim after school, around 6:00 PM on the day of his death. 
        - She was added to the list of suspects as a secondary person of interest.

        Kaori Ito

        {i}Relationship to victim: {color=#ff0000}More complex than stated.{/color} {/i}
        - According to the anonymous witness, Kaori was seen speaking with the victim near the school at
        approximately 10:40PM. The two remained there for some time.
        {color=#ff0000}- Lied about her whereabouts.{/color}
        {color=#ff0000}- The content of their conversation is still unknown.{/color}
        - At around 10:50PM, the victim left the area. Kaori reportedly walked in the same direction a few
        minutes later. 
        {color=#ff0000}- She headed to the convenience store.{/color}
        {color=#ff0000}- Reported seeing a suspicious person wearing a dark-blue hoodie.{/color}

        {color=#ff0000}All events described above were confirmed by the principal using security camera footage.{/color}
        """

    elif talked_kaori and not talked_sakura:
        $ report = """
        {size=+12}Case No. 234{/size}
        Summary 

        Victim's Full Name: Hiro Tanaka
        Body discovered: 03:40 AM
        Location: Riverbank, Mizunagi Street
        Estimated time of death: Around 11:00 PM 

        Body Evidence:
            1. Skin appears pale and wrinkled.
            2. Bruising present around the neck.
            3. Victim's blood found beneath his fingernails.

        {color=#ff0000}{i}*INFORMATION DISCLOSED TO INVESTIGATOR*{/i}{/color}
        
        Ivy Lee

        {i}Relationship to victim: Friend / Classmate{/i}
        {color=#ff0000}- Hiro Tanaka requested to borrow the suspect's flash drive.{/color}
        {color=#ff0000}- She went to convenience store around 11PM that night, allegedly to buy a charger.{/color}
        {color=#ff0000}- Ivy reported that she did not see Kaori Ito or Hiro Tanaka that night.{/color}

        Kaori Ito

        {i}Relationship to victim: Friend / Classmate{/i}
        - According to the anonymous witness, Kaori was seen speaking with the victim near the school at
        approximately 10:40PM. The two remained there for some time.
        - The content of their conversation is unknown.
        - At around 10:50 PM, the victim left the area. Kaori reportedly walked in the same direction a few
        minutes later. 

        {color=#ff0000}All events described above were confirmed by the principal using security camera footage.{/color}
        """
    elif talked_sakura and talked_kaori and not is_riverbank:
        $ report = """
        {size=+12}Case No. 234{/size}
        Summary 

        Victim's Full Name: Hiro Tanaka
        Body discovered: 03:40 AM
        Location: Riverbank, Mizunagi Street
        Estimated time of death: Around 11:00 PM 

        Body Evidence:
            1. Skin appears pale and wrinkled.
            2. Bruising present around the neck.
            3. Victim's blood found beneath his fingernails.

        {color=#ff0000}{i}*INFORMATION DISCLOSED TO INVESTIGATOR*{/i}{/color}\
        
        Ivy Lee

        {i}Relationship to victim: Friend / Classmate{/i}
        - Hiro Tanaka requested to borrow the suspect's flash drive.
        - She went to convenience store around 11PM that night, allegedly to buy a charger.
        - Ivy reported that she did not see Kaori Ito or Hiro Tanaka that night.


        Kaori Ito

        {i}Relationship to victim: More complex than stated. {/i}
        - According to the anonymous witness, Kaori was seen speaking with the victim near the school at
        approximately 10:40PM. The two remained there for some time.
        - Lied about her whereabouts.
        - The content of their conversation is still unknown.
        - At around 10:50PM, the victim left the area. Kaori reportedly walked in the same direction a few
        minutes later. 
        - She headed to the convenience store.
        - Reported seeing a suspicious person wearing a dark-blue hoodie.

        {color=#ff0000}All events described above were confirmed by the principal using security camera footage.{/color}

        {s}They both love me. No. No. Not now.{/s}
        """

    label case:
        if talked_kaori and talked_sakura and not is_riverbank:
            menu:
                "Report":
                    call screen big_text(report)
                    jump case
                "Visit the Riverbank":
                    jump riverbank
        elif is_riverbank:
            scene class
            $ report = """
                {size=+12}Case No. 234{/size}
                Summary 

                Victim's Full Name: Hiro Tanaka
                Body discovered: 03:40 AM
                Location: Riverbank, Mizunagi Street
                Estimated time of death: Around 11:00 PM 

                {color=#ff0000}Cause of Death: Strangulation{/color}
                {color=#ff0000}Location of Death: Footbridge{/color}

                {color=#ff0000}{i}*INFORMATION DISCLOSED TO INVESTIGATOR*{/i}{/color}
                
                Ivy Lee

                {i}Relationship to victim: Friend / Classmate{/i}
                - She went to convenience store around 11PM that night, allegedly to buy a charger.
                {color=#ff0000}- Ivy didn't enter the store. She continued in the same direction as Hiro.{/color}
                {color=#ff0000}- Ten minutes later, she returned carrying a dark-blue hoodie.{/color}
                {color=#ff0000}- She appeared frightened and conflicted when speaking with the store employee.{/color}
                {color=#ff0000}- Ivy requested access to the store's security footage. Motive unknown.{/color}


                Kaori Ito

                {i}Relationship to victim: More complex than stated. {/i}
                - The content of the conversation is still unknown.
                - At around 10:50PM, the victim left the area. Kaori reportedly walked in the same direction a few
                minutes later. 
                - She headed to the convenience store.
                {color=#ff0000}- Kaori left the convenience store and proceeded toward the women's dorm. Confirmed by store security footage.{/color}
                - Reported seeing a suspicious person wearing a dark-blue hoodie. {color=#ff0000}It was Ivy.{/color}

                {color=#ff0000}All events described above were confirmed by the principal using security camera footage.{/color}

                {s}They both love me. No. No. Not now.{/s}
                """
            menu:
                "Report":
                    call screen big_text(report)
                    jump case
                "Talk to Kaori":
                    jump choice_dialogue 

        elif not talked_sakura or not talked_kaori:
            menu:
                "Report":
                    call screen big_text(report)
                    jump case
                "Investigate...":
                    jump dialogue_scene
    
            
    label dialogue_scene:
        if not talked_kaori and not talked_sakura:
            "It's time to decide who to investigate first."
        elif talked_kaori:
            "I talked to Ivy. Now it's time for Kaori."
            jump sakura_dialogue
        elif talked_sakura:
            "I talked to Kaori. Now it's time for Ivy."
            jump kaori_dialogue
        menu:

            "Ivy" if not talked_kaori:
                jump kaori_dialogue
            "Kaori" if not talked_sakura:
                jump sakura_dialogue
    return 
#endregion

#region Ivy Dialogue
label kaori_dialogue:
    $ talked_kaori = True 
    $ name = "Sol"

    pause 1.0
    scene black with fade

    "I go downstairs and step outside to school yard. Ivy is already there, sitting at the bench, staring at a phone. No one else is around."
    scene yard with fade
    u "Hey, Ivy."
    k "..."
    u "...Ivy"
    k "..."
    u "Ivy!"
    show kaori serious with vpunch
    "I raise my voice a little. She flinches slightly."
    show kaori happy with dissolve
    k "[first_name]? Oh- sorry, I didn’t notice you at all."
    "She quickly locks her phone and puts it into her pocket."
    u "Yeah... you really need to start taking this seriously."
    "I sit down beside her."
    u "This isn’t exactly a normal situation. Your life’s kind of on the line here."
    show kaori normal with dissolve
    k "I’m sorry..."
    if talked_sakura:
        show kaori serious with dissolve
        k "Wait, why am I the one apologizing? Shouldn’t you be apologizing for not coming to me first!?"
        u "Why would I do that?"
        k "We're friends."
        u "So? Kaori's my friend too."
        u "Besides… I had my reasons."
        u "The way you’re reacting... Are you jealous or something?"
        show kaori blush with dissolve
        k "No, I’m not... I mean- maybe, just a little."
        u "Huh? What’s wrong with you?"
        k "Hmph..."
        show kaori serious with dissolve
        "Her eyes drift toward the ground."
        "Sometimes, I really don’t understand her."
        u "Look, you’re not the one I’m most suspicious of."
        u "Kaori had more suspicious behavior that night, so I decided to start with her."
        u "Can we just start the questioning?"
        show kaori happy with dissolve
        k "Haha... I was just joking."
        k "Don’t be so serious."
        "This girl."
    else:
        show kaori happy with dissolve
        k "You came to me first. Hehe. Am I that significant to you?"
        "She leans forward slightly, clearly interested in my answer."
        u "No, it's not like that."
        show kaori normal with dissolve
        k "Hmm."
        u "Would you have a problem if I went to Kaori first?"
        show kaori serious with dissolve
        k "Of course I would."
        u "What? Why?"
        k "We're friends."
        u "So? Kaori's my friend too."
        k "But we're closer. Obviously, you should come to me first."
        u "I don't think it works like this."
        k "I think it does."
        u "You're acting weird."
        "She shrugs and leans back against the bench."
        k "I'm always weird in people's eyes."
        u "Not in mine."
        show kaori happy with dissolve
        k "Hehe. Thank you."
        u "Well, maybe-"
        show kaori normal with dissolve
        k "That's enough. I liked your answer."
        u "Haha."
    "...Alright. What will I ask first?"
    label kaori_questions:

        if asked_q1 and asked_q2 and asked_q3:
            if talked_sakura:
                scene black with fade
                "Ivy confessed to me... Ivy said she likes me."
                "I’ve never looked at her that way before."
                "I mean, she’s pretty. Beautiful, even."
                "But she’s always been my friend. Nothing more."
                "It's true, that I like being around her."
                "...And Kaori? I’m so happy she feels the same way I do."
                "But this isn’t the best time to discover this."
            else:
                scene black with fade
                "What!" with vpunch
                "Ivy confessed to me..."
                "What am I supposed to do with that? I’ve never looked at her that way before."
                "I mean, she’s pretty. Beautiful, even."
                "But she’s always been my friend. Nothing more."
                "It's true, that I like being around her..."
                "But then there is Kaori."
               
            u "Ugh...I need to think. I should get back to the classroom."
            "During the class I report everything I found out till now."
            jump test
        menu:
            "What were you doing the night Hiro died?" if not asked_q1 and talked_sakura:
                if talked_sakura:
                    $ first_sakura = True
                    show kaori normal with dissolve
                    u "Simple question. What were you doing around 11PM that night?"
                    k "I went to the convenience store, the one we passed this morning."
                    u "Huh? That late? Why?"
                    k "My charger suddenly broke, so I had to get a new one. I can’t go to school without my phone."
                    u "On your way there, did you see someone wearing dark blue school hoodie?"
                    k "School hoodie?"
                    u "Yes."
                    k "Blue?"
                    u "Am I not clear or what?"
                    k "What about them?"
                    u "Kaori saw someone heading toward the store you were going to."
                    k "..."
                    k "I think I do know something."
                    show kaori happy with dissolve
                    k "It was me. Haha..."
                    "She raises her hand as if volunteering in class."
                    u "..."
                    u "...Damn it."
                    "There goes one of my better theories."
                    k "Was that who you thought the real culprit was?"
                    u "Yes. It was."
                    k "Hahaha... I'm sorry for that."
                    u "Don’t be. Because now, you’re just as suspicious as Kaori was before this conversation started."
                    show kaori normal with dissolve
                    k "Oh..."
                    u "How did you pass her without saying a word? It’s not like you."
                    k "I was wearing headphones, so I wasn’t really paying attention. It was dark too."
                    u "Did you notice anything unusual that night?"
                    k "Hmm..."
                    k "I don’t think so."
                    u "What about Hiro? He was heading the same way."
                    "She tilts her head and thinks for a moment before answering."
                    k "...Hiro?"
                    k "I didn't see him."
                    "I let out a long breath."
                    "It's as if he vanished. Neither of them saw him. Yet both of them were headed the same direction."
                $ asked_q1 = True
                jump kaori_questions
            "According to report..." if not asked_q1 and not talked_sakura:
                $ first_kaori = True
                u "According to the report, you were seen with Hiro around 6 PM after school."
                k "Yes, that's true."
                u "What were you doing together? What did you talk about?"
                k "Why? Are you jealous?"
                u "Answer the question."
                k "Ugh. He asked if he could borrow my flash drive."
                u "A flash drive?"
                k "Yeah... I found it weird too. He said his drive was full."
                k "I've never filled up all the storage in my life."
                "Obviously. You've never downloaded anything larger than a selfie."
                u "Unless you have a lot of data. Do you know what he needed it for?"
                "She shrugs."
                k "No. But he said he needed it quickly. He couldn't even wait a day, so we went to my dorm."
                u "And?"
                k "I gave it to him. Then he left."
                u "What about around 11pm?"
                k "I went to the convenience store, the one we passed this morning."
                u "Huh? That late? Why?"
                k "My charger suddenly broke, so I had to get a new one. I can’t go to school without my phone."
                u "Have you seen anything strange? Anyone suspicious?"
                k "No, I don't think so."
                u "What about Kaori? Did you see her with Hiro?"
                k "No, I didn't."
                "I rub the back of my neck and sigh."
                u "Huh... you're pretty useless."
                show kaori serious with dissolve
                "She stares at me in disbelief."
                k "Useless? That's not how you talk to a lady."
                u "Do you see one?"
                k "Hmm... Meanie."
                show kaori normal with dissolve
                u "What happened after you bought the charger?"
                k "I went to my dorm. The cameras can confirm it."
                $ asked_q1 = True
                jump kaori_questions
            "Why are you so happy today?" if not asked_q3:
                show kaori normal with dissolve
                u "What's with you today? You seem too happy."
                k "Am I? Well...this situation just reminded me of something."
                k "So, I guess I'm a little excited."
                u "Reminded you of what?"
                k "My eighth birthday. You were there too."
                u "What about it?"
                k "Do you remember my cousin, Elena?"
                u "Um... not really."
                k "She's about my age. She used to live in Chicago too."
                u "..."
                k "Doesn't matter."
                k "It happened at my house."
                k "She lost her favorite doll, or at least she thought she had."
                k "After searching everywhere and still not finding it, she started crying."
                k "You saw what happened and immediately started looking for it."
                k "A few minutes later, you found it in my room."
                u "..."
                u "Did you steal it?"
                show kaori serious with dissolve
                k "I didn't steal it. I just wanted to play with it. I was a child."
                k "She told her mom about it. And my parents nagged me, like they always did. Even on my birthday."
                k "I cried and ran away to my room. No one came to see me, to check if everything was alright."
                show kaori normal with dissolve
                k "Until you came. You sat next to me, and said nothing. You were just sitting there, playing with your robot."
                u "...I was shy back then."    
                k "I'm not sure why, but I calmed down pretty quickly. Maybe I was too embarrassed to cry in front of you."
                k "We played together until your parents came to take you home."
                u "Was that the first time we met?"
                k "Yeah."
                u "I can't believe you remember something like this."
                show kaori serious with dissolve
                k "You..."
                k "Well... It was the day I made my first friend."
                u "..."
                k "So of course I remember it."
                u "..."
                "It happened almost eleven years ago. How could I possibly remember something like that?"
                "Well..."
                "She remembered."
                u "Ahem."
                u "Let’s get back to questioning."
                show kaori normal with dissolve
                k "...Yeah."
                $ asked_q3 = True
                jump kaori_questions
            "What’s happened between you and Kaori?" if not asked_q2 and asked_q1 and asked_q3:
                if talked_sakura:
                    u "I wanted to ask about Kaori. You two don’t get along very well. Why?"
                    show kaori normal with dissolve
                    k "Didn’t she already tell you."
                    u "She did, but I want to hear your version."
                    k "I don’t really hate her. She’s actually pretty nice."
                    k "It just like she said. We both like the same person, haha."
                    u "Ivy... are you serious right now? Don’t tell me there’s actually someone you like?"
                    show kaori serious with dissolve
                    k "I do... Is that really something extraordinary?"
                    u "In your case? Yeah, a little. Well... I’m more worried about that person, haha."
                    k "Hey! That’s mean, you know! And what about you?"
                    k "Aren’t you worried that someone might take your precious Kaori from you."
                    u "What are you... where is that coming from?"
                    k "Don’t play dumb, I’m not Kaori. "
                    k "I’ve known you for a long time. I see your eyes when you look at her. The way you act around her. "
                    u "..."
                    u "Is it really that obvious?"
                    show kaori normal with dissolve
                    k "Obvious? The whole class knows that."
                    u "The whole..."
                    "I lower my head in embarrassment."
                    k "..."
                    u "..."
                    show kaori serious with dissolve
                    k "I'm sorry, I shouldn't have talked to you like that."
                    u "No, I should be the one apologizing. My mistake for treating your feelings as a joke."
                    k "..."
                    k "S-so... about the person we like."
                    u "What about them? Was it Hiro?"
                    k "N-No, it’s not him. It’s... um..."
                    show kaori blush with dissolve
                    k "Hehe..."
                    k "I-It’s you."
                    u "Me? What are you talking about?"
                    k "The person we both like."
                    u "..."
                    u "Ivy, stop. This isn’t a time for jokes."
                    k "I’m... not joking."
                    "Her voice trembles. I lift my head and see her looking awkwardly away, her cheeks slightly red."
                    "Her hands rest on her lap, tightly gripping her skirt."
                    u "What?! What d-d-do you mean?"
                    k "What do you mean what do I mean! Don’t make me say it again."
                    k "Yes, I l-like you, I’ve liked you for quite a while now. Happy?"
                    u "...I-I"
                    k "Why aren’t you saying anything? Just say something."
                    u "I'm sorry... I just don't know what to say! It's so sudden!"
                    k "I-I... Ugh."
                    u "I’m happy, I really am."
                    k "Probably just about Kaori."
                    u "N-No, about you too! It’s just..."
                    k "That’s fine. I already knew how this would end. I just wanted to tell you today."
                    k "Because... If not today, then when?"
                    u "Ivy..."
                    k "I said it’s fine! Do you have any more questions?"
                    u "N-No... I don’t."
                    k "Then I’ll go."
                    "She gets up and rapidly leaves the place."
                    show kaori blush at exit_to_left, walk_bob
                    pause 0.8
                    hide kaori
                else:
                    u "I wanted to ask about Kaori. You two don’t get along very well. Why?"
                    show kaori normal with dissolve
                    k "You've never asked that before."
                    u "I never really cared. But I want to know now."
                    k "I don’t really hate her. She’s actually pretty nice."
                    k "It's just that I admire her."
                    show kaori serious with dissolve
                    k "I admire her so much that I end up feeling something negative toward her."
                    k "People are drawn to her. She has this strange ability to make everyone like her."
                    k "I'm not like that. No matter how hard I try, I can't connect with people the way she does."
                    k "Even when there's someone I have feelings for."
                    u "Ivy..." 
                    u "Are you serious right now? Don’t tell me there’s actually someone you like?"
                    show kaori serious with dissolve
                    k "I do... Is that really something extraordinary?"
                    u "In your case? Yeah, a little. Well... I’m more worried about that person, haha."
                    k "Hey! That’s mean, you know! And what about you?"
                    k "Aren’t you worried that someone might take your precious Kaori from you."
                    u "What are you... where is that coming from?"
                    k "Don’t play dumb, I’m not Kaori."
                    k "I’ve known you for a long time. I see your eyes when you look at her. The way you act around her. "
                    u "..."
                    u "Is it really that obvious?"
                    show kaori normal with dissolve
                    k "Obvious? The whole class knows that."
                    u "The whole..."
                    "I lower my head in embarrassment."
                    k "..."
                    u "..."
                    show kaori serious with dissolve
                    k "I'm sorry, I shouldn't have talked to you like that."
                    u "No, I should be the one apologizing. My mistake for treating your feelings as a joke."
                    k "..."
                    show kaori normal with dissolve
                    k "S-so... about the person I like."
                    u "What about them? Was it Hiro?"
                    k "N-No, it’s not him. It’s... um..."
                    "She takes a deep breath."
                    show kaori blush with dissolve
                    k "Hehe..."
                    k "I-It’s you."
                    u "Me? What are you talking about?"
                    k "The person I-I like."
                    u "..."
                    u "Ivy, stop. This isn’t a time for jokes."
                    k "I’m... not joking."
                    "Her voice trembles. I lift my head and see her looking awkwardly away, her cheeks slightly red."
                    "Her hands rest on her lap, tightly gripping her skirt."
                    u "What?! What d-d-do you mean?"
                    k "What do you mean what do I mean! Don’t make me say it again."
                    k "Yes, I l-like you, I’ve liked you for quite a while now. Happy?"
                    u "...I-I"
                    k "Why aren’t you saying anything? Just say something."
                    u "I'm sorry... I just don't know what to say! It's so sudden!"
                    k "You probably don't even care."
                    u "N-No, I'm happy, I really am. It’s just..."
                    k "That’s fine. I already knew how this would end. I just wanted to tell you today."
                    k "Because... If not today, then when?"
                    u "Ivy..."
                    k "I said it’s fine! Do you have any more questions?"
                    u "N-No... I don’t."
                    k "Then I’ll go."
                    "She gets up and quickly leaves."
                    show kaori blush at exit_to_left, walk_bob
                    pause 0.8
                    hide kaori
                $ asked_q2 = True
                jump kaori_questions
#endregion

#region Kaori Dialogue
label sakura_dialogue:
    $ name = "Viktor"
    $ talked_sakura = True

    pause 1.0
    scene black with fade
    "I go downstairs and step into the cafeteria. Kaori is already there, sitting at the table, with a book. No one else is around."
    scene cafe with fade

    u "Hey... Kaori."
    show sakura normal with dissolve
    s "Oh... [first_name], you’re here."
    "She closes her book and sets it aside."

    if talked_kaori:
        "She’s... cute."
        u "Y-Yeah..."
        "When I talk to her when no one is around, I feel nervous. I need to calm down."
    else:
        s "You came to me first. I thought you’d go to Ivy first."
        "She’s... cute."
        u "I mean... yeah. I just thought it made more sense to start here."
        "When I talk to her when no one is around, I feel nervous. I need to calm down."
        
    s "You look kind of nervous..."
    s "Is it because of everything that's happening?"
    "I sit down at the table across from her."
    u "Hm... yeah, something like that. "
    show sakura serious with dissolve
    s "By the way, are you okay? I didn’t get to ask you earlier."
    u "I’m fine. Thanks. "
    show sakura normal with dissolve
    s "Hiro seemed like a really good person. I was quite curious about him."
    s "Smart, athletic... I kind of wish I got to know him better."
    "Seemed? According to the report, they met in secret at night."
    "People usually don't schedule mysterious nighttime meetings with strangers."
    "And why did she mention that he was athletic?"
    "That's a very specific compliment."
    u "Yeah... he was."

    label sakura_questions:
        
        if asked_qq1 and asked_qq2 and asked_qq3:
            u "That’s all I wanted to ask. You’re free to go."
            "Kaori stands up and leaves the places."
            show sakura normal at exit_to_right, walk_bob
            pause 0.8
            hide sakura

            pause 0.5

            if talked_kaori:
                scene black with fade
                "What a day..."
                "Now, on top of everything else, I find out Kaori likes me too."
                "I’m happy... I just don’t know what to do with that."
                "I need to focus on finding the real killer. I can deal with everything else later."
                "During class, I report everything I’ve found so far."
                jump test
            else:
                scene black with fade
                "I don’t know..."
                "She lied. Was she really just scared? Or is she still hiding something?"
                "At first glance, she seems innocent. Still, I need to check the cameras to confirm it."
                jump test

        menu:
            "What were you doing the night Hiro died?" if not asked_qq1:
                u "Simple question. What were you doing around 11PM that night?"
                "The moment I ask, her eyes begin darting around the room."
                "Her fingers tighten around the edge of her skirt."
                s "I... I was in my dorm. Getting ready to sleep. You know, shower and... stuff."
                "She's lying. Is she scared it could rocket back at her?"
                u "Kaori... Do you know why you’re on the suspect list?"
                show sakura serious with dissolve
                s "Honestly, I’m quite puzzled by this question myself."
                u "According to witness, you were the last person seen with Hiro that day. Around 10:40PM to that. Right before his death."
                "Kaori lowers her head"
                s "That’s not..."
                u "It was also confirmed by the school’s camera footage."
                s "..."
                show sakura panick with dissolve
                "Her expression changes drastically."
                u "Why would you lie Kaori? Were you involved?"
                s "I thought no one saw us that night... so, I decided to hide it."
                "She lowers her gaze and twists the fabric of her sleeve."
                s "I thought..."
                u "Why? Did you kill him, Kaori?"
                s "No, I didn’t... I didn’t...!"
                "Her voice trembles. Her hands begin to shake."
                show sakura sad with dissolve
                s "sniff, sniff"
                s "Please... you have to believe me. We just talked... then he went his way."
                s "I left a few minutes later. I had nothing to do with it."
                s "You have to believe me."
                u "Hey... hey. It’s okay. Don’t cry. Here."
                "I take a napkin from my pocket and hand it over to her."
                s "Thank you..."
                u "What did you talk about?"
                s "I... I can't tell you that. It’s something I’d rather keep to myself."
                u "Why?"
                s "It's... personal."
                u "Personal enough to stay silent. Even now?"
                s "Y-Yes..."
                u "...Alright."
                u "Then why did you lie?"
                s "I-I'm just... scared."
                "She wraps her arms around herself."
                s "Scared that I might... die."
                u "Hey. Don’t worry. I’ll do my best to find the real culprit."
                u "From now on, all I want is the truth. Do you understand that?"
                "I know she’s a vulnerable person, but I’m still surprised to see her like this."
                s "Yes... I understand."

                $ asked_qq1 = True
                jump sakura_questions
            "What’s happened between you and Ivy?" if not asked_qq2:
                    if not asked_qq1:
                        show sakura normal with dissolve
                        
                    u "You and Ivy don’t seem to get along. I’ve never questioned this, but now I think it’s time to know the truth."
                    show sakura serious with dissolve
                    s "That’s true."
                    u "Why? Something must have happened."
                    s "I just... hate her. She’s annoying, narcissistic. Always acting like she’s better than everyone."
                    u "That doesn’t come out of nowhere."
                    show sakura normal with dissolve
                    s "It's quite embarrassing to say... haha."
                    u "I still need to know."
                    show sakura blush with dissolve
                    "She fidgets with a strand of her hair."
                    s "You see... it happens that we both like the same person."
                    u "What?!" with vpunch
                    "My voice comes out louder than I expected. Kaori flinches slightly."
                    u "I'm sorry for this."
                    if talked_kaori:
                        "Wait. Ivy told me she likes me. Was it a lie? Or is Kaori telling the truth?"
                        "Also, looking at her face... she seems uncomfortable, like she’s embarrassed in front of me."
                        show sakura blush with dissolve
                        s "Something happened, [first_name]? Your face suddenly went pale."
                        u "No, no, I’m just surprised. What about you? Your face is red."
                        s "Oh... is it? It's just... umm, I'm fine."
                        "She presses her knees together and looks away."
                        "Looking at her face... it has to be true. She’s really in love with me."
                        "Damn... I'm happy."
                        s "A-Are you alright?"
                        "I can feel my face getting warmer."
                        u "Y-Yeah. I'm fine. I'm fine."
                        "I need to calm down. I really should."
                        "But I can’t. I’m just... that happy."
                        "Still... I should make sure."
                        u "...Is it Hiro?"
                        show sakura normal with dissolve
                        s "Hiro? No, it’s not him. Don’t worry. He has nothing to do with this."
                        u "That’s... good. I mean... it’s nothing."
                    else:
                        "Ivy likes someone. That girl can’t like anyone but herself. Ha... Is she doing this on purpose? Yeah... hundred percent."
                        "Also to think that Kaori already likes someone... and it’s not me."
                        show sakura normal with dissolve
                        s "Something happened, [first_name]? Your face suddenly went pale."
                        u "No, no, I’m just surprised. Do you mind telling me who it is?"
                        s "..."
                        "She shifts uncomfortably in her seat."
                        show sakura blush with dissolve
                        s "I don’t want to. It doesn’t have anything to do with the case anyway. And I’m not required to tell you, ahem..."
                        u "...Is it Hiro?"
                        show sakura normal with dissolve
                        s "Hiro? No, it’s not him. Don’t worry. He has nothing to do with this."
                        u "That’s... good. I mean... it’s nothing."

                    $ asked_qq2 = True
                    jump sakura_questions
            "Something unusual happened that night?" if not asked_qq3 and asked_qq1:
                    u "Let’s talk more about that night."
                    s "Alright..."
                    u "You said you went the same way a few minutes later after your conversation ended. "
                    show sakura serious with dissolve
                    s "I didn’t say that."
                    u "The report did. Why did you go that way? The women’s dorm is in the opposite direction."
                    s "I had to stop by the convenience store."
                    u "Why? What's the reason?"
                    s "I needed to buy a few things for myself."
                    u "Weren’t you scared to go there alone?"
                    s "Why would I be? We live in a quiet area."
                    "Not so quiet as it appears."
                    u "Did you see anything unusual? Anyone suspicious?"
                    s "I don’t think so... Hm...Wait."
                    s "When I was walking, a person passed me. They were wearing a dark blue school hoodie."
                    u "Did you see their face? Anything else?"
                    s "It was too dark. I couldn’t see anything."
                    "She shakes her head apologetically."
                    s "Their steps were fast... like they were in a hurry."
                    u "What happened after that?"
                    s "I don't know where that person went. Once I reached the convenience store, I couldn’t see them anymore."
                    u "You bought what you needed. What happened next?"
                    show sakura normal with dissolve
                    s "I went back to my dorm room."
                    u "Can anyone confirm that?"
                    s "I'm sure the dorm's cameras would have recorded me."

                    if talked_kaori:
                        u "Did you maybe see Ivy that night?"
                        s "No, I didn't. Was she there?"
                        u "What about the store? She was heading in that direction."
                        s "Not that I remember."
                    $ asked_qq3 = True
                    jump sakura_questions
#endregion

#region Riverbank
label riverbank:
    pause 1.0
    scene bus with fade
    "The riverbank where Hiro's body was found isn't far from the school, but getting there requires taking a bus."
    "When I arrive, there’s obviously nothing suspicious left at the scene."
    "Let's think about what I've read in the report."

    "His body was found here at 3:40AM."
    "His skin appeared pale and wrinkled."
    "Considering the amount of water exposure, the body was most likely in the river for quite some time before it was discovered."
    "Blood was found beneath his fingernails."
    "That suggests he fought desperately for his life."

    "I close my eyes and try to put the facts in order."
    scene board:
        zoom 1.025 
    with fade

    label drag_select:
        $ quick_menu = False

        $ selected_place = None
        $ selected_cause = None
        $ correct_place = False
        $ correct_cause = False

        call screen drag_both_scene
        
        $ quick_menu = True

        if correct_place:
            if correct_cause:
                "Right. The riverbank wasn't where Hiro died."
                "It was only the place where his body was discovered."
                "And judging by the report, strangulation is the most likely cause of death."
                "The marks on his body and the lack of other fatal injuries point to it."
            elif selected_cause == "stabbing":
                "Right. The riverbank wasn't where Hiro died."
                "It was only the place where his body was discovered."
                "But stabbing doesn't fit."
                "The report never mentioned any stab wounds."
                "If Hiro had been stabbed, it would have been immediately obvious."
                jump drag_select
            elif selected_cause == "gunshooting":
                "Right. The riverbank wasn't where Hiro died."
                "It was only the place where his body was discovered."
                "But a gunshot doesn't make sense."
                "There were no bullet wounds and no mention of a firearm in the report."
                jump drag_select
        elif selected_place == "riverbank":
            if correct_cause:
                "Strangulation seems correct."
                "But the riverbank doesn't."
                "The condition of the body suggests it had been in the water for quite some time."
                jump drag_select
            elif selected_cause == "stabbing":
                "Neither conclusion feels right."
                "The riverbank was where the body was found, not necessarily where the murder happened."
                "And there were no signs of stabbing mentioned in the report."
                jump drag_select
            elif selected_cause == "gunshooting":
                "No. That doesn't fit the evidence."
                "The riverbank being the murder scene already seems unlikely."
                "And nothing suggests a firearm was involved."
                jump drag_select
        elif selected_place == "school":
            if correct_cause:
                "Strangulation makes sense."
                "But the school doesn't."
                "After speaking with Kaori, Hiro headed toward the dormitory area."
                "There's nothing placing him back at the school afterward."
                jump drag_select
            elif selected_cause == "stabbing":
                "I don't think either answer is correct."
                "Hiro was last seen heading away from the school."
                "And the report contains no evidence of stab wounds."
                jump drag_select
            elif selected_cause == "gunshooting":
                "That doesn't add up."
                "The school is the wrong location."
                "And there's no evidence Hiro was shot."
                jump drag_select
        else:
            jump drag_select


    "More likely, his body was thrown into the river somewhere upstream, and the current brought it here."
    scene city with fade
    "The easiest way to do that would be from one of the bridges further along the river. I follow the upstream."
    "About fifteen minutes later, I spot a familiar footbridge. I use it every day on my way to the dorm. Hiro used it too."
    "A footbridge is almost the perfect place to commit a murder. No cameras. Water underneath. A current strong enough to wash away evidence, maybe even fingerprints."
    scene store_afternoon with fade
    "And, almost mockingly, there’s a convenience store just fifty meters before the bridge."
    "The same store Ivy said she was going to that night. The same place Kaori mentioned before returning to her dorm."

    "Right before reaching the store, I notice Ivy leaving. She seems in a hurry, looking around as she heads back toward the school."

    "I head inside."
    show cashier with dissolve 
    u "Good afternoon. I have some questions to ask."
    c "Huh? Again? What do you want?"
    u "Again? What do you mean?"
    c "Some kind of girl was here before you. She gave me a hard time."
    u "A hard time? What did she ask?"
    c "She wanted to... Wait, who are you?"
    u "Oh... My name is [first_name] [last_name]."
    u "I’m investigating the case assigned by the school."
    c "From that academy? Ugh... I hate them."
    c "But they’re scary. Not like I can do anything about it."
    u "So, what did she ask?"
    c "She wanted to look at camera footage."
    u "You let her?"
    c "Obviously not! They told me to only show it if a special card is presented by a student."
    "Special card? Oh... It must be the one inside the report. I put it in my wallet."
    u "Here. May I see the footage, please?"
    c "Hmm... Alright. Come with me."
    hide cashier with dissolve
    "Did Ivy want to delete the data? I’m curious what I’ll see."
    "We step into the security room."

    c "Please be careful. Last time, a boy from your academy deleted a week of footage."
    "Heh."
    "I guess, you made a mistake after all, Ronn."
    u "Sure..."
    "I open the footage from the night Hiro was killed. On the screen, I see Hiro walking past the store. Then, a person in a dark hoodie passes by."
    "Looking at the build of the person, I don't think of a girl. A boy comes to mind instead."
    "And after that... Kaori enters the store. She picks up a few items and leaves, heading back toward the school."

    if first_sakura:
        "I guess she wasn’t lying. But what about Ivy? She passed the store and followed Hiro."
        "I scroll through ten more minutes of footage. Ivy returns to the store, holding the hoodie in her hands. She looks sweaty, like she’s been running."
        "The school is divided in almost every way. Nearly everything is separated between boys and girls."
        "The hoodies are no exception. Blue belongs to the boys. Pink belongs to the girls."
        "Did Ivy borrow the hoodie from another guy? She doesn't have many male friends."
        "Only Hiro and me."
        "..."
        "Is that why I couldn't find mine?"
        "Ivy came to the store at 11:05PM. That’s around Hiro’s estimated time of death."
        "I watch her for a few minutes. She paces back and forth, thinking about something."
        "Was she really involved?"
        "The fact that Ivy wanted to see the footage almost confirms her involvement."
    elif first_kaori:
        "I guess she wasn’t lying. But what about Ivy? I haven't see her yet. Was she here way before?"
        "I scroll through ten more minutes of footage. Ivy returns to the store, holding hoodie in her hands."
        "So the person wearing the dark blue hoodie was Ivy? She was the one who passed Kaori."
        "She didn’t tell me that. She told me she didn’t see her."
        "The school is divided in almost every way. Nearly everything is separated between boys and girls."
        "The hoodies are no exception. Blue belongs to the boys. Pink belongs to the girls."
        "Did Ivy borrow the hoodie from another guy? She doesn't have many male friends."
        "Only Hiro and me."
        "..."
        "Is that why I couldn't find mine?"
        "I watch Ivy for a few minutes. She paces back and forth, thinking about something."
        "Was she really involved?"
        "The fact that she wanted to see the footage almost confirms her involvement."

    "But I can't think of a reason for her to kill him. The same goes for Kaori."
    "Ivy was coming from the same direction as Hiro and Kaori."
    "There's a chance she overheard their conversation."
    "It's worth asking about. I should talk to Kaori next."
    
    $ is_riverbank = True
    jump case
#endregion

#region Second Dialogues
label choice_dialogue:
    # $ first_name = "Viktor"
    pause 1.0 
    scene black with fade
    "I go downstairs and step into the cafeteria. Kaori is already there, sitting at the table, with a book. No one else is around."
    scene cafe with fade
    pause 0.5 

    show sakura normal with dissolve
    s "Hey again, [first_name]."
    u "H-Hi... I have something else to ask."
    "...It's akward for me knowing everything."
    "Should I... no, not right now."
    s "...Alright."
    "I sit down at the table across from her."
    u "What did you and Hiro talk about? I know you asked me not to bring it up, but I need to know."
    show sakura serious with dissolve
    s "..."
    u "I need this information."
    s "Not very comfortable to say, but..."
    show sakura normal with dissolve
    s "I confessed to him... that I... that I liked him."
    "Confessed..."
    "It looks like I won't get anywhere without bringing up what Ivy told me."
    label choice:
        menu:
            "Force the truth out of her":
                u "(Whisper) Damn it… "
                show sakura serious with dissolve
                s "I’m sorry?"
                "I don’t really want to do this. It might destroy our relationship."
                "I stand up and start pacing."
                u "Look, Kaori. I don't have much time right now. I don't need your lies."
                show sakura normal with dissolve
                s "B-But I'm telling the truth. Why would I lie?"
                u "I'm asking myself the same thing."
                u "Why would you hide the fact that Hiro confessed to you?"
                u "Were you embarrassed?"
                u "Because if your life is on the line, embarrassment shouldn't matter."
                s "I- just ask my friends... right, my friends. I’m sure they’ll confirm it."
                u "Your friends? What friends?"
                s "That's... oh, right. Ask Himari. She'll definetely tell you."
                s "You know I don't have time for that."
                u "And Himari? Oh... The same Himari who talks behind your back the moment she gets the chance?"
                s "That's not true. She's not like-"
                u "Of course she is. That’s the kind of school we’re in."
                u "You still don't get it, do you?"
                u "All they care about are themselves."
                u "And the moment you seem useful, they start clinging to you."
                show sakura serious with dissolve
                s "[first_name]? Why are you…"
                u "I’m one break away from deciding who dies." 
                u "Right now, I don't care about your feelings."
                show sakura blush with dissolve
                s "What's that supposed to mean?"
                u "I know everything..."
                if first_sakura:
                    u "About your feelings. Ivy told me."
                    s "W-What do you mean?"
                    u "What you feel toward me. You love me, don’t you?"
                    s "I-I... Did Ivy tell you that?"
                    u "She did. And your face confirms it well enough."
                elif first_kaori:
                    u "About your feelings."
                    s "W-What do you mean?"
                    u "What you feel toward me. You love me, don’t you?"
                    s "H-How do you-"
                    u "Doesn't matter. Your face confirms it well enough."
                s "[first_name], I-I..."
                u "Whether it’s you or Ivy, I’m ready to choose either of you."
                s "It’s not like you… You’re not thinking clearly."
                u "Oh… believe me, I’m perfectly fine. This damn school put me in this position, so I don’t care anymore."
                u "Hiro... Hiro didn’t deserve to die."
                show sakura serious with dissolve
                s "..."
                s "Hiro didn’t deserve to die?"
                s "That scumbag?"
                "A bitter laugh escapes her lips."
                u "What's that suppo-?"
                s "It seems you really know nothing about him after all."
                "She leans closer to me."
                s "That bastard was someone all the girls at this school were afraid of."
                s "I don't know how, but he had countless private photos on his phone."
                s "He used them to blackmail us."
                s "And if someone refused to do what he wanted..."
                s "...he'd threaten to sell them."
                "Her voice trembles with anger."
                s "And that night... I was going to be his next target."
                u "What are you...?"
                s "The school didn’t help because of their stupid rules."
                s "'The school doesn’t interfere in students’ lives unless a death occurs.'"
                s "I never intended to tell you this. I wanted to keep you away from all of it."
                s "He was your friend. I didn't want to hurt you."
                s "I decided to deal with it myself. But then… then he died."
                s "..."
                s "You know what?"
                s "I did not do it..."
                s "I did not kill Hiro, but I wish that I had."
                s "He deserved it. Not because of me, but because of all the girls he hurt."
                s "And you..."
                s "Ugh... I hope you're acting like this because of today."
                s "Because if not..."
                s "...Damn it."
                "She wipes her eyes with the back of her hand."
                s "I imagined my confession would be different."
                s "..."
                s "...I’ll go. I don't have anything else to say."
                "She pushes her chair back and gets to her feet."
                "She turns around and walks away."
                show sakura serious at exit_to_right, walk_bob
                pause 0.8
                hide sakura
                $ offensive = True
            "Open your heart to her":
                u "(Whisper) Damn it..."
                s "I'm sorry."
                "I need to calm down. I don’t want to handle this the wrong way."
                u "Kaori, I need to know the truth. The whole truth."
                u "Because I’m not buying that 'confessed' story."
                s "I-I’ve been telling the truth..."
                u "I know. Or at least... I want to believe that."
                u "But, I don't have much time."
                u "And I don’t want to accuse you without understanding what really happened."
                u "Because I don't want to make the wrong choice. Not when it comes to you."
                s "W-When it comes to me?"
                "Her eyes widen slightly."
                u "..."
                u "Heh..."
                s "Everything alright?"
                u "Y-Yeah... I just..."
                "You can do this. Come on."
                u "I-I..."
                u "I love you, Kaori Ito."
                show sakura blush with dissolve
                s "Huh?"
                s "What do you m-mean?"
                u "I-I like your kidness. The way you help people without expecting anything in return."
                u "Your strength. The way you keep smiling... even when you're hurting."
                u "Your smile. The kind that can make everything feel a little brighter."
                s "[first_name]..."
                s "..."
                u "K-Kaori?"
                u "Please... say something."
                "My heart pounds against my chest."
                "Was I wrong after all?"
                s "I-I...."
                "She lowers her head."
                s "sniff... sniff..."
                show sakura sad with dissolve
                "She looks up again, her eyes filled with tears."
                s "I'm so happy..."
                "A relieved laugh escapes her between sobs."
                s "I'm so happy you said that."
                s "I-I love you too... [first_name]. I love you so much."
                s "I love y... 'sniff'"
                "I take out a napkin and give it to her."
                u "You know... I don’t have an infinite supply of napkins. Hehe..."
                s "I'm sorry. I shouldn't-"
                u "It's okay."
                s "..."
                "A minute passes before she calms down."
                u "...I don't want to lose you."
                u "You don't need to force yourself, but if there is something you're hiding... I need to know."
                show sakura serious with dissolve
                s "..."
                s "I'll tell you."
                s "I'm sorry to say this, but Hiro wasn't a good person."
                u "What do you mean?"
                s "It turned out he had been harming girls at this school."
                s "He blackmailed them using private photos."
                u "Blackmailed?"
                u "Private... Where did he get those?"
                s "I don't know. There were rumors about a hidden camera in the girls' changing room."
                s "The school didn’t help because of their stupid rules."
                s "'The school doesn’t interfere in students’ lives unless a death occurs.'"
                s "I wanted to confront him and do something about it."
                s "But it turned out that he had something on me as well."
                s "And I... eventually became his target that night."
                u "Why? Why didn't you tell me?"
                s "I don't know. I didn't want to hurt you. He was your friend."
                u "..."
                u "That's okay. And... I'm sorry for what he did. I-"
                show sakura normal with dissolve
                s "Why are you apologizing? You're not him. And it's not like you knew."
                s "You're different."
                u "..."
                u "Thanks, Kaori." 
                u "You should go. I need to talk to Ivy."
                s "Sure..."
                "She stands up and steps closer to me."
                show sakura normal at slight_zoom_up
                "She lowers her head and kisses me on the right cheek."
                show sakura blush at slight_zoom_bounce
                s "See you later!"
                "Then she quickly leaves the room."
                show sakura at exit_to_right, walk_bob
                pause 0.8
                hide sakura
                $ normal = True
    
    if offensive:
        "No."
        "I don't believe it. I don't want to."
        "Was Hiro really this kind of person the whole time?"
        "And I never saw it?"
        "He tried to hurt Kaori..."
        u "And I did nothing!"
        u "What about Ivy? Did the same thing happen to her too?"
        "I sit there for a few more minutes, then leave the cafeteria and head to the school yard to speak with Ivy."

        stop music fadeout 2.0
        play music "audio/sound5.mp3" volume 1.5 fadein 2.0
        pause 1.0
        scene black with fade
        "I step outside and see Ivy sitting on the bench. She doesn’t look at me, even though she definitely noticed me."

        scene yard with fade

        pause 0.5
        show kaori happy with dissolve
        u "Ivy..."
        "I quietly sit down beside her."
        k "Oh... hey, [first_name]. Haven’t seen you in a while, hehe."
        show kaori serious with dissolve
        k "Hm? What happened?"
        u "Nothing in particular."
        k "Was it Kaori? Did she reject you or something? I should go talk to her and-"
        "She starts to stand up."
        u "Ivy..."
        u "Stop it. Don’t you have anything else to think about?"
        k "I do. But I’m your friend..."
        show kaori blush with dissolve
        k "Maybe even more. So it’s normal to worry about you."
        u "I'm fine. Don't worry about me."
        show kaori normal with dissolve
        k "Good. But you can talk to me if something’s wrong. Okay?"
        u "Talk? You lied to me."
        u "I checked the footage you wanted to see. You never went inside the store. Not until twenty minutes later, after you followed Hiro." 
        u "Care to explain?"
    elif normal:
        "No."
        "I don't believe it. I don't want to."
        "Was Hiro really this kind of person the whole time?"
        "And I never saw it?"
        "He tried to hurt Kaori..."
        u "And I did nothing!"
        u "What about Ivy? Did the same thing happen to her too?"
        "I sit there for a few more minutes, then leave the cafeteria and head to the school yard to speak with Ivy."
        "Wait?"
        "Did she kiss me?"
        "..."
        "She did."

        stop music fadeout 2.0
        play music "audio/sound5.mp3" volume 1.5 fadein 2.0

        pause 1.0
        scene black with fade
        "I step outside and see Ivy sitting on the bench. She doesn’t look at me, even though she definitely noticed me."
        scene yard with fade

        pause 0.5
        show kaori happy with dissolve
        u "Ivy..."
        "I sit down beside her."
        k "Oh... hey, [first_name]. Haven’t seen you in a while, hehe."
        show kaori serious with dissolve

        k "Huh? What’s with that look?"
        u "What about it?"
        k "Did something good happen? You’re practically glowing."
        u "Uh... you could say that."
        k "What? Did you two get together or something?"
        u "I'm not sure. I just told her how I feel."
        k "Oh..."
        k "I see."
        u "It doesn't really matter right now. Care to explain something for me?"
        k "Explain what?"
        u "Your lie. I checked the footage you wanted to see."
        u "You never entered the store. Not until twenty minutes later, after you followed Hiro."

    k "Well... I never said I went inside, hehe."
    u "Was it you?"
    show kaori normal with dissolve 
    k "Me? Um-"
    u "Even if it was... I still keep questioning it."
    u "Because I realized that you didn’t really like Hiro."
    u "You always acted strange around him. Avoided him. You never spent time with us together."
    k "Well... that’s not entirely true. But I did find him strange. Still, he was your friend, and I..."
    u "Finding someone strange doesn’t make them deserve to die. So there must be something else."
    k "Something else?"
    u "Like blackmail."
    k "..."
    k "So, you knew?"
    u "Kaori told me."
    k "Kaori... interesting. Was she one of his victims too?"
    u "Does it matter?"
    k "Oh... no it doesn't." 
    k "I just... thought she was smarter than the others."
    k "Hiro couldn’t do anything to me. And yet I’m the one people think is the fool?"
    "She looks away, clicking her tongue in irritation."
    u "Ivy..."
    k "I did hate him, that's true. But not because of that."
    u "Then wh-"
    k "He didn't deserve to have a friend like you."
    k "What kind of person thinks their best friend is that blind?"
    k "He really thought he was better and smarter than you."
    u "What-"
    k "Oh, it was obvious. Remember, I've known you for a long time."
    k "Nothing escapes your eyes... unless you choose not to see it." 
    k "...And you never did anything to stop it. Kind of disappointing."
    u "Ivy, I-"
    k "I understand you. I do..." 
    k "After all, he wasn’t always like that. There was a part of you that still hoped he’d change."
    u "Ivy!"
    show kaori serious with dissolve
    "She freezes."
    u "I have no idea what you're talking about."
    u "Like I said, I didn’t know anything until Kaori told me."
    k "But..."
    u "But what?"
    k "..."
    show kaori happy with dissolve
    k "Hehe..."
    k "...I guess I made a mistake."
    u "...Mistake?"
    show kaori normal with dissolve
    k "Ahem..."
    k "T-Then I overheard his conversation with Kaori."
    u "Don't change the subject."
    u "Why did you follow Hiro?"
    k "..."
    "She looks away."
    k "And I couldn't hold myself back anymore."
    u "Ivy..."
    k "God... you’ve never seen him like that."
    "Her fingers curl into fists."
    k "That vicious smile of his. I’ll never forget it."
    k "And that girl... still acting like she didn’t matter to anyone. Thinking about others while being blackmailed..."
    k "..."
    k "She’s a good person. Better than me, that’s for sure."
    "She stands up, preparing to leave."
    u "...Ivy?"
    show kaori normal with dissolve
    k "I will go."
    u "Wait! We're not done yet."
    k "And [first_name]..."
    k "I'm sorry..."
    k "For putting you in this position."

    u "Ivy! What's that supposed to mean?"
    show kaori normal at exit_to_left, walk_bob
    pause 0.8
    hide kaori
    "BEEP! BEEP! BEEP! BEEP! BEEP!" with vpunch
    "A loud sound blasts from the school speakers, hurting my ears. I lower my head and cover them, trying to escape the noise."
    "The sound stops. I take a few seconds to regain my senses. When I look up, no one is standing in front of me."
    u "What the hell?!"
    i "Your time is up. You may no longer speak with the suspects."
    i "Final decision must be made within an hour. You know the rules. The room you choose will decide who dies."
    u "Hey! You bastards! How was I supposed to figure this out in one day?!"
    i "..."
    i "Rules are the rules."

    jump ending
#endregion

#region Ending
label ending:
    $ report = """
        {size=+12}Case No. 234{/size}
        Summary 

        Victim's Full Name: Hiro Tanaka
        Body discovered: 03:40 AM
        Location: Riverbank, Mizunagi Street
        Estimated time of death: Around 11:00 PM 

        Cause of Death: Strangulation
        Location of Death: Footbridge

        {color=#ff0000}{i}*INFORMATION DISCLOSED TO INVESTIGATOR*{/i}{/color}

        Both Kaori and Ivy showed a clear hatred toward Hiro. Both of them had reasons to wish for his death.
        Ivy was not one of Hiro's victims. Her hatred seemed to stem from the way he treated me and those around him.
        That alone doesn't feel like enough reason to commit murder.
        Kaori was one of Hiro's victims. Her hatred came from the harm he caused her and other girls at this school. 
        She had a far stronger motive.
        Yet the evidence points toward Ivy. The store's security footage places her near the victim before the estimated time of death.
        There is still no definitive proof against either suspect. Both could be innocent. Both could be guilty.
        """

    pause 0.5
    scene class with fade

    label ending_choice:
        menu:
            "Final Report":
                call screen big_text(report)
                jump ending_choice
            "Final Decision":  
                "This is the final decision."
                "You may want to save your progress now if you'd like to return later and see another ending."

                menu:
                    "Ivy":
                        u "...Ivy"
                        i "You have made your decision. Please proceed to Ivy Lee's dormitory room."
                        pause 1.0
                        scene black with fade
                        "I step out of the classroom and head toward the women's dormitory."
                        scene building with fade
                        "Before reaching the final door, I wonder if I made the right decision."
                        "Will I regret this later? Will I regret it for the rest of my life?"
                        scene kitchen_night with fade
                        "I open the door to Ivy's apartment. It's dark inside."
                        "Near the entrance, I notice a table with a pistol resting on top of it."
                        "A faint light shines from one of the rooms. I pick up the gun."
                        scene bedroom2:
                            zoom 1.5
                        with fade
                        show kaori normal with dissolve
                        "I open the bedroom door and see Ivy sitting quietly on the bed."
                        "As soon as she notices me, she slowly stands up and steps closer."
                        "The same damn smile on her face."
                        k "So... you're here."
                        u "You're not surprised?"
                        k "I expected as much."
                        u "Expected? I'm still not sure it was you."
                        k "And yet you still chose me. Meaning I made mistakes that led you here."
                        u "What happened to your eyes? They're red."
                        "She quickly looks away."
                        k "I'm just... a little tired."
                        u "Did you really kill Hiro?"
                        k "..."
                        k "Does it matter anymore? I'm not leaving this room alive."
                        i "[first_name] [last_name]..."
                        "I lift my right hand toward her."
                        "My fingers tighten around the grip."
                        "The barrel trembles as it points at her."
                        "I try to steady my hand."
                        "A realization suddenly hits me."
                        "This is the first time I've ever pointed a gun at another person."
                        "The first time I've even held one."
                        "My throat feels dry."
                        "Who thought this was a good idea?"
                        "Who allowed them to make teenagers do something like this?"
                        "I knew a day like this might come eventually."
                        "But now that it's here..."
                        "I regret choosing this school."

                        menu:
                            "Shoot":
                                u "I-I'm sorry..."
                                "My hands start to shake violently."
                                "My vision blurs."
                                "I can barely keep the gun pointed at her."
                                "She takes a small step toward me."
                                k "It's okay..."
                                k "I love yo-"
                                jump ending_three
                            "Don't shoot":
                                u "No..."
                                show kaori serious with dissolve
                                k "[first_name]?"
                                i "Ugh..."
                                i "You know the rules."
                                i "If she lives, then you die."
                                "Before the sentence is even finished, I notice a red dot near my chest."
                                show kaori serious at slight_zoom_up
                                k "No! Wait!"
                                k "D-Don't kill him."
                                "Ivy lowers her head."
                                "Her hands curl into fists at her sides."
                                u "Ivy...?"
                                k "...Kill me."
                                "Her voice trembles."
                                u "What!?"
                                show kaori sad with dissolve
                                "When she raises her head again, tears fill her eyes."
                                k "I did it. I killed Hiro."
                                k "I'm the one who deserves to die. Not you!"
                                u "Ivy?"
                                k "Please..."
                                "She takes a step forward."
                                i "I'll give you one final opportunity."
                                menu:
                                    "Shoot":
                                        u "I'm sorry..."
                                        "My hands start to shake violently."
                                        "I can barely keep the gun pointed at her."
                                        k "[first_name]..."
                                        k "I love yo-"
                                        "The gun fires."
                                        jump ending_three
                                    "I don't believe you":
                                        u "No..."
                                        u "I don't believe you."
                                        u "And I won't kill you. Not you."
                                        k "Wait! [first_name]!"
                                        i "We had high expectations for you."
                                        i "But... have it your way."
                                        k "No! Wait!"
                                        "The gun fires."
                                        "A sharp pain tears through my chest."
                                        "My stomach drops."
                                        "No..."
                                        "My legs give out beneath me."
                                        "I fall on my knees."
                                        k "[first_name]!"
                                        "Ivy rushes to me."
                                        k "Why?"
                                        k "Why would you do something so stupid...?"
                                        u "Iv..."
                                        u "..."
                                        jump ending_x
                    "Kaori":
                        u "...Kaori"
                        i "You have made your decision. Please proceed to Kaori Ito's dormitory room."
                        pause 1.0
                        scene black with fade
                        "I step out of the classroom and head toward the women's dormitory."
                        scene building with fade
                        "Before reaching the final door, I wonder if I made the right decision."
                        "Will I regret this later? Will I regret it for the rest of my life?"
                        scene apartment_night with fade
                        "I open the door to Kaori's apartment. It's dark inside."
                        "Near the entrance, I notice a table with a pistol resting on top of it."
                        scene apartment_day
                        show sakura panick with dissolve
                        "I turn on the lights and see Kaori sitting on the sofa, terrified."
                        "The moment our eyes meet, her expression changes drastically." 
                        "Her eyes widen as she understands what my presence means."
                        "I pick up the gun and slowly step closer to her."

                        if offensive:
                            s "No..."
                            show sakura sad with dissolve
                            s "No, no, no..."
                            "Tears begin to stream down her face."
                            s "It wasn't me."
                            s "You know it wasn't me."
                            s "You checked the dorm cameras, right?"
                            s "You saw I went back."
                            u "Kaori, I—"
                            s "Then why are you here?"
                            s "Why are you standing here with that gun?"
                            s "It was Ivy."
                            u "It wasn't her, Kaori."
                            show sakura panick with dissolve
                            s "You know I'm innocent, and you're still going to kill me?"
                            s "Or maybe you knew from the start."
                            s "Maybe you just needed someone to blame."
                            u "That isn't true."
                            s "Then why did you choose me!?"
                        elif normal:
                            show sakura sad with dissolve
                            s "No..."
                            s "No, please..."
                            "Tears begin to stream down her face."
                            s "It wasn't me."
                            s "You said you believed me."
                            s "You checked the dorm cameras, right?"
                            s "You know I went back."
                            u "Kaori, I—"
                            s "Then why are you here? Why are you holding that?"
                            s "It was Ivy."
                            u "It wasn't her, Kaori."
                            show sakura sad with dissolve
                            s "You told me you loved me."
                            s "Was that a lie too?"
                            u "No... I meant it."
                            s "Then why?"
                            s "Why me?"
                            u "That's-"
                            s "..."
                            show sakura panick with dissolve
                            s "Maybe I was wrong."
                            s "Maybe I was never the one you wanted to save."
                            u "That isn't true."
                            s "Then lower the gun."
                            

                        i "[first_name] [last_name]..."
                        "I lift my right hand toward her."
                        "My fingers tighten around the grip."
                        "The barrel trembles as it points at her."

                        "A realization suddenly hits me."
                        "This is the first time I've ever pointed a gun at another person."
                        "The first time I've even held one."
                        "My throat feels dry."
                        "Who thought this was a good idea?"
                        "Who allowed them to make teenagers do something like this?"
                        "I knew a day like this might come eventually."
                        "But now that it's here..."
                        "I regret choosing this school."


                        menu:
                            "Shoot":
                                u "I'm sorry... Kaori."
                                "My hands start to shake violently."
                                s "No! It wasn't me."
                                "My vision blurs."
                                "I can barely keep the gun pointed at her."
                                s "I hate yo-"
                                "The gun fires."
                                jump ending_one
                            "Don't shoot":
                                u "No! I can't."
                                show sakura sad with dissolve
                                u "I won't shoot."
                                s "Thank you, [first_name]. Thank you."
                                u "I don't think either of them did it. They're innocent."
                                i "Ugh..."                           
                                i "You know the rules."
                                i "Someone has to die. If it isn't Kaori, it will be you."
                                "Before the sentence is even finished, I notice a red dot near my chest."
                                u "No! Wait!"
                                i "..."
                                i "Interesting. You don't want to die."
                                i "But you refuse to kill."
                                i "Most people choose one or the other."
                                i "Very well. I'll give you one final opportunity."
                                i "Think carefully. Your life..."
                                i "...or the life of the person you love."
                                menu:
                                    "Shoot":
                                        u "..."
                                        s "[first_name]?"
                                        "My hands start to shake violently."
                                        u "I'm sorry... Kaori."
                                        "My vision blurs."
                                        s "No! Wai-"
                                        jump ending_one
                                    "Don't shoot":
                                        u "No..."
                                        "My arm slowly lowers."
                                        u "I won't do it."
                                        s "[first_name]..."
                                        i "But... have it your way."
                                        "The gun fires."
                                        "A sharp pain tears through my chest."
                                        "My stomach drops."
                                        "No..."
                                        "My legs give out beneath me."
                                        "I fall on my knees."
                                        s "[first_name]?"
                                        u "Kao..."
                                        u "..."
                                        jump ending_x                      
                    "Return":
                        jump ending_choice
#endregion

#region Endings
label ending_one:
    hide sakura with vpunch
    "Before she can finish her sentence, the bullet strikes her in the chest."
    "For a moment, she remains standing, as if her body still hasn’t understood what happened."
    "Then she stumbles backward and collapses onto the sofa, one trembling hand pressing against the wound."
    s "Nngh..."
    s "Nngh..."
    s "..."
    u "..."
    "My hands won't stop shaking."
    "I've never liked the sight of blood. This case is no different."
    "My stomach twists."
    "I quickly turn away and start coughing."
    "Just looking at the blood makes me want to throw up."
    u "D-Did she-"
    i "Kaori Ito is dead."
    i "Congratulations on your first case, [first_name] [last_name]."
    u "W-Was it her?"
    i "Does the truth matter anymore? She's dead."
    u "I'm starting to think this school is nothing more than an excuse for you people to entertain yourselves."
    u "What's the point of all this?"
    u "How is a detective supposed to live with a sacrifice like that if he doesn't even know whether it was for justice."
    i "..."
    u "Why are you silent?!"
    i "Because we're not certain either."
    u "What?"
    i "We have no confirmation of the real killer. Only a collection of facts. And a conclusion we chose to believe."
    i "You'll never know for certain whether you fought for justice..."
    i "...or condemned an innocent person. Not everyone tells the truth."
    i "This is the reality of the world you're about to enter."
    i "Now, you are free to return to your life."
    i "Assuming you're still capable of it."

    u "..."

    stop music fadeout 2.0
    play music "audio/end.mp3" volume 1.5 fadein 2.0


    pause 1.0
    scene black with fade
    "Meanwhile..."
    pause 0.5
    scene bedroom2:
        zoom 1.5
    with fade
    i "How do you feel?"
    show kaori serious with dissolve
    k "I'm not sure. I-I didn't want her to die."
    k "And yet... Deep down, part of me is happy."
    k "He chose me."
    k "..."
    i "Do you think he feels the same way you do?"
    k "I don't know. Maybe."
    k "But he had every reason to choose me."
    k "Everything pointed to me, and yet he chose Kaori."
    k "Even though he knew she was innocent."
    k "..."
    i "Don't worry about it. You're free to return to the life you had before."
    k "I most definitely will."
    i "..."
    show kaori happy with dissolve
    k "Heh. We're the same, [first_name]."
    k "In the end..."
    show kaori sad with dissolve
    k "We both..."
    k "We both killed for someone we love."
    hide kaori with dissolve

    pause 1.0
    scene black with fade

    "We meet with Ivy in front of the apartment building."
    "Her eyes are red. She must have been crying."
    "I don't say anything. I want to. But I can't."
    "We continue walking forward in total silence."

    pause 0.5
    scene store_night with fade

    show kaori normal with dissolve
    k "...[first_name]"
    k "[first_name]!"
    u "Ugh..."
    u "I'm sorry. I was lost in thought."
    k "It’s okay. I think you'll be thinking about this for a long time."
    u "Yeah..."
    u "Why are you coming with me?"
    k "..."
    k "I just didn't want you to be alone."
    "She keeps her eyes fixed on the ground as she walks."
    u "Do you think I made the right choice?"
    k "I don't think I'm the right person to answer that."
    u "Heh... That's true."
    u "I don't know how I'm supposed to feel. I killed her."
    show kaori serious with dissolve
    "My voice barely rises above a whisper."
    u "I failed her. I wasn't able to help her... To save her."
    k "You tried. More than anyone else would have. I know that."
    k "But you're not alone now. You don't have to carry all of this by yourself."
    show kaori normal with dissolve
    k "I'm here for you."
    u "Thanks, Ivy."
    "She looks at me with that same gentle smile."
    "A smile I've seen countless times before."
    "But today, it feels different."
    "Maybe because, right now, she's the only thing keeping me from falling apart."
    "I quietly reach for her hand."
    show kaori blush with dissolve
    k "Huh! What are you—"
    u "I'm sorry. I-I just..."
    u "..."
    k "..."
    k "I-It's okay."
    k "I don't mind."
    "She gently squeezes my hand."
    "I squeeze back."
    "Neither of us says another word as we walk to my apartment together."
    pause 1.0
    hide kaori with dissolve
    scene black with fade

    $ current_ending = "kaori"


    jump end_credits

label ending_three:
    "Before she can finish her sentence, the bullet strikes her in the chest."
    "For a moment, she remains standing, as if her body still hasn’t understood what happened."
    hide kaori with vpunch
    "Then she stumbles backward and collapses onto the bed, one trembling hand pressing against the wound."
    k "Nngh..."
    k "Nngh..."
    k "..."
    u "..."
    "I've never liked the sight of blood. This case is no different."
    "My stomach twists."
    "I quickly turn away and start coughing."
    "Just looking at the blood makes me want to throw up."
    u "D-Did she-"
    i "Ivy Lee is dead."
    i "Congratulations on your first case, [first_name] [last_name]."
    u "W-Was it her?"
    i "Does the truth matter anymore? She's dead."
    u "I'm starting to think this school is nothing more than an excuse for you people to entertain yourselves."
    u "What's the point of all this?"
    u "How is a detective supposed to live with a sacrifice like that if he doesn't even know whether it was for justice."
    i "..."
    u "Why are you silent?!"
    i "You'll never know for certain whether you fought for justice..."
    i "...or condemned an innocent person. Not everyone tells the truth."
    i "This is the reality of the world you're about to enter."
    i "Now, you are free to return to your life."
    i "Assuming you're still capable of it."

    stop music fadeout 2.0
    play music "audio/end.mp3" volume 1.5 fadein 2.0
    pause 0.5
    scene class with fade
    "Two days later, everyone is still talking about it. People look at me differently now."
    "I sit in class, staring out the window."
    show sakura normal at enter_from_right, walk_bob
    pause 0.8
    hide sakura
    show sakura normal
    s "[first_name]?"
    u "Ugh... I'm sorry. I was lost in thought."
    s "That's okay. I know it's been tough for you."
    u "Yeah..."
    show sakura at slight_zoom_up
    "She steps closer and gently takes my hand."
    "Her grip is warm."
    s "Are you ready for the final test?"
    u "Test? Oh... yeah, I think so. Are you?"
    s "I think I am. I'm just nervous."
    u "Heh. Don't worry. I know you'll do fine."
    s "Thanks, [first_name]."
    u "Um..."
    u "D-Do you want to go see a movie with me tommorow?"
    u "There's a new comedy coming out. I heard it's pretty good."
    s "A movie? With you?"
    show sakura blush with dissolve
    s "Yes! I-I'd love to."
    u "Great. I'll... I'll wait for you after school."
    s "I can't wait. Hehe."
    "Her smile makes my chest feel lighter."
    "For the first time in days, I feel like things might be okay."

    hide sakura with dissolve
    scene bedroom_evening with fade
    "After school, I return to my room."
    "There is no confirmation that it was Ivy. The school refuses to tell me anything."
    "I lean back against the wall and let out a long sigh."
    "But the more I think about her, the more restless I become."
    "In the end, I decide to visit her room one last time."
    scene kitchen_night with fade
    "I enter an apartment. It's dark inside."
    scene kitchen_day
    "I turn on the light and head toward Ivy's room."
    i "You're not supposed to be here."
    u "Damn it! I always forget you can do this."
    i "You're not allowed to enter the women's dormitory when it isn't necessary."
    u "Come on... she's not here anymore."
    scene bedroom2:
        zoom 1.5
    with fade
    "I enter her room."
    "I walk toward her desk and notice that damn hoodie draped over the chair."
    "Is it the same one Ivy was wearing that night?"
    "Was it here when I talked to her?"
    "I pick it up and check the pockets. A flash drive falls into my hand."
    "I insert it into the laptop resting on the desk."
    "Inside, I find a single video. 'Untitled1.mp4'"
    scene black with fade
    pause 0.5

    scene bk:
        zoom 3
        blur 6
    with fade

    show kaori serious:
        zoom 1.85
        xalign 0.5
        yalign 0.25
    with dissolve

    k "Ahem..."
    k "It's time for you to choose..."
    k "And If you're watching this video... then you chose me."
    show kaori happy with dissolve
    k "Hehe. Not in the way I hoped."
    show kaori normal with dissolve
    k "I'm not sure if this is the right time to tell you the truth."
    k "But I lied. I lied a lot. Especially today. And I hope you'll understand why."
    k "I hope you'll understand that everything I did... I did it because of you."
    k "..."
    k "It was you..."
    k "You were the one who killed Hiro Tanaka."
    k "I saw it with my own eyes. I saw your face when you were killing him."
    "What?"
    "That's impossible. I don't rem-"
    show kaori serious with dissolve
    k "I think it's called dissociative amnesia."
    k "Triggered by acute psychological trauma."
    k "A person tends to forget a specific traumatic period."
    k "Sometimes memories from before or after the event become fragmented as well."
    k "It was you in that hoodie."
    k "After you killed Hiro..."
    k "You hid it and ran."
    k "I didn't know what to think."
    k "I knew it would lead back to you..."
    k "That's why I decided to make myself a suspect instead."
    k "I'm not sure if it was the right choice."
    k "But I don't regret it."
    k "..." 
    k "The next day, I came to see you. I wanted to talk to you. To figure out what to do."
    k "That's when I realized something was wrong."
    k "You remembered nothing."
    k "Not what you did. Not the bridge."
    k "Your memories... just disappeared."
    k "I can't imagine what kind of night you went through."
    k "You were alone..."
    k "And I wasn't there to help you."
    show kaori normal with dissolve
    k "Heh."
    k "You couldn't even remember how we first met."
    k "You idiot."
    k "Do you have any idea how sad that made me?"
    k "..."
    k "You also forgot the truth about Hiro."
    k "That was when I realized just how bad it was."
    k "After all, that was the reason you killed him in the first place."
    k "You wanted to protect her."
    k "Protect Kaori..."
    k "And she's..."
    k "She's innocent."
    show kaori serious with dissolve
    k "It was me who told the school about her meeting with Hiro."
    k "I was the one who made her a suspect."
    k "I was the one who dragged her into this."
    k "She's just a victim of mine."
    k "I-I wanted to protect you."
    k "..."
    k "Ugh..."
    k "Who am I trying to fool?"
    k "I wanted to protect myself."
    k "I don't want to die."
    k "Deep down, I hope you'll choose Kaori."
    k "Because I'm..."
    k "..."
    show kaori sad with dissolve
    k "I'm terrified."
    k "I really don't want to die."
    k "I want to stay by your side. I want to see you graduate."
    k "I want to walk to school with you again."
    k "I want to work at the same company as you."
    k "I want all of it."
    "Her voice cracks."
    k "Even if someone innocent has to pay the price."
    k "Even if that makes me a terrible person."
    k "..."
    k "Your memories..."
    k "They'll probably return eventually."
    k "I thought it would be better if I was the one to tell you the truth."
    k "So you wouldn't have to face those memories alone."
    k "But that's not completely true either."
    k "The truth is, I want you to remember me."
    k "I want to be the person you think about."
    k "The person you can't forget."
    k "The person who loved you more than anyone else."
    "She laughs weakly through her tears."
    k "..."
    k "Heh."
    k "How selfish."
    "A door opens somewhere in the background."
    "She wipes her eyes."
    show kaori normal with dissolve
    k "..."
    k "I guess this is goodbye."
    k "I love you, my dear friend."
    k "I always will."
    "The video ends."
    hide kaori with dissolve
    scene bedroom2:
        zoom 1.5
    with fade
    u "..."
    "Tears begin to fall."
    u "B-But I-"
    u "I'm sorry."
    u "Ivy."
    u "I'm so sorry."   
    "I slowly turn toward her bed."
    u "..."
    "All that's left is a dark stain where her blood dried."
    pause 1.0

    $ current_ending = "ivy"

    jump end_credits

label ending_x:
    scene black
    pause 2
    show text "Sol Paver died." at truecenter
    with fade
    pause 2
    show text "The loss of someone Kaori truly cared about broke her. She tried to act normally, as if nothing happened. She attended classes. Answered questions. Smiled when people talked to her. But each day became a little harder than the last. Eventually, the weight became too much to bear. A week later, Kaori Ito withdrew from the academy." at truecenter
    with fade
    pause 12
    show text "Ivy Lee decided to remain at the academy. The smile that once seemed permanently etched onto her face was gone. At first, people assumed it was temporary. Yet the days turned into weeks, and the smile never returned. Eventually, a rumor began to spread throughout the academy. There was a student who had lost her smile. Ivy Lee." at truecenter
    with fade
    pause 14

    $ current_ending = "refuse"

    pause 3
    
    jump end_credits
#endregion

label end_credits:
    # $ quick_menu = False
    scene black

    show text "{size=90}{color=#FFFFFF}THE CULPRIT I LOVE{/color}{/size}" at truecenter
    with fade
    pause 4

    hide text
    with fade

    show text "{size=40}{color=#FFFFFF}written by VKaiuk{/color}{/size}" at truecenter
    with fade
    pause 3

    hide text
    with fade

    show text "{size=40}{color=#FFFFFF}UI Design by Skolaztika\nCharacter Design by Abiboge\nBackground Design by NoranekoGames{/color}{/size}" at truecenter
    with fade
    pause 3

    hide text
    with fade

    if current_ending == "ivy" and not persistent.seen_ivy_ending_note:
        $ persistent.seen_ivy_ending_note = True
        if persistent.seen_kaori_ending_note:
            $ note = """
            You've completed Ivy's and Kaori's Endings.
            
            I had a great time creating this story, and I hope you enjoyed
            Sol's journey as much as I enjoyed writing it. 
            There's still one more ending to discover. Try choosing "Don't 
            Shoot" during the final decision to unlock a short additional 
            ending.

            I hope you enjoyed the story.
            And if you did, please consider leaving a review. It really helps
            and means a lot to me as a developer.
            """
            call screen ending_note(note)
        else:
            $ note = """
            You've completed Ivy's Ending.
            
            I had a great time creating this story, and I hope you enjoyed
            Sol's journey as much as I enjoyed writing it. 
            You can unlock another ending by choosing Kaori during the final
            decision.

            I hope you enjoyed the story.
            And if you did, please consider leaving a review. It really helps
            and means a lot to me as a developer.
            """
            call screen ending_note(note)

    elif current_ending == "kaori" and not persistent.seen_kaori_ending_note:
        $ persistent.seen_kaori_ending_note = True
        if persistent.seen_ivy_ending_note:
            $ note = """
            You've completed Ivy's and Kaori's Endings.
            
            I had a great time creating this story, and I hope you enjoyed
            Sol's journey as much as I enjoyed writing it. 
            There's still one more ending to discover. Try choosing "Don't
            Shoot" during the final decision to unlock a short additional
            ending.

            I hope you enjoyed the story.
            And if you did, please consider leaving a review. It really helps
            and means a lot to me as a developer.
            """
            call screen ending_note(note)
        else:
            $ note = """
            You've completed Kaori's Ending.
            
            I had a great time creating this story, and I hope you enjoyed
            Sol's journey as much as I enjoyed writing it. 
            You can unlock another ending by choosing Ivy during the final
            decision.

            I hope you enjoyed the story.
            And if you did, please consider leaving a review. It really helps
            and means a lot to me as a developer.
            """
            call screen ending_note(note)

    $ current_ending = None

    scene black with Fade(1.0, 1.0, 1.0)
    pause 1.0

    return

screen ending_note(message):
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        padding (50, 50)

        vbox:
            spacing 30

            text "Thank you for playing The Culprit I Love!" size 45
            text message size 28

            textbutton "Continue":
                text_color "#fff"

                xalign 2
                action Return()

screen big_text(info):

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1700
        ysize 900
        padding (90, 140, 90, 120)
        
        vbox:
            viewport:
                scrollbars "vertical"
                mousewheel True
                text info size 28 color "#fff"

            textbutton "CLOSE":
                text_color "#fff"

                xpos 10
                ypos -700
                action Return()

screen drag_both_scene:
    #LEFT HALF
    frame:
        xpos 0
        ypos 0
        xsize 960
        ysize 1080
        background None
        text "Where did Hiro die?" xpos 570 ypos 40 size 50 color "#4e4e4e"

        draggroup:
            if selected_place != "riverbank":
                drag:
                    drag_name "riverbank"
                    xpos 0.20
                    ypos 0.20
                    drag_raise True
                    draggable True
                    droppable False
                    dragged drag_place

                    fixed:
                        xsize 200
                        ysize 100

                        add "gui/drag_dark.png":
                            xsize 200
                            ysize 100
                        
                        text "Riverbank":
                            xalign 0.5
                            yalign 0.5

            if selected_place != "school":
                drag:
                    drag_name "school"
                    xpos 0.40
                    ypos 0.35
                    drag_raise True
                    draggable True
                    droppable False
                    dragged drag_place

                    fixed:
                        xsize 200
                        ysize 100

                        add "gui/drag_dark.png":
                            xsize 200
                            ysize 100
                        
                        text "School":
                            xalign 0.5
                            yalign 0.5

            if selected_place != "unknown":
                drag:
                    drag_name "unknown"
                    xpos 0.60
                    ypos 0.50
                    drag_raise True
                    draggable True
                    droppable False
                    dragged drag_place
                    
                    fixed:
                        xsize 200
                        ysize 100

                        add "gui/drag_dark.png":
                            xsize 200
                            ysize 100
                        
                        text "Unknown":
                            xalign 0.5
                            yalign 0.5

            drag:
                drag_name "place_of_death"
                xpos 0.2
                ypos 0.65
                draggable False
                droppable True

                fixed:
                    xsize 600
                    ysize 300

                    add "gui/drag_back.png":
                        xsize 600
                        ysize 300

                    text "Place of Death":
                        xalign 0.5
                        yalign 0.5
    
    # RIGHT HALF
    frame:
        xpos 960
        ypos 0
        xsize 960
        ysize 1080
        background None
        text 'How did Hiro die?' xpos 25 ypos 40 size 50 color "#4e4e4e"

        draggroup:

            if selected_cause != "strangulation":
                drag:
                    drag_name "strangulation"
                    xpos 0.60
                    ypos 0.20
                    drag_raise True
                    draggable True
                    droppable False
                    dragged cause_place

                    fixed:
                        xsize 200
                        ysize 100

                        add "gui/drag_dark.png":
                            xsize 200
                            ysize 100
                        
                        text "Strangulation":
                            xalign 0.5
                            yalign 0.5

            if selected_cause != "stabbing":
                drag:
                    drag_name "stabbing"
                    xpos 0.40
                    ypos 0.35
                    drag_raise True
                    draggable True
                    droppable False
                    dragged cause_place

                    fixed:
                        xsize 200
                        ysize 100

                        add "gui/drag_dark.png":
                            xsize 200
                            ysize 100
                        
                        text "Stabbing":
                            xalign 0.5
                            yalign 0.5
            
            if selected_cause != "gunshooting":
                drag:
                    drag_name "gunshooting"
                    xpos 0.20
                    ypos 0.50
                    drag_raise True
                    draggable True
                    droppable False
                    dragged cause_place
                    
                    fixed:
                        xsize 200
                        ysize 100

                        add "gui/drag_dark.png":
                            xsize 200
                            ysize 100
                        
                        text "Gunshooting":
                            xalign 0.5
                            yalign 0.5

            drag:
                drag_name "cause_of_death"
                xpos 0.18
                ypos 0.65
                draggable False
                droppable True

                fixed:
                    xsize 600
                    ysize 300

                    add "gui/drag_back.png":
                        xsize 600
                        ysize 300

                    text "Cause of Death":
                        xalign 0.5
                        yalign 0.5

    add Solid("#e9626840"):
        xpos 952
        ypos 30
        xsize 20
        ysize 1080

    add Solid("#e96268"):
        xpos 959
        ypos 30
        xsize 4
        ysize 1080


    if selected_place and selected_cause:
        timer 0.1 action Return()

default selected_place = None
default selected_cause = None
default correct_place = False
default correct_cause = False

init python:

    def drag_place(drags, drop):
        if not drop:
            return

        store.selected_place = drags[0].drag_name

        if store.selected_place == "unknown" and drop.drag_name == "place_of_death":
            store.correct_place = True
        else:
            store.correct_place = False

        renpy.restart_interaction()

    def cause_place(drags, drop):
        if not drop:
            return

        store.selected_cause  = drags[0].drag_name

        if store.selected_cause == "strangulation" and drop.drag_name == "cause_of_death":
            store.correct_cause = True
        else:
            store.correct_cause = False

        renpy.restart_interaction()


screen ten_min_timer():

    frame:
        xpos 0.85
        ypos 0.05
        background "#C41A00"
        padding (12, 6)

        text "Time: [time_left // 60:02d]:[time_left % 60:02d]" color "#FAFAFA"

    timer 1.0 repeat True action If(
        time_left > 1,
        SetVariable("time_left", time_left - 1),
        [SetVariable("time_left", 0), Hide("ten_min_timer"), Jump("timeup_ending")]
    )

# xpos 0.15
# xpos 0.65
