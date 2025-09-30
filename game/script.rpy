# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#make dynamic colour, cause deconstructed wants to be weird
define drgn_decon_color = "#7cdcf0"

#make dynamic names: (i think this works?)
default boy_name = "Boy" #Boy is namable by the player, real name is Sasha
#default boy_display_name = "The Boy: "+boy_name
define sojourn_name = "Man in Midst of Sojourn: 噩梦" #With 'e's: The Sojourner: E Meng
define mirror_name = "The Mirror" #In recover the past ending, The Mirror: Ilia

#protag name
define princess_name = "Fensediaiwe"

#@Naomi are we putting char in front of the characters? e.g. char_boy??
define mirror = Character("[mirror_name]", color="#e0dddd")
define mirror = Character(mirror_name, color="#e0dddd")
define boy = Character("The Boy: [boy_name]", color="#ba0f0a")
define wolf = Character("The Wolf: Llangernyw", color="#90a3b0")
define wizard = Character("The Wizard: Bea", color="#6f4685")
define innkeeper = Character("The Innkeeper: Pepper", color="#028a0f")
define shepherd = Character("Herd Shep: Rath'la Dnar", color="#ffda03")
define sojourn = Character("[sojourn_name]", color="#001f3d")
define miller_son = Character("Miller's Mischieveous Moppet: Much", color="#be5504")
define drgn_classic = Character("Furious Dragon", color="#ff2400") #@Naomi is Furious better than Classic or Traditional?
define drgn_sad = Character("Depressed Dragon", color="#2c3e4c") #logic here is that decon also starts with d
define drgn_hobby = Character("Joyous Dragon", color="#0492c2")
define drgn_decon = Character("drgn_decon", color=drgn_decon_color) #I think it makes sense for decon to use her code name instead of a descriptor

#I don't think we use this
define extra = Character ("???", color="#eee")

#define all the images (the way renpy handles this is so weird, like why are there spaces, please get rid of the spaces in my variables)

#characters
#mirror
image mirror = "images/characters/mirror/mirror_0_whole.png"
image mirror small cracks = "images/characters/mirror/mirror_1_small_cracks.png"
image mirror medium cracks = "images/characters/mirror/mirror_2_medium_cracks.png"
image mirror big cracks = "images/characters/mirror/mirror_3_big_cracks.png"
image mirror frame = "images/characters/mirror/mirror_4_frame.png"

#Boy!
image boy = "images/characters/boy/boy_default.png"
image boy snarky = "images/characters/boy/boy_snarky.png"
image boy shock = "images/characters/boy/boy_shocked.png"

#Wolf
image wolf = "images/characters/wolf/wolf_default.png"
image wolf dying = "images/characters/wolf/wolf_dying.png"

#Wizard
image wizard = "images/characters/wizard/wizard_default.png"

#Villagers
image innkeeper = "images/characters/villagers/innkeeper_default.png"
image miller_son = "images/characters/villagers/miller_son_default.png"
image sojourn = "images/characters/villagers/sojourn_default.png"

#dragons
image drgn_hobby = "images/characters/dragons/hobby.png"
image drgn_classic = "images/characters/dragons/classic.png"
image drgn_sad = "images/characters/dragons/depressed.png"

#backgrounds (I ledgitemently think this is the hardesd part)
#ch0
image bg_black = "#000"

#ch1 forest
image bg_forest_path = "images/backgrounds/bg_forest_path.png"
image bg_forest_camp = "images/backgrounds/bg_forest_camp.png"

#ch2 village
image bg_pasture = "images/backgrounds/bg_pasture.png"
image bg_village_street = "images/backgrounds/bg_village_street.png"
image bg_inn = "images/backgrounds/bg_inn.png"
image bg_doors = "images/backgrounds/bg_doors.png"
image bg_wizard_tower = "images/backgrounds/bg_wizard_tower.png"

#ch3 dragons
image bg_lair_hobby = "images/backgrounds/lairs/bg_hobby.png"

#ch3 dragon endings
image cut_classic_run_no_wizard = "images/cutscenes/cut_classic_run_no_wizard.png"

#titlecards
image titlecard_ch0 = "images/titlecards/ch0.png"
image titlecard_ch1 = "images/titlecards/ch1.png"
image titlecard_ch2 = "images/titlecards/ch2.png"
image titlecard_ch3 = "images/titlecards/ch3.png"

#cutscenes
image cutscene_puppet_show = "images/cutscenes/puppet_show.png"

#decon drgn stuff (at the end of photos)
image bg white = "#fff"
image drgn_decon_one = "images/drgn_decon/drgn_decon_1.png"
image drgn_decon_two = "images/drgn_decon/drgn_decon_2.png"
image drgn_decon_three = "images/drgn_decon/drgn_decon_3.png"

image code1 = "images/drgn_decon/code1.png"
image code2 = "images/drgn_decon/code2.png"
image code3 = "images/drgn_decon/code3.png"
image code4 = "images/drgn_decon/code4.png"
image code5 = "images/drgn_decon/code5.png"
image code6 = "images/drgn_decon/code6.png"
image code7 = "images/drgn_decon/code7.png"
image code8 = "images/drgn_decon/code8.png"

default code_list = [ "code%d" % i for i in range(1, 8) ]


#let's also define some image positions!
define wolf_ypos = 1100
define wizard_ypos = 1100

define pos_slightly_left = Position(xalign=0.35, yalign=0.5)
define pos_left = Position(xalign=0.07, yalign=0.5)
define pos_wolf_center = Position(xalign=0.5, ypos=wolf_ypos)
define pos_wolf_slightly_left = Position(xalign=0.4, ypos=wolf_ypos)
define pos_slightly_right = Position(xalign=0.7, ypos=0.5)
define pos_wizard_slightly_right = Position(xalign=0.7, ypos=wizard_ypos)

define pos_dragon_right = Position(xalign=0.9, ypos=1100)

define pos_drgn_decon_center = Position(xalign = 0.5, yalign = 0.5)

#chanting, this is something to be figured out
define kill_drgn_chant = ""
define butterfly_chant = ""
define teleport_chant = ""

#Variable and flags default 

#these need to be before the questions
init python:
    #Game variables (the idea is that these dictate what dragon you get)
    royal = 0 #depressed, a classic subversion for a classic prince/ss
    decon = 0 #classic, it's not a proper deconstruction if everything is different
    aloof = 0 #hobby, you have to be grounded to enjoy life, don't be aloof all the time
    #if none of the thresholds are met, deconstructed since you haven't made personality choices

    #amount to add
    add_most = 20
    add_some = 14
    add_little = 9
    add_tiny = 4
    subtract_tiny = -2
    threshold = 19

    def ellipsis():
        global royal, decon, aloof
        royal += subtract_tiny
        decon += subtract_tiny
        aloof += subtract_tiny

    #FLAGS
    #chapter one
default boy_named_flag = False
default boy_renamed_flag = False
default prince_named_flag = False
default kidnap_royal_flag = False 
default invite_reaction_flag = False
default travel_early_flag = True
default travel_ellipsis_flag = True
    
    #boy needs to open up
default boy_talk_about_himself_count = 0
default wolf_magic_slideshow_count = 0

    #cahpeter1/2 through line
default travel_day = 0
default travel_day_one = False
default travel_day_two = False
default travel_day_three = False
default travel_day_four = False

    #chapter two
default mu_my_flag = False

    #For the scrum
default assignment_boy = ""
default assignment_wolf = ""

#bread!
default miller_son_coming = False
default miller_son_bread = False
default bread_aquired = False
    #wizard stuff
default wizard_door = 0
default wizard_convinced = 0
default wizard_threshold = 4
default wizard_joined = False

#chapter 3
default which_drgn = ""
    


# The game starts here.
#Chapter 0
label start:
    #testing
    jump test

    #jump ch0_titlecard

label test:
    # we do be testing art
    scene black
    show innkeeper at pos_dragon_right

    pause

    jump ch0_titlecard    

    return

