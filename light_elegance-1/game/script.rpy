# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default first_name = "?"
default last_name = "?"
define q = Character("????")
define k = Character("Kaori")
define s = Character("Sakura")
define u = Character("[first_name]")
define i = Character("AI748") 
define c = Character("Cashier")

image sakura normal = Transform("images/images/Sakura/normal.png", zoom=0.35, ypos=1.53)
image sakura panick = Transform("images/images/Sakura/panick.png", zoom=0.35, ypos=1.53)
image sakura sad = Transform("images/images/Sakura/sad.png", zoom=0.35, ypos=1.53)
image sakura blush = Transform("images/images/Sakura/blush.png", zoom=0.35, ypos=1.53)
image sakura serious = Transform("images/images/Sakura/serious.png", zoom=0.35, ypos=1.53)

image kaori normal = Transform("images/images/Kaori/normal.png", zoom=0.35, ypos=1.52)
image kaori happy = Transform("images/images/Kaori/happy.png", zoom=0.35, ypos=1.52)
image kaori sad = Transform("images/images/Kaori/sad.png", zoom=0.35, ypos=1.52)
image kaori serious = Transform("images/images/Kaori/serious.png", zoom=0.35, ypos=1.52)
image kaori blush = Transform("images/images/Kaori/blush.png", zoom=0.35, ypos=1.52)

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
# The game starts here.

#region Start
label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "audio/sybil_system_-_glorytothemachine.mp3" fadein 1.0
    pause 1.5
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    jump test
    "BEEP! BEEP! BEEP!"
    scene bedroom
    i "Hmhm... "
    i "Student with ID #2257, it's time to wake up."
    u "Ugh... Damn it. I forgot you people had this perverted side of yours. Who allowed you to put a speaker in my room?"
    i "You did. When you signed the documents."
    u "Ugh..."
    i "You remember the rules, right?"
    i "You can't speak with the main suspects once you enter the school building."
    i "You'll have four breaks to find the real culprit."
    i "Only during those four breaks will you have the opportunity to speak with the suspects."
    i "At the end of the day, you'll make a choice that can't be changed."
    i "Hey! Are you listening!?"
    u "I'm listening."
    i "Great. Please confirm your understanding by stating your first and last name."
    $ first_name = 'Sol'
    $ last_name = 'Payver'
    u "Sol Payver."
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
    u "Can you tell me why I only have one day to solve this?"
    i "We believe the case can be resolved within a day. And we believe you're capable of it."
    u "I don't think I am."
    i "Enough."
    i "[first_name] [last_name], We wish you luck."

    "Meiyaku Academy. A place unlike any ordinary school. It was specifically designed to raise the finest detectives… at least, that’s what they say."

    "If a crime is committed and it involves me in any way, I am the one responsible for the investigation."
    "And once the culprit is found..."
    "They face the death penalty."
    "Nothing leaves this institution. Every case is resolved within its walls."

    "And yesterday... My best friend's body was found."
    "As his closest friend, it falls to me to find the person responsible. And today is the day I must make my decision." 
    "There are two people considered as the primary suspects."
    "My childhood friend..."
    "And someone I truly care about."
    "Who should I believe? Who should I trust? As a detective, I should let go of my emotions, especially in moments like this."
    "But how do I... how do I choose who lives or dies?"

    pause 1.0

    scene store_day with fade

    pause 1.0
    "On my way to school, I see a girl running toward me. She’s wearing a school uniform, holding a pink school hoodie in her hands."
    "She waves one hand in the air, calling out to me from a distance. I can’t really hear her, but I can already guess who it is."
    show kaori happy with dissolve

    q "Hey [first_name]! I've been calling you forever! Why didn't you wait for me?"
    "This girl is Kaori and she’s my childhood friend. Our parents work together, and somewhere along the way, we naturally became close."
    "Always smile on her face. I even think I’ve never seen her sad or devastated before. Even today..."
    k "It's been a while. How are you?"
    u "I'm fine... You seem awfully cheerful for a day like this."
    show kaori normal with dissolve
    k "Why shouldn't I?"
    u "Two weeks ago, a boy from our class died. Aren’t you scared?"
    k "Most people probably are..."
    k "I think I’m scared too. Just... not that much."

    k "I know you're capable of finding the real culprit."
    k "So I choose to believe in you."
    u "You sure are confident about me. But don’t expect me to go easy on you just because we’re friends."
    show kaori happy with dissolve
    k "Haha... Don’t worry. I know how serious you are when it comes to things like this."
    u "Are you really okay?"

    show kaori serious with dissolve
    k "Yeah... Honestly, I’m more worried about you. A lot has happened these past few days."
    k "I don’t think anyone could handle all of this alone."
    k "So if you need anything... talk to me. I’ll always be there for you."
    u "Thanks... really, Kaori."
    k "..."

    show kaori normal with dissolve
    k "So... who do you think the real culprit is? Between me and Sakura."
    u "I don't think I should answer."
    k "Why? If you tell me now, you can see later whether you had good intuition."
    k "That's an important trait for a great detective. So?"
    menu:
        "Kaori":
            u "Between the two of you, I think it’s you."
            show kaori serious with dissolve
            k "What? Why?"
            u "I just don’t think Sakura is capable of killing someone."
            k "Oh... so you think I am?"
            u "No... but-"
            q "Of course you are."

            "I turn my head to the left. It’s Sakura."
            "The person I... I feel something deeper for than friendship."
            show kaori serious
            show kaori serious:
                linear 0.2 xpos 0.70

            show sakura normal
            show sakura normal:
                linear 0.2 xpos 0.25 

            s "Look at your face. It practically screams, 'I'm the killer.'"
            k "Ugh... why are you here?"
        "Sakura":
            u "Between the two of you, I think it’s Sakura."
            q "Why?"
            u "I don’t know her as well as I know you."
            "I turn my head to the left, expecting to see Kaori, but I see Sakura instead."
            "The person I... I feel something deeper for than friendship."
            show kaori serious
            show kaori serious:
                linear 0.2 xpos 0.70

            show sakura normal
            show sakura normal:
                linear 0.2 xpos 0.25 
            u "S-Sakura!? What are you doing here?"
            s "I decided to join your conversarion."
            u "I'm sorry... I-"
            s "No, I understand. That’s how this works."
            show sakura normal with dissolve
        "None of you":
            u "I don’t think it was either of you."
            k "Why is that?"
            u "I don’t think Sakura is capable of killing someone."
            u "And you... I’ve known you for a long time, so I know it wasn’t you."
            q "So who do you think it was?"
            "I turn my head to the left. It’s Sakura."
            "The person I... I feel something deeper for than friendship."
            show kaori serious
            show kaori serious:
                linear 0.2 xpos 0.70

            show sakura normal
            show sakura normal:
                linear 0.2 xpos 0.25 

            u "S-Sakura!? What are you doing here?"
            s "I decided to join your conversarion. So?"
            u "I-I don’t know. I’ll have to read the report first."
            s "Hmm..."


    # scene front_school_day
    # scene gate_day at blur_bg
    s "You both seem... happy this morning. Walking to school together and all."
    show kaori normal with dissolve
    show sakura serious with dissolve
    s "You only met him because of today's situation, right Kaori? You two never walk together."

    show kaori serious with dissolve
    k "N-No, that's not true"
    k "We're childhood friends. I don't think it's strange for friends to walk to school together."

    k "What about you? Are you scared he’s going to choose you today? Is that why you came out looking for him?"
    s "No... I’m not. Why would I be... I haven’t done anything wrong."

    "Right... the two of them weren't on good terms. To be honest, I never knew why."
    u "Let's calm down everyone..."
    "An awkward silence settles between us. Still, it feels like Sakura came here for a reason."
    u "You wanted to tell us something, Sakura?"

    s "Mmm... yes, right."
    s "You’ve already been informed about the rules, haven’t you?"
    u "Yes, I were."
    s "Then, Kaori, you and I are not allowed to speak to each other once we enter the building."

    show kaori normal with dissolve
    k "Phew... I wasn't planning to."
    u "Kaori..."
    k "...What?"
    s "Oh... and the case report, along with all information found is on your desk."


    show sakura normal with dissolve
    s "That's everything from me." 
    s "And [first_name]... I wish you luck."

    hide sakura normal with dissolve
    hide kaori normal with dissolve
    "Sakura turns and walks into the school. Kaori follows after her, but pauses and glances back at me."

    show kaori happy with dissolve
    k "Just wait and see, [first_name]. I'll prove I had nothing to do with it, haha."
    hide kaori happy with dissolve

    "Kaori is different from others. Even though her life may be on the line, she wears a pure smile, as if none of this frightens her at all."
    "Sakura though, seems anxious. Her eyes are full of sadness, even when she tries to hide that."

    scene classroom_day at blur_bg 
    with fade

    "I walk into the classroom, and every student’s gaze is fixed on me. Well... it’s different from what usually happens."
    "I make my way to my desk, and just like Sakura mentioned, the report case is already there."

    jump test

    return
