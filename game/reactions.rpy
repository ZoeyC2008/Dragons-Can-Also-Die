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
    python:
        wolf_magic_slideshow_count += 1
    return
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
    
    return

label sojourn_story_one:
    $ sojourn_name = "The Sojourner: E Meng"
    sojourn "Thank Heavens, thank Earth."
    sojourn "I'm pretty sure only Miss Pepper has asked about my journey so far."
    sojourn "And it's only when I speak of my journey, my voyage, that I can freely use all sounds without anticipating a new nightmare to come upon me in the dead of night."
    sojourn "So was their anything specific you wanted to ask about?"
    $ sojourn_name = "Man in Midst of Sojourn: 噩梦"
    return

label sojourn_story:
    $ sojourn_list = ["sojourn_cinderella", "sojourn_snegurochka", "sojourn_zhuangzi"]

    $ random_call_from_list(sojourn_list, True)
    return

label sojourn_cinderella:
    $ sojourn_name = "The Sojourner: E Meng"
    
    sojourn "Just before I arrived at the village, there was a big castle--not a palace, for it wasn't so big to be a city onto itself--but I think it was the biggest castle I'd seen so far."
    sojourn "The royals let be stay as a guestroom and told to be up before the evening."
    sojourn "As if, for it was already near evening and I refused to let something like that get eh better of my rest, I would leave my morning anyhow."
    sojourn "I was collapsed on the bed only to be awoken by celebratory sounds. I ducked my head out to ask a passing servant about what the fuss was."
    sojourn "By then, I had an excellent grasp of many of the local languages, horrible as they are--whoever thought of all those articles should rot in diyu, not to mention all those stupid verbs that seem to do something different when you so much as breath on them."
    sojourn "I was informed that the prince was looking for a bride and thus hosting a ball."
    sojourn "I did not quite understand his train of thought, when he should have just went to a matchmaker."
    sojourn "I realized the revelry would go on through the night and I would not, in fact, be returning to my beutiful sleep."
    sojourn "On what to spend the rest of the night, I could join the festivities, but I did not have the fortitude to face any foreign nobles."
    sojourn "So instead, I went down to the kitchens to help out with the servants, washing the china plates that were constanly sent back down and returned up piled with more food."
    sojourn "I was rather happy to make passing talk with the servants and they too were curious about my sojourn. They praised the marvels of my home, they furrowed brows at the strangenss I found just passed it, and shuddered at frigidness of both this kindgom and even further North."
    sojourn "I found it strange why anyone would live up here, why abide half the year in discomfort and then find joy in summers that were often colder that the winter's of my home."
    sojourn "I could not comprehend their mentality and I would never walk paths beneath needled trees when I could be walking between bamaboo groves."
    sojourn "I left later that same night, once the party had begun to died down and I could avoid any nobles on my way out."
    sojourn "I passed more than a few drunk stranglers, when I reached the door and the grand, sweeping staircase, there was a young man moaning about true love and holding a glass slipper."
    sojourn "When he saw me he lept up in a display of fine motor skills which led me to the rather suprising conclusion that he was not, in fact, drunk."
    sojourn "He asked me about a women and proceeded to describe in great detail, and talking about how she must fit the slipper in his hand."
    sojourn "I politely asked what this young women's name was, he told me he did not know."
    sojourn "I informed him that I did not know any of the guests and he slumped back in the perfect posture of disappointment."
    sojourn "The young man, without any prompting, declared the women to be his one true love. I slowly fled from the conversation before he can tell me the exact number of hairs or something equally ridiculous."
    sojourn "The next night, I slept under a canopy of stars, back against frost and wind playing a melancholic tone through the leaves."
    sojourn "I stared at the constellations, unchanging no matter where I was in the world, they are not flighty, unlike that prince who'd declared his true love after one night."
    sojourn "I think I shall never understand his instantaneous passion for someone he did not truely know, and I find those people to be just as swift falling out of love as he did falling in it."

    $ sojourn_name = "Man in Midst of Sojourn: 噩梦"
    return

