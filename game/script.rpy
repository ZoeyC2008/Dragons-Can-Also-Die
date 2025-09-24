# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#make dynamic colour, cause deconstructed wants to be weird
define drgn_decon_color = "#000000"

#make dynamic names: (i think this works?)
default boy_name = "" #Boy is namable by the player, real name is Sasha
#default boy_display_name = "The Boy: "+boy_name
define sojourn_name = "Man in Midst of Sojourn: 噩梦" #With 'e's: The Sojourner: E Meng
define mirror_name = "The Mirror" #In recover the past ending, The Mirror: Ilia

#protag name
define princess_name = ""

#@Naomi are we putting char in front of the characters? e.g. char_boy??
#the protagonist!
define mc = Character("The Princess: [princess_name], the Heir to the Billyburrows, Duchess ...", color="#eee")

#everyone else
define mirror = Character(mirror_name, color="#e0dddd")
define boy = Character("The Boy: [boy_name]", color="#ba0f0a")
define wolf = Character("The Wolf: Llangernyw", color="#90a3b0")
define wizard = Character("The Wizard: Bea", color="#6f4685")
define innkeeper = Character("The Innkeeper: Pepper", color="#028a0f")
define shepherd = Character("Herd Shep: Rath'la Dnar", color="#ffda03")
define sojourn = Character(sojourn_name, color="#001f3d")
define miller_son = Character("Miller's Mischieveous Moppet: Much", color="#be5504")
define drgn_classic = Character("Traditional Dragon", color="#ff2400") #@Naomi is Furious better than Classic or Traditional?
define drgn_sad = Character("Depressed Dragon", color="#2c3e4c") #logic here is that decon also starts with d
define drgn_happy = Character("Joyous Dragon", color="#0492c2")
define degn_decon = Character("drgn_decon", color=drgn_decon_color) #I think it makes sense for decon to use her code name instead of a descriptor


#define all the images (the way renpy handles this is so weird, like why are there spaces, please get rid of the spaces in my variables)

#mirror
image mirror = "mirror_0_whole.png"
image mirror small cracks = "mirror_1_small_cracks.png"
image mirror medium cracks = "mirror_2_medium_cracks.png"
image mirror big cracks = "mirror_3_big_cracks.png"
image mirror frame = "mirror_4_frame.png"

#Boy!
image boy = "boy_default.png"
image boy snarky = "boy_snarky.png"
image boy shock = "boy_shocked.png"

#Wolf
image wolf = "wolf_default.png"

#backgrounds (I ledgitemently think this is the hardesd part)
image bg forest path = "bg_forest_path.png"
image bg forest camp = "bg_forest_camp.png"

#let's also define some image positions!
define wolf_ypos = 1100

define pos_slightly_left = Position(xalign=0.35, yalign=0.5)
define pos_left = Position(xalign=0.15, yalign=0.5)
define pos_wolf_center = Position(xalign=0.5, ypos=wolf_ypos)

init python:
    #Game variables (the idea is that these dictate what dragon you get)
    royal = 0 #depressed, a classic subversion for a classic prince/ss
    aloof = 0 #happy, you have to be grounded to enjoy life, don't be aloof all the time
    decon = 0 #classic, it's not a proper deconstruction if everything is different
    
    #if none of the thresholds are met, deconstructed since you haven't made personality choices

    #amount to add
    add_most = 16
    add_some = 10
    add_little = 6
    add_tiny = 2
    subtract_tiny = -2
    threshold = 40

    #FLAGS
    #chapter one
    boy_named_flag = False
    boy_renamed_flag = False
    prince_named_flag = False
    kidnap_royal_flag = False 
    invite_reaction_flag = False
    travel_early_flag = True
    travel_ellipsis_flag = True
    
    #boy needs to open up
    boy_talk_about_himself = 0

    #cahpeter1/2 through line
    travel_day = 0

    #chapter two
    mu_my_flag = False

    #this is a vaiable affecting function
    def ellipsis():
        global royal, decon, aloof
        royal += subtract_tiny
        decon += subtract_tiny
        aloof += subtract_tiny

    


# The game starts here.
#Chapter 0
label start:
    #shadow puppet of a prince and princess

    #initial choices
    "...And so they lived, happily ever after."
    
    #first menu, mirror opening
    menu:
        "That was lovely. I'm glad they found joy after all their hardships.":
            $ royal += add_most
        "That is such a cliche. Happily ever after doesn't exist, it's just a tad unrealistic.":
            $ decon += add_most
        "I don't care. There was nothing for me to be emotionally invested in, thus 'happily ever after' doesn't matter one bit.":
            $ decon += add_some
            $ aloof += add_some
        "That was boring. Next.":
            $ aloof += add_most
        
    jump ch0_mirror_question_hub