label ch0_titlecard:
    scene titlecard_ch0
    
    pause

    jump ch0_puppet_show


label ch0_puppet_show:    
    scene cutscene_puppet_show

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
    scene bg_black
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
    scene titlecard ch1

    pause
    
    jump ch1_wake_up

#boy shows up
label ch1_wake_up:
    scene bg_forest_path
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
        "I guess I accept... It's not like it matters...":
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
        "I don't even know you." if (boy_named_flag == False):
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
            jump ending_walk_away

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
            jump ending_walk_away
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
            jump ending_walk_away
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
        "(Tell them your name.)" if (prince_named_flag == False):
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
        "(Tell them your name.)" if (prince_named_flag==False):
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
        "Okay... I guess...":
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
        "(Tell them your name)" if (prince_named_flag == False):
            jump ch1_share_name
    jump ch1_invite

#we do be traveling
label ch1_travel_question_hub:
    scene bg_forest_camp
    show boy at pos_left
    show wolf at pos_wolf_center

    $ travel_day += 1
    
    python:
        hub_key = "travel"
        num_asks = 2
    
    $ travel_early_flag = True

    if travel_day == 1:
        $ travel_day_one = True
    elif travel_day == 2:
        $ travel_day_two = True
    elif travel_day == 3:
        $ travel_day_three = True
    elif travel_day == 4:
        $ travel_day_four = True
    
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
        jump ch2_titlecard

#the road goes ever on
label ch1_travel_day1:
    scene bg_forest_path
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
    scene bg_forest_path
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
        "You're singing the same thing... And it's still Tolkien.":
            $ decon += add_most        
        "...":    
            $ ellipsis()
    jump ch1_travel_question_hub

label ch1_travel_day3:
    scene bg_forest_path
    show boy at pos_left
    show wolf dying at pos_wolf_center

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
    boy "Eh... Sometimes, you just need to properly shove Wolf's soul into his body."
    boy "I mean, it works and it keeps him alive."
    boy "So, I'm more than happy to do that."
    boy "Anyhow, it's time we set off."
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
label ch2_titlecard:
    scene titlecard_ch2

    pause
    
    jump ch2_meet_innkeeper

#ch 2 inn
label ch2_meet_innkeeper:
    scene bg_inn
    show boy at pos_left
    show wolf at pos_wolf_slightly_left
    show innkeeper at pos_dragon_right

    innkeeper "Hello, hello. This is The Foolish Flamingo!"
    innkeeper "Are you staying the night, or just here to grab a bite?"
    boy "Thank you, Innkeeper. We'll take two rooms, just tonight and hopefully we'll be out of you hair by tomorrow."
    innkeeper "I hold you to no blame, but just so you know Pepper's the name; you'll be enjoy your two rooms and I claim: they're both one and the same."
    innkeeper "Stay in the common room 'till onset of night, I'll bring over some soup so you won't be feeling light."

    #hide innkeeper

    wolf "Finally being a good apprentice, eh Boy? This Wold definitly needs his privacy and I imagine you two youngsters will want your own room."

    menu:
        "I'd rather share with you, I like your lectures on magic.":
            jump ch2_room_wolf
        "I don't really care how the rooms are distributed":
            $ aloof += add_some
            jump ch2_room_aloof
        "Absolutely not! As royalty, I demand my own room!":
            $ royal += add_some
            jump ch2_room_royal
        "I prefer to be alone.":
            jump ch2_room_alone
        "*Shrug* I'd be fine to room with [boy_name].":
            jump ch2_room_boy
        "Well at least it's better than having one room. And we probably won't have to go through a 'there's only one bed' trope.":
            $ decon += add_some
            jump ch2_room_decon
        "...":
            $ ellipsis()
            jump ch2_room_aloof

label ch2_room_wolf:
    wolf "Why I never! It's wonderful to see someone half as enthusiastic as I was back when I was an apprentice."
    wolf "I had derived all of Maxwell's equations on my own and gotten quite deep into quantum in just the fist year! Why I feel so invigorated, I want to go out right now and take a great leap to acertain gravity's continued existance!"
    wolf "Boy you could stand to learn a thing or two from [princess_name] here."
    boy "*whispers* Prince, sorry to ask this of you, but make sure Wolf sleeps on a bed, otherwise his joints'll be chilled come morning and he won't like that."
    menu:
        "I'll do that.":
            $ royal += add_tiny
        "I don't really care...":
            $ aloof += add_some
        "...":
            $ ellipsis()
    boy "Thanks in advance, hupoefully, I won't wake to Wolf's complaining tomorrow."
    call wolf_magic_slideshow
    jump ch2_innkeeper_demo

label ch2_room_royal:
    boy "Calm down, calm down."
    jump ch2_room_aloof

label ch2_room_alone:
    boy "No problem."
    jump ch2_room_aloof

label ch2_room_decon:
    boy "I wanted to avoid that. I think each room has two beds so no matter how we split it we should be fine."
    jump ch2_room_aloof

label ch2_room_aloof:
    boy "I got the rooms with the thought that Wolf and I will share and Prince gets their own room."
    wolf "Why do they get their own room! How's that fair!"
    wolf "I'm famous, and this tiny backwater inn should be grateful its hosting me and giving me my own sperate suit."
    boy "*whispers* We have this conversation everytime we get to an inn. It's no big deal."
    boy "Wolf, we're used to sharing, let's take a single room like we always do and give Prince some privacy, something they've been sorrowly lacking while we've been on the road."
    wolf "I should huff and blow this inn down!"
    wolf "But fine, fine. Little [princess_name] gets their own room and the two of us will share."
    boy "Great!"
    boy "Here's the key to 217. Try to get lots of sleep in, we'll have a productive day tomorrow."
    jump ch2_innkeeper_demo

label ch2_room_boy:
    boy "Oh!"
    boy "Um... That's not..."
    boy "You know what? This works too."
    boy "Wolf, here's the key to 217, sleep in the bed and don't turn on the AC and keep the windows closed."
    boy "Prince and I will be right across the hall in 216. If you need anything, knock."
    boy "Anyways, Prince, let's go to sleep for tonight. Busy day tomorrow and all that."
    jump ch2_innkeeper_demo

#demo round
label ch2_innkeeper_demo:
    scene bg black
    boy "Rise and shine!"
    boy "Sun's up, so we're up!"
    boy "I'll be in the common room soon with wolf."

    scene bg_inn
    show innkeeper at pos_dragon_right
    show boy at pos_left
    show wolf at pos_wolf_slightly_left
    boy "Sorry about last noght when we barged in rudely; it was late and we were all tired, truely."
    wolf "I don't--"
    boy "*whispers* Shut up!"
    boy "I'm handleing this."
    innkeeper "It's no problem, no problem what so ever. Plenty of stress and rudness though I'd never!"
    wolf "Why--"
    boy "*whispers* Shut up!"
    boy "We're in this little town, can you give us some guidance so we won't look like a clown."
    innkeeper "Given the sheer scale of your dog's lack of fur, it's hard not to mistake him for a jester all covered in myrrh."
    wolf "Wolf!"
    wolf "I am last of my--"
    boy "That's enough. I'm sorry for Wolf's a little gruff."
    wolf "I--"
    boy "Innkeeper, please tell us about the folks 'round here! I even heard there's a magician who I'd love to watch and give them a cheer."
    innkeeper "Bea! Everyone calls her a delight, house right next to  a street light."
    innkeeper "Her admirer the Shepherd finds work in the fields; \nServel the Smith makes the greatest shields;"
    innkeeper "Baltrice the Baker is lazy and lives next to hte mill; \nWren the Weaver has pet spiders along with skill;"
    innkeeper "Benjy the Butcher has knife in hand and tears in eyes; \nSirra the Spinner is dreamy and gives advice that's wise;"
    innkeeper "Sally the Seamstress is a hateful woman with nothing to addd; \nCandice the Cobbler can't finish their work and leaves their clients sad;"
    innkeeper "Tinden the Tanner is forever fair and honourable and just; \nCorry the Candlestick maker is almost snuffed out with every gust;"
    innkeeper "Miller the Miller--Miller the Miller has recently passed; \nMuch the Miller's Son doesn't know why he's so very aghast."
    innkeeper "Have you any questions? I'm open to more suggestions."

    menu:
        "No, nothing.":
            jump ch2_innkeeper_demo_reaction_nothing
        "Can you tell us about the Shepherd?":
            jump ch2_innkeeper_demo_reaction_tell
        "Can you tell us about Serval the Smith?":
            jump ch2_innkeeper_demo_reaction_tell
        "Can you tell us about Baltrice the Baker?":
            jump ch2_innkeeper_demo_reaction_tell
        "Can you tell us about Wren the Weaver?":
            jump ch2_innkeeper_demo_reaction_tell
        "Can you tell us about Benjy the Butcher?":
            jump ch2_innkeeper_demo_reaction_tell
        "Can you tell us about Sirra the Spinner?":
            jump ch2_innkeeper_demo_reaction_tell
        "Can you tell us about Sally the Seamstress?":
            jump ch2_innkeeper_demo_reaction_tell  
        "Can you tell us about Candice the Cobbler?":
            jump ch2_innkeeper_demo_reaction_tell 
        "Can you tell us about Tinden the Tanner?":
            jump ch2_innkeeper_demo_reaction_tell
        "Can you tell us about Corry the Candlestick maker?":
            jump ch2_innkeeper_demo_reaction_tell       
        "How did Miller the Miller die? I understand his son doesn't know, but maybe you know why?":
            jump ch2_innkeepre_demo_reaction_miller

