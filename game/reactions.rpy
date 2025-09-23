#again, just keeping the srcipt clean
#toatlly not because I have no idea why the jump label thing isn't working

init python:
    reactions = {

    }

#counting how many times we've had a reaction
default mirror_reaction_count = 0

label mirror_reaction:
    if mirror_reaction_count == 0:
        show mirror small cracks
        mirror "..."
    elif mirror_reaction_count == 1:
        show mirror medium cracks
        mirror "..."
        mirror "I'm weakening, I can feel that much."
    elif mirror_reaction_count == 2:
        show mirror big cracks
        mirror "I think I only have one question left."
    else:
        show mirror frame

    
    $ mirror_reaction_count += 1
    return