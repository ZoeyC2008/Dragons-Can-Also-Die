# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#make dynamic colour, cause deconstructed wants to be weird
define drgn_decon_color = "#000000"

#make dynamic names: (i think this works?)
define boy_name = "" #Boy is namable by the player, real name is Sasha
define boy_display_name = "The Boy: "+boy_name
define sojourn_name = "Man in Midst of Sojourn: 噩梦" #With 'e's: The Sojourner: E Meng
define mirror_name = "The Mirror" #In recover the past ending, The Mirror: Ilia


#@Naomi are we putting char in front of the characters? e.g. char_boy??
define mirror = Character(mirror_name, color="#e0dddd")
define boy = Character(boy_display_name, color="#ba0f0a")
define wolf = Character("The Wolf: Youagi", color="#90a3b0")
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
#Boy!
image boy = "boy_default.png"
image boy snarky = "boy_snarky.png"
image boy shock = "boy_shocked.png"

#Wolf
image wolf = "wolf_default.png"

#backgrounds (I ledgitemently think this is the hardesd part)
image bg forest path = "bg_forest_path.png"

#let's also define some image positions!
define wolf_ypos = 1100

define pos_slightly_left = Position(xalign=0.35, yalign=0.5)
define pos_left = Position(xalign=0.15, yalign=0.5)
define pos_wolf_center = Position(xalign=0.5, ypos=wolf_ypos)

#Game variables (the idea is that these dictate what dragon you get)
default royal = 0 #depressed, a classic subversion for a classic prince/ss
default aloof = 0 #happy, you have to be grounded to enjoy life, don't be aloof all the time
default decon = 0 #classic, it's not a proper deconstruction if everything is different
    #if none of the thresholds are met, deconstructed since you haven't made personality choices

init python:
    #amount to add
    add_most = 16
    add_some = 10
    add_little = 6
    add_tiny = 2
    subtract_tiny = -2
    threshold = 40

# The game starts here.
#Chapter 0
label start:
    #shadow puppet of a prince and princess

    #initial choices
    "...And so they lived, happily ever after."
    
    #first menu, mirror opening
    menu mirror_opening:
        "That was lovely. I'm glad they found joy after all their hardships.":
            $ royal += add_most
        "That is such a cliche. Happily ever after doesn't exist, it's just a tad unrealistic.":
            $ decon += add_most
        "I don't care. There was nothing for me to be emotionally invested in, thus 'happily ever after' doesn't matter one bit.":
            $ decon += add_some
            $ aloof += add_some
        "That was boring. Next.":
            $ aloof += add_most
        
    jump mirror_question_hub

label mirror_question_hub:
    #show mirror_whole
    #set hub
    python:
        hub_key = "mirror"
        num_asks = 4
    
    call hub_loop
    
    jump mirror_end

label mirror_end:
    #reset the hub
    python:
        hub_key = None
        num_asks = 0
    
    mirror "I suppose one of us doesn't have any time left."
    mirror "I hope to see you soon, after I've rested."
    mirror "And I hope you'll recieve me then."

    jump meet_boy

#Chapter 1
label meet_boy:
    scene bg forest path
    show boy at pos_left
    

    boy "Wake up!"
    
    boy "This is wolf:"

    show wolf at pos_wolf_center
    wolf "*I am a cynical wolf.*"

    show boy snarky
    boy "I'm shocked, shocked that Wolf would say that."

    show boy -snarky
    boy "We're just saying test statements, really."
    
    return #no idea why it's not returning to start, oh well

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

#kinda just ignoring the whole ending thing
label ending:
    # This ends the game.

    return