label ch0_mirror_question_hub:
    show mirror
    
    python:
        hub_key = "mirror"
        num_asks = 4
    
    mirror "Good. This is right."

    call hub_loop
    
    jump ch0_mirror_end

label ch0_mirror_end:
    #reset the hub
    python:
        hub_key = None
        num_asks = 0
    
    mirror "I suppose one of us doesn't have any time left."
    mirror "I hope to see you soon, after I've rested."
    mirror "And I hope you'll recieve me then."

    jump ch1_titlecard

#Chapter 1
label ch1_titlecard:
    #scene
    #scene titlecard ch1
    jump ch1_wake_up

#boy shows up
label ch1_wake_up:
    scene
    scene bg forest path
    show boy at pos_left
    

    boy "Wake up!"
    
    show boy snarky
    boy "Hey, Wolf didn't you say this was the middle of nowhere and about as many as people live here as at the edge of the world?:"

    show boy -snarky
    wolf "I remember my own words, Boy, my mind is sharp. And my senses told me there is no one."

    show wolf at pos_wolf_center
    wolf "Oh."

    show boy snarky
    boy "Then why is there a person? not so all-knowing now, are you."

    show boy -snarky
    wolf "I--"
    wolf "Nevermind."
    wolf "Who are you?"
    
    menu:
        "Who ARE you?":
            jump ch1_wolf_name
        "(Tell them your name.)":
            jump ch1_share_name

    return

$ boy_name_prince_react = 0
label ch1_share_name:
    $ prince_named_flag = True
    menu:
        "I'm just [princess_name].":
            $ decon += add_some
            $ boy_name_prince_react = 1
            jump ch1_name_prince_react
        "I am Princess [princess_name], Heir to the Billyburrows, Duchess of Viantara, and the Dreamer of Zalon.":
            $ decon += add_some
            $ boy_name_prince_react = 2
            jump ch1_name_prince_react
        "I don't think my name matters.":
            $ aloof += add_some
            $ boy_name_prince_react = 3
            jump ch1_name_prince_react
        "...":
            $ ellipsis()
            $ boy_name_prince_react = 3
            jump ch1_name_prince_react

label ch1_name_prince_react:
    if boy_name_prince_react == 1:
        boy "That name doesn't suit you."
        boy "I think you look more like prince instead."
    elif boy_name_prince_react == 2:
        boy "No, I think that's too long."
        boy "Hm..."
        boy "Prince, Prince suits you."
    elif boy_name_prince_react == 3:
        boy "in that case, do you mind if I call you prince?"

    menu:
        "You--you can't just call me Prince!":
            $ royal += add_little
            jump ch1_prince_name_deny
        "But I'm not a Prince?? At least no one's told me that? Including the labels?":
            $ decon += add_little
            jump ch1_prince_name_deny
        "I guess I accept...It's not like it matters...":
            $ aloof += add_little
            jump ch1_prince_name_accept
        "...":
            $ ellipsis()
            jump ch1_prince_name_accept

label ch1_prince_name_accept:
    wolf "Guess I 'ought to be half-way impressed you know better than to flight the battles you cannot win."
    jump ch1_invite 

label ch1_prince_name_deny:
    wolf "Don't bother arguing."
    wolf "Once Boy has his sights set on a name, you're accepting it. Take me, I'm supposed to be Llangernyw, but he insists on calling me Wolf."
    wolf "I've had the unfortunance of learning not bother fighting it."
    jump ch1_invite

label ch1_invite:
    boy "Anyways, Prince, if you're not busy, why don't you come with the two of us?"
    menu:
        "I don't even know you." if not boy_named_flag:
            jump ch1_wolf_name
        "Are you trying to kidnap royalty? And maybe hold them hostage?":
            $ royal += add_some
            $ kidnap_royal_flag = True
            jump ch1_invite_reaction
        "Can you elaborate a tad on where we'll be going?":
            jump ch1_invite_place
        "...":
            $ ellipsis()
            jump ch1_invite_reaction
        "No thank you.":
            jump ending_ch1_walk_away