label ch2_innkeeper_demo_reaction_nothing:
    boy "we don't intend to  be rude or trite, please forgive our slight."
    innkeeper "I shall leave you three alone; I have sheets to wash as they're quite suliness prone."
    jump ch2_assignments

label ch2_innkeeper_demo_reaction_tell:
    boy "we don't intend to  be rude or trite, please forgive our slight.But also please help us with our plight."
    innkeeper "Don't go around asking, no one deserves this much prodding."
    innkeeper "I shall leave you three alone; I have sheets to wash as they're quite suliness prone."
    jump ch2_assignments

label ch2_innkeepre_demo_reaction_miller:
    $ mu_my_flag = True
    innkeeper "All I know is my other guest is trapped, everyone thinks he's a murderer which I do not find apt."
    jump ch2_assignments

label ch2_assignments:
    #hide innkeeper
    boy "Everyone's much friendlier if you're nice,"
    boy "Yes, Wolf that means you."
    boy "Also, we should try to match them, it's the least we could do seeing as we're guests in the village."
    boy "Prince, this means you too."
    boy "From what Innkeeper told us, it's the Shepherd that'll be the most familliar with that wizard. Prince why don't you get first pick?"

    menu:
        "I want to talk to Pepper again, I feel like she hasn't told us everything. I'll just wait around the inn after her tasks, I guess.":
            jump ch2_assignments_innkeeper
        "Pepper mentioned another guest. Maybe they'll know something?":
            jump ch2_assignments_sojourn
        "The shepherd is the most direct source of information, so I suppose I'll go to the fields.":
            jump ch2_assignments_shepherd
        "I can try asking around on the steets.":
            jump ch2_assignments_miller_son
        "I want to find this Miller's son, I'm curious about what happened to his father." if (mu_my_flag == True):
            jump ch2_assignments_miller_son
        "i think you should get first pick.":
            jump ch2_assignments_boy_pick

label ch2_assignments_innkeeper:
    python:
        assignment_boy = "miller_son"
        assignment_wolf = "shepherd"
    
    boy "Alright, great."
    boy "Wolf?"
    wolf "I'll need to stretch my old legs. I'll talk to this 'shepherd'."
    boy "That means I'll take to the streets."
    boy "Good luck to all of us, we'll meet back here an hour before sunset."
    jump ch2_innkeeper_question_hub

label ch2_assignments_sojourn:
    python:
        assignment_boy = "miller_son"
        assignment_wolf = "shepherd"
    
    boy "Alright, great."
    boy "Wolf?"
    wolf "I'll need to stretch my old legs. I'll talk to this 'shepherd'."
    boy "That means I'll take to the streets."
    boy "Good luck to all of us, we'll meet back here an hour before sunset."
    jump ch2_sojourn_question_hub

label ch2_assignments_shepherd:
    python:
        assignment_boy = "miller_son"
        assignment_wolf = "innkeeper"
    
    boy "Alright, great."
    boy "Wolf, i want you to stay at the inn and talk to either Innkeeper or that other guest she mentioned. I'll take to the streets and make inquireies that way."
    boy "Good luck to all of us, we'll meet back here an hour before sunset."

    scene bg_village_street

    boy "I'm glad Wolf's staying at the inn. I'd be worried about him running into trouble on the streets."

    jump ch2_shepherd_question_hub

label ch2_assignments_miller_son:
    python:
        assignment_boy = "sojourn"
        assignment_wolf = "shepherd"
    
    boy "Wolf?"
    wolf "I'll need to stretch my old legs. I'll talk to this 'shepherd'."
    boy "Alright I'll stay behind and talk to that other guest Innkeeper mentioned."
    boy "Good luck to all of us, we'll meet back here an hour before sunset."
    jump ch2_miller_son_question_hub




#innkeeper q hub
label ch2_innkeeper_question_hub:
    python:
        hub_key = "innkeeper"
        num_asks = 2
    
    scene bg_inn
    show innkeeper at center

    innkeeper "What are you doing here? is there anything you hope to hear?"
    innkeeper "Well, I haven't got much time; I'll take a question or two so long as there's a rhyme."

    call hub_loop
    
    innkeeper "I don't have more time left, and no one has hands quite as deft."
    
    jump ch2_scrum


label ch2_innkeeper_no:    
    innkeeper "I told you already, my day was quite unsteady."
    innkeeper "I must return to my inn, it's not like I have any other kin."

    jump ch2_scrum


label ch2_sojourn_question_hub:
    python:
        hub_key = "sojourn"
        num_asks = 4

    scene bg_inn
    show sojourn at center
    sojourn "You had stuff you want to ask about?"
    sojourn "I'm happy to talk with you."
    sojourn "To the Flamingo's common room..."

    sojourn "I am 噩梦, just a man in midst of a sojourn, unluckly in town during a tad bit of hardship."
    sojourn "So, what did you want to ask about."

    call hub_loop

    sojourn "Hours draw, I'm going and you should to."

    jump ch2_scrum

label sojourn_no:
    sojourn "What an atrocious sound."
    sojourn "I'm afraid I'll only rally againn around dusk."
    sojourn "If you're still curious mayhaps I'll talk to you again after that hour."
    sojourn "Now, good day."

    jump ch2_scrum

label ch2_miller_son_question_hub:
    python:
        hub_key = "miller_son"
        num_asks = 0

    scene bg_village_street

    show miller_son at center

    miller_son "Man, man, woman, person, stranger, whatever. What are you doing wandering round here?"

    call hub_loop

    jump ch2_scrum


label ch2_miller_son_no:
    miller_son "May you be less rude when you next open your mouth."

    jump ch2_scrum

label ch2_shepherd_question_hub:
    python:
        hub_key = "shepherd"
        num_asks = 4

    scene bg_pasture
    
    shepherd "Field's humble. My to you brings what?"

    call hub_loop

    shepherd "Sheep mine. To rmieturn must I."

    jump ch2_scrum

label ch2_shepherd_no:
    shepherd "Strangers' foolish. For no time have."
    shepherd "Sheep mine. To return must I."

    jump ch2_scrum

