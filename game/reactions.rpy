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

label wolf_sleep:
    wolf "I'll leave you youngsters to the camp."
    wolf "These old bones need their rest."
    hide wolf

        
label wolf_magic_slideshow:
    #we'll figure this our

#the travel ellipsis saga!
default ellipsis_count = 0
label ellipsis_saga:
    
    python:
        ellipsis()
        #math of ellipsis
        conversation_count = 0
        conversation_count += (travel_day-1) * 2
        if not travel_early_flag:
            conversation_count += 1
    
    if ellipsis_count != conversation_count:
        boy "Common on, I've heard you talk before. Don't go all quiet on me now."
        $ travel_ellipsis_flag = False
    elif ellipsis_count == 0:
        boy "You're really quiet, aren't you? Just like Wolf, he doesn't much like talking either."
        wolf "Boy, you'd do well enough to leave them alone if they aren't going to talk to you."
        boy "If you don't want me chattering, just say something, won't you."
    elif ellipsis_count == 1:
        boy "It's okay if you don't wan to talk and all. I'm just really happy you're listening, it's not like Wolf does that."
        boy "I think he might be tired with me. I mean, we've been travelling together for years now and I'm not exactly the best student and all that."
    elif ellipsis_count == 2:
        boy "So like, I'm not exacly talented at magic. No background and all that, didn't know a single rune, spell, or charm before Wolf started on theory and couldn't channel mana for life."
        boy "I'm really grateful that Wolf has stuck with me this whole time. If he's half of what he says he was, then he could have any apprentice he wants."
        boy "Instead there's just me, someone completely new to magic."
    elif ellipsis_count == 3:
        boy "Without Wolf, I would have never known the magic, of well, magic."
        boy "It's one of the best things that's happened to me in life."
        boy "And I adore it."
    elif ellipsis_count == 4:
        boy "I know Wolf wants to give lessons in magic. Don't always listen to him!"
        boy "Anytime you mention magic, he'll say something completely out of pocket! But I love those lectures and bad powerpoints anyways, they feel like peaks into other worlds that I can't even imagine."
        boy "That's my favourite thing about magic as well; It overturns the laws of this world anf makes the impossible possible."
    elif ellipsis_count == 5:
        boy "Like me."
        boy "I had the opportunity to reshape my body--not entirely sure, but enough that I feel at home in it now."
        boy "It let the outside see how I felt on the inside."
        boy "How can that be anything short of a miracle."
    elif ellipsis_count == 6:
        boy "You know, I left home precisly because I my body didn't feel right."
        boy "Mama probaly would have forced me into marriage and find a 'man' to take care of me."
        boy "Magic offered me an escape from that."
        boy "And so I'm here, in this forest, with you and Wolf, on a quest to slay a dragon."
    elif ellipsis_count == 7:
        boy "I don't even know what more I could talk about right now."
        boy "You've made feel really comfortable."
        boy "Let's go to sleep, we'll make it to the village tomorrow."
