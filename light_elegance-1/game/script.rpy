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

image sakura normal = Transform("images/Chie_Outfit_Pack_1/s_smile.png", zoom=0.35, ypos=1.5)
image sakura frown = Transform("images/Chie_Outfit_Pack_1/s_frown.png", zoom=0.35, ypos=1.5 )
image sakura embarassed = Transform("images/Chie_Outfit_Pack_1/s_open.png", zoom=0.35, ypos=1.5 )
image sakura serious = Transform("images/Chie_Outfit_Pack_1/s_closed_frown.png", zoom=0.35, ypos=1.5)
image sakura frown blush = Transform("images/Chie_Outfit_Pack_1/Chie_SummerUni_Frown_Blush.png", zoom=0.35, ypos=1.5)
image sakura normal blush = Transform("images/Chie_Outfit_Pack_1/Chie_SummerUni_Smile_Blush.png", zoom=0.35, ypos=1.5)


image kaori normal = Transform("images/Miki Outfit Pack 1/Miki Winter Uniform/Miki_A_WinterUniform_Smile.png", zoom=0.35, ypos=1.5)
image kaori frown = Transform("images/Miki Outfit Pack 1/Miki Winter Uniform/Miki_A_WinterUniform_Frown.png", zoom=0.35, ypos=1.5)
image kaori frown closed = Transform("images/Miki Outfit Pack 1/Miki Winter Uniform/Miki_A_WinterUniform_Closed_Frown.png", zoom=0.35, ypos=1.5)
image kaori happy closed = Transform("images/Miki Outfit Pack 1/Miki Winter Uniform/Miki_A_WinterUniform_Closed_Open_Blush.png", zoom=0.35, ypos=1.5)
image kaori happy = Transform("images/Miki Outfit Pack 1/Miki Winter Uniform/Miki_A_WinterUniform_Open.png", zoom=0.35, ypos=1.5)
image kaori frown closed blush = Transform("images/Miki Outfit Pack 1/Miki Winter Uniform/Miki_A_WinterUniform_Closed_Frown_Blush.png", zoom=0.35, ypos=1.5)
image kaori frown open blush = Transform("images/Miki Outfit Pack 1/Miki Winter Uniform/Miki_A_WinterUniform_Frown_Blush.png", zoom=0.35, ypos=1.5)
image kaori normal blush = Transform("images/Miki Outfit Pack 1/Miki Winter Uniform/Miki_A_WinterUniform_Smile_Blush.png", zoom=0.35, ypos=1.5)

image cashier normal = Transform("images/cashier.png",  ypos=1.4)