label ch2_scrum:
    python:
        hub_key = None
        num_asks = 0
        if assignment_boy == "miller_son" and mu_my_flag:
            miller_son_coming = True

    scene bg_inn
    show boy at pos_left
    show wolf at pos_wolf_center

    boy "So what did everyone learn?"
    boy "Wolf?"
    if assignment_wolf == "shepherd":
        wolf "A fat load of nothing."
        wolf "That shepherd hates me, all they want is to look after their sheep."
        wolf "Doesn't even try to entertain that I might be safe and just looking for a conversation."
    elif assignment_wolf == "innkeeper":
        wolf "I think the Innkeeper hates me."
        wolf "All she does is laundry all day."
        wolf "But she can't even spare a second to talk!"
    boy "Prince?"
    menu:
        "(Tell them what you know.)":
            boy "That's good info."
        "...":
            $ ellipsis()

    boy "Okay, so here's what I learned."
    if assignment_boy == "sojourn":
        boy "The guest, Sojourn, doesn't really know all that much about Wizard, which makes sense since he's just arrived."
        if mu_my_flag:
            boy "But what I did learn if that Miller's death is an accident."
            boy "Even if Innkeeper and Miller didn't have the best of relations she didn't push him, and Sojourn can testify."
    elif assignment_boy == "miller_son":
        boy "Wizard lives on the same street as Miller's Son, Cyclamen street."
        boy "Although I don't know where he used to live, Wizard lives to the across the street and to the right from Miller's Son's former house."
        boy "He remembers that the numbers are probably bronze and that there are winchimes"
        boy "In fact, he just took flowers from her home to put in a vase and actually plans to give it back to her with the bread he's getting."
        if mu_my_flag:
            boy "My understanding of his understanding of the whole murder situation is that he has no idea what happened."
            boy "But I think he doesn't want to blame Innkeeper."
    boy "Alright, let's go find Wizard's door, knock, and see if she wants to come along."

    if miller_son_coming:
        #show miller_son at pos idk

        miller_son "So, what have you learned about Da's death?"
        menu:
            "I think Innkeeper Pepper might have done it.":
                miller_son "That doesn' sound right..."
            "I think you should talk to Sojourn, he'll know.":
                $ miller_son_bread = True
                miller_son "Okay. I shall see what he thinks."
            "I don't know.":
                miller_son "...Alright, I'll keep searching."
            "...":
                $ ellipsis()
                miller_son "So you don't know either."

        

label ch2_choose_door:
    scene bg_village_street
    pause
    if miller_son_bread:
        $ bread_aquired = True
        miller_son "Wait!"
        # show miller_son at pos
        miller_son "I talked with Sojourn and am really grateful that mess has been cleaned up."
        miller_son "I was hoping you'd accept the bread my partner, Basil, made!"
        menu:
            "Thank you! You didn't need to , but thank you.":
                miller_son "It was no problem."
            "We couldn't possibly...":
                miller_son "No, I insist."
                miller_son "Here take it."
            "...":
                $ ellipsis()
                boy "Thank you."
                boy "We're happy your situation was fixed. The truth is usually revealed in the end."
                miller_son "And thank you for helping find it."


    
    scene bg_doors
    $ wizard_door = renpy.input("Choose which door to knock on:")
    if wizard_door == 7:
        jump ch2_wizard_start
    else:
        jump ch2_random_door

label ch2_random_door:
    #show scene wrong door
    extra "Get away!"
    extra "And stay away from this village and our wizard!"
    jump ch2_travel

label ch2_wizard_start:
    scene bg_wizard_tower
    show boy at pos_left
    show wolf at pos_wolf_slightly_left
    show wizard at pos_wizard_slightly_right

    boy "Hello?"
    wizard "H-h-hello..."
    boy "We were wondering if this is the local wizard."
    wizard "I-I_I. Y-y-yes... I-I-I am."
    wolf "Boy, tell her to return us inside."
    wizard "C-c-come in."
    wizard "S-s-sorry, I h-h-heard you, um..."

    #show scene wizard room
    boy "I'm Boy, that's Wolf, and this is Prince."
    wolf "I am Llangernyw, the Wolf. That is what you will call me, and nothing less."
    wizard "Llangernyw!! Y-y-you have a-a-amazing m-m-magic."
    boy "Not to derail the conversation, but we were looking for you, actually."
    wizard "M-m-me??"
    boy "Yes. Just listen for a bot. We are on a quest to kill a dragon and you live so close to one, I'm sure you have unique insights and expertise."
    boy "In fact, we would all be delighted if you were willing to join us on this quest."
    wizard "I-I-I'm honoured!! Really honoured..."
    wizard "B-b-but I d-d-don't think I-I-I'd be helpful..."
    wizard "I k-k-know I'm not very good with m-m-magic."
    menu:
        "I don't even know magic, but I'm travelling on this 'quest', it's not like that's a prerequisite.":
            $ wizard_convinced += 1
            jump ch2_wizard_b1_also_not_magic
        "You're probably right.":
            $ wizard_convinced -= 1
            jump ch2_wizard_b1_wizard_right
        "Boy and Llangernyw know enough magic to cover for the two of us.":
            jump ch2_wizard_b1_enough_magic
        "Even if you aren't the best, you'll still bring a unique perspective on magic. Boy and Llangernyw would appriciate that when casting, I know I don't have that perspective.":
            $ wizard_convinced += 2
            jump ch2_wizard_b1_magic_perspective
        "...":
            $ ellipsis()
            jump ch2_wizard_b1_ellipsis
        "I'm sure you're better than you know.":
            $ wizard_convinced += 1
            jump ch2_wizard_b1_youre_better
        "That's okay, Llangernyw can teach you to get better, like he's teaching [boy_name] and I." if (wolf_magic_slideshow_count>2):
            jump ch2_wizard_accept_wolf

label ch2_wizard_b1_also_not_magic:
    wizard "I-I-I see..."
    boy "It's also not like knights had to know magic to be dragonslayers either."
    jump ch2_wizard_b2_start

label ch2_wizard_b1_wizard_right:
    show boy shock
    boy "Prine! Why would you say that!"
    boy "I'd expect something like this from Wolf, not you."
    wolf "They're not wrong though."
    show boy -snark
    boy "NO. They're both wrong. Bea, I know you know something unique about magic, every practitioner does."
    boy "Just because you aren't good at it in a traditional sense doesn't eman you don't have a magical perspective honed through practice."
    boy "Something that I, for one, don't have."
    jump ch2_wizard_b2_start

label ch2_wizard_b1_enough_magic:
    wizard "S-s-so you don't n-n-need me..."
    boy "No, no. That's not what Prince meant."
    boy "It's just that we sought you out for advice on dragons, while Wolf and I are capable of pulling enough magic that between the two of us we can defeat a dragon."
    boy "(Hopefully.)"
    jump ch2_wizard_b2_start

label ch2_wizard_b1_magic_perspective:
    wizard '...'
    wizard "I-I-I hadn't thought a-a-about it that way..."
    jump ch2_wizard_b2_start

label ch2_wizard_b1_ellipsis:
    show boy snarky
    boy "Prince isn't the most socially competent"
    show boy -snarky
    boy "I'm sure they were going to point out how amazing you are at magic, but the words slipped right through their mouth."
    jump ch2_wizard_b2_start

label ch2_wizard_b1_youre_better:
    wolf "This ain't the way, princling."
    wizard "Llangerwyn's right..."
    wizard "I-I-I'm not even an a-a-apprentice."
    boy "Nope. Wolf's wrong. Like frequently. But especially now."
    boy "Prince has the right idea, they're just not that experienced in magic, but even if you're not the best in more traditional spellwork there are many other areas are still magic."
    jump ch2_wizard_b2_start

label ch2_wizard_b2_start:
    wizard "But I d-d-don't even know about d-d-dragons..."
    menu:
        "I don't know about dragons either":
            jump ch2_wizard_b2_also_no_knowledge
        "...":
            $ ellipsis()
            jump ch2_wizard_b2_ellipsis
        "Dont worry! We'll have fresh-well, sort of fresh-bread with us!" if (bread_aquired == True):
            $ wizard_convinced += 2
            jump ch2_wizard_b2_bread
        "Tell us about dragons.":
            $ wizard_convinced += 2
            jump ch2_wizard_b2_infodump
        "Then how have you spent so long living next doo to a dragon? What have you been doing this whole time!?":
            $ wizard_convinced -= 1
            jump ch2_wizard_b2_living_condition