label ch1_invite_reaction:
    $ invite_reaction_flag = True
    if kidnap_royal_flag:
        boy "No, no!"
        boy "Neither Wolf nor I are interested in politicking or money."
        boy "We ain't got need for it, so..."
        
    boy "I was just wondering if you'd like to travel with us for at least until the next village. It ain't safe for anyone in the middle of the forest."
    show boy snarky
    boy "I would know, I was almost eaten by wolves, you know."
    show boy -snarky
    wolf "That's not what happened!"
    boy "Moving past that, Wolf and I, we're on a quest to kill a dragon, and we'll eventually make it to a village, where we'll be looking for a wizard."
    boy "So, you want to come along?"

    menu:
        "I'm not going anywhere with strangers.":
            jump ending_ch1_walk_away
        "Where is this next village anyway?":
            jump ch1_invite_place
        "Sure, I'll come along":
            jump ch1_travel_question_hub
        "...":
            $ ellipsis()
            jump ch1_travel_question_hub

label ch1_invite_place:
    boy "Well, I'm not all that sure."
    boy "But I know there'll be a village before we properly head into dragon territory."
    if not invite_reaction_flag:
        boy "I was just wondering if you'd like to travel with us for at least until the next village. It ain't safe for anyone in the middle of the forest."
        show boy snarky
        boy "I would know, I was almost eaten by wolves, you know."
        show boy -snarky
        wolf "That's not what happened!"
        boy "Moving past that, Wolf and I, we're on a quest to kill a dragon, and we'll eventually make it to a village."
    boy "So, you want to come along?"
    
    menu:
        "I'm not going anywhere with strangers.":
            jump ending_ch1_walk_away
        "Sure, I'll come along":
            jump ch1_travel_question_hub
        "...":
            $ ellipsis()
            jump ch1_travel_question_hub

#boy naming subplot
label ch1_wolf_name:

    wolf "I am Llangernyw, the wolf."

    show boy snarky
    boy "The one wolf to rule them all, the last of his kind, etc, etc. And my very kind and generous teacher."

    show boy -snarky

    wolf "Yes exactly so. Boy understands my importance."

    show boy snarky
    boy "As always, the joke goes right over his head."

    show boy -snarky
    boy "As for me, I'm not all that impressive. I'm just a boy."

    menu:
        "(Tell them your name.)" if not prince_named_flag:
            jump ch1_share_name
        "Aren't you just inflating Llangernyw's ego?":
            jump ch1_wolf_ego
        "But you haven't told me your name?":
            jump ch1_boy_name

label ch1_wolf_ego:
    show boy snarky
    boy "No doubt, no doubt."

    show boy -snarky
    wolf "I could smite you for you insolence, Boy."

    boy "Don't worry, he wouldn't. And his ego's large enough that I'm hardly adding a drop in the bucket."

    menu:
        "You still haven't told me your name?":
            jump ch1_boy_name
        "(Tell them your name.)" if not prince_named_flag:
            jump ch1_share_name

label ch1_boy_name:
    $ boy_named_flag = True
    boy "Well, like I said, I'm just Boy everyone calls me that."

    menu:
        "But that's hardly a name! I need to call you something else.":
            jump ch1_almost_pick_boy_name
        "I don't think anyone should be called that, but if you insist.":
            if not prince_named_flag:
                jump ch1_boy_asks_for_name
            else:
                jump ch1_accept_boy_name
        "Alright, Boy then, not like I care.":
            $ aloof += add_some
            if not prince_named_flag:
                jump ch1_boy_asks_for_name
            else:
                jump ch1_accept_boy_name
        "But that can't be your true name, so why not think of something else?":
            $ royal += add_tiny
            jump ch1_almost_pick_boy_name
        "...":
            $ ellipsis()            
            if not prince_named_flag:
                jump ch1_boy_asks_for_name
            else:
                jump ch1_accept_boy_name

label ch1_accept_boy_name:
    $ boy_name = "Boy"
    boy "Thank you!"
    boy "Not everyone likes my name, but it's what I'm comfortable with."
    jump ch1_invite

label ch1_boy_asks_for_name:
    $ boy_name = "Boy"
    boy "Good, good. And, in exchange, I'd say its only fair if you share your name too."
    jump ch1_share_name

label ch1_almost_pick_boy_name:
    boy "it's a perfectly good name for me. Take it or leave it."
    
    menu:
        "May I call you something else?":
            jump ch1_almost2_pick_name
        "Okay...I guess...":
            if not prince_named_flag:
                jump ch1_boy_asks_for_name
            else:
                jump ch1_accept_boy_name

label ch1_almost2_pick_name:
    boy "Call me whatever you like. I'm just saying that I prefer Boy."

    menu:
        "Okay, I'll call you ___":
            jump ch1_pick_boy_name
        "Fine, fine, I'll use Boy.":
            if not prince_named_flag:
                jump ch1_boy_asks_for_name
            else:
                jump ch1_accept_boy_name

label ch1_pick_boy_name:
    $ boy_name = renpy.input("Choose Boy's name")
    $ boy_renamed_flag = True
    if boy_name == "":
        $ boy_name = "Boy"
        $ boy_renamed_flag = False
    
    menu:
        "(Tell them your name)" if not prince_named_flag:
            jump ch1_share_name
    jump ch1_invite