default time_left = 300
# 600

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
    xpos 0.55
    ypos 0.09
    
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
    "BEEP! BEEP! BEEP!"
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
    i "Hey! Are you listening, or are you still half asleep?"
    u "I'm listening."
    i "Great. Please confirm your understanding by stating your first and last name."

    label ask_name:
        $ first_name = renpy.input("Enter the first name: ", length=32).strip()
        if first_name == "":
            "First name is required."
            jump ask_name
        jump last_name

    label last_name:
        $ last_name = renpy.input("Enter the last name: ", length=32).strip()
        if last_name == "":
            "Last name is required."
            jump last_name


    i "Thank you for your confirmation."
    i "[first_name] [last_name], I wish you luck."

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
    with fade

    pause 1.0
    "On my way to school, I see a girl running toward me. She’s wearing a school uniform, holding a pink hoodie in her hands."
    "She waves one hand in the air, calling out to me from a distance. I can’t really hear her, but I can already guess who it is."
    show kaori happy
    with dissolve

    q "Hey [first_name]! I've been calling you forever! Why didn't you wait for me?"
    "This girl is Kaori and she’s my childhood friend. Our parents work together, and somewhere along the way, we naturally became close."
    "Always smile on her face. I even think I’ve never seen her sad or devastated before. Even today..."
    k "It's been a while. How are you?"
    u "I'm fine... You seem awfully cheerful for a day like this."
    k "Well... My friend died, and the whole school sees me as one of the main suspects."
    k "Most people would probably be terrified right now... But not me."

    show kaori happy closed with dissolve
    k "After all, we've known each other for a long time. And I know you're capable of finding the real culprit."
    k "So, I'm not worried."
    u "You sure are confident about me. But don’t expect me to go easy on you just because we’re friends."
    k "Haha... Don’t worry. I know how serious you are when it comes to this."
    u "Are you really okay? He was your friend too."

    show kaori frown with dissolve

    k "Yeah... Honestly, I’m more worried about you. A lot has happened these past few days."
    k "I don’t think anyone could handle all of this alone."
    k "So If you need anything... talk to me. I’ll always be there for you."
    u "Thanks... really, Kaori."

    hide kaori frown



    scene front_school_day
    "As we get close to the school, I spot another classmate waiting near the front entrance."
    "That is Sakura. The person I... I feel something deeper for than friendship."

    show sakura normal with dissolve
    s "Hello, [first_name]."
    s "You both seem... happy this morning. Walking to school together and all."

    show sakura frown with dissolve
    s "You only met him because of today's situation, right Kaori? You two never walk together."

    show sakura frown:
        linear 0.2 xpos 0.25 
    
    show kaori frown at right_kaori
    with dissolve


    k "N...No, that's not true"
    k "We're childhood friends. I don't think it's strange for friends to walk to school together."

    k "What about you? Are you scared he’s going to choose you today? Is that why you came out to meet him?"

    show sakura embarassed with dissolve
    s "No... I’m not. Why would I be... I haven’t done anything wrong."

    "Right... the two of them weren't on good terms. To be honest, I never knew why."
    u "Let's calm down everyone..."
    "An awkward silence settles between us. Still, it feels like Sakura came here for a reason."
    u "You wanted to tell me something, Sakura?"

    show sakura serious with dissolve
    s "Mmm... yes, right."
    s "I’m here to explain the rules the school has set for today."

    show sakura frown with dissolve
    s "First, Kaori and I are not allowed speak to each other once we enter the building."

    show kaori normal with dissolve
    k "Phew... I wasn't planning to."
    u "Kaori..."
    k "...What?"
    s "You’ve already been told everything else, haven’t you?"
    u "Yes, I were."
    s "Oh... and the case report, along with all information found is on your desk."

    show sakura normal with dissolve
    s "That's everything from me." 
    s "And [first_name]... I hope you’ll make a right decision."
    hide kaori frown with dissolve
    hide sakura normal with dissolve
    "Sakura turns and walks into the school. Kaori follows after her, but pauses and glances back at me."
    show kaori happy with dissolve
    k "Just wait and see, [first_name]. I'll prove I had nothing to do with it, haha."
    hide kaori normal with dissolve

    "Kaori is different from others. Even though her life may be on the line, she wears a pure smile, as if none of this frightens her at all."
    "Sakura though, seems anxious. Her eyes are full of sadness, even when she tries to hide that."

    scene classroom with fade

    "I walk into the classroom, and every student’s gaze is fixed on me. Well... it’s different from what usually happens."
    "I make my way to my desk, and just like Sakura mentioned, the report case is already there."

    jump test

    return
#endregion