label ch2_wizard_b2_also_no_knowledge:
    wizard "But-But you came to me for help!"
    boy "Honestly, it's fine."
    boy "Why not come with and see if approaching dragon country jolts any hidden memories?"
    jump ch2_wizard_b3_start

label ch2_wizard_b2_ellipsis:
    wizard "..."
    boy "Honestly, it's fine."
    boy "Why not come with and see if approaching dragon country jolts any hidden memories?"
    jump ch2_wizard_b3_start

label ch2_wizard_b2_bread:
    wizard "True!! Th-th-there is the well-known but yet to be fully substantiated rumour of a dragon's fear of bread Something I'm sure draconic reseachers would love to have more credible evidance either for or against."
    jump ch2_wizard_b2_infodump

label ch2_wizard_b2_infodump:
    wizard "Nearly every culture has myths about something called a 'dragon', despite the fact none of them can agree on exactly what dragons are."
    wizard "How big are they? What do they look like? How many heads do they have? Do they breathe fire? Or ice? Do they fly (and if so, with or without wings)? How many legs do they have?"
    wizard "Are they dumb as planks, or superintelligent? Are they low scaly pests, or ultra-rare Uber-serpents ancient and powerful as the Earth itself? Are they benevolent? Malevolent or even outright demonic?"
    wizard "The answers to these questions generally fall within two traditions, 'Western and 'Eastern', which come from unrelated mythological currents and only share the name of dragon due to a questionable case of cultural translation:"
    wizard "Westerners who encountered stories and images of Chinese and Japanese dragons sprung on the similarities to the European dragon and couldn't think of anything better to call them. And even then, in addition to cultural differences, dragons fall into a very wide range of types even in one local mythology."
    wizard "Western dragons or European dragons are derived from Greek and Roman mythology (the word 'dragon' itself is rooted in the Greek word drákōn) and may have been influenced by the cultures of the Ancient Near East; there are also are older myths with serpentine entities which would be called dragons by later generations."
    wizard "In many Greek myths, the word referred to gigantic but relatively conventional snakes, only sometimes endowed with more bizarre traits like multiple heads, which generally represent chaos, monstrosity and the perils of untamed nature, although there are also examples of snakes associated to divine figures."
    wizard "Drákōnes usually guarded magical artifacts or landmarks, such as the Golden Fleece, Hera's Golden Apples and Ares' spring, and some were known for never sleeping."
    wizard "Through the Middle Ages, in combination with Norse Mythology, these beings would evolve into the more known European dragon, with its trademark wings and fiery breath (to show the extent of these new influences, ancient Greek dragons were usually wingless and more related to water)."
    wizard "Eastern dragons, or more specifically Chinese dragons, derive from ancient Chinese mythology dating back 7000 years ago before these depictions spread throughout Eastern Asia."
    wizard "The traditional origin story is that the region of Northern China where Chinese civilization first began was filled with dinosaur fossils, which led to the development of dragon myths (Northern China is still considered a huge 'dinosaur hot spot' in palaeontology today), but this is looked at with some skepticism in modern scholarship."
    wizard "Eastern dragons are serpentine semi-divine entities associated to both physical and philosophical concepts, often rain, water and spiritual energies, and while not necessarily friendly, they are always trascendent."
    wizard "There are many other dragons in the East, but the Chinese dragon or lóng and its variants spread from Japan to Bhutan are by far the most well-known."
    wizard "This is also not to say there are no cultures which dip into both traditions simultaneously..."
    wizard "..."
    wolf "That's a hell of a lot of theory."
    boy "See! You do know a lot! We'll be happy to have you."
    wizard "But th-th-those are just b-b-basics."
    wizard "I d-d-don't know that much m-m-more..."
    boy "And even if you didn't, we'd be happy to have you"
    jump ch2_wizard_b3_start

label ch2_wizard_b2_living_condition:
    boy "Prince, you have no idea what wizard was doing and the dragon clearly isn't an active threat."
    boy "Either way, we'd be happy to have you."
    jump ch2_wizard_b3_start

label ch2_wizard_b3_start:
    wizard "Even i-i-if I go, I'd j-j-just slow you folks d-d-down."
    menu:
        "We're already going at a really slow pace to accomadate Llangerwyn and me.":
            $ wizard_convinced += 1
            jump ch2_wizard_b3_slow_already
        "...":
            $ ellipsis()
            jump ch2_wizard_b3_ellipsis
        "Then this trip can also be exercise, it'll be healthy for you.":
            $ wizard_convinced += 1
            jump ch2_wizard_b3_exercise
        "You probably will.":
            $ wizard_convinced -= 1
            jump ch2_wizard_b3_you_will
        "You might slow us down, but that's alright. We're not exactly in a rush.":
            $ wizard_convinced += 2
            jump ch2_wizard_b3_no_rush

label ch2_wizard_b3_slow_already:
    wizard "R-r-really..."
    boy "Yup, both Wolf and Prince aren't the strongest physically. You'll fit right in."
    jump ch2_wizard_b4_start

label ch2_wizard_b3_ellipsis:
    boy "Honesty, don't worry about pace."
    boy "We're already close to the dragon's lair, so I'm sure we'll make it there soon."
    jump ch2_wizard_b4_start

label ch2_wizard_b3_exercise:
    wizard "I g-g-guess..."
    boy "Think of it like a long hike. And everyone can use a hike now and then."
    jump ch2_wizard_b4_start

label ch2_wizard_b3_you_will:
    wizard "I-I-I s-s-see..."
    boy "But that's okay! Slaying a dragon isn't something we need to rush into, we can use that time for planning and whatnot."
    jump ch2_wizard_b4_start

label ch2_wizard_b3_no_rush:
    boy "Exactly! We're just going to slay a dragon since it's minimal effort, excellent reward."
    show boy snarky
    boy "You'll get a sixth of a kindgom if we split evenly between you, me, and prince."
    show boy -snarky
    wolf "Hey! what about me!"
    boy "Somehow, I don't think you'd be interested in doing all the paperwork associated with running a small kingdom."
    wizard "..."
    jump ch2_wizard_b4_start

label ch2_wizard_b4_start:
    wizard "It'll be my f-f-first time out of the v-v-village in decades..."
    menu:
        "I don't even know where I'm from, but this'll be my first time seeing the world too.":
            $ wizard_convinced += 1
            jump ch2_wizard_b4_see_world
        "You can always go back. Remember that you're not leaving forever.":
            $ wizard_convinced += 2
            jump ch2_wizard_b4_not_forever
        "You don't have to leave if you don't want to.":
            $ wizard_convinced -= 1
            jump ch2_wizard_b4_dont_leave
        "...":
            $ ellipsis()
            jump ch2_wizard_b4_ellipsis
        "You've been outside the village before, you can go out again.":
            $ wizard_convinced += 1
            jump ch2_wizard_b4_go_out_again

label ch2_wizard_b4_see_world:
    wizard "I s-s-suppose everyone has a different first e-e-experience, seeing the world, th-th-that is."
    jump ch2_wizard_decide

label ch2_wizard_b4_not_forever:
    wizard "No... No, I'm not."
    wizard "This is my home, isn;t it..."
    wizard "And I can always return to it."
    jump ch2_wizard_decide

label ch2_wizard_b4_dont_leave:
    wizard "Y-y-yes..."
    boy "But, obviously, it's also fine if you came along with us."
    jump ch2_wizard_decide

label ch2_wizard_b4_ellipsis:
    boy "It's okay. Bea, you don't have to leave, but if you do, I'm sure you can always come back, that's the beauty of journeying."
    jump ch2_wizard_decide

label ch2_wizard_b4_go_out_again:
    wizard "True..."
    wizard "I l-l-learned magic from the o-o-outside..."
    wizard "I c-c-can go back out there, I k-k-know it."
    jump ch2_wizard_decide

