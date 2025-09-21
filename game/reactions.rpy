#again, just keeping the srcipt clean
#toatlly not because I have no idea why the jump label thing isn't working

init python:
    reactions = {

    }

#counting how many times we've had a reaction
default mirror_reaction_count = 0

label mirror_reaction:
    if mirror_reaction_count == 0:
        #show mirror_small_cracks
        mirror "One."
    elif mirror_reaction_count == 1:
        #show mirror_medium_cracks
        mirror "Two."
    elif mirror_reaction_count == 2:
        #show mirror_big_cracks
        mirror "Three."
    else:
        #show mirror_fractured
        mirror "Four."
    
    $ mirror_reaction_count += 1
    return