#endregion

#region Choice System
label test:
    scene classroom_day at blur_bg 
    with fade
    # $ talked_kaori = True
    # $ talked_sakura = True
    if not talked_kaori and not talked_sakura:
        $ report = """
        {size=+12}{b}Case No. 234{/b}{/size}
        {b}Summary{/b} 
        Victim: Hiro Tanaka
        Body discovered: 03:40 AM
        Location: Riverbank, Mizunagi Street
        Cause of death: Evidence of strangulation (marks present on the neck).
        Estimated time of death: Around 11:00 PM 

        {i}*INFORMATION DISCLOSED TO INVESTIGATOR{/i}
        
        {b}Kaori Ito{/b}
        {i}Relationship to victim: Friend / Classmate{/i}
        - Kaori Ito was the last person seen with the victim after school, around 6:00 PM on the day of his death. 
        - She was added to the list of suspects as a secondary person of interest.

        {b}Sakura Sato{/b}
        {i}Relationship to victim: Friend / Classmate{/i}
        - According to the anonymous witness, Sakura was seen speaking with the victim near the school at
        approximately 10:40PM. The two remained there for some time, though the content of their conversation is 
        unknown.
        - At around 10:50 PM, the victim left the area. Sakura reportedly walked in the same direction a few
        minutes later. 
        - All events described above were confirmed by the principal using security camera footage.
        """
    elif talked_sakura and not talked_kaori:
        $ report = """
        {size=+12}{b}Case No. 234{/b}{/size}
        {b}Summary{/b} 
        Victim: Hiro Tanaka
        Body discovered: 03:40 AM
        Location: Riverbank, Mizunagi Street
        Cause of death: Evidence of strangulation (marks present on the neck).
        Estimated time of death: Around 11:00 PM 

        {i}*INFORMATION DISCLOSED TO INVESTIGATOR{/i}
        
        {b}Kaori Ito{/b}
        {i}Relationship to victim: Friend / Classmate{/i}
        - Kaori Ito was the last person seen with the victim after school, around 6:00 PM on the day of his death. 
        - She was added to the list of suspects as a secondary person of interest.

        {b}Sakura Sato{/b}
        {i}Relationship to victim: {s}Friend / Classmate{/s} {color=#ff0000}More complex than stated.{/color} {/i}
        - According to the anonymous witness, Sakura was seen speaking with the victim near the school at
        approximately 10:40PM. The two remained there for some time, though the content of their conversation is 
        unknown.
        {color=#ff0000}- Lied about her whereabouts. Is she scared it could rocket back at her? Or is there something else?{/color}
        {color=#ff0000}- Content of their conversation still unknown.{/color}
        - At around 10:50PM, the victim left the area. Sakura reportedly walked in the same direction a few
        minutes later. 
        {color=#ff0000}- She headed to the convenience store.{/color}
        {color=#ff0000}- Reported seeing a suspicious person wearing a dark-blue hoodie.{/color}
        {color=#ff0000}- After that, she headed straight to her dorm room.{/color}
        - All events described above were confirmed by the principal using security camera footage.
        """
    elif talked_sakura and talked_kaori and not is_riverbank:
        $ report = """
        {size=+12}{b}Case No. 234{/b}{/size}
        {b}Summary{/b} 
        Victim: Hiro Tanaka
        Body discovered: 03:40 AM
        Location: Riverbank, Mizunagi Street
        Cause of death: Evidence of strangulation (marks present on the neck).
        Estimated time of death: Around 11:00 PM 

        {i}*INFORMATION DISCLOSED TO INVESTIGATOR{/i}
        
        {b}Kaori Ito{/b}
        {i}Relationship to victim: Friend / Classmate{/i}
        - {s}Kaori Ito was the last person seen with the victim after school, around 6:00 PM on the day of his death.{/s}
        {color=#ff0000}- She went to convenience store around 11PM that night, allegedly to buy a charger.{/color}
        - {s}She was added to the list of suspects as a secondary person of interest.{/s}
        - {color=#ff0000}No longer considered a secondary person of interest.{/color}


        {b}Sakura Sato{/b}
        {i}Relationship to victim: {s}Friend / Classmate{/s} {color=#ff0000}More complex than stated.{/color} {/i}
        - According to the anonymous witness, Sakura was seen speaking with the victim near the school at
        approximately 10PM. The two remained there for some time, though the content of their conversation is 
        unknown.
        {color=#ff0000}- Lied about her whereabouts. Is she scared it could rocket back at her? Or is there something else?{/color}
        {color=#ff0000}- Content of their conversation still unknown.{/color}
        - At around 10:30 PM, the victim left the area. Sakura reportedly walked in the same direction a few
        minutes later. 
        {color=#ff0000}- She headed to the convenience store.{/color}
        {color=#ff0000}- {s}Reported seeing a suspicious person wearing a dark-blue hoodie.{/s} It was Kaori.{/color}
        - All events described above were confirmed by the principal using security camera footage.

        {color=#ff0000}{s}They both love me. No. No. Not now.{/s}{/color}
        """

    elif talked_sakura and talked_kaori and is_riverbank:
        $ report = """
        {size=+12}{b}Case No. 234{/b}{/size}
        {b}Summary{/b} 
        Victim: Hiro Tanaka
        Body discovered: 03:40 AM
        Location: Riverbank, Mizunagi Street
        Cause of death: Evidence of strangulation (marks present on the neck).
        Estimated time of death: Around 11:00 PM 

        {i}*INFORMATION DISCLOSED TO INVESTIGATOR{/i}
        
        {b}Kaori Ito{/b}
        {i}Relationship to victim: Friend / Classmate{/i}
        - She went to the convenience store around 11:00 PM that night, allegedly to buy a charger.
        - Kaori lied about going into the store. She passed it and followed Hiro instead.
        - Kaori returned about 20 minutes later, holding her hoodie in her hands. She was sweaty, as if she was running.

        {b}Sakura Sato{/b}
        {i}Relationship to victim: {s}Friend / Classmate{/s} {color=#ff0000}More complex than stated.{/color}{/i}
        - According to an anonymous witness, Sakura was seen speaking with the victim near the school at approximately 10:00 PM.
        - The content of their conversation remains unknown. {color=#ff0000}It might be the key.{/color}
        - At around 10:30 PM, the victim left the area. Sakura reportedly walked in the same direction a few minutes later.
        - She headed to the convenience store.
        - After leaving the convenience store, she headed back toward the school. Confirmed by store security footage.
        """

    label case:
        if talked_kaori and talked_sakura and not is_riverbank:
            menu:
                "Report":
                    call screen big_text(report)
                    jump case
                "Riverbank":
                    jump riverbank
        elif is_riverbank:
                menu:
                    "Report":
                        call screen big_text(report)
                        jump case
                    "Talk to Sakura":
                        jump choice_dialogue 
        elif not talked_sakura or not talked_kaori:
            menu:
                "Report":
                    call screen big_text(report)
                    jump case
                "Investigate":
                    jump dialogue_scene
    
            
    label dialogue_scene:
        if not talked_kaori and not talked_sakura:
            "It's time to decide who to investigate first."
        elif talked_kaori:
            "I talked to Kaori. Now it's time for Sakura."
            jump sakura_dialogue
        elif talked_sakura:
            "I talked to Sakura. Now it's time for Kaori."
            jump kaori_dialogue
        menu:

            "Kaori" if not talked_kaori:
                jump kaori_dialogue
            "Sakura" if not talked_sakura:
                jump sakura_dialogue
    return 
#endregion