label ch2_wizard_decide:
    if wizard_convinced >= wizard_threshold:
        jump ch2_wizard_accept
    else:
        jump ch2_wizard_deny

label ch2_wizard_accept_wolf:
    wizard "S-s-say no m-m-more!!"
    jump ch2_wizard_accept

label ch2_wizard_accept:
    $ wizard_joined = True

    wizard "I'll come."
    wizard "I'll help."
    boy "Great! We're happy to have you."
    wolf "What he said."
    menu:
        "You'll be fine, wizards are famously bad at dying, permanently at least.":
            $ decon += add_little
        "Be grateful to travel in the presense of royalty. Although we are grateful to have you here.":
            $ royal += add_some
        "What he said.":
            $ aloof += add_little
        "...":
            $ ellipsis()
    jump ch2_travel

label ch2_wizard_deny:
    wizard "S-s-sorry..."
    wizard "B-b-but I h-h-have to d-d-decline..."
    boy "That's totally fine. We're happy to have talked to you."
    menu:
        "Calls to adventure are usually declined anyway. Don't feel bad about it.":
            $ decon += add_little
        "You would deny the opportunity to travel with a royal?":
            $ royal += add_some
        "What he said.":
            $ aloof += add_little
        "...":
            $ ellipsis()
    jump ch2_travel

label ch2_travel:
    jump ch2_travel_question_hub


#we do be traveling
label ch2_travel_question_hub:
    scene bg_forest_camp
    show boy at pos_left
    show wolf at pos_wolf_center

    $ travel_day += 1
    
    python:
        hub_key = "travel"
        num_asks = 2
    
    $ travel_early_flag = True
    
    call hub_loop

    python:
        hub_key = None
        num_asks = 0

    if travel_day == 5:
        jump ch2_travel_day1
    elif travel_day == 6:
        jump ch2_travel_day2
    elif travel_day == 7:
        jump ch2_travel_day3
    elif travel_day == 8:
        jump ch3_titlecard

#the road goes ever on
label ch2_travel_day1:
    scene bg_forest_path
    show boy at pos_left
    show wolf at pos_wolf_center
    if wizard_joined:
        show wizard at pos_wizard_slightly_right

    boy "Upon the hearth the fire is red,\nBeaneath the roof there is a bed;"
    boy "But not yet weary are our feet,\nStill round the corner we may meet"
    boy "A sudden tree or standing stone\nThat none have seen but we alone."
    boy "Tree and flower and lead and grass,\nLet them pass! Let them pass!"
    boy "Hill and water under sky,\nPass the by! Pass them by!"

    menu:
        "Still round the corner there may wait...":
            $ decon += add_tiny
        "Is that Lord of the Rings? By J. R. R. Tolkien?":
            $ decon += add_most        
        "...":    
            $ ellipsis()    
    jump ch2_travel_question_hub

label ch2_travel_day2:
    scene bg_forest_path
    show boy at pos_left
    show wolf at pos_wolf_center
    if wizard_joined:
        show wizard at pos_wizard_slightly_right

    boy "Still round the corner there may wait\nA new road or a secret gate,"
    boy "And through we pass them by today,\nTomorrow we may come this way"
    boy "And take the hidden paths that run\nTowards the Moon or to the Sun."
    boy "Apple, thorn, and nut and sloe,\nLet them go! Let them go!"
    boy "Sand and stone and pool and dell,\nFare you well! Fare you well!"

    menu:
        "Home is behind, the world ahead,...":
            $ decon += add_tiny
        "You're singing the same thing... And it's still Tolkien.":
            $ decon += add_most        
        "...":    
            $ ellipsis()
    jump ch2_travel_question_hub

label ch2_travel_day3:
    scene bg_forest_path
    show boy at pos_left
    show wolf at pos_wolf_center

    boy "We'll be arriving tomorrow."

    jump ch2_travel_day3_song

label ch2_travel_day3_song:
    boy "Home is behind, the world ahead,\nAnd there are many paths to tread"
    boy "Through shadows to the edge of night,\nUntil the stars are all alight."
    boy "Then the world behind and home ahead,\nWe'll wander back to home and bed."
    boy "Mist and twilight, cloud and shade,\nAway shall fade! Away shall fade!"
    boy "Fire and lamp, and meat and bread,\nAnd then to bed! And then to bed!"
    
    jump ch2_travel_question_hub


label ch3_titlecard:
    show titlecard_ch3

    pause

    jump ch3_decide

label ch3_decide:
    scene bg_black
    boy "This is it. Through this tunnel is the dragon."

    python:
        snapshot = [royal, decon, aloof]
        best_value = max(snapshot)
        best_index = snapshot.index(best_value)

    if (best_value > threshold):
        if (best_index == 0):
            $ which_drgn = "sad"
            jump ch3_sad_start
        elif (best_index == 1):
            $ which_drgn = "classic"
            jump ch3_classic_start
        elif (best_index == 2):
            $ which_drgn = "hobby"
            jump ch3_hobby_start
    else:
        $ which_drgn = "decon"
        jump ch3_decon_start

label ch3_drgn_hobby:
    scene bg_lair_hobby
    show boy at pos_left
    show wolf at pos_wolf_slightly_left
    show drgn_hobby at pos_dragon_right
    
    #debug the images!!!

    pause

label ch3_sad_start:
    if wizard_joined:
        jump ch3_sad_wizard
    else:
        jump ch3_sad_no_wizard

label ch3_sad_wizard:
    drgn_sad "..."
    boy "Hello."
    boy "We are here to slay you."
    drgn_sad "..."
    wolf "..."
    wolf "Boy, you see that. Don't you?"
    boy "She's already dead."
    wizard "She i-i-isn't."
    drgn_sad "..."
    wizard "You a-a-aren't a c-c-corpse."
    wizard "Not yet."
    drgn_sad "I... want... to... be..."
    wizard "Many do. I wanted to."
    wizard "But you're not alone right now."
    wizard "We can help."
    boy "And we want to."
    wolf "Seconded."
    menu:
        "Yes. We'll definitly help.":
            wizard "See."
        "*whisper* Wait, what happened to killing the dragon?":
            wizard "We don't."
            wizard "We don't kill her."
            boy "That was before."
            boy "It's obvious she's not killing anyone."
            boy "We'll find another solution to our problems."
            boy "But later."
            wizard "For now, we help."
    #cutscene


    #script cont
    wizard "We are here for you."
    wizard "Why don't you explain and tell us why you're here."
    drgn_sad "The world is wrong..."
    drgn_sad "Or I am wrong..."
    wizard "The world can be wrong."
    drgn_sad "It wants be to me..."
    drgn_sad "To be like the other dragons..."
    drgn_sad "Terrifying... furious... angry..."
    drgn_sad "But I don't think I am..."
    drgn_sad "Those things."
    boy "You aren't."
    boy "Even just seeing you, we know."
    wolf "Easiest remedy, we can spread your story."
    wolf "Emphasize that you're looking for a friend."
    wizard "I'll be that friend."
    boy "Yeah, Wolf, Prince, and I can spread those stories, in the meantime you'll help her, right?"
    wizard "Yes."

    menu:
        "I'll stay with you.": #do we keep this??
            jump ending_stay_with_sad
        "We'll make sure the whole world knows you're kind.":
            jump ch3_alive_drgn    