label sojourn_snegurochka:
    $ sojourn_name = "The Sojourner: E Meng"
    
    sojourn "Snegurochka and her family are one of my few good memories from winter in the North."
    sojourn "I had made it past their little town, not all that different from this one, in the bleakness that everyone feels after winter properly sets in."
    sojourn "Their house was far off and in the direction I was heading in, and they welcomed me for the night."
    sojourn "The couple were elderly and I would have thought Snegurochka to be their grand-daughter had tehy not told me she was, in fact, their daughter. I did not pry, for it is not that stragne to have children far into old age."
    sojourn "I had an excellent night's rest by the living room fire as I was not so impolite to intrude on one of their rooms. It was warmth in a way I don't think I've ever experienced."
    sojourn "One cannot know true warmth without first experiencing the bitter cold, they are opposites yet cannot exist without the other."
    sojourn "Similarily, who better than one in eternal summer to know the relief of a cold drink."
    sojourn "The next day, I walked on at break of dawn. I knew if i stayed the nightmares would truely start, softly at first than escalating."
    sojourn "Snegurochka accompanied me for almost half a day for she had not much else to do."
    sojourn "I admit I was quite jealous of how unaffected she was by the icy chill and of how she gilded through the snowy landscape with ease while it seemed to be that with every step I took, I would sink down at least two or three palms."
    sojourn "On the way we spoke. I told her of my sojourn, of the lush forests and sweeping waterfalls."
    sojourn "Snegurochka talked of the festival she had recently attended, that she had made her first friend there and that she danced with a young man. She was now pondering whether she should return to the town and meet with her new friends."
    sojourn "I did not give my opinion, for the effort to keep relationships alive should be up to one's own ability."
    sojourn "I myself had a well trained carrier pidgeon that I used to conect with my family. In those Northern states she would spend weeks between journeys recovering on my families estate."
    sojourn "By the time Snegurochka left me at the edge of the forest, she had talked herself into and out of going to the village several times over."
    sojourn "Although I do not know what she chose in the end, I hppe she went back since I felt an aching in her, a lonliness that could only be cured through close friends."
    sojourn "Perhaps she herself did not feel this lonliness, as the cold man does not know he is cold until they feel the warmth of fire, the lonly man does not know he is lonly until they feel the warmth of companionship."
    
    $ sojourn_name = "Man in Midst of Sojourn: 噩梦"
    return

label sojourn_zhuangzi:
    $ sojourn_name = "The Sojourner: E Meng"
    
    sojourn "I did not think my home wonderous until I left it. These days, I can scarcely even recall the call of pheasants, the taste of fine rice, or the sound of the bubling stream ran near our home."
    sojourn "I dare not go back of course, for if I did my nighmares would overtake me. When I was younger they, too, were weaker, but I shudder now to think of what may await me if I do return."
    sojourn "Thus, like one of your dragons, I must hoard what few memories I do have, least they flee away to the sea of oblivion."
    sojourn "However, one memory that has not and will not wade, nor do I wish it to, is that of the man I met on the bridge over that stream. I was young then, but around the age to start questioning the world around me and, foolishly, expect an answer."
    sojourn "I do not remember how both of us found ourselves on the bridge, what I don remeber is the conversation that would follow."
    sojourn "The stranger pointed at the fish and told me they looked happy and free."
    sojourn "I laughed, and said that he was not fish, so how could he possible know what fish thought. Back then, I had an understanding that because I wasn't an adult I could not understand how they thought."
    sojourn "I know better now, no one can know what others truely think, and the best we can do is try to be empathetic. Of course, that doesn't stop me from thinking some people to be rather ridiculous, but I'm certain they had their own reasons."
    sojourn "If I was back there now, I would likely tell that man that the fish were only acting happy and free and that there was no way to divine their true feelings."
    sojourn "But alas, I am not, and it was my precocious younger self in that conversation, so you will have to forgive the lack of better logic."
    sojourn "Thankfully, the man did not take offense to laughter and actually started laughing with me. He said, with all the confidece of a great elephant, that I was also not him and thus could not know that he did not know the joy of fishes."
    sojourn "Back then, I accepted this as flawless magic and made no further argument."
    sojourn "He then asked me of my dreams."
    sojourn "It was a simple request, but even my dreams back then were filled with terror. In fact, this was how I earned my name, E Meng, it means nightmare and that was what had chased me across the world."
    sojourn "I told him of them and each time he was able to twist them into something harmless."
    sojourn "The hungry foxes did not want to eat me, for they were just looking for their lost cubs. And do on and so forth, that men had a way of spinning the worst dreams into something almost comforting."
    sojourn "Once I was a butterfly caught in a storm, wings wet and being churnned head over heel."
    sojourn "He told me to think of myself not as caught in the storm for we all our cauht in the storm of life, but that the storm would guide me somewhere and that as a butterfly, I could drift in the winds and behold all the world had to offer."
    sojourn "This is what I have become, in its own way, a butterfly fluttering from place to place, beholding all that I could see."
    sojourn "At this the man told me that in a strange coincidence he had also had a butterfly dream. And that for both of us to have such dreams, perhaps we were not men dreaming of butterflys, but rather butterflys dreaming of being men."
    sojourn "In truth I found this stupid, I wasn't anything that I found only in the dream world. That is known. And I told the man that much."
    sojourn "What happened after that is much blurrier. And if the man ever told me his name, I do not recall now."
    sojourn "But I am glad to have at least one clear memory of my home, of the little stream, of the willow trees on the grave, and despite how much I hated it at the time, the crows that would caw from the treetops."
    sojourn "No matter how far I wander on my sojourn, I am not lost for I know my home, I know that is where I'll return at the end of my life."

    $ sojourn_name = "Man in Midst of Sojourn: 噩梦"
    return