#region Kaori Dialogue
label kaori_dialogue:
    $ talked_kaori = True 
    $ name = "Sol"

    pause 1.0
    scene black with fade

    "I go downstairs and step outside to school yard. Kaori is already there, sitting at the bench, staring at a phone. No one else is around."
    scene yard_day at blur_bg
    with fade
    u "Hey, Kaori."
    k "..."
    u "...Kaori"
    k "..."
    u "Kaori!"
    show kaori serious with vpunch
    "I raise my voice a little. She flinches slightly"
    show kaori happy with dissolve
    k "[first_name]? Oh- sorry, I didn’t notice you at all."
    u "Yeah... you really need to start to take this serious."
    u "This isn’t exactly a normal situation. Your life’s kind of on the line here."
    show kaori normal with dissolve
    k "I’m sorry..."
    if talked_sakura:
        show kaori serious with dissolve
        k "Wait, why I’m the one apologizing. Shouldn’t you be apologizing for not coming to me first!?"
        u "Why would I do that?"
        k "We're friends."
        u "So? Sakura's my friend too."
        u "Besides… I had my reasons."
        u "The way you’re reacting, are you jealous or something?"
        show kaori blush with dissolve
        k "No, I’m not... I mean- maybe, just a little."
        u "Huh? What’s wrong with you?"
        k "Hm..."
        show kaori serious with dissolve
        "She turns her head away."
        "Sometimes, I really don’t understand her."
        u "Look, you’re not the one I’m most suspicious of."
        u "Sakura... had more strange behaviour that night. I decided to start with her."
        u "So, can we just start the questioning."
        show kaori happy with dissolve
        k "Haha... I was just joking. Don’t be so serious."
        "This girl."
    else:
        show kaori happy with dissolve
        k "You came to me first. Hehe. Am I that significant to you?"
        u "No, it's not like that."
        show kaori normal with dissolve
        k "Hmm."
        u "Would you have a problem if I went to Sakura first?"
        show kaori serious with dissolve
        k "Of course I would."
        u "What? Why?"
        k "We're friends."
        u "So? Sakura's my friend too."
        k "But we're closer. Obviously, you should come to me first."
        u "I don't think it works like this."
        k "I think it does."
        u "You're acting weird."
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
                "I think I’ve got everything I can here. I need to check the riverbank myself."
                "The break ends and I return to the classroom."
                "During the class I report everything I found out till now."
                jump test
                return
            else:
                scene black with fade
                "What!" with vpunch
                "Kaori confessed to me..."
                "What am I supposed to do with that? I’ve never looked at her that way before."
                "I mean, she’s pretty. Beautiful, even."
                "But she’s always been my friend. Nothing more."
                "It's true, that I like being around her..."
                "But then there is Sakura."
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
                    u "Sakura saw someone heading toward the store you were going to."
                    k "..."
                    k "I think I do know something."
                    show kaori happy with dissolve
                    k "It was me. Haha..."
                    u "..."
                    u "...Damn it."
                    k "Was that who you thought the real culprit was?"
                    u "Yes. It was."
                    k "Hahaha... I'm sorry for that."
                    u "Don’t be. Because now, you’re just as suspicious as Sakura was before this conversation started."
                    show kaori normal with dissolve
                    k "Oh..."
                    u "How did you pass her without saying a word? It’s not like you."
                    k "I was wearing headphones, so I wasn’t really paying attention. It was dark too."
                    u "Did you notice anything unusual that night?"
                    k "Hmm..."
                    k "I don’t think so."
                    u "What about Hiro? He was heading the same way."
                    k "...Hiro?... I didn't see him."
                    "It’s as if he vanished. Neither of them saw him. And yet, they both were headed the same direction."
                    "It's either one of them is lying or I'm looking at the wrong suspects."
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
                u "Unless you have a lot of data. Do you know what he needed it for?"
                k "No. But he said he needed it quickly. He couldn't even wait a day, so we went to my dorm."
                u "And?"
                k "I gave it to him. Then he left."
                u "What about around 11pm?"
                k "I went to the convenience store, the one we passed this morning."
                u "Huh? That late? Why?"
                k "My charger suddenly broke, so I had to get a new one. I can’t go to school without my phone."
                u "Have you seen anything strange? Anyone suspicious?"
                k "No, I don't think so."
                u "What about Sakura? Did you see her with Hiro?"
                k "No, I didn't."
                u "Huh... you're pretty useless."
                show kaori serious with dissolve
                k "Useless? That's not how you talk to a lady."
                u "Do you see one?"
                k "Hmm... Meanie."
                show kaori normal with dissolve
                u "Ugh. What happened after you bought the charger?"
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
                k "I have a cousin, Hina. She was about my age."
                k "I took my her doll to my room. She couldn't find it, so she started to cry."
                k "You saw that and immediately found it in my room."
                u "You stole it. That's the right word."
                show kaori serious with dissolve
                k "I didn't steal it. I just wanted to play with it. I was a child."
                u "A monster, not a child."
                k "She told her mom about it. Then my parents nagged me, like they always did. Even on my birthday."
                k "I cried and ran away to my room. No one came to see me, to check if everything was alright."
                show kaori normal with dissolve
                k "Until you came. You sat next to me, and said nothing. You were just sitting there, playing with your robot."
                u "Yeah...I was shy back then."    
                k "I'm not sure why, but I calmed down pretty quickly. Maybe I was too embarrassed to cry in front of you."
                k "We played together until your parents came to take you home."
                u "Was that the first time we met?"
                k "Yeah."
                u "And you still remember this?"
                k "Of course I do. It's the day I got my first friend."
                u "Hah...me too."
                k "..."
                u "Let's get back to questeniong. Shall we?"
                k "...Yeah."
                $ asked_q3 = True
                jump kaori_questions
            "What’s happened between you and Sakura?" if not asked_q2 and asked_q1 and asked_q3:
                if talked_sakura:
                    u "I wanted to ask about Sakura. You two don’t get along very well. Why?"
                    show kaori normal with dissolve
                    k "Didn’t she already tell you."
                    u "She did, but I want to hear your version."
                    k "I don’t really hate her. She’s actually pretty nice."
                    k "It just like she said. We both like the same person, haha."
                    u "Kaori... are you serious right now? Don’t tell me there’s actually someone you like?"
                    show kaori serious with dissolve
                    k "I do... Is that really something extraordinary."
                    u "In your case? Yeah, a little. Well... I’m more worried about that person, haha."
                    k "Hey! That’s mean, you know! And what about you?"
                    k "Aren’t you worried that someone might take your precious Sakura from you."
                    u "What are you... where is that coming from?"
                    k "Don’t play dumb, I’m not Sakura. "
                    k "I’ve known you for a long time. I see your eyes when you look at her. The way you act around her. "
                    k "Like a little boy looking for candy."
                    u "..."
                    u "Is it really that obvious?"
                    show kaori normal with dissolve
                    k "Obvious? Please. The whole class knows that."
                    u "The whole..."
                    "I lower my head in embarrassment"
                    k "..."
                    u "..."
                    show kaori serious with dissolve
                    "An awkward silence settles between us."
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
                    u "Kaori, stop. This isn’t a time for jokes."
                    k "I’m... not joking."
                    "Her voice trembles. I lift my head and see her looking awkwardly away, her cheeks slightly red. I’ve never seen this image on her face before."
                    u "What?! What d-d-do you mean?"
                    k "What do you mean what do I mean! Don’t make me say it again."
                    k "Yes, I l-like you, I’ve liked you for quite a while now. Happy?"
                    u "...I-I"
                    k "Why aren’t you saying anything? Just say something."
                    u "I'm sorry... I just don't know what to say! It's so sudden!"
                    k "I-I... Ugh."
                    u "I’m happy, I really am."
                    k "Probably just about Sakura, right?"
                    u "N-No, about you too! It’s just..."
                    k "That’s fine. I already knew how this would end. I just wanted to tell you today. Because, you know, If not today, then when?"
                    u "Kaori..."
                    k "I said it’s fine! Do you have any more questions?"
                    u "N-No... I don’t."
                    k "Then I’ll go."
                    "She gets up and rapidly leaves the place."
                    hide kaori with dissolve
                else:
                    u "I wanted to ask about Sakura. You two don’t get along very well. Why?"
                    show kaori normal with dissolve
                    k "You've never asked this before."
                    u "I never really cared. But I want to know now."
                    k "I don’t really hate her. She’s actually pretty nice."
                    k "It's just that I admire her."
                    show kaori serious with dissolve
                    k "I admire her so much that I end up feeling something negative toward her."
                    u "Admire her in what way?"
                    k "People love her, unlike me. She has this... magnet that attracts people."
                    k "I'm not like her. I’m not capable of that, even if there’s someone I love."
                    u "Kaori..." 
                    u "Are you serious right now? Don’t tell me there’s actually someone you like?"
                    show kaori serious with dissolve
                    k "I do... Is that really something extraordinary."
                    u "In your case? Yeah, a little. Well... I’m more worried about that person, haha."
                    k "Hey! That’s mean, you know! And what about you?"
                    k "Aren’t you worried that someone might take your precious Sakura from you."
                    u "What are you... where is that coming from?"
                    k "Don’t play dumb, I’m not Sakura."
                    k "I’ve known you for a long time. I see your eyes when you look at her. The way you act around her. "
                    k "Like a little boy looking for candy."
                    u "..."
                    u "Is it really that obvious?"
                    show kaori normal with dissolve
                    k "Obvious? Please. The whole class knows that."
                    u "The whole..."
                    "I lower my head in embarrassment"
                    k "..."
                    u "..."
                    show kaori serious with dissolve
                    "An awkward silence settles between us."
                    k "I'm sorry, I shouldn't have talked to you like that."
                    u "No, I should be the one apologizing. My mistake for treating your feelings as a joke."
                    k "..."
                    show kaori normal with dissolve
                    k "S-so... about the person I like."
                    u "What about them? Was it Hiro?"
                    k "N-No, it’s not him. It’s... um..."
                    show kaori blush with dissolve
                    k "Hehe..."
                    k "I-It’s you."
                    u "Me? What are you talking about?"
                    k "The person I-I like."
                    u "..."
                    u "Kaori, stop. This isn’t a time for jokes."
                    k "I’m... not joking."
                    "Her voice trembles. I lift my head and see her looking awkwardly away, her cheeks slightly red. I’ve never seen this image on her face before."
                    u "What?! What d-d-do you mean?"
                    k "What do you mean what do I mean! Don’t make me say it again."
                    k "Yes, I l-like you, I’ve liked you for quite a while now. Happy?"
                    u "...I-I"
                    k "Why aren’t you saying anything? Just say something."
                    u "I'm sorry... I just don't know what to say! It's so sudden!"
                    k "You probably don't even care."
                    u "N-No, I'm happy, I really am. It’s just..."
                    k "That’s fine. I already knew how this would end. I just wanted to tell you today."
                    k "Because, you know, If not today, then when?"
                    u "Kaori..."
                    k "I said it’s fine! Do you have any more questions?"
                    u "N-No... I don’t."
                    k "Then I’ll go."
                    "She gets up and rapidly leaves the place."
                    hide kaori with dissolve
                $ asked_q2 = True
                jump kaori_questions