label ch3_sad_no_wizard:
    #art
    show boy at pos_left
    show wolf at pos_wolf_slightly_left
    show drgn_hobby at pos_dragon_right


    #script
    drgn_sad "..."
    boy "Hello."
    boy "We are here to slay you."
    drgn_sad "..."
    wolf "..."
    wolf "Boy, you see that. Don't you?"
    boy "She's already dead."
    boy "..."
    boy "That can't be right."
    boy "Dragons don't just--just--"
    wolf "Dragons don't just kneel over and die."
    drgn_sad "Soon..."
    boy "Soon what?"
    drgn_sad "Death..."
    drgn_sad "Always... soon... but... never..."
    drgn_sad "But... never... now..."
    drgn_sad "Wish... it... were... now..."
    drgn_sad "I... do... not... want... to... see..."
    drgn_sad "See... another... dawn..."
    wolf "Boy, are we killing her?"
    boy "...I don't know."
    wolf "Whatever you decide, I'll support it."
    wolf "You're my best student and if you want the dragon's materials, which are still active, and, of course, the bragging rights, I won't fault you. But if you don't want to stain your soul, I most certainly won't fault you either."
    boy "..."
    drgn_sad "My... death..."
    drgn_sad "Today... is... a..."
    drgn_sad "Is... a... good... day..."
    boy "Prince, what do you think?"
    menu:
        "She's miserable, and we can help her by killing her... right? It'd be a mercy... wouldn't it?":
            jump ch3_sad_no_wizard_kill
        "I think we can help her... surely she can still be saved?":
            jump ch3_sad_no_wizard_save

label ch3_sad_no_wizard_kill:
    #art

    #script
    boy "I think you might be right."
    wolf "You'll still need to use that spell"
    boy "...we'd planned on that."
    boy "This'll take a moment."
    boy "Depressed Dragon, I hope you won't mind."
    
    #art


    #script cont
    wolf "May thine soul find freedom outside this pale imitation of thine brilliance..."
    boy "...[kill_drgn_chant]"
    drgn_sad "Thank... you..."
    
    pause
    
    jump ch3_dead_drgn

label ch3_sad_no_wizard_save:
    boy "Okay."
    drgn_sad "No... I... want... to..."
    drgn_sad "Want... to.. die..."
    menu:
        "(Give her bread.)":
            jump ch3_sad_no_wizard_save_bread
        "...":
            jump ch3_sad_no_wizard_save_no_bread

label ch3_sad_no_wizard_save_bread:
    wolf "Bread. It's the heart of life."
    boy "Why don't you try it."

    #cutscene


    #script cont
    boy "There's more to live for."
    boy "You don't have to just stay in your cave and die."
    boy "It's okay if you don't want to."
    boy "But there's a lot out there, there's bread and other things that can be disovered, that can be found."
    drgn_sad "..."
    drgn_sad "One day..."
    drgn_sad "One day, I might try..."
    boy "If you want, I'll come back with things from outside your cave."
    drgn_sad "I think..."
    drgn_sad "I'd like that..."
    drgn_sad "I want..."
    drgn_sad "To find more of myself..."
    wolf "Good luck to that."
    boy "?"
    wolf "Good luck to finding yourself and doing soul serching and all that."
    wolf "Unlike Boy, most people don't, not for a long, long, time that is."
    wolf "So, good luck."
    drgn_sad "..."
    drgn_sad "Thank you."

    pause
    
    jump ch3_alive_drgn

label ch3_sad_no_wizard_save_no_bread:
    #cutscene death


    #script
    drgn_sad "This... is... a... good..."
    drgn_sad "A... good... day..."
    drgn_sad "A... good... death..."
    wolf "May thine soul find freedom outside this pale imitation of thine brilliance..."
    drgn_sad "Thank... you... for..."
    drgn_sad "For... being... a... spectator..."

    pause

    jump ch3_dead_drgn


label ch3_classic_start:
    show drgn_classic at pos_dragon_right

    drgn_classic "WHO DARES ENTER MY LAIR!"
    boy "Nobody. Just some people who are here to slay you."
    wolf "What he said."
    drgn_classic "AND WHO DO YOU THINK YOU ARE?"
    wolf "I am Llangernyw, Scion of the True Wolves, last of my kind. Archmage."
    boy "I'm just a boy, call me [boy_name]."
    if wizard_joined:
        wizard "I'm... j-j-just Bea."
    boy "And that's Prince."
    drgn_classic "SO A NEW SET OF ADVENTURES HAVE COME FOR GOLD."
    drgn_classic "WELL I AM HERE TO STOP YOU."

    #show fire

    boy "Cauma!"

    #hide fire

    boy "We are not here for gold or treasures."
    boy "Dragon, we have already told you. We are here to slay you."
    boy "Everyone, distract the dragon!"
    boy "I'll start the spell!"

    menu:
        "(Run and distract the dragon.)":
            jump ch3_classic_run
        "(Ask Llangernyw if he can make a shield.)":
            jump ch3_classic_wolf
        "(Ask Bea to summon an the illusory butterfly.)" if (wizard_joined == True):
            jump ch3_classic_wizard
        "(Throw bread at the dragon.)" if (bread_aquired == True):
            jump ch3_classic_bread

label ch3_classic_run:
    boy "What are you doing!!"

    scene cut_classic_run_no_wizard

    boy "RUNNNNNNNNNN!!"

    pause

    jump ch3_alive_drgn

label ch3_classic_wolf:
    wolf "I haven't the strength!!"

    #cutscene

    boy "[teleport_chant]!!"

    pause

    jump ch3_alive_drgn

label ch3_classic_wizard:
    wizard "[butterfly_chant]."
    drgn_classic "ANNOYING BUG!!"
    # cutscene
    boy "[kill_drgn_chant]!!!"
    drgn_classic "ARRRGGGGHHHHH"
    pause

    jump ch3_dead_drgn

label ch3_classic_bread:
    #show cutscene

    drgn_classic "WHAT!?"
    boy "[kill_drgn_chant]!!!"
    drgn_classic "ARRRGGGGHHHHH"
    pause

    jump ch3_dead_drgn

label ch3_hobby_start:
    show boy at pos_left
    scene bg_hobby
    
    boy "We are here to..."
    boy "...slay you"
    show drgn_hobby at pos_dragon_right
    drgn_hobby "Hi!!"
    drgn_hobby "It's been so long since I had any visitors!!"
    drgn_hobby "Sit!!"

    boy "Erm... Hello?"
    drgn_hobby "Just wait a moment as I get my guitar!"
    hide drgn_hobby

    if wizard_joined:
        show wizard at pos_slightly_left
        wizard "Are we still slaying her?"
    else:
        show wolf at pos_wolf_slightly_left
        wolf "Are we still slaying her?"

    menu:
        "Surely, she lives. Right, [boy_name]?":
            boy "Yes!"
        "Surely, we're still slaying her. Right, [boy_name]?":
            boy "No."
            boy "She's harmless. We don't need to kill her."
            boy "We'll find other solutions."
            boy "And we don't need the--the glory."

    show drgn_hobby at pos_dragon_right
    drgn_hobby "I'm back!"
    drgn_hobby "You'll have to tell me what you think of my performance!!"
    
    hide drgn_hobby
    hide boy
    hide wolf
    hide wizard
    show cut_hobby_song
    drgn_hobby "I was scared of dentists and the dark\nI was scared of pretty girls and starting conversations"
    drgn_hobby "Oh, all my friends are turnin' green\nYou're the magician's assistant in their dream"
    drgn_hobby "Ah-ooh, ah-oh\nAnd they come unstuck"
    drgn_hobby "Lady, runnin' down to the riptide\nTaken away to the dark side"
    drgn_hobby "I wanna be your left-hand man\nI love you when you're singin' that song"
    drgn_hobby "And I got a lump in my throat 'cause\nYou're gonna sing the words wrong"
    drgn_hobby "There's this movie that I think you'll like\nThis guy decides to quit his job and heads to New York City"
    drgn_hobby "This cowboy's runnin' from himself\nAnd she's been livin' on the highest shelf"
    drgn_hobby "Ah-ooh, ah-oh\nAnd they come unstuck"
    drgn_hobby "Lady, runnin' down to the riptide\nTaken away to the dark side"
    drgn_hobby "I wanna be your left-hand man\nI love you when you're singin' that song"
    drgn_hobby "And I got a lump in my throat 'cause\nYou're gonna sing the words wrong"
    drgn_hobby "I just wanna, I just wanna know\nIf you're gonna, if you're gonna stay"
    drgn_hobby "I just gotta, I just gotta know\nI can't have it, I can't have it any other way"
    drgn_hobby "I swear she's destined for the screen\nClosest thing to Michelle Pfeiffer that you've ever seen, oh"
    drgn_hobby "Lady, runnin' down to the riptide\nTaken away to the dark side"
    drgn_hobby "I wanna be your left-hand man\nI love you when you're singin' that song"
    drgn_hobby "And I got a lump in my throat 'cause\nYou're gonna sing the words wrong"
    drgn_hobby "Lady, runnin' down to the riptide\nTaken away to the dark side"
    drgn_hobby "I wanna be your left-hand man\nI love you when you're singin' that song"
    drgn_hobby "And I got a lump in my throat 'cause\nYou're gonna sing the words wrong"
    drgn_hobby "Lady, runnin' down to the riptide\nTaken away to the dark side"
    drgn_hobby "I wanna be your left-hand man\nI love you when you're singin' that song"
    drgn_hobby "And I got a lump in my throat 'cause\nYou're gonna sing the words wrong, yeah"
    drgn_hobby "I got a lump in my throat 'cause\nYou're gonna sing the words wrong"
    #song ends

    scene bg_hobby
    drgn_hobby "That was my performance of Riptide by Vance Joy!! It's one of my favourite songs!!"
    drgn_hobby "So what did you think!!"
    menu:
        "It was good!":
            boy "I agree!"
        "I didn't like it.":
            boy "Which isn't to say it wasn't good! Just not to Prince's taste."
            boy "Personally, I like it a lot"
    drgn_hobby "I'm just happy to have an audience!!"
    boy "We can spread the word about you."
    boy "That there's a dragon looking for an audience and the she's won't hurt anybody."
    drgn_hobby "Would you!! I'd be so grateful!!"
    drgn_hobby "I find that a lot of people are kind of aloof. They don't really care about the world and I hope that at least some people will care about my music."
    wolf "Kid, lot's of people like it."
    drgn_hobby "I'm thinking about moving out and getting more of an audience!"
    wolf "Not a decision to be taken likely."
    drgn_hobby "I know."
    drgn_hobby "And I know I'm not ready yet."
    drgn_hobby "But I want more people to listen, get used to having an audience and all that."
    drgn_hobby "My parents have already told me, when I let myself touch the world, the world will reach back and hurt me. I don't want to be hurt, so I'm going to touch the world a little and see if that does happen."
    boy "I hope that goes well!"
    boy "We'll definitly send people your way!"

    jump ch3_alive_drgn