#region Choice System
label test:
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
    scene classroom with fade

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
    scene yard with fade
    u "Hey, Kaori."
    k "..."
    u "...Kaori"
    k "..."
    u "Kaori!"
    show kaori normal with dissolve
    "I raise my voice a little. She flinches slightly"
    show kaori happy with dissolve
    k "[first_name]? Oh- sorry, I didn’t notice you at all."
    u "Yeah... you really need to start to take this serious."
    u "This isn’t exactly a normal situation. Your life’s kind of on the line here."
    show kaori frown with dissolve
    k "I’m sorry..."
    if talked_sakura:
        k "Wait, why I’m the one apologizing. Shouldn’t you be apologizing for not coming to me first!?"
        u "Why would I do that? I had my reasons."
        u "Besides… what’s this all about? The way you’re reacting, are you actually jealous or something?"
        show kaori normal blush with dissolve
        k "No, I’m not... I mean- maybe, just a little."
        u "What’s with you today?"
        k "Hm..."
        show kaori frown closed blush with dissolve
        "She turns her head away."
        "Sometimes, I really don’t understand her."
        u "Okay, look. You’re not the one I’m most suspicious of. "
        u "Sakura... had more strange behaviour that night. So, can we just start the questioning."
        show kaori frown open blush with dissolve
        k "Okay... geez, I was just joking. Don’t be so serious."
        "This girl."
    else:
        "Something else."
    "...Alright. What will I ask first?"
    label kaori_questions:

        if asked_q1 and asked_q2:
            scene black with fade
            "I think I’ve got everything I can here. I need to check the riverbank myself."
            "The break ends and I return to the classroom."
            "During the class I report everything I found out till now."
            jump test
            return
        menu:
            "What were you doing the night Hiro died?" if not asked_q1:
                if talked_sakura:
                    show kaori normal with dissolve
                    u "Simple question. What were you doing around 11PM that night?"
                    k "I went to the convenience store, the one we passed this morning."
                    u "Huh? That late? Why?"
                    k "My charger suddenly broke, so I had to get a new one. I can’t go to school without my phone."
                    u "On your way there, did you see someone wearing dark blue school hoodie?"
                    k "Oh..."
                    u "Oh?"
                    k "What about them?"
                    u "Sakura saw someone heading toward the store you were going to."
                    k "I think I do know something about that person."
                    "Nice! Thanks, Sakura"
                    show kaori happy with dissolve
                    k "It was me. Haha..."
                    u "..."
                    u "...Damn it."
                    k "Was that who you thought the real culprit was?"
                    u "Yes. It was."
                    k "Hahaha... sorry for ruining that."
                    u "Don’t be. Because now, you’re just as suspicious as Sakura was before this conversation started."
                    show kaori normal with dissolve
                    k "Oh..."
                    "Damn it. Damn it."
                    u "How did you pass her without saying a word? It’s not like you."
                    k "I was wearing headphones, so I wasn’t really paying attention. It was dark too."
                    u "Did you notice anything unusual that night?"
                    show kaori frown with dissolve
                    k "...I don’t think so."
                    u "What about Hiro? He was heading the same way."
                    k "...Hiro?... I didn't see him."
                    "It’s as if he vanished. Neither of them saw him. And yet, they both were headed the same direction."
                    "Is one of them lying? Or am I looking at the wrong suspects?"
                else:
                    "Something"
                $ asked_q1 = True
                jump kaori_questions
            "What’s wrong with you and Sakura" if not asked_q2 and asked_q1:
                if talked_sakura:
                    u "I wanted to ask about Sakura. You two don’t get along very well. Why?"
                    show kaori normal with dissolve
                    k "Didn’t she already tell you."
                    u "She did, but I want to hear your version."
                    k "I don’t really hate her. She’s actually pretty nice."
                    k "It just like she said. We both like the same person, haha."
                    u "Kaori... are you serious right now? Don’t tell me there’s actually someone you like?"
                    show kaori frown with dissolve
                    k "I do... Is that really something extraordinary."
                    u "In your case? Yeah, a little. Well... I’m more worried about that person, haha."
                    k "Hey! That’s mean, you know! And what about you?"
                    k "Aren’t you worried that someone might take your precious Sakura from you."
                    u "What are you... where is that coming from?"
                    show kaori frown closed with dissolve
                    k "Don’t play dumb, I’m not Sakura. "
                    k "I’ve known you for a long time. I see your eyes when you look at her. The way you act around her. "
                    k "Like a little boy, who seeks for a candy."
                    u "..."
                    u "Is it really that obvious?"
                    show kaori normal with dissolve
                    k "Obvious? Please. The whole class already knows that."
                    u "The whole..."
                    "I lower my head in embarrassment"
                    show kaori frown with dissolve
                    k "..."
                    u "..."
                    "An awkward silence settles between us."
                    show kaori frown open blush with dissolve
                    k "I'm sorry, I shouldn't have talked to you like that."
                    u "No, I should be the one apologizing. I didn’t know your feelings were real."
                    k "..."
                    k "It’s you."
                    u "Me? What are you talking about?"
                    k "The person we both like."
                    u "..."
                    u "Kaori, stop. This isn’t a good time for jokes."
                    show kaori frown closed blush with dissolve
                    k "I’m... not joking."
                    "Her voice trembles. I lift my head and see her looking awkwardly away, her cheeks slightly red. I’ve never seen this image on her face before."
                    u "What?! What d-d-do you mean?"
                    show kaori frown open blush with dissolve
                    k "What do you mean what do I mean! Don’t make me say it again."
                    k "Yes, I l-like you, I’ve liked you for quite a while now. Happy?"
                    "What should I say. I’m happy Sakura feels that way, but Kaori."
                    k "Why aren’t you saying anything? Just say something."
                    u "I'm sorry... I just don't know what to say! You said it very suddenly!"
                    k "I-I... Ugh."
                    u "I’m happy, I really am."
                    k "Probably just about Sakura, right?"
                    u "N-No, about you too. It’s just... you know how I feel."
                    k "That’s fine. I already knew how this would end. I just wanted to tell you today. Because, you know, If not today, then when?"
                    u "Kaori... I’m sorry."
                    k "I said it’s fine! Do you have any more questions?"
                    u "No... I don’t."
                    k "Then I’ll go."
                    "She gets up and rapidly leaves the place."
                    hide kaori frown open blush with dissolve
                else:
                    "Something."
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
    scene cafeteria_day with fade

    u "Hey... Sakura."
    show sakura normal with dissolve
    s "Oh... [first_name], you’re here."
    s "You came to me first. I thought you’d go to Kaori first."
    "She’s... cute."
    u "I mean... yeah. I just thought it made more sense to start here."
    "When I talk to her when no one is around, I feel nervous. I need to calm down."
    s "You look kind of nervous... first case?"
    u "Hm... yeah, something like that. "
    "It’s not just that though."
    u "It's obvious why I’m here?"
    show sakura frown with dissolve
    s "That’s right. By the way, are you okay? I didn’t get to ask you earlier."
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
            hide sakura frown with dissolve
            pause 0.5
            scene black with fade
            "Based on what she said, it seems it wasn’t her. Still, I’ll need to confirm it at the convenience store and the dorm when I get the chance."
            "The break ends and I return to the classroom."
            "During the class I report everything I found out till now."
            jump test
            return
        menu:
            "What were you doing the night Hiro died?" if not asked_qq1:
                if talked_kaori:
                    "Something based on Kaori"
                else:
                    u "Let’s start with a simple question. What were you doing around 11PM that night?"
                    s "I... I was in my dorm. Getting ready to sleep. You know, shower and... stuff."
                    "Shower... No, no what am I even thinking about."
                    "She's lying. Is she scared it could rocket back at her."
                    u "Sakura... Do you know why you’re on the suspect list?"
                    show sakura frown with dissolve
                    s "Honestly, I’m quite puzzled by this question myself."
                    u "According to witness, you were the last person seen with Hiro that day. Around 10PM to that. Right before his death."
                    "Sakura lowers her head"
                    s "That’s not..."
                    u "It was also confirmed by the school’s camera footage."
                    s "..."
                    "Her expression changes drastically."
                    u "Why would you lie Sakura? Were you involved?"
                    s "I thought no one saw us that night. So, I decided to hide it."
                    u "Why? Did you kill him, Sakura?"
                    s "No, I didn’t... I didn’t...!"
                    "Her voice trembles. Her hands begin to shake."
                    s "‘sniff, sniff’"
                    s "Please... you have to believe me. We just talked... then he went his way."
                    s "I left a few minutes later. I had nothing to do with it. "
                    "I take a napkin from my pocket and hand it over to her."
                    u "Talked about what?"
                    s "I... I don't want to talk about it. It’s something I’d rather keep to myself."
                    u "Why?"
                    s "It's... personal."
                    u "Personal enough to stay silent. Even today?"
                    s "Y-Yes..."
                    u "...Alright."
                    u "From now on, all I want is the truth. Do you understand that?"
                    "My heart is about to explode. I feel confused seeing her the way she is right now."
                    s "Yes... I understand."

                $ asked_qq1 = True
                jump sakura_questions
            "What’s wrong with you and Kaori?" if not asked_qq2:
                    u "You and Kaori don’t seem to get along. I’ve never questioned this, but now I think it’s time to know the truth."
                    s "That’s true."
                    u "Why? Something must have happened."
                    s "I just... hate her. She’s annoying, narcissistic. Always acting like she’s better than everyone."
                    u "That doesn’t come out of nowhere."
                    show sakura normal blush with dissolve
                    s "It's quite embarrassing to say... haha."
                    s "You see... it happens that we both like the same person."
                    u "What?!"
                    "My voice comes out louder than I expected. Sakura flinches slightly."
                    "Kaori likes someone. That girl can’t like anyone but herself. Ha... Is she doing this on purpose? Yeah... hundred percent."
                    "Also to think that Sakura already likes someone... and it’s not me."
                    show sakura frown blush with dissolve
                    s "Something happened, [first_name]? Your face suddenly went pale."
                    u "No, no, I’m just surprised. Do you mind telling me who it is?"
                    s "..."
                    show sakura embarassed with dissolve
                    s "I don’t want to. It doesn’t have anything to do with the case anyway. And I’m not required to tell you, ahem..."
                    u "...Is it Hiro?"
                    s "Hiro? No, it’s not him. Don’t worry. He has nothing to do with this."
                    u "That’s... good. I mean... it’s nothing."
                    $ asked_qq2 = True
                    jump sakura_questions
            "Something unusual happened that night?" if not asked_qq3 and asked_qq1:

                    u "Let’s talk more about that night."
                    show sakura normal with dissolve
                    s "Alright..."
                    u "You said you went the same way a few minutes later after your conversation ended. "
                    s "I didn’t say that."
                    u "The report did. Why did you go that way? The women’s dorm is in the opposite direction."
                    s "I had to stop by the convenience store."
                    u "Why? What's the reason?"
                    s "I needed to buy a few things for myself."
                    u "Weren’t you scared to go there alone?"
                    s "Why would I be? We live in a quiet area."
                    "Not so quiet as it appears."
                    u "Did you see anything unusual? Anyone suspicious?"
                    show sakura frown with dissolve
                    s "I don’t think so... Hm...Wait."
                    s "When I was walking, a person passed me. They were wearing a dark blue school hoodie."
                    u "Did you see their face? Anything else?"
                    s "It was too dark. I couldn’t see anything. But their steps were fast... like they were in a hurry."
                    u "What happened after that?"
                    s "I don't know where that person went. Once I reached the convenience store, I couldn’t see them anymore."
                    u "You bought what you needed. What happened next?"
                    s "I went back to my dorm room."
                    u "Can anyone confirm that?"
                    s "I'm sure the dorm's cameras would have recorded me."
                    $ asked_qq3 = True
                    jump sakura_questions