#endregion

#region Sakura Dialogue
label sakura_dialogue:
    $ name = "Viktor"
    $ talked_sakura = True

    pause 1.0
    scene black with fade
    "I go downstairs and step into the cafeteria. Sakura is already there, sitting at the table, with a book. No one else is around."
    scene library at blur_bg 
    with fade

    u "Hey... Sakura."
    show sakura normal with dissolve
    s "Oh... [first_name], you’re here."

    if talked_kaori:
        s "You came."
        "She’s... cute."
        u "Y-Yeah..."
        "When I talk to her when no one is around, I feel nervous. I need to calm down."
    else:
        s "You came to me first. I thought you’d go to Kaori first."
        "She’s... cute."
        u "I mean... yeah. I just thought it made more sense to start here."
        "When I talk to her when no one is around, I feel nervous. I need to calm down."
        
    s "You look kind of nervous... first case?"
    u "Hm... yeah, something like that. "
    "It’s not just that though."
    show sakura serious with dissolve
    s "By the way, are you okay? I didn’t get to ask you earlier."
    u "I’m fine. Thanks. "
    show sakura normal with dissolve
    s "Hiro seemed like a really good person. I was quite curious about him."
    s "Smart, athletic... I kind of wish I got to know him better."
    "Seemed? According to the report, they met at night, secretively. Doesn’t that mean they weren’t strangers in the end."
    "And what’s with the whole ‘athletic’ thing? Was she interested in him romantically?"
    u "Yeah... he was."

    label sakura_questions:
        
        if asked_qq1 and asked_qq2 and asked_qq3:
            u "That’s all I wanted to ask. You’re free to go."
            "Sakura stands up and leaves the places."
            hide sakura with dissolve
            pause 0.5

            if talked_kaori:
                scene black with fade
                "What a day..."
                "Now, on top of everything else, I find out Sakura likes me too."
                "I’m happy... I just don’t know what to do with that."
                "I need to focus on finding the real killer. I can deal with everything else later."
                "During class, I report everything I’ve found so far."
                jump test
            else:
                scene black with fade
                "Based on what she said, it seems it wasn’t her. Still, I’ll need to confirm it at the convenience store and the dorm when I get the chance."
                "The break ends and I return to the classroom."
                "During the class I report everything I found out till now."
                jump test

        menu:
            "What were you doing the night Hiro died?" if not asked_qq1:
                u "Simple question. What were you doing around 11PM that night?"
                s "I... I was in my dorm. Getting ready to sleep. You know, shower and... stuff."
                "Shower... No, no what am I even thinking about."
                "She's lying. Is she scared it could rocket back at her."
                u "Sakura... Do you know why you’re on the suspect list?"
                show sakura serious with dissolve
                s "Honestly, I’m quite puzzled by this question myself."
                u "According to witness, you were the last person seen with Hiro that day. Around 10:40PM to that. Right before his death."
                "Sakura lowers her head"
                s "That’s not..."
                u "It was also confirmed by the school’s camera footage."
                s "..."
                show sakura panick with dissolve
                "Her expression changes drastically."
                u "Why would you lie Sakura? Were you involved?"
                s "I thought no one saw us that night... so, I decided to hide it."
                s "I thought..."
                u "Why? Did you kill him, Sakura?"
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
                s "Scared that I might... die."
                u "Hey. Don’t worry. I’ll do my best to find the real culprit."
                u "From now on, all I want is the truth. Do you understand that?"
                "I know she’s a vulnerable person, but I’m still surprised to see her like this."
                s "Yes... I understand."

                $ asked_qq1 = True
                jump sakura_questions
            "What’s happened between you and Kaori?" if not asked_qq2:
                    if not asked_qq1:
                        show sakura normal with dissolve
                        
                    u "You and Kaori don’t seem to get along. I’ve never questioned this, but now I think it’s time to know the truth."
                    show sakura serious with dissolve
                    s "That’s true."
                    u "Why? Something must have happened."
                    s "I just... hate her. She’s annoying, narcissistic. Always acting like she’s better than everyone."
                    u "That doesn’t come out of nowhere."
                    show sakura normal with dissolve
                    s "It's quite embarrassing to say... haha."
                    u "I still need to know."
                    show sakura blush with dissolve
                    s "You see... it happens that we both like the same person."
                    u "What?!" with vpunch
                    "My voice comes out louder than I expected. Sakura flinches slightly."
                    u "I'm sorry for this."
                    if talked_kaori:
                        "Wait. Kaori told me she likes me. Was it a lie? Or is Sakura telling the truth?"
                        "Also, looking at her face... she seems uncomfortable, like she’s embarrassed in front of me."
                        show sakura blush with dissolve
                        s "Something happened, [first_name]? Your face suddenly went pale."
                        u "No, no, I’m just surprised. What about you? Your face is red."
                        s "Oh... is it? It's just... umm, I'm fine."
                        "She looks away, embarrassed."
                        "Looking at her face... it has to be true. She’s really in love with me."
                        "Damn... I'm happy."
                        s "A-Are you alright?"
                        u "Y-Yeah. I'm fine. I'm fine."
                        "I need to calm down. I really should."
                        "But I can’t. I’m just... that happy."
                        "Still... I should make sure."
                        u "...Is it Hiro?"
                        show sakura normal with dissolve
                        s "Hiro? No, it’s not him. Don’t worry. He has nothing to do with this."
                        u "That’s... good. I mean... it’s nothing."
                    else:
                        "Kaori likes someone. That girl can’t like anyone but herself. Ha... Is she doing this on purpose? Yeah... hundred percent."
                        "Also to think that Sakura already likes someone... and it’s not me."
                        show sakura normal with dissolve
                        s "Something happened, [first_name]? Your face suddenly went pale."
                        u "No, no, I’m just surprised. Do you mind telling me who it is?"
                        s "..."
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
                    s "It was too dark. I couldn’t see anything. But their steps were fast... like they were in a hurry."
                    u "What happened after that?"
                    s "I don't know where that person went. Once I reached the convenience store, I couldn’t see them anymore."
                    u "You bought what you needed. What happened next?"
                    show sakura normal with dissolve
                    s "I went back to my dorm room."
                    u "Can anyone confirm that?"
                    s "I'm sure the dorm's cameras would have recorded me."

                    if talked_kaori:
                        u "Did you maybe see Kaori that night?"
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
    "Riverbank isn’t far from the school, but getting there requires taking a bus."
    "When I arrive, there’s obviously nothing suspicious left at the scene."
    "Let's think about what I've read in the report."

    call puzzle_start
    "Where did Hiro die?"
    call riverbank_thinking

    "That means Hiro was strangled, thrown into the water, and carried to the riverbank."
    "More likely, his body was thrown into the river somewhere upstream, and the current brought it here."

    scene city with fade
    "The easiest way to do that would be from one of the bridges further along the river. I follow the upstream."
    "About fifteen minutes later, I spot a familiar bridge. I use it every day on my way to the dorm. Hiro used it too."
    "A bridge is almost the perfect place to commit a murder. No cameras. Water underneath. A current strong enough to wash away evidence, maybe even fingerprints."
    scene store_afternoon with fade
    "And, almost mockingly, there’s a convenience store just fifty meters before the bridge."
    "The same store Kaori said she was going to that night. The same place Sakura mentioned before returning to her dorm."

    "Right before reaching the store, I notice Kaori leaving. She seems in a hurry, looking around as she heads back toward the school."

    "I head inside"
    show cashier with dissolve 
    u "Good afternoon. I have some questions to ask."
    c "Huh? Again? What do you want?"
    u "Again? What do you mean?"
    c "Some kind of girl was here before you. She gave me a hard time."
    u "A hard time? What did she ask?"
    c "She wanted to... Wait, who are you?"
    u "Oh... My name is [first_name] [last_name]."
    u "I’m investigating the case assigned by the school."
    c "From that academy? Between us, I hate those bastards."
    c "But they’re scary. Not like I can do anything about it."
    u "So, what did she ask?"
    c "She wanted to look at camera footage."
    u "You let her?"
    c "Obviously not! They told me to only show it if a special card is presented by a student."
    "Special card? Oh... It must be the one inside the report. I put it in my wallet."
    u "Here. May I see the footage, please?"
    c "Hmm... Alright. Come with me."
    hide cashier with dissolve
    "Did Kaori want to delete the data? I’m curious what I’ll see."
    "We step into the security room."

    c "Please be careful. Last time, a boy from your academy deleted a week of footage."
    u "Sure..."
    "I open the footage from the night Hiro was killed. On the screen, I see Hiro walking past the store. Then, a person in a dark hoodie passes by. And after that... Sakura enters the store."
    "She picks up a few items and leaves, heading back toward the school."

    if first_sakura:
        "I guess she wasn’t lying. But what about Kaori? She passed the store and followed Hiro."
        "I scroll through twenty more minutes of footage. Kaori returns to the store, holding the hoodie in her hands. She looks sweaty, like she’s been running."
        "And she went after Hiro. Was she involved after all?"
        "Also, the fact that she wanted to delete the footage almost confirms her involvement."
    elif first_kaori:
        "I guess she wasn’t lying. But what about Kaori? I haven't see her yet. Was she here way before?"
        "I scroll through twenty more minutes of footage. Kaori returns to the store, holding hoodie in her hands."
        "So the person wearing the dark blue hoodie was Kaori? She was the one who passed Sakura."
        "She didn’t tell me that. She told me she didn’t see her."
        "And the fact that she wanted to delete the footage almost confirms her involvement."

    "I need to talk to Sakura one more time. I need to know what they talked about. It might be the key."
    scene classroom with fade
    $ is_riverbank = True
    jump test