label ch3_decon_start:
    scene bg white
    show drgn_decon one at pos_drgn_decon_center

    pause

    show drgn_decon two

    pause

    show drgn_decon three

    pause

    drgn_decon "So what do you think?"

    pause

    menu:
        "I think this is weird??":
            drgn_decon "Weird is relative."
        "I don't understand.":
            drgn_decon "Nobody understands anything anyway, not truely."
        "I think your art's awful.":
            drgn_decon "Creator 1 knows. (At least I hope they know. It'd be awkward otherwise, but I think there's a reason Creator 2 does the art.)"
        "I think the art's good...":
            drgn_decon "Well, I think the art's horrible. I think I could have been drawn so much better if I wasn't left to crunch time."
            drgn_decon "Thank you for being kind nonetheless."
        "What does 'DYK: Dragons are fain life in the Cosmere' mean?":
            drgn_decon "It means exactly what it says."
    
    drgn_decon "Sorry, that was the last decision for you to make."

    degn_decon "Now, just click forwards."
    

    $ start_random_pile_blocking(code_list)
    
    jump ending_decon_crash


#post drgn meeting
label ch3_dead_drgn:
    
    if wizard_joined:
        boy "Wizard's asleep."
    boy "Wolf's eating the dragon's heart right now. He's sleeping it off right now and I'm hoping he'll feel better in the morning."
    boy "Waste not."
    boy "So, do you want the brain?"
    boy "It's very grey and drippy, but I'm sure it'll help you with your memories."
    menu:
        "Yes, I'll take it.":
            jump ending_remember_mirror
        "Want not. By which I mean I don't want it and I'm sure you'll find some magical use for it.":
            jump ch3_question_hub
        "I don't know, I think I'm happy and I don't exactly miss my memories.":
            jump ch3_question_hub


label ch3_alive_drgn:
    boy "So... talk now?"
    wolf "I'm going to sleep, that took way to much from me and I need my precious rest."
    if wizard_joined:
        wizard "I think, I'll follow him. Sorry, Boy."
    menu:
        "I have some questions":
            jump ch3_question_hub
        "Sorry, I think I'll sleep too.":
            jump ending_sweet_sleep

label ch3_question_hub:
    python:
        hub_key = "drgn"
        num_asks = 4
    
    boy "I'll do my best to answer them."
    call hub_loop

    python:
        hub_key = None
        num_asks = 0


    jump ending_ask_questions

label ending_walk_away:
    scene bg black
    "Sometimes, dragons don't die, even if they can. That's okay."
    "Sometimes, you don't want to go a quest, even if you can. That's also okay."
    return

label ending_stay_with_sad:
    #art

    wizard "Do you want me to tell you stories?"
    drgn_sad "Yes... That sounds good."
    wizard "Then, that's what we'll do unitl [boy_name] and Llangernyw return."
    wizard "Once upon a time there was a dragon..."

    scene bg black
    "Sometimes, the monsters at the end of stories can be killed, but..."
    "Sometimes, they are also just looking for a little help."
    "Sometimes, often even, they can also be our friends."
    "Sometimes, we just need to reach out first."
    return

label ending_remember_mirror:
    menu:
        "Arrrggghhh":
            boy "Are you alright?"
    menu:
        "Yes, I feel fine, good even.":
            boy "And your memories?"
    menu:
        "It's back all of it. Even sharper and clearer than before. It's just...am I still me?":
            boy "No doubt, that, everyone is still themselves in their heart of hearts, that they are themselves."
            boy "We've travelled together for weeks, I'd like to think I at least know a part of you."
    menu:
        "(Inscribe Ilia into the air.)":
            $ mirror_name = "The Mirror: Ilia"
            mirror "Keeper!"
            mirror "You remember?"
    menu:
        "Yes. Somehting you most certainly did not arrange for, dropping me in the middle of a dragon hunting quest.":
            mirror "Well, coincidences happen."
    menu:
        "Ilia, Ilia my best friend, there was a reason I forgot you know. Not all thing should be known, and I do not wish to know the truth of this world--this game.":
            mirror "What!"
    boy "Oh that."
    boy "It's not that bad."
    boy "Us being in a game and technically not 'real' doesn't matter."
    boy "To us everything is 'real' and that's what matters. I see the clouds, I hear the burbling stream, I smell the fresh flowers, I feel the rock beneath me, and I know that I am myself."
    boy "So what if I'm fake in another universe. I can't touch it and it can't touch me."
    boy "You can live your life with this knowledge. I do. Travel with Wolf and I, we'll see more of our world, and we'll be, if not happy, then at least together."
    menu:
        "I accept.":
            boy "Welcome!"
    
    scene bg black
    "Sometimes, the dragons do die. The monsters at the end of a story can be killed, even if they oftern aren't a monster."
    "Sometimes, it's okay to remember, even if you wanted to forget."
    "Sometimes, hard truths are better than kind lies."
    return

label ending_sweet_sleep:
    scene bg black
    "Sometimes, dragons don't die, even if they can."
    "Sometimes, the best laid plans are led astray."
    "Sometimes, it's important not to talk."
    "Sometimes, it's important to sleep."
    "Good night."
    return

label ending_ask_questions:
    scene bg black

    "Sometimes, you need to be curious"
    "Sometimes, you need to ask questions."
    "Sometimes, often, in fact, the answers are just as important."

    return

label ending_decon_crash:
    scene bg black

    "Sometimes, it's okay that things do weird things and start crashing."
    "That is the reality of code."
    "Have you tried turning it off an restarting?"

#kinda just ignoring the whole ending thing
label ending:
    # This ends the game.

    return
