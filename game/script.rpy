# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define dynamic colour, cause deconstructed wants to be weird
define drgn_decon_color = "#000000"

#define dynamic names: (i think this works?)
define boy_name = "The Boy" #Boy is namable by the player, real name is Sasha
define sojourn_name = "Man in Midst of Sojourn: 噩梦" #With 'e's: The Sojourner: E Meng
define mirror_name = "The Mirror" #In recover the past ending, The Mirror: Ilia


#@Naomi are we putting char in front of the characters? e.g. char_boy??
define mirror = Character(mirror_name)
define boy = Character(boy_name, color="#ba0f0a")
define wolf = Character("The Wolf:", color="#90a3b0")
define wizard = Character("The Wizard: Bea", color="#6f4685")
define innkeeper = Character("The Innkeeper: Pepper", color="#028a0f")
define shephed = Character("Herd Shep: Rath'la Dnar", color="#ffda03")
define sojourn = Character(sojourn_name, color="#001f3d")
define miller_son = Character("Miller's Mischieveous Moppet: Much", color="#be5504")
define drgn_classic = Character("Traditional Dragon", color="#ff2400") #@Naomi is Furious better than Classic or Traditional?
define drgn_sad = Character("Depressed Dragon", color="#2c3e4c") #logic here is that decon also starts with d
define drgn_happy = Character("Joyous Dragon", color="#0492c2")
define degn_decon = Character("drgn_decon", color=drgn_decon_color) #I think it makes sense for decon to use her in code name

#Game variables (the idea is that these dictate what dragon you get)
init python:
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

#mirror needs a variable to keep track of how many times we've been to the hub
$ mirror_hub_count = 0

label mirror_question_hub:
    call hub_loop("mirror", 4)
    
    mirror "I see neither of us have any time left. I hope to see you soon, after I've rested."


#Chapter 1
label meet_boy:
    boy "Wake up!"
    

#kinda just ignoring the whole ending thing
label ending:
    # This ends the game.

    return