#endregion

#region Second Dialogues
label choice_dialogue:
    # $ first_name = "Viktor"
    pause 1.0 
    scene black with fade
    "I go downstairs and step into the cafeteria. Sakura is already there, sitting at the table, with a book. No one else is around."
    scene cafeteria_day with fade
    pause 0.5 

    show sakura normal with dissolve
    s "Hey again, [first_name]."
    u "H-Hi... I have something else to ask."
    "Awkward. Should I bring up what Kaori told me?"
    "No, not right now."
    s "... Alright."
    "I sit down at the table across from her."
    u "What did you and Hiro talk about? I know you asked me not to bring it up, but it’s an important piece of the puzzle right now."
    show sakura serious with dissolve
    s "..."
    u "I need that piece of information."
    s "Not very comfortable to say, but..."
    show sakura normal with dissolve
    s "I confessed to him... that I... that I liked him."
    "Confessed…"
    "It seems like I won’t get an information without bringing up what Kaori told me."
    label choice:
        menu:
            "Be Offensive":
                u "(Whisper) Damn it… "
                show sakura serious with dissolve
                s "I’m sorry?"
                "I don’t really want to do this. It might destroy our relationship. But what choice do I have?"
                "I stand up and start pacing."
                u "Look, Sakura. I don't have much time right now. I don't need your lies."
                show sakura normal with dissolve
                s "B-But I'm telling the truth. Why would I lie?"
                u "I'm asking myself the same thing. Why would you?"
                s "I- just ask my friends... right, my friends. I’m sure they’ll confirm it."
                u "Your friends? What friends?"
                s "That's... oh, right. Ask Himari. She'll definetely tell you."
                u "Which Himari are you talking about? The one who talks behind your back the moment she gets the chance?"
                s "That's not true. She's not like-"
                u "Oh... don’t bullshit me. The people around you only care about their own future. They don’t care about you or your feelings."
                u "You still don't understand it, do you?"
                u "They’re circling around you like dogs, hoping you’ll be useful to them at some point."
                u "That’s the kind of school we’re in."
                show sakura serious with dissolve
                s "[first_name]? Why are you…"
                u "Do you even understand what’s happening right now? I’m one break away from deciding who dies." 
                u "I don’t care about you or what you feel toward me."
                show sakura blush with dissolve
                s "What's that supposed to mean?"
                u "I know everything..."
                u "About your feelings. Kaori told me."
                s "W-What do you mean?"
                u "What you feel toward me. You love me, don’t you?"
                s "I-I... Did Kaori tell you that?"
                u "She did. And your face confirms it well enough."
                s "[first_name], I-I..."
                u "Look, It's not like I care. Whether it’s you or Kaori, I’m ready to choose either of you."
                s "It’s not like you… You’re not thinking clearly."
                u "Oh… believe me, I’m perfectly fine. This damn school put me in this position, so I don’t care anymore."
                u "Hiro... Hiro didn’t deserve to die."
                show sakura serious with dissolve
                s "..."
                s "Hiro didn’t deserve to die?"
                s "That scumbag?"
                u "What's that suppo-?"
                s "It seems you know nothing about him after all."
                s "That bastard was someone all the girls at this school were afraid of."
                s "I don’t know how, but he had tons of 'private' images on his phone, which he used to blackmail us."
                s "And that night... I was going to be his next target."
                u "What are you...?"
                s "I never intended to tell you this. I wanted to keep you away from all of it."
                s "He was your friend. I didn't want to hurt you."
                s "I wanted to deal with it myself. But then… then he died."
                show sakura normal with dissolve
                s "And you know what? I was happy."
                s "I genuinely felt relieved."
                s "He deserved it, and not because of me, but because of all the girls he hurt."
                s "..."
                s "I did not do it. I did not kill Hiro, but I wish that I had."
                s "And you… you’re different from him. I hope you're like this, only because of today."
                s "Because if not..."
                show sakura serious with dissolve
                s "...Damn it."
                s "I imagined my confession would be different."
                s "..."
                s "...I’ll go. I don't have anything else to say."
                "She stands up and leaves."
                hide sakura with dissolve
                $ offensive = True
            "Be Normal":
                u "(Whisper) Damn it..."
                s "I'm sorry."
                "I need to calm down. I don’t want to handle this the wrong way."
                u "Sakura, I need to know the truth. The whole truth."
                u "Because I’m not buying that 'confessed' story."
                s "I-I’ve been telling the truth..."
                u "I know. Or at least... I want to believe that."
                u "But, I don't have much time."
                u "And I don’t want to accuse you without understanding what really happened."
                u "Because I don't want to make the wrong choice. Not when it comes to you."
                s "Me? What's so special about me?"
                u "..."
                u "Your kidness. The way you help people without thinking about yourself."
                u "Your strength. The way you keep smiling… even when you’re hurting."
                show sakura blush with dissolve
                u "Your smile. The kind that can light a room, not matter how dark it feels."
                s "[first_name]... Why are you saying all of this..."
                u "Because you matter to me. Not just as a friend, but as something more."
                s "Does that mean you-"
                u "Yes... I love you, Sakura Sato."
                s "..."
                s "I-I...."
                "She lowers her head."
                show sakura sad with dissolve
                "sniff... sniff..."
                "She looks up again, her eyes filled with tears."
                s "I'm so happy..."
                s "I'm so happy you said that."
                s "I-I love you too... [first_name]. I love you so much."
                "I take out a napkin and give it to her."
                s "I'm sorry. I shouldn't-"
                u "That's okay."
                s "..."
                "A minute passes before she calms down."
                u "Do you understand now? I don't want to lose you."
                u "You don't need to force yourself, but if there is something you're hiding... I need to know."
                show sakura serious with dissolve
                s "..."
                s "I'll tell you."
                s "That night... I knew Hiro would be there."
                s "I'm sorry to say this, but Hiro wasn't a good person."
                u "What do you mean?"
                s "It turned out that he was harming female students."
                s "He used to blackmail them using 'private' images."
                u "But where did he get those from?"
                s "I'm not sure. Maybe there were a hidden camera inside girls' changing room."
                s "I wanted to confront him and do something about it."
                s "But it turned out that he had something on me as well."
                s "And I... eventually became his target that night."
                u "Why? Why didn't you tell me?"
                s "I don't know. I didn't want to hurt you. He was your friend."
                u "..."
                u "That's okay. And I'm sorry for what he did. I-"
                show sakura normal with dissolve
                s "Why are you apologizing. You're not him. And it's not like you knew."
                s "You're different."
                u "..."
                u "Thanks, Sakura." 
                u "You should go. I need to talk to Kaori."
                s "Sure... See you later."
                "She stands up and leaves."
                hide sakura with dissolve
                $ normal = True
    
    if offensive:
        "Ugh... At some point, I forgot I was acting. Part of what I said came straight from my heart."
        u "Different. Am I really that different?"
        "I knew about Hiro all along. What he was doing. I wonder if he ever realized that."
        "He wasn’t always like that. This school changed him, that’s for sure."
        "No one understood me better than him. I hoped he would change. That he would stop on his own."
        "Shouldn't I feel the same as Sakura? Instead of this... sadness?"
        "And this situation I ended up in?"
        "Is all of this a punishment for me? For what I did... and what I didn’t?"
        "I sit there for a few more minutes, then leave the cafeteria and head to the school yard to speak with Kaori."

        pause 1.0
        scene black with fade
        "I step outside and see Kaori sitting on the bench. She doesn’t look at me, even though she definitely noticed me."
        scene yard with fade

        pause 0.5
        show kaori happy with dissolve
        u "Kaori..."
        k "Oh... hey, [first_name]. Haven’t seen you in a while, hehe."
        show kaori serious with dissolve
        k "Hm? What happened? Your eyes… they’re red."
        u "Nothing in particular."
        k "Was it Sakura? Did she reject you or something? I should go talk to her and-"
        "She starts to stand"
        u "Kaori..."
        u "Stop it. Don’t you have anything else to think about?"
        k "I do. But I’m your friend..."
        show kaori blush with dissolve
        k "And I l-like you too. So it’s normal to worry about you."
        u "I'm fine. Don't worry about me."
        show kaori normal with dissolve
        k "Good. But you can talk to me if something’s wrong. Okay?"
        u "Talk? You lied to me. Remember?"
        u "I checked the footage you wanted to delete. You never went inside the store. Not until twenty minutes later, after you followed Hiro." 
        u "Care to explain?"
    elif normal:
        u "Different. Am I really that different?"
        "I knew about Hiro all along. What he was doing. I wonder if he ever realized that."
        "He wasn’t always like that. This school changed him, that’s for sure."
        "No one understood me better than him. I hoped he would change. That he would stop on his own."
        "And I didn’t stop him. He even hurt Sakura."
        "And this situation I ended up in?"
        "Is this a punishment I deserve? For what I did... and what I didn’t?"
        "I sit there for a few more minutes, then leave the cafeteria and head to the school yard to speak with Kaori."

        pause 1.0
        scene black with fade
        "I step outside and see Kaori sitting on the bench. She doesn’t look at me, even though she definitely noticed me."
        scene yard with fade

        pause 0.5
        show kaori happy with dissolve
        u "Kaori..."
        k "Oh... hey, [first_name]. Haven’t seen you in a while, hehe."
        show kaori serious with dissolve

        k "Huh? What’s with that look?"
        u "What about it?"
        k "Did something good happen? You’re practically glowing."
        u "Uh... you could say that."
        k "What, did you two get together or something?"
        u "No, we didn't. I just told her how I feel."
        k "Oh..."
        k "I see."
        u "It doesn't really matter right now. Care to explain something for me?"
        k "Explain what?"
        u "I'm talking about your lie. I checked the footage you wanted to delete."
        u "You never went inside the store. Not until twenty minutes later, after you followed Hiro."

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
    u "Like... blackmail."
    k "..."
    k "So, you knew?"
    u "Sakura told me."
    k "Sakura... interesting. Was she one of his victims too?"
    u "Does it matter?"
    k "Oh... no it doesn't." 
    k "I just... thought she was smarter than the others."
    k "Hiro couldn’t do anything to me. And yet I’m the one people think is the fool?"
    u "Kaori..."
    k "I did hate him, that's true. But not because of that."
    u "Then wh-"
    k "He didn't deserve to have a friend like you."
    k "What kind of person thinks their best friend is that blind?"
    k "He really thought he was better and smarter than you."
    u "How-"
    k "Oh, it was obvious. Remember, I've known you for a long time."
    k "Nothing escapes your eyes... unless you choose not to see it." 
    k "...And you never did anything to stop it. Kind of disappointing."
    k "But I understand you. I do..." 
    k "After all, he wasn’t always like that. There was a part of you that still hoped he’d change."
    show kaori serious with dissolve
    k "But then I overheard his conversation with Sakura."
    k "And I couldn't hold myself back anymore."
    k "God... you’ve never seen him like that. That vicious smile of his. I’ll never forget it."
    k "And that girl... still acting like she didn’t matter to anyone. Thinking about others while being blackmailed..."
    k "..."
    k "She’s a good person. Better than me, that’s for sure."
    "She stands up, preparing to leave."
    u "...Kaori?"
    show kaori normal with dissolve
    k "[first_name]... I'm sorry."
    k "..."
    k "For putting you in this position."

    u "Kaori! What's that supposed to mean?"
    hide kaori frown with dissolve
    "BEEP! BEEP! BEEP! BEEP! BEEP!" with vpunch
    "A loud sound blasts from the school speakers, hurting my ears. I lower my head and cover them, trying to escape the noise."
    "The sound stops. I take a few seconds to regain my senses. When I look up, no one is standing in front of me."
    u "What the hell?!"
    i "Student with ID #2257. Your time is up. You may no longer speak with the suspects."
    i "Your final decision must be made in 59 minutes. You know the rules. The side of the roof you choose will determine your final answer."
    u "Hey! You bastards! How was I supposed to figure this out in ten hours?!"
    i "..."
    i "Rules are the rules."

    jump ending