#we do be traveling
label ch1_travel_question_hub:
    scene bg forest camp
    show boy at pos_left
    show wolf at pos_wolf_center

    python:
        travel_day += 1
        hub_key = "travel"
        num_asks = 2
        travel_early_flag = True
    
    call hub_loop

    python:
        hub_key = None
        num_asks = 0

    if travel_day == 1:
        jump ch1_travel_day1
    elif travel_day == 2:
        jump ch1_travel_day2
    elif travel_day == 3:
        jump ch1_travel_day3
    elif travel_day == 4:
        jump ch2_meet_innkeeper

#the road goes ever on
label ch1_travel_day1:
    scene bg forest path
    show boy at pos_left
    show wolf at pos_wolf_center

    boy "Roads go ever ever on,"
    boy "Over rock and under tree,"
    boy "By caves where never sun has shone,"
    boy "By streams that never find the sea;"
    boy "Over snow by winter sown,"
    boy "And through the merry flowers of June,"
    boy "Over grass and over stone,"
    boy "And under mountains in the moon."

    menu:
        "Roads go ever ever on...":
            $ decon += add_tiny
        "Is that Lord of the Rings? By J. R. R. Tolkien?":
            $ decon += add_most        
        "...":    
            $ ellipsis()    
    jump ch1_travel_question_hub

label ch1_travel_day2:
    scene bg forest path
    show boy at pos_left
    show wolf at pos_wolf_center

    boy "Roads go ever ever on"
    boy "Under cloud and under star,"
    boy "Yet feet that wandering have gone"
    boy "Turn at last to home afar."
    boy "Eyes that fire and sword have seen"
    boy "And horror in the halls of stone"
    boy "Look at last on meadows green"
    boy "And trees and hills they long have known."

    menu:
        "Roads go ever ever on...":
            $ decon += add_tiny
        "Is that Lord of the Rings? By J. R. R. Tolkien?":
            $ decon += add_most        
        "...":    
            $ ellipsis()
    jump ch1_travel_question_hub

label ch1_travel_day3:
    scene bg forest path
    show boy at pos_left
    show wolf at pos_wolf_center

    wolf "arrrgggghhhh"
    boy "*sigh*"
    boy "Fëa Llangernyw entulessë hröa. Firië vá haryatyë." #I don't think my translation is correct, but it's supposed to be Quenya

    show wolf
    menu:
        "What just happened??":
            jump ch1_travel_explain_soul
        "...":
            $ ellipsis()
            jump ch1_travel_day3_song

label ch1_travel_explain_soul:
    wolf "Nothing you need to worry about."
    wolf "This has no differance on my power, I'm still more that powerful enough to smite everyone in my vincity."
    boy "Eh...Sometimes, you just need to properly shove Wolf's soul into his body."
    boy "I mean, it works and it keeps him alive."
    boy "So, I'm more than happy to do that."
    jump ch1_travel_day3_song

label ch1_travel_day3_song:
    boy "The Road goes ever on and on"
    boy "Down from the door where it began."
    boy "Now far ahead the Road has gone,"
    boy "And I must follow, if I can,"
    boy "Pursuing it with eager feet,"
    boy "Until it joins some larger way"
    boy "Where many paths and errands meet."
    boy "And wither then? I cannot say."
    jump ch1_travel_question_hub


#chapter 2
#innkeeper q hub
label innkeeper_question_hub:
    python:
        hub_key = "innkeeper"
        num_asks = 2
    
    innkeeper "What are you doing here? is there anything you hope to hear?"
    innkeeper "Well, I haven't got much time; I'll take a question or two so long as there's a rhyme."

    call hub_loop

    jump innkeeper_end

label innkeeper_no:
    python:
        hub_key = None
        num_asks = 0
    
    innkeeper "I told you already, my day was quite unsteady."
    innkeeper "I must return to my inn, it's not like I have any other kin."

    jump ch2_scrum

label innkeeper_end:
    innkeeper ""

label shepherd_question_hub:
    python:
        hub_key = "shepherd"
        num_asks = 4
    
    shepherd "Field's humble. My to you brings what?"

    call hub_loop

    jump ch2_scrum

label shepherd_no:
    shepherd "Strangers' foolish. For no time have."
    shepherd "Sheep mine. To return must I."

    jump ch2_scrum

label ch2_scrum:
    show boy at pos_left

label ending_ch1_walk_away:
    return

#kinda just ignoring the whole ending thing
label ending:
    # This ends the game.

    return