#endregion

#region Riverbank
label riverbank:
    pause 1.0
    scene bus with fade
    "Riverbank isn’t far from the school, but getting there requires taking a bus."
    "When I arrive, there’s obviously nothing suspicious left at the scene. Still, I never really expected to find anything useful there."
    "What bothers me is why Hiro’s body was found here in the first place. He obviously wasn’t killed at the riverbank."
    "More likely, his body was thrown into the river somewhere upstream, and the current carried it here."
    scene city with fade
    "The easiest way to do that would be from one of the bridges further along the river. I follow the upstream."
    "About fifteen minutes later, I spot a familiar bridge. I use it every day on my way to the dorm. Hiro used it too."
    "A bridge is almost the perfect place to commit a murder. No cameras. Water underneath. A current strong enough to wash away evidence, maybe even fingerprints."
    scene store_afternoon with fade
    "And, almost mockingly, there’s a convenience store just fifty meters before the bridge."
    "The same store Kaori said she was going to that night. The same place Sakura mentioned before returning to her dorm."

    "Right before reaching the store, I notice Kaori leaving. She seems in a hurry, looking around as she heads back toward the school."

    "I head inside"
    show cashier normal with dissolve 
    u "Good afternoon. I have some questions to ask."
    c "Huh? Again? What do you want?"
    u "Again? What do you mean?"
    c "Some kind of girl was here before you. She gave me a hard time."
    u "A hard time? What did she ask?"
    c "She wanted to... Wait, who are you?"
    u "Oh... My name is [first_name] [last_name]."
    u "I’m investigating the case assigned by the school."
    c "From that academy? Bastards. But they’re scary. Can’t really do anything about it."
    u "So, what did she ask?"
    c "She wanted to look at camera footage."
    u "You let her?"
    c "Obviously not! They told me to only show it if a special card is presented by a student."
    "Special card? Oh... It must be the one inside the report. I put it in my wallet."
    u "Here. May I see the footage, please?"
    c "Hmm... Alright. Come with me."
    hide cashier normal with dissolve
    "Did Kaori want to delete the data? I’m curious what I’ll see."
    "We step into the security room."

    c "Please be careful. Last time, a boy from your academy deleted a week of footage."
    u "Sure..."
    
    "I open the footage from the night Hiro was killed. On the screen, I see Hiro walking past the store. Then, a person in a dark hoodie passes by. And after that... Sakura enters the store."
    "She picks up a few items and leaves, heading back toward the school."
    "I guess she wasn’t lying. But what about Kaori? She passed the store and followed Hiro."
    "I scroll through twenty more minutes of footage. Kaori returns to the store, holding the hoodie in her hands. She looks sweaty, like she’s been running."

    "Does that mean Kaori lied? Did she kill him? If she did, why? As far as I know, there was no problem between her and Hiro."
    scene classroom with fade
    "And if Kaori is guilty... it’s not like I have confirmation. I need to talk to Sakura one more time. I need to know what they talked about. It might be the key."
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
    show sakura frown with dissolve
    s "..."
    u "I need that piece of information."
    show sakura embarassed with dissolve
    s "Not very comfortable to say, but..."
    s "I confessed to him... that I... that I liked him."
    "Confessed…"
    "It seems like I won’t get an information without bringing up what Kaori told me."
    label choice:
        menu:
            "Be Offensive":
                u "(Whisper) Damn it… "
                show sakura frown with dissolve
                s "I’m sorry?"
                "I don’t really want to do this. It might destroy our relationship. But what choice do I have?"
                "I stand up and start pacing."
                u "Look, Sakura. I don't have much time right now. I don't need your lies."
                show sakura embarassed with dissolve
                s "B-But I'm telling the truth. Why would I lie?"
                u "I'm asking myself the same thing. Why would you?"
                s "I- just ask my friends... right, my friends. I’m sure they’ll confirm it."
                u "Your friends? What friends?"
                show sakura serious with dissolve
                s "That's... oh, right. Ask Himari. She'll definetely tell you."
                u "Oh... don’t bullshit me. Are you talking about Himari? The one who talks behind your back the moment she gets the chance?"
                show sakura frown with dissolve
                s "That's not true. She's not like-"
                u "The people around you only care about their own future. They don’t care about you or your feelings."
                u "You still don't understand it, do you?"
                u "They’re circling around you like dogs, hoping you’ll be useful to them at some point."
                u "That’s the kind of school we’re in."
                s "[first_name]? Why are you…"
                u "Do you even understand what’s happening right now? I’m one break away from deciding who dies." 
                u "I don’t care about you or what you feel toward me."
                show sakura embarassed with dissolve
                s "What's that supposed to mean?"
                u "I know everything..."
                u "About your feelings. Kaori told me."
                s "W-What do you mean?"
                u "What you feel toward me. You love me, don’t you?"
                s "I-I... Did Kaori tell you that?"
                u "She did. And your face confirms it well enough."
                show sakura normal blush with dissolve
                s "[first_name], I-I..."
                u "Whether it’s you or Kaori, I’m ready to end either of you."
                s "It’s not like you… You’re not thinking clearly."
                u "Oh… believe me, I’m perfectly fine. This damn school put me in this position, so I don’t care anymore."
                u "Hiro... Hiro didn’t deserve to die."
                show sakura frown with dissolve
                s "..."
                s "Hiro didn’t deserve to die?"
                s "That scumbag?"
                u "What's that suppo-?"
                s "It seems you know nothing about him after all."
                s "That bastard was someone all the girls at this school were afraid of."
                s "I don’t know how, but he had tons of images on his phone, different kinds, which he used to blackmail us."
                show sakura serious with dissolve
                s "And that night... I was going to be his next target."
                u "What are you...?"
                s "I never intended to tell you this. I wanted to keep you away from all of it."
                show sakura frown with dissolve
                s "He was the only person you saw as a friend."
                s "I wanted to deal with it myself. But then… then he died."
                s "And you know what? I was happy."
                s "I genuinely felt relieved."
                s "He deserved it, and not because of me, but because of all the girls he hurt."
                s "I just wish I had been the one who killed that piece of trash."
                s "And you… you’re different from him. I hope you're like this because of today."
                s "Because if not..."
                s "...Damn it. "
                s "I imagined my confession would be different."
                s "..."
                s "...I’ll go. I don't have anything else to say."
                "She stands up and leaves."
                hide sakura frown with dissolve
                $ offensive = True
            "Be Normal":
                u "(Whisper) Damn it..."
                s "I'm sorry."
                "I need to calm down. I don’t want to handle this the wrong way."
                u "Sakura, I need to know the truth. The whole truth."
                u "Because I’m not buying that “confessed” story."
                s "I-I’ve been telling the truth..."
                u "I know. Or at least... I want to believe that."
                u "But, I don't have much time."
                u "And I don’t want to accuse you without understanding what really happened."
                s "Why are you... being like this?"
                u "Because I don't want to make the wrong choice. Not when it comes to you."
                s "Me? What's so speacial about me?"
                u "You're matter to me."
                s "M-Matter?"
                u "You may not realize it, but I look at you whenever I get the chance."
                u "And when I can, I try to spend time with you."
                s "[first_name]... Are you saying that you..."
                u "Yes... I like you."
                s "I-I'm...."
                "She starts to cry."
                s "I'm so happy... I'm so happy you said that."
                s "I love you too... [first_name]. I love you so much."
                "I take out a napkin and give it to her."
                s "I'm sorry. I shouldn't-"
                u "That's okay."
                s "..."
                "A minute passes before she calms down."
                u "You don't need to force yourself."
                u "But if there is something you're hiding... I need to know."
                s "I'll tell you."
                s "That night... I knew Hiro would be there."
                s "I'm sorry to say this, but Hiro wasn't a good person."
                u "What do you mean."
                s "A lot of girls were hurt because of him."
                s "I don't know how, but he had a lot of images, that... things he used to blackmail us."
                s "And I... was going to be his next target."
                s "I never wanted to tell you this. He was your friend. I didn't want to hurt you."
                u "..."
                u "That's okay. And I'm sorry for what he did. I-"
                s "Why are you apologizing. You're not him, I know that. You're different."
                u "..."
                u "Thanks, Sakura." 
                u "You should go. I need to talk to Kaori."
                s "Sure... See you later."
                "She stands up and leaves."
                $ normal = True
    
    if offensive:
        "Ugh... At some point, I forgot I was acting. Part of what I said came straight from my heart."
        u "Huh... different. Am I really that different?"
        "I knew about Hiro all along. What he was doing. I wonder if he ever realized that."
        "He wasn’t always like that. This school changed him, that’s for sure."
        "No one understood me better than him. I was scared that without him, there would be no one left for me."
        "Tears start to fall."
        "Damn it. Why am I crying? What’s wrong with me? Am I missing him? Shouldn't I feel the same as Sakura?"
        "What a pathetic person I am."
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
        show kaori frown with dissolve
        k "Hm? What happened? Your eyes… they’re red."
        u "Nothing in particular."
        k "Was it Sakura? Did she reject you or something? I should go talk to her and-"
        "She starts to stand"
        u "Kaori..."
        u "Stop it. Don’t you have anything else to think about?"
        k "I do. But I’m your friend... and I l-like you too. So it’s normal to worry about you."
        u "I'm fine. Don't worry about me."
        k "Good. But you can talk to me if something’s wrong. Okay?"
        u "Talk? You lied to me. Remember?"
        u "I checked the footage you wanted to delete. You never went inside the store. Not until twenty minutes later, after you followed Hiro." 
        u "Care to explain?"
    elif normal:
        u "Huh... different. Am I really that different?"
        "I knew about Hiro all along. What he was doing. I wonder if he ever realized that."
        "He wasn’t always like that. This school changed him, that’s for sure."
        "No one understood me better than him. I was scared that without him, there would be no one left for me."
        "And I didn’t stop him. He even hurt Sakura. What am I supposed to do now?"
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
        show kaori frown with dissolve

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
    k "What kind of person doesn’t realize their best friend already knew everything?"
    k "What kind of person thinks their best friend is that blind?"
    u "How-"
    k "Oh, it was obvious. Remember, I've known you for a long time."
    k "Nothing escapes your eyes... unless you choose not to see it." 
    k "...And you never did anything to stop it. Kind of disappointing."
    k "But I understand you. I do..." 
    k "After all, he wasn’t always like that. There was a part of you that still hoped he’d change."
    k "But then I overheard his conversation with Sakura."
    k "And I couldn't hold myself back anymore."
    k "God... you’ve never seen him like that. That vicious smile of his. I’ll never forget it."
    k "And that girl... still acting like she didn’t matter to anyone. Thinking about others while being blackmailed..."
    k "..."
    k "She’s a good person. Better than me, that’s for sure."
    "She stands up, preparing to leave."
    u "...Kaori?"

    k "[first_name]... I'm sorry."
    k "..."
    k "For putting you in this position."

    u "Kaori! What's that supposed to mean?"
    hide kaori frown with dissolve
    "BEEP! BEEP! BEEP! BEEP! BEEP!"
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
                        
                        if offensive:
                            i "You have made your decision. Please proceed to the west side of the roof."
                            "I step out of the classroom and head up the stairs."
                            "Before reaching the final door, I wonder if I made the right decision."
                            "Ugh... It’s not like I can change it now anyway."

                            "I open the door and see Sakura standing on the edge of the roof. She can’t move freely, as some kind of mechanism is holding her in place."
                            "The moment our eyes meet, her expression changes drastically." 
                            "Her eyes widen as she understands what my presence means."
                            s "No. No. No!"
                            "Tears begin to stream down her face."
                            s "It wasn't me. It wasn't me!"
                            s "Why me? It was Kaori, not me."
                            s "I-I-I... You checked the dorm's cameras?"
                            u "..."
                            s "You did, right?"
                            u "Sakura, I-"
                            i "Sakura Sato. The time is-"
                            s "Shut up! Shut up! I don't want to die."
                            s "It... wasn't me."
                            s "..."
                            s "It's because of Kaori. That's right, she convinced you it was me."
                            s "You know it wasn’t me, and yet you still came here. It’s all because of her."
                            u "It wasn’t her, Sakura. It was my decision, and mine alone."
                            s "Then why? Shouldn’t you make your choice based on facts?"
                            s "You know I love you. I’d never kill him. I would never hurt you."
                            i "[first_name] [last_name]..."
                            u "I'm sorry... Sakura."
                            s "No! No! It wasn't m-"
                            "Before she can finish her sentence, the mechanism releases her."
                            "Unable to keep her balance, she falls from the four-story building."
                            "No sound escapes her mouth, as if she dies midair. Only the sound of her body hitting the ground is heard."
                            "..."
                            i "Good job... Detective [last_name]."
                            "..."
                            u "Is-Is this confirmation that I was right?"
                            i "Who knows. You may never know the truth."
                            u "..."
                            u "...I failed him once." 
                            u "And now I’ve done it again."
                        elif normal:
                            "Yet to be written."

                        pause 1.0
                        scene black with fade
                        "Meanwhile..."
                        
                        pause 0.5
                        
                        i "An interesting choice he made."
                        k "Interesting indeed."
                        i "How do you feel?"
                        k "Conflicted. I didn't want her to die."
                        k "And yet... deep down, I feel happy about the choice he made."
                        k "He chose me."
                        k "Haha."
                        i "What's funny?"
                        k "It's nothing. I just realized something."
                        k "We both ended up killing for someone we love."
                        i "Do you think he feels the same way you do?"
                        k "Then why did he choose me?"
                        k "He had all the facts in his hands."
                        k "Everything pointed to me, and yet he chose Sakura… knowing it wasn’t her."
                        k "That’s more than love."
                        i "..."
                        i "What do you plan to do next?"
                        k "Nothing. If you mean whether I’ll tell him the truth, I won’t."
                        k "You people are the only ones who know the whole truth. I hope you won’t tell him either."
                        i "Don't worry. You prepared a wonderful theatrical experience, one that will be remembered for quite some time."
                        i "And it was we who decided to play your game. You satisfied us enough."
                        i "You are free to live as you did before."
                        k "I most definetely will."

                        pause 1.0 
                        scene black with fade
                        "Two days later, the whole school is still talking about what happened."
                        "Naturally, a lot of eyes are on me. Different kinds of eyes."
                        k "...[first_name]"
                        k "[first_name]!"
                        u "Ugh..."
                        u "I'm sorry. I was lost in thoughts."
                        k "It’s okay. You’ll probably think about this for the rest of your life."
                        u "Yeah..."
                        u "Um... Do you think I made the right choice?"
                        k "I don't think I'm the right person to ask this."
                        u "Heh. That's true."
                        k "But If you need me for anything else, I'll always be there to help you."
                        u "Thanks, Kaor-"
                        "Wait… didn’t she say something like that before? And what’s with her expression today?"
                        "I can't stop looking at her."
                        "What is this feeling... this urge?"
                        "I slowly reach for her hand and gently take it."
                        k "Hey! What are you-"
                        u "I'm sorry. I-I just... You don't like it?"
                        k "..."
                        k "No, I-It's not like that."
                        k "I-I like it."

                        pause 1.0
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

    show text "{size=40}{color=#FFFFFF}UI Design by Skolaztika\nCharacter Design by NoranekoGames\nBackground Design by NoranekoGames{/color}{/size}" at truecenter
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

# xpos 0.15
# xpos 0.65