#endregion

#region Ending
label ending:
    $ report = """
        {size=+12}{b}Case No. 234{/b}{/size}
        {b}Summary{/b} 
        Victim: Hiro Tanaka
        Body discovered: 03:40 AM
        Location: Riverbank, Mizunagi Street
        Cause of death: Evidence of strangulation (marks present on the neck).
        Estimated time of death: Around 11:00 PM 

        {i}*INFORMATION DISCLOSED TO INVESTIGATOR{/i}
        
        {b}Kaori Ito{/b}
        {i}Relationship to victim: Friend / Classmate{/i}
        - She went to the convenience store around 11:00 PM that night, allegedly to buy a charger.
        - Kaori lied about going into the store. She passed it and followed Hiro instead.
        - Kaori returned about 20 minutes later, holding her hoodie in her hands. She was sweaty, as if she had been running.

        {b}Sakura Sato{/b}
        {i}Relationship to victim: {s}Friend / Classmate{/s} {color=#ff0000}More complex than stated.{/color}{/i}
        - According to an anonymous witness, Sakura was seen speaking with the victim near the school at approximately 10:00 PM.
        - The content of their conversation remains unknown. {color=#ff0000}It might be the key.{/color}
        - At around 10:30 PM, the victim left the area. Sakura reportedly walked in the same direction a few minutes later.
        - She headed to the convenience store.
        - After leaving the convenience store, she headed back toward the school. Confirmed by store security footage.
        """

    pause 1.0
    scene classroom with fade

    label ending_choice:
        show screen ten_min_timer
        
        menu:
            "Final Report":
                call screen big_text(report)
                jump ending_choice
            "Make a Choice":    
                menu:
                    "Kaori":
                        hide screen ten_min_timer
                        "tEXT"

                    "Sakura":
                        hide screen ten_min_timer
                        pause 1.0
                        
                        i "You have made your decision. Please proceed to the west side of the roof."
                        "I step out of the classroom and head up the stairs."
                        "Before reaching the final door, I wonder if I made the right decision."
                        "Ugh... It’s not like I can change it now anyway."
                        "I open the door and see Sakura standing on the edge of the roof. She can’t move freely, as some kind of mechanism is holding her in place."
                        "The moment our eyes meet, her expression changes drastically." 
                        "Her eyes widen as she understands what my presence means."

                        if offensive:
                            show sakura sad with dissolve
                            s "No. No. No!"
                            "Tears begin to stream down her face."
                            s "It wasn't me. It wasn't me!"
                            s "Why me? It was Kaori, not me."
                            s "I-I-I... You checked the dorm's cameras?"
                            u "..."
                            show sakura panick with dissolve
                            s "You did, right?"
                            u "Sakura, I-"
                            s "Shut up! Shut up! I don't want to die."
                            s "It... wasn't me. I promise."
                            s "..."
                            s "That's right, Kaori planned all of this."
                            s "You know it wasn’t me, and yet you're here. It’s all because of her."
                            u "It wasn’t her, Sakura. It was my decision, and mine alone."
                            s "Then why? You know it wasn't me."
                            s "Or maybe... you planned this too. Did you want to protect her."
                            u "That isn't true."
                            s "The why did you choose me!?"
                            i "[first_name] [last_name]..."
                            u "I'm sorry... Sakura."
                            s "No! It wasn't me."
                            s "I hate yo-"
                        elif normal:
                            show sakura sad with dissolve
                            s "No. No. No!"
                            "Tears begin to stream down her face."
                            s "It wasn't me. It wasn't me!"
                            s "Why me? It was Kaori, not me."
                            s "I-I-I... You checked the dorm's cameras?"
                            u "..."
                            s "You did, right?"
                            u "Sakura, I-"
                            s "Shut up! Shut up! I don't want to die."
                            s "It... wasn't me. I promise."
                            s "..."
                            show sakura panick with dissolve
                            s "That's right, Kaori planned all of this."
                            s "You know it wasn’t me, and yet you're here. It’s all because of her."
                            u "It wasn’t her, Sakura. It was my decision, and mine alone."
                            s "Then why? You told me you love me."
                            u "And I meant it."
                            s "Maybe... maybe I’m not the one you truly love. Maybe it’s Kaori."
                            u "Sakura, that's not-"
                            s "Then why did you choose me!"
                            s "Or maybe... you together planned all of this. You wanted to protect her."
                            u "That isn't true."
                            i "[first_name] [last_name]..."
                            u "I'm sorry... Sakura."
                            s "No! It wasn't me."
                            s "I hate yo-"


                        hide sakura with vpunch
                        "Before she can finish her sentence, the mechanism releases her."
                        "Unable to keep her balance, she falls from the four-story building."
                        "No sound escapes her mouth, as if she dies midair. Only the sound of her body hitting the ground is heard."
                        "..."
                        i "Gongratulations on the first case... Detective [last_name]."
                        "..."
                        u "Is... is this confirmation that I was right?"
                        i "Who knows. You may never know the truth."
                        u "..."
                        i "You're free to live as you did before."
                        u "...Yeah."
                        u "...I failed him once." 
                        u "And now I’ve done it again."

                        pause 1.0
                        scene black with fade
                        "Meanwhile..."
                        
                        pause 0.5
                        
                        i "An interesting choice he made."
                        show kaori normal with dissolve
                        k "Interesting indeed."
                        i "How do you feel?"
                        show kaori serious with dissolve
                        k "I'm not sure. I-I didn't want her to die."
                        k "And yet... deep down, I feel happy about the choice he made."
                        k "He chose me."
                        k "..."
                        show kaori happy with dissolve
                        k "Haha."
                        i "What's funny?"
                        show kaori normal with dissolve
                        k "It's nothing. I just realized something."
                        k "We both ended up killing for someone we love."
                        i "Do you think he feels the same way you do?"
                        k "Then why did he choose me?"
                        k "He had all the facts in his hands."
                        k "Everything pointed to me, and yet he chose Sakura… knowing it wasn’t her."
                        k "That’s more than just love."
                        i "..."
                        i "What do you plan to do next?"
                        k "Nothing. If you mean whether I’ll tell him the truth, I won’t."
                        k "You people are the only ones who know the whole truth."
                        i "Don't worry. You prepared a wonderful experience, one that will be remembered for quite some time."
                        i "And it was we who decided to play your game. You satisfied us enough."
                        i "You're free to live as you did before."
                        k "...I most definetely will."
                        hide kaori with dissolve

                        pause 1.0 
                        scene black with fade
                        "Two days later, the whole school is still talking about what happened."
                        "Naturally, a lot of eyes are on me. Different kinds of eyes."

                        pause 0.5
                        scene store_day with fade
                        show kaori normal with dissolve
                        k "...[first_name]"
                        k "[first_name]!"
                        u "Ugh..."
                        u "I'm sorry. I was lost in thoughts."
                        k "It’s okay. You’ll probably think about this for the rest of your life."
                        u "Yeah..."
                        u "Ugh... Do you think I made the right choice?"
                        k "Um... I don't think I'm the right person to ask this."
                        u "Heh. That's true."
                        k "But If you need me for anything else, I'll always be there to help you."
                        u "Thanks, Kaor-"
                        "Wait… hasn't she said something like that before? And what’s with her face today?"
                        "She's... beautiful. I can't take my eyes off her."
                        "What is this feeling... this urge?"
                        "I slowly reach for her hand and gently take it."
                        show kaori blush with dissolve
                        k "Hey! What are you-"
                        u "I'm sorry. I-I just..."
                        u "You don't like it?"
                        k "..."
                        k "No, I-It's not like that."
                        k "I-I like it."
                        pause 1.0
                        hide kaori with dissolve
                        scene black with fade
                        jump end_credits
                    "Return":
                        jump ending_choice


