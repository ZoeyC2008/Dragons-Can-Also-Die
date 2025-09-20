# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#@Naomi are we putting char in front of the characters? e.g. char_boy??
define mirror = Character("The Mirror")
define boy = Character("The Boy" + boy_name)
define wolf = Character("The Wolf:")
define wizard = Character("The Wizard: Bea")
define innkeeper = Character("The Innkeeper: Pepper")
define shephed = Character("Herd Shep: Rath'la Dnar")
define sojourn = Character(sojourn_name)
define miller_son = Character("Miller's Mischieveous Moppet: Much")
define drgn_classic = Character("Classic Dragon") #@Naomi is Furious better than Classic?
define drgn_sad = Character("Depressed Dragon") #logic here is that decon also starts with d
define drgn_happy = Character("Joyous Dragon")
define degn_decon = Character("drgn_decon") #I think it makes sense for decon to use her in code name


#Some characters need different names
$ boy_name = ""
#Boy is namable and he'll later choose Sasha
$ sojourn_name = "Man in Midst of Sojourn: 噩梦" 
#This will change to The Sojourner: E Meng when he's telling the stories of his journey


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