label end_credits:
    $ quick_menu = False
    scene black

    show text "{size=80}{color=#FFFFFF}THE END{/color}{/size}" at truecenter
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

    pause 0.5

    return

label timeup_ending:
    "Timer is up!"




    # "Was it Kaori? She lied to me about going into the store but instead passed by and followed Hiro. But why would she kill him? Was she angry because of what he was doing?"
    # "Was it Sakura? She was angry, that’s for sure. And her words… about wishing to kill him. But would someone who actually killed him say something like that?"
    # "I have a report to read. Maybe I should try to build a chain of what happened."
    # "Player chooses to kill Kaori."
    # "Beep!"
    # i "...Kaori. Interesting choice."
    # "I go upstairs and approach the door leading to the roof. I feel unsure about my decision. I really don’t want to open that door."
    # "Kaori… she’s someone precious to me. I never realized how much she cared about me."
    # "Maybe if I had noticed sooner, it wouldn’t have come to this. Hiro wouldn’t have died, and I…"
    # "…Tch. I only care about myself."
    # "I never even tried to understand her feelings. Was she scared? …Of course she was. She always hid her true feelings behind that smile."
    # "I open the door."
    # "I see Kaori standing on the edge of the roof. Some kind of mechanism is holding her in place, as if waiting to be activated."
    # k "[first_name]…"
    # "Beep!"
    # k "[first_name]. There is no turning back. You cannot escape this situation. Neither by running away nor changing your decision. Before Kaori Ito dies, you may have one last conversation."
    # "I walk closer to her."
    # k "[first_name]… That’s the choice I expected."
    # k "What are you…"
    # k "You love her, don’t you? I guess that’s your answer to my confession, haha."
    # k "…"
    # k "Did you really kill him?"
    # k "Does it matter anymore? It’s not like you can change the past. Oh… don’t be sad. Your life won’t change much. I wasn’t that important anyway—"
    # k "That’s not true!"
    # k "You were…"
    # k "My friend. My closest friend. It wasn’t Hiro… it was you. Only you."
    # u "And I’m sorry I realized it too late. If I hadn’t… then today wouldn’t have happ—"
    # k "[first_name]… I think it’s time to say goodbye. Don’t forget me, okay? At least for two years… haha."
    # i "Kaori Ito."
    # k "I love you, [first_name]. I love you so mu—"
    # "The mechanism activates before she can finish."
    # "She falls from the four-story building."
    # "Kaori dies."
    # "I can’t bring myself to leave the roof."
    # "Maybe because I know I’ll never come back here again."
    # "Did Kaori really kill Hiro? Was I wrong?"
    # "Those questions keep spinning in my head."
    # "I decide to go to Kaori’s dorm room. I don’t even know why. I just… haven’t been there in a long time."
    # "I stand in front of the girls’ dorm building. I’m not allowed to be here this late, but I don’t care."
    # "I go upstairs and open the door with the key Kaori once gave me."
    # "BEEP!"
    # i "[first_name]. You are violating the rules. You are not allowed to be here."
    # u "…I forgot you people had this perverted side. Even inside the girls’ dorm. Are you all insane?"
    # i "You chose this school yourself."
    # u "I wish I didn’t."
    # "I step inside her room. It’s surprisingly clean."
    # "I walk over to the sofa and sit down."
    # i "Initiating playback of the final message requested by Kaori Ito."
    # u "What—?"
    # k "Testing, testing. Is this working?"
    # k "Testing, testing. Is this working?"
    # k "[first_name]… if you’re hearing this, then I’m already dead."
    # k "There are 30 minutes left before your final decision. I decided to record this message."
    # k "You’re probably wondering… even now… which parts of what I said were truth, and which were lies."
    # k "Like you guessed, it was a perfect crime. The bridge is the perfect place to dispose of evidence. No cameras, easy escape."
    # k "But what if someone saw something?"
    # k "A normal person would report it and move on."
    # k "But someone obsessed… someone who truly cares… might stay silent."
    # k "They would try to protect that person instead."
    # k "So, when that person returned the next morning, they discovered something strange."
    # k "The culprit didn’t remember anything."
    # k "I don’t know how or why… but there were no signs they even knew what they had done."
    # k "I guess it was short-term memory loss. I read it could stem from extreme stress and chronic anxiety. I guess he wasn’t ready to kill someone."
    # k "Later, when the news of Hiro’s death spread, that person was genuinely shaken."
    # k "That’s when I decided to help them."
    # k "I called the school and reported Sakura… even though she had nothing to do with it."
    # k "I was ready to sacrifice anyone… as long as it wasn’t you."
    # k "But when I saw Sakura today… those eyes… she was innocent."
    # k "That’s when I decided to include myself."
    # k "To even the odds."
    # k "I lied. A lot."
    # k "You were so focused on finding the truth… and trying to save us…"
    # k "that you couldn’t even see something simple."
    # k "The hoodie."
    # k "Dark blue is for boys. Girls wear pink."
    # k "I was even wearing it this morning… when I walked to school with you."
#endregion

screen big_text(info):

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1700
        ysize 900
        padding (90, 140, 90, 120)
        
        viewport:
            scrollbars "vertical"
            mousewheel True

            text info size 28 color "#000000" outlines [(2, "#FFFFFF", 0, 0)]
        hbox:
            xalign 0.98

            textbutton "Close":
                action Return()

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


label riverbank_thinking:
    $ strangle = 0
    $ stab = 0
    $ gun = 0
    $ school = ""
    $ riverbank = ""
    $ unknown = ""
    $ message_place = ""
    $ message = ""

    label thinking:
        menu:
            "Riverbank":
                $ riverbank = "Riverbank"
                "How did he die?"
                menu:
                    "Strangulation":
                        $ strangle = 1
                        $ message_place = message_display_place(school, riverbank, unknown)
                        $ message = message_display(strangle, stab, gun)
                        "[message_place]"
                        "[message]"
                        jump riverbank_thinking
                    "Stabbing":
                        $ stab = 1
                        $ message_place = message_display_place(school, riverbank, unknown)
                        $ message = message_display(strangle, stab, gun)
                        "[message_place]"
                        "[message]"
                        jump riverbank_thinking
                    "Gunshooting":
                        $ gun = 1
                        $ message_place = message_display_place(school, riverbank, unknown)
                        $ message = message_display(strangle, stab, gun)
                        "[message_place]"
                        "[message]"
                        jump riverbank_thinking

            "Near School":
                $ school = "School"
                "How did he die?"
                menu:
                    "Strangulation":
                        $ strangle = 1
                        $ message_place = message_display_place(school, riverbank, unknown)
                        $ message = message_display(strangle, stab, gun)
                        "[message_place]"
                        "[message]"
                        jump riverbank_thinking
                    "Stabbing":
                        $ stab = 1
                        $ message_place = message_display_place(school, riverbank, unknown)
                        $ message = message_display(strangle, stab, gun)
                        "[message_place]"
                        "[message]"
                        jump riverbank_thinking
                    "Gunshooting":
                        $ gun = 1
                        $ message_place = message_display_place(school, riverbank, unknown)
                        $ message = message_display(strangle, stab, gun)
                        "[message_place]"
                        "[message]"
                        jump riverbank_thinking
            "Unknown":
                $ unknown = "Unknown"
                "How did he die?"
                menu:
                    "Strangulation":
                        $ strangle = 1
                        $ message_place = message_display_place(school, riverbank, unknown)
                        $ message = message_display(strangle, stab, gun)
                        "[message_place]"
                        "[message]"
                        return
                    "Stabbing":
                        $ stab = 1
                        $ message_place = message_display_place(school, riverbank, unknown)
                        $ message = message_display(strangle, stab, gun)
                        "[message_place]"
                        "[message]"
                        jump riverbank_thinking
                    "Gunshooting":
                        $ gun = 1
                        $ message_place = message_display_place(school, riverbank, unknown)
                        $ message = message_display(strangle, stab, gun)
                        "[message_place]"
                        "[message]"
                        jump riverbank_thinking

    init python:
        def message_display_place(school, riverbank, unknown):
            if school == "School":
                return "Hiro couldn't have been killed near the school. After his conversation with Sakura, he headed toward the boys' dorm."
            elif riverbank == "Riverbank":
                return "The report says riverbank, but that doesn't make sense."
            elif unknown == "Unknown":
                return "That's right! The riverbank wasn't the place of death. It was where the body was found."
            return ""

        def message_display(strangle, stab, gun):
            if strangle == 1:
                return "That's right! His body's condition suggests that strangulation was the cause of death."
            elif stab == 1:
                return "No wounds or signs of stabbing were found on his body. It wasn't a stabbing."
            elif gun == 1:
                return "Hiro wasn't killed with a gun. There is no evidence pointing to that."

label puzzle_start:
    default remaining_steps = [
        "Skin appears pale and wrinkled.",
        "Bruising around his neck.",
        "His blood under his fingernails.",
    ]
    "Which details were actually found on Hiro's body?"

    label body_loop:
        menu:
            "Signs of struggle on the arms.":
                "No... there were no signs of struggle mentioned in the report."
                jump body_loop

            "Stab wound":
                "No... there was no stab wound mentioned in the report."
                jump body_loop

            "Skin appears pale and wrinkled." if "Skin appears pale and wrinkled." in remaining_steps:
                "It wasn't mentioned in the report."
                "But his skin most likely looked pale and wrinkled because the body was in the water for quite some time."
                $ remaining_steps.remove("Skin appears pale and wrinkled.")
                jump body_loop

            "His blood under his fingernails." if "His blood under his fingernails." in remaining_steps:
                "Correct. That suggests he may have struggled while fighting for his life."
                $ remaining_steps.remove("His blood under his fingernails.")
                jump body_loop

            "Bruising on the ribs.":
                "No... bruising on the ribs was not part of the report."
                jump body_loop

            "Bruising around his neck." if "Bruising around his neck." in remaining_steps:
                "Correct. This was mentioned in the report."
                $ remaining_steps.remove("Bruising around his neck.")
                jump body_loop

            "End":
                if not remaining_steps:
                    jump puzzle_success
                else:
                    "Not yet. I have to think about the details before moving forward."
                    jump body_loop

    label puzzle_success:

        "The important details are the blood under his fingernails, the water exposure, and the injuries around his neck."
        return


# xpos 0.15
# xpos 0.65