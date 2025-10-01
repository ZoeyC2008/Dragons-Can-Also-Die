#this is to keep script clean
#I'm using a data-driven prerequisites (understanding? No, copy & paste code form internet is good)

init 1 python:
    #the big list of questions (20/09 i wonder if it'll be longer than the script?)

    questions = {
        #really long, but this is basically all the text i need for my question hubs
        #which are like, a good half? of the game, and where most of the exploration is
        
        #mirror hub
        "mirror_where":{
            "title":"Where am I?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"We are anywhere you want to be--a forest, a town, a cavern, a castle."},
                
                {"who":"mirror", 
                "text":"Any of it, all of it, remains the same."},
                
                {"who":"mirror", 
                "text":"After all, we are in a dream within a dream."},
                
                {"choices":[
                    {"text":"Then I would like to be in my castle.", 
                    "effects":{"royal":add_most}},
                
                    {"text":"A dream is a delight.", 
                    "effects":{"decon":add_some, "aloof":add_some}},
                
                    {"text":"It's like you said then, where I am doesn't matter.", 
                    "effects":{"aloof":add_most}},
                
                    {"text":"A forest is of mine would be relaxing.", 
                    "effects":{"royal":add_little, "decon":add_little, "aloof":add_little}}
                ]}
            ],
            "hub":"mirror",
            "requires":[]
        },

        "mirror_wakeup":{
            "title":"Wake up!",
            "answer_lines":[
                {"who":"mirror", 
                "text":"...I see."},

                {"who":"mirror", 
                "text":"That is your choice"},

                {"choices":[
                    {"text":"Or, or maybe I don't want to.",
                    "effects:":{"royal":add_little, "decon":add_little, "aloof":add_little}},
                    {"text":"Wake up! Wake up! WAKE UP!",
                    "jump_label":"ch0_mirror_end"}
                ]}
            ],
            "hub":"mirror",
            "requires":["mirror_leave"]
        },

        "mirror_dream":{
            "title":"What is a dream within a dream?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"You were asleep, and in that sleep you lay in dream."},
                
                {"who":"mirror", 
                "text":"It doesn't concern either of use what that dream was about."},
                
                {"who":"mirror", 
                "text":"But then, I pulled you into this dream."},
                
                {"who":"mirror", 
                "text":"Thus, we are in a dream within a dream."},
                
                {"choices":[
                    {"text":"You're wrong. This is two sequesntial dreams, a dream within a dream means that I fell asleep in a dream and then began another, not this.", 
                    "effects":{"decon":add_most}},
                    
                    {"text":"I am special! If a strange mirror took attention to me, I must be.", 
                    "effects":{"royal":add_most}},

                    {"text":"Now that I've heart that, I've realized that being in 'a dream within a dream' isn't anything to concern myself more than any other dream.", 
                    "effects":{"aloof":add_most}},

                    {"text":"But I know what my dream was! It was a prince and princess getting their happily ever after.", 
                    "effects":{"royal":add_some, "decon":add_some}}
                ]}
            ],
            "hub":"mirror",
            "requires":["mirror_where"]
        },

        "mirror_pull":{
            "title":"Why did you pull me into another dream?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"I don't know."},

                {"who":"mirror", 
                "text":"I suppose it felt right."},

                {"choices":[
                    {"text":"Well, I know why. It's because I'm special.", 
                    "effects":{"royal":add_most}},
                    
                    {"text":"I suppose it doesn't matter, I'm here anyway.", 
                    "effects":{"aloof":add_most}},
                    
                    {"text":"That's stupid, people--er things don't just forget their motivations.", 
                    "effects":{"royal":add_some, "decon":add_some}},
                    
                    {"text":"It must be for what's going to happen next...", 
                    "effects":{"decon":add_most}}
                ]}
            ],
            "hub":"mirror",
            "requires":["mirror_dream"]
        },

        "mirror_other_dream":{
            "title":"What isn't that other dream important?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"Because it doesn't concern the present."},

                {"who":"mirror", 
                "text":"It could of been of flight, of stress, of a grand never-ending tale, but none of these would change that I am talking to you, in the here, in the now."},

                {"choices":[
                    {"text":"You're right, I was always meant to talk to you", 
                    "effects":{"royal":add_most}},
                    
                    {"text":"You're right, nothing matters anyway.", 
                    "effects":{"aloof":add_most}},
                    
                    {"text":"You're wrong, there was a prince and a princess, that had to mean something...because if they didn't, doesn't that mean I also mean nothing...", 
                    "effects":{"royal":add_some, "decon":add_some}},
                    
                    {"text":"You're wrong, I made an opinion about that dream. It may not have been a good opinion or a correct opinion, but it was an opinion nonetheless that dream must have meant something, to me if no one else.", 
                    "effects":{"decon":add_most}}
                ]}
            ],
            "hub":"mirror",
            "requires":["mirror_dream"]
        },

        "mirror_leave":{
            "title":"How do I leave this--this dream?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"Wake up."},
                
                {"choices":[
                    {"text":"So like any other dream.", 
                    "effects":{"aloof":add_most}},
                    
                    {"text":"I knew that much, but I don't know if this could be like a nightmare, a dream from which I can't simply 'wake up'.", 
                    "effects":{"decon":add_most}},
                    
                    {"text":"That sounds almost too simple, there must be a catch for such a unique situation.", 
                    "effects":{"royal":add_some, "decon":add_some}},

                    {"text":"Since this is lucid, I can wake myself up if I so choose", 
                    "effects":{"royal":add_little, "decon":add_little, "aloof":add_little}}
                ]}
            ],
            "hub":"mirror",
            "requires":["mirror_where"]
        },

        "mirror_what":{
            "title":"What are you?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"I am a mirror."},
                
                {"who":"mirror", 
                "text":"But I am also you."},
                
                {"who":"mirror", 
                "text":"And all I know is that for every question asked I lose a little more of 'myself'."},
                
                {"choices":[
                    {"text":"That doesn't make sense!", 
                    "effects":{"royal":add_little, "decon":add_little, "aloof":add_little}},
                    
                    {"text":"You can't be me, you're not - you're not special", 
                    "effects":{"royal":add_most}},
                    
                    {"text":"So I'm playing as a mirror, okay, okay, okay.", 
                    "effects":{"decon":add_most}},

                    {"text":"I think what you 'represent' doesn't matter. You're just here to answer my questions.", 
                    "effects":{"royal":add_some, "aloof":add_some}}
                ]}
            ],
            "hub":"mirror",
            "requires":[]
        },

        "mirror_made_of":{
            "title":"But what are you made of?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"..."},
                
                {"who":"mirror", 
                "text":"Silver and glass and starlight and nothing more."},

                {"who":"mirror", 
                "text":"Later on, a hint of magic was added by my then keeper."},

                {"who":"mirror", 
                "text":"They told me to be free, as if that's something I can just be..."},

                {"choices":[
                    {"text":"Aha, so you want to be me since I'm something you're not.", 
                    "effects":{"royal":add_most}},
                    
                    {"text":"So I'm talking to a magic mirror like the Evil Queen...fascinating.", 
                    "effects":{"decon":add_most}},
                    
                    {"text":"You're keeper was foolish, an ordinary mirror, no matter how magic was added can be 'free', whatever that means.", 
                    "effects":{"royal":add_some, "aloof":add_some}},
                    
                    {"text":"I need not be concerned with what a former person wanted...but it doesn't feel--no, I am not concerned with...with that.", 
                    "effects":{"aloof":add_most}}
                ]}
            ],
            "hub":"mirror",
            "requires":["mirror_what"]
        },

        "mirror_am_me":{
            "title":"How can you be 'me' if 'I' am 'me'?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"There can always be more than one 'you'."},

                {"who":"mirror", 
                "text":"But if it brings you peace of mind, think of me as a reflection of 'you'."},

                {"choices":[
                    {"text":"I knew it, I'm too unique for there to be more than one of 'me'.", 
                    "effects":{"royal":add_most}},
                    
                    {"text":"It doesn't matter who's who. We're talking to each other, simple.", 
                    "effects":{"aloof":add_most}},
                    
                    {"text":"I didn't want an easy way out, I wanted to know if I'm-I'm something or somesone--someone different! Not just a reflection in a mirror!", 
                    "effects":{"royal":add_some, "decon":add_some}},
                    
                    {"text":"So I'm not playing as a mirror...", 
                    "effects":{"decon":add_some}}
                ]}
            ],
            "hub":"mirror",
            "requires":["mirror_what"]
        },

        "mirror_who":{
            "title":"Who am I?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"You are a Princess, of course. Someone of sufficient import, but not so politically active that you'll be missed, after all your parents have more than enough spawn that five could go missing without anyone in court noticing."},

                {"who":"mirror", 
                "text":"You also have many titles gifted for a variety of reasons. You are Heir to the Billyburrows, Duchess of Viantara, and the Dreamer of Zalon, among many others."},

                {"choices":[
                    {"text":"I always expected that, I really am special.", 
                    "effects":{"royal":add_most}},

                    {"text":"...But I don't think those titles mean anything.", 
                    "effects":{"decon":add_some, "aloof":add_some}},

                    {"text":"It doesn't amtter what titles I have, I'm already myself and that's more than unique enough.", 
                    "effects":{"royal":add_little, "decon":add_little, "aloof":add_little}},
                    
                    {"text":"So, I'm a semi-important figurehead, else the titles won't be so silly.", 
                    "effects":{"royal":add_some, "decon":add_some}}
                ]}
            ],
            "hub":"mirror",
            "requires":[]
        },

        "mirror_titles":{
            "title":"What do all those titles mean?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"All of nothing."},

                {"who":"mirror", 
                "text":"At least, they won't earn you any respect nor do they contain even an iota of power, thus they mean nothing"},

                {"choices":[
                    {"text":"I don't need useless titles, I am more than enough on my own merits.", 
                    "effects":{"royal":add_little, "decon":add_little, "aloof":add_little}},
                    
                    {"text":"No title mattered in the first place.", 
                    "effects":{"aloof":add_most}},
                    
                    {"text":"This is an outrage! I deserve titles; anything more, anything better.", 
                    "effects":{"royal":add_most}},
                    
                    {"text":"They mean something to me, that is enough.", 
                    "effects":{"royal":add_some, "decon":add_some}}
                ]}
            ],
            "hub":"mirror",
            "requires":["mirror_who"]
        },

        "mirror_but_who":{
            "title":"But who am I? Not my titles, as a person, who am I?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"I cannot answer that."},

                {"who":"mirror", 
                "text":"For if you ask a thousand people, you'll recieve a thousnad answers."},

                {"who":"mirror", 
                "text":"And I am interested in the one and only truth."},

                {"choices":[
                    {"text":"Losts of people cared about me, I knew it, I am special.", 
                    "effects":{"royal":add_most}},
                    
                    {"text":"But that applies to everyone, I'm hardly special.", 
                    "effects":{"decon":add_some, "aloof":add_some}},
                    
                    {"text":"I implies I'm famous, if over a thousand people have an opinion on me, be they good or bad, I do not know. I suppose I am honoured.", 
                    "effects":{"royal":add_some, "decon":add_some}},
                    
                    {"text":"I can't possibly know nor care about a thousand people.", 
                    "effects":{"aloof":add_most}}
                ]}
            ],
            "hub":"mirror",
            "requires":["mirror_who"]
        },

        "mirror_then_who":{
            "title":"Then who am I to you?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"..."},

                {"who":"mirror", 
                "text":"..."},

                {"who":"mirror", 
                "text":"Nevermind."},

                {"who":"mirror", 
                "text":"You won't understand."},

                {"who":"mirror", 
                "text":"I suppose you could say it's not important."},

                {"who":"mirror", 
                "text":"..."},

                {"who":"mirror", 
                "text":"But it's also not unimportant..."},

                {"who":"mirror", 
                "text":"No, you don't need to know."},

                {"who":"mirror", 
                "text":"Yes, that is correct. That is the one and only truth."},

                {"who":"mirror", 
                "text":"It's..."},

                {"who":"mirror", 
                "text":"It's for your own good..."},

                {"who":"mirror", 
                "text":"I promised..."},

                {"who":"mirror", 
                "text":"Please don't answer me."},

                {"choices":[
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"I'm glad that you're fullfilling your promise."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."}
                ]}
            ],
            "hub":"mirror",
            "requires":["mirror_but_who"]
        },

        "mirror_reflection":{
            "title":"Why aren't you showing my reflection?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"I am already your reflection."},

                {"who":"mirror", 
                "text":"There no need to 'show' it."},

                {"choices":[
                    {"text":"The reason doesn't matter, in the end there is no image.", 
                    "effects":{"aloof":add_most}},
                    
                    {"text":"Well, I would like to see my reflection.", 
                    "effects":{"royal":add_most}},
                    
                    {"text":"I guess you're not a real mirror, just one conjured by my own mind as a representation of 'me'--more specificly the 'me' with answers--and that's why I cannot see 'myself' as I do not have any answers.", 
                    "effects":{"decon":add_most}},
                    
                    {"text":"That's stupid, you're a mirror, you should show a reflection.", 
                    "effects":{"royal":add_some, "aloof":add_some}}
                ]}
            ],
            "hub":"mirror",
            "requires":[]
        },

        "mirror_story":{
            "title":"What was the story I just saw?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"Story...?"},

                {"who":"mirror", 
                "text":"I don't know what you're talking about."},

                {"who":"mirror", 
                "text":"I'd assume it was just a dream."},

                {"who":"mirror", 
                "text":"Think nothing of it."},

                {"choices":[
                    {"text":"No, I am a princess--or a prince--or - or whatever.", 
                    "effects":{"royal":add_most}},
                    
                    {"text":"I don't know, it felt right, like something that will happen, but the future doesn't matter, not yet, not compared to the present.", 
                    "effects":{"royal":add_little, "decon":add_little, "aloof":add_little}},
                    
                    {"text":"If it was a dream then it must symbolize something. Like maybe I desire marriage above all else--no that doesn't sound right; maybe I want stability--I think that's closer; or maybe--no, i don't think there's any use speculating.", 
                    "effects":{"decon":add_most}},
                    
                    {"text":"That makes sense, of course it didn't matter.", 
                    "effects":{"aloof":add_most}}
                ]}
            ],
            "hub":"mirror",
            "requires":[]
        },

        "mirror_will_story":{
            "title":"Will this story, this dream happen?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"I don't even know what story you're talking about."},

                {"who":"mirror", 
                "text":"But in a sense, all stories will happen sooner or later, it's just a question of whether you're alive at that point, after every possible event of this world has been played out."},

                {"choices":[
                    {"text":"I have a feeling that I'll see this one fulfilled, maybe it's destiny", 
                    "effects":{"royal":add_most}},
                    
                    {"text":"It was shown, thus I should witness it. That's just good foreshadowing", 
                    "effects":{"decon":add_most}},
                    
                    {"text":"I won't see it then...", 
                    "effects":{"aloof":add_most}},
                    
                    {"text":"That can't be right, some things are just impossible. Like touching a falling star", 
                    "effects":{"decon":add_some, "aloof":add_some}}
                ]}
            ],
            "hub":"mirror",
            "requires":["mirror_story"]
        },

        "mirror_why":{
            "title":"Why am I here?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"..."},

                {"who":"mirror", 
                "text":"Because are you needed here."},

                {"who":"mirror", 
                "text":"I say that's a good enough answer."},

                {"choices":[
                    {"text":"I am needed! I really am special", #"I rEaLly aM thE prOtAgoNiSt" 
                    "effects":{"royal":add_most}},
                    
                    {"text":"So I'm here because the game needs me to be, okay, got it.", 
                    "effects":{"decon":add_most}},
                    
                    {"text":"That can't be right, I'm never 'needed', no one ever is.", 
                    "effects":{"aloof":add_most}},
                    
                    {"text":"You should find someone else.", 
                    "effects":{"decon":add_some, "aloof":add_some}}
                ]}
            ],
            "hub":"mirror",
            "requires":[]
        },

        "mirror_but_why":{
            "title":"But why am I 'needed'?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"That's a complex question."},

                {"who":"mirror", 
                "text":"You see, many people need you for many different reasons."},

                {"who":"mirror", 
                "text":"Which of course came with the territory of being a prince/ss"},

                {"choices":[
                    {"text":"Naturally, a Prince/ss is important.", 
                    "effects":{"royal":add_most}},
                    
                    {"text":"A pointless answer. Sure, i'm needed, that's good, but doesn't explain why I'm here.", 
                    "effects":{"royal":add_some, "decon":add_some}},
                    
                    {"text":"That can't be right, I couldn't have been useful to the running of a kingdom, at least I don't think so, at most I would have been a figurehead.", 
                    "effects":{"decon":add_most}},
                    
                    {"text":"You're wrong. No one is 'needed', especially not for 'many reasons'.", 
                    "effects":{"aloof":add_most}}
                ]}
            ],
            "hub":"mirror",
            "requires":["mirror_why"]
        },

        "mirror_then_why":{
            "title":"Then why am I 'needed' for you?",
            "answer_lines":[
                {"who":"mirror", 
                "text":"..."},

                {"who":"mirror", 
                "text":"..."},

                {"who":"mirror", 
                "text":"You're royalty."},

                {"who":"mirror", 
                "text":"That's a good enough reason."},

                {"who":"mirror", 
                "text":"..."},

                {"who":"mirror", 
                "text":"Who am I kidding."},

                {"who":"mirror", 
                "text":"That's not an answer."},

                {"who":"mirror", 
                "text":"..."},

                {"who":"mirror", 
                "text":"I knew someone."},

                {"who":"mirror", 
                "text":"Someone who 'needed'--"},

                {"who":"mirror", 
                "text":"No, someone who cared."},

                {"who":"mirror", 
                "text":"Someone who cared about you."},

                {"who":"mirror", 
                "text":"..."},

                {"who":"mirror", 
                "text":"I can't say more."},

                {"who":"mirror", 
                "text":"But I think that was a good answer..."},

                {"who":"mirror", 
                "text":"It has to be a good answer..."},

                {"who":"mirror", 
                "text":"Please don't tell me if it was..."},

                {"choices":[
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"It was a good answer."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."},
                    {"text":"..."}
                ]}
            ],
            "hub":"mirror",
            "requires":["mirror_but_why"]
        },

        #travel hub
        "travel_dragon_reason_one":{
            "title":"Why are you trying to kill a dragon?",
            "hub":"travel",
            "requires":["travel_day_one"],
            "answer_lines":[
                {"who":"boy",
                "text":"Well, you know, the standard reward."},

                {"who":"boy",
                "text":"Half the kindgom and the heir's hand in marriage."}
            ]
        },

        "travel_dragon_reason_two":{
            "title":"Why are you trying to kill a dragon?",
            "hub":"travel",
            "requires":["travel_dragon_reason_one"],
            "answer_lines":[
                {"who":"boy",
                "text":"Didn't you already ask?"},

                {"who":"boy",
                "text":"Obviously, I want half the kindgom and the heir's hand in marriage."},

                {"who":"boy",
                "text":"I mean, isn't that why everyone wants to kill a dragon?"}
            ]
        },

        "travel_dragon_reason_three":{
            "title":"I don't think you want the 'standard reward' Why are you trying to kill a dragon?",
            "hub":"travel",
            "requires":["travel_dragon_reason_two"],
            "answer_lines":[
                {"who":"boy",
                "text":"Fine, fine. I don't actually want to rule a kingdom. That would be exhausting."},

                {"who":"boy",
                "text":"I have no experience in management and I can't even imagine the amount of paperwork! No, I'd leave it to the those who want it."},

                {"who":"boy",
                "text":"As for the heir's hand in marriage, I'm not interested in a romantic relationship and I don't want to force a marriage when the other party doesn't want it."},

                {"who":"boy",
                "text":"Especially since I'm rather incompetant at politicking and would hardly be a favourable match."},

                {"who":"boy",
                "text":"So, you see this is a test of skills, see if I'm good enough to slay a dragon. That's it. That's all there is to it."}
            ]
        },

        "travel_dragon_reason_four":{
            "title":"You don't seem like the kind of person to kill something for pride. I'll ask again, why are you on a quest to slay a dragon?",
            "hub":"travel",
            "requires":["travel_dragon_reason_three"],
            "answer_lines":[
                {"who":"boy",
                "text":"..."},                

                {"who":"boy",
                "text":"*whispers* I want to save Wolf. The dragon's heart is said to be invigorating. I'm hoping it'll be able to heal him."},

                {"who":"boy",
                "text":"I've never seen him at his prime, when he was younger, top of the world and all that."},

                {"who":"boy",
                "text":"But I know he misses it and he's given me everything. This is the least I could do."},

                {"who":"boy",
                "text":"..."},

                {"who":"boy",
                "text":"It could help you too."},

                {"who":"boy",
                "text":"The dragon's mind can also heal minds, it'd definitely help you with your missing memories."},
            ]
        },

        "travel_wolf_give":{
            "title":"[boy_name], what did Llangernyw give you?",
            "hub":"travel",
            "requires":["travel_dragon_reason_four"],
            "answer_lines":[
                {"who":"boy",
                "text":"..."},
                
                {"who":"boy",
                "text":"My life I guess."},

                {"who":"boy",
                "text":"He took me in as an apprentice when I ran into him in the dark forest."},

                {"who":"boy",
                "text":"And magic shaped me in every way possible."},

                {"who":"boy",
                "text":"It is my life now."},
            ]
        },
        
        "travel_wolf_know_reason":{
            "title":"Does Llangernyw know what you're planning to do?",
            "hub":"travel",
            "requires":["travel_dragon_reason_four"],
            "answer_lines":[
                {"who":"boy",
                "text":"Yes?"},
                
                {"who":"boy",
                "text":"I think so?"},

                {"who":"boy",
                "text":"Wolf isn't dumb, despite all appearances."},

                {"who":"boy",
                "text":"I don't know any other reason we'd be off to kill a dragon at least."},
            ]
        },

        "travel_tell_wolf_reason":{
            "title":"[boy_name], you should tell Llangernyw why you're trying to kill the dragon. Now, when he's still awake.",
            "hub":"travel",
            "requires":["travel_wolf_know_reason", "travel_early_flag"],
            "answer_lines":[
                {"who":"boy",
                "text":"Hey Wolf!"},
                
                {"who":"boy",
                "text":"You know we're killing the dragon to get its heart right?"},

                {"who":"wolf",
                "text":"Okay?"},

                {"who":"wolf",
                "text":"I don't really care what's being harvested from the dragon."},

                {"who":"boy",
                "text":"I mean getting the heart for you."},

                {"who":"wolf",
                "text":"..."},

                {"who":"wolf",
                "text":"..."},

                {"who":"wolf",
                "text":"...Thanks."},

                {"who":"wolf",
                "text":"..."},

                {"who":"wolf",
                "text":"But there was no need."},

                {"who":"wolf",
                "text":"I am youthful as always."},

                {"who":"wolf",
                "text":"*cough* Like I said, youthful as always."},

                {"who":"wolf",
                "text":"Anyhow, my pendant and monocle are perfect focuses. Not that I'm saying no to a dragon's heart!"}
            ]
        },

        "travel_village":{
            "title":"What is the village we're going to?",
            "hub":"travel",
            "requires":["travel_day_one", "travel_early_flag"],
            "answer_lines":[
                {"who":"boy",
                "text":"Well, I don't know all that much."},

                {"who":"boy",
                "text":"It's pretty small and they do like farming and what not. definitely has a lot of farmers and shepherds, maybe has a lost heir and a magic sword, seeing as there's a wizard hiding over there."},
                
                {"who":"boy",
                "text":"ALthough it probably doesn't. The chances of a random town having a true magic sword is one in a million."},

                {"who":"boy",
                "text":"Well, one can dream and at least one tiny, lucky, backwater village has a magic sword that'll grant a hapless farmboy kingship."},

                {"who":"boy",
                "text":"But more on topic--the village is on the outskirts of the forest."},

                {"who":"boy",
                "text":"Whoever buildt it was either very smart or very lucky as the village is just past dragon country and I doubt no dragons ever bothered them."}
            ]
        },

        "travel_village_wizard":{
            "title":"Can you tell me more about this wizard we're trying to meet?",
            "hub":"travel",
            "requires":["travel_day_one", "travel_early_flag"],
            "answer_lines":[
                {"who":"wolf",
                "text":"I would never mistake a magical signiture, even from this far away, and I felt one coming from the village we're heading towards."},
                
                {"who":"wolf",
                "text":"It was also the only one close to the mountains and the dragons we're nearing."},

                {"who":"wolf",
                "text":"Magic users just aren't as competent as they once were."},

                {"who":"wolf",
                "text":"Back in the day, there would be a full squadron making sure dragons didn't encroach onto civillization"},

                {"who":"wolf",
                "text":"And this has been reduced to what? A single wizard?"},

                {"who":"boy",
                "text":"Anyways, I figured we should go visit them! They've been living near the dragons for so long, they must have some sort of advice on how to face fire-breathing lizards."},

                {"who":"boy",
                "text":"I also do hope they're nice and willing to help out."},
            ]
        },

        "travel_boy_name_why":{
            "title":"Why do you call yourself 'Boy'?",
            "hub":"travel",
            "requires":["travel_day_one", not "boy_renamed_flag"],
            "answer_lines":[
                {"who":"boy",
                "text":"It's just a name I identify with."},
                
                {"who":"boy",
                "text":"No more, no less."}
            ]
        },

        "travel_boy_name_find":{
            "title":"In that case, can I help you find a new name?",
            "hub":"travel",
            "requires":["travel_boy_name_why"],
            "answer_lines":[
                {"who":"boy",
                "text":"..."},
                
                {"who":"boy",
                "text":"I'm happy with my name as it is."},

                {"who":"boy",
                "text":"But, I guess...I guess I'll take your suggestion, but I probably, like ninety-nine percent sure, that I won't take it."}
            ]
        },

        "travel_boy_name_epiphany":{
            "title":"Have you got any thought on what you'd like to be called other than Boy?",
            "hub":"travel",
            "requires":["travel_boy_name_find"], #boy_talk_about_himself_count > 4
            "answer_lines":[
                {"who":"boy",
                "text":"Now that I think about it more, I think I'd be happy to try and choose something."},
                
                {"who":"boy",
                "text":"Like something that suits me."},

                {"who":"boy",
                "text":"But I also know Boy suits me."},

                {"who":"boy",
                "text":"It sits up there now."},

                {"who":"boy",
                "text":"And that feels right. But like Wolf also had more after what feels right too."},

                {"who":"boy",
                "text":"I think I might try to find something for myself as well."}
            ]
        },

        "travel_wolf_magic_slideshow":{
            "title":"Llangernyw, can you teach me about magic?",
            "hub":"travel",
            "requires":["travel_day_one", "travel_early_flag"],
            "answer_lines":[
                {"repeat":"true"},
                {"call":"wolf_magic_slideshow"}
            ]
        },

        "travel_boy_wolf_relationship":{
            "title":"[boy_name], you and Llangernyw are really close. How did meet?",
            "hub":"travel",
            "requires":["travel_day_two"],
            "answer_lines":[
                {"who":"boy",
                "text":"It wasn't anything special. I met him in the woods, obviously."},
                
                {"who":"boy",
                "text":"I was running an errand for my Mama."},

                {"who":"boy",
                "text":"He was really nice and polite, well I know better now."},

                {"who":"boy",
                "text":"Wolf's only nice 'cause he wanted to make a good first impression."},

                {"who":"boy",
                "text":"Granted, he was also super frail and everything, but he didn't see it that way."},

                {"who":"boy",
                "text":"Anyway, not relevant. I became his apprentice and we've been traveling together ever since."}
            ]
        },

        "travel_boy_errand":{
            "title":"What errand were you doing for your Mama?",
            "hub":"travel",
            "requires":["travel_boy_wolf_relationship"],
            "answer_lines":[
                {"who":"boy",
                "text":"Nothing much, just delivering some cookies, soup, and other what not for Grandmama."},
                
                {"who":"boy",
                "text":"Grandmama insisted on living in a cottage in the middle of the Woods, you see. That never made much sense to me, I thought that was a death wish."}
            ]
        },

        "travel_walking_song":{
            "title":"[boy_name], where did you learn that walking song?",
            "hub":"travel",
            "requires":["travel_day_two"],
            "answer_lines":[
                {"who":"boy",
                "text":"My Mama taught it to me back when both of us would go visit Grandmama."},
                
                {"who":"boy",
                "text":"These days, walking in any forest reminds of them, so I sing this song."},

                {"who":"boy",
                "text":"Those days weren't the best, and I think I'm doing better now, but I'd say my time then wasn't unhappy."}
            ]
        },

        "travel_boy_parents":{
            "title":"[boy_name], are your parents still--still alive?",
            "hub":"travel",
            "requires":["travel_walking_song"],
            "answer_lines":[
                {"who":"boy",
                "text":"Father's been gone as far as I could remember."},

                {"who":"boy",
                "text":"It's always been just Mama and me as far as I could remember, while Grandmama lived in the forest, a ways from the village."},

                {"who":"boy",
                "text":"And I think Mama and Grandmama are still safe, sound, and alive."}
            ]
        },

        "travel_wolf_teaching":{
            "title":"Llangernyw, why are you teaching Boy?",
            "hub":"travel",
            "requires":["travel_day_two", "travel_early_flag"],
            "answer_lines":[
                {"who":"wolf",
                "text":"Don't let that idiot fool you. Boy has talent."},

                {"who":"wolf",
                "text":"After only a year he was already making his own spells. Most never get there, you know. Sure it was still later than me, first pieve of magic I cast was of my own making."},

                {"who":"wolf",
                "text":"But still impressive."},
                
                {"who":"wolf",
                "text":"And I guess I could do a lot worse for an apprentice. He's just a tad too chatty, but he takes care of everything else and he has a good heart."},

                {"who":"wolf",
                "text":"Now stop asking me irrelevant questions! You're ruinging my sleep."}
            ]
        },

        "travel_wolf_sleep":{
            "title":"Llangernyw, how do you fall asleep so fast?",
            "hub":"travel",
            "requires":["travel_day_three", "travel_early_flag"],
            "answer_lines":[
                {"who":"wolf",
                "text":"..."},
                
                {"who":"wolf",
                "text":"Stop drinking coffee."},

                {"who":"wolf",
                "text":"..."},

                {"who":"wolf",
                "text":"Don't stay up all night chattering."},
            ]
        },

        "travel_wolf_soul":{
            "title":"Is the soul thing normal??",
            "hub":"travel",
            "requires":["travel_day_four", "travel_early_flag"],
            "answer_lines":[
                {"who":"boy",
                "text":"Eh...more or less."},
                
                {"who":"wolf",
                "text":"There was no soul thing!"},
            ]
        },

        "travel_ellipsis_saga":{
            "title":"...",
            "hub":"travel",
            "requires":["travel_day_one", "travel_ellipsis_flag"],
            "answer_lines":[
                {"repeat":"true"},
                {"call":"ellipsis_saga"}
            ]
        },

        "travel_wizard_dragon":{
            "title":"Bea, what do you know about dragons?",
            "hub":"travel",
            "requires":["wizard_joined"],
            "answer_lines":[
                {"repeat":"true"},
                {"call":"wizard_dragon"}
            ]
        },

        "travel":{
            "title":"Bea, what can you do with magic?",
            "hub":"travel",
            "requires":["wizard_joined"],
            "answer_lines":[
                {"who":"wizard",
                "text":"Oh, I can summon the illusion of a butterfly!"},
                
                {"who":"wizard",
                "text":"That's it, that's all, that's everything I can do."}
            ]
        },

        "travel":{
            "title":"",
            "hub":"travel",
            "requires":[not "travel_day_one"],
            "answer_lines":[
                {"who":"boy",
                "text":""},
                {}
            ]
        },


        #village hubs
        #innnkeeper alone
        "innkeeper_no_wizard":{
            "title":"You didn't mention wizard when you were introducing everyone. Tell me about them please",
            "hub":"innkeeper",
            "requires":[],
            "answer_lines":[
                {"jump":"ch2_innkeeper_no"}
            ]
        },

        "innkeeper_no_miller":{
            "title":"Were you involved in the Miller's death in any way, shape, or form?",
            "hub":"innkeeper",
            "requires":["mu_my_flag"],
            "answer_lines":[
                {"jump":"ch2_innkeeper_no"}
            ]
        },

        "innkeeper_no_town":{
            "title":"Do you like living here, in a small town that's almost on the edge of dragon territory?",
            "hub":"innkeeper",
            "requires":[],
            "answer_lines":[
                {"jump":"ch2_innkeeper_no"}
            ]
        },

        "innkeeper_yes_dragon":{
            "title":"Have you any advice to handle a dragon? I'd rather not step onto the 'running away' band wagon.",
            "hub":"innkeeper",
            "requires":[],
            "answer_lines":[
                {"who":"innkeeper",
                "text":"I've heard a rumour 'round parts, that the dragon eats people's hearts."},
                {"who":"innkeeper",
                "text":"Can't say I know any way to stop that bit, that's just not the way the tale is writ."}
            ]
        },

        "innkeeper_no_help":{
            "title":"Even the barest hint would be helpful.",
            "hub":"innkeeper",
            "requires":["innkeeper_yes_dragon"],
            "answer_lines":[
                {"jump":"ch2_innkeeper_no"}
            ]
        },

        "innkeeper_yes_help":{
            "title":"My companions and I will face this dragon help or no help; so if you can think of anything, anything at all, even if it's so boring and basic as kelp.",
            "hub":"innkeeper",
            "requires":["innkeeper_yes_dragon"],
            "answer_lines":[
                {"who":"innkeeper",
                "text":"Well at least mean you aren't rushing, and I guess there isn't nothing."},
                {"who":"innkeeper",
                "text":"Some say the dragons fears the good, solid loaf of bread; As if I'd believe them, it'd be like a spider being afraid of thread."}
            ]
        },

        "innkeeper_yes_miller":{
            "title":"I just wanted to ask about something from the past, what was your relation with the Miller that passed?",
            "hub":"innkeeper",
            "requires":["mu_my_flag"],
            "answer_lines":[
                {"who":"innkeeper",
                "text":"Miller is-was my fiancee, my husband-to-be; I would never kill him don't you see? I'm just as much as a victem, this what I plea."},
                {"who":"innkeeper",
                "text":"It brings me too much to reminise; please, please speak of something with a little more bliss."}
            ]
        },

        "innkeeper_yes_wizard":{
            "title":"[boy_name] already asked you about the magician, I'm really hoping to learn more since it'll help with my mission.",
            "hub":"innkeeper",
            "requires":[],
            "answer_lines":[
                {"who":"innkeeper",
                "text":"The magician is quite odd, but I think she's just a sod."}
            ]
        },

        "innkeeper_no_wizard_info":{
            "title":"I meant where should I make my inquiries, if I want to meet her that is.",
            "hub":"innkeeper",
            "requires":["innkeeper_yes_wizard"],
            "answer_lines":[
                {"jump":"ch2_innkeeper_no"}
            ]
        },

        "innkeeper_yes_wizard_info":{
            "title":"Where can she be found? I don't wish to look everywhere around.",
            "hub":"innkeeper",
            "requires":["innkeeper_yes_wizard"],
            "answer_lines":[
                {"who":"innkeeper",
                "text":"Can't quite remember, but it was the left side of the cul-de-sac. And I do think her house number was prime, though I think it's closer to a shack."}
            ]
        },

        "shepherd_no_royal":{
            "title":"As a royal, I need you to fullfill some requests",
            "hub":"shepherd",
            "requires":[],
            "answer_lines":[
                {"effects":{"royal":add_some}},
                {"jump":"ch2_shepherd_no"}
            ]
        },

        "shepherd_yes_what":{
            "title":"Shepherd is what? New am I.",
            "hub":"shepherd",
            "requires":[],
            "answer_lines":[
                {"who":"shepherd",
                "text":"Sheep for care take we, job simple."},
                
                {"who":"shepherd",
                "text":"Peaceful is it. For it like I."},

                {"who":"shepherd",
                "text":"Sheep wanderin no and flowers bright and skies sunny. Than more for ask never would I."}
            ]
        },

        "shepherd_no_wizard":{
            "title":"Where does the wizard live?",
            "hub":"shepherd",
            "requires":[],
            "answer_lines":[
                {"jump":"ch2_shepherd_no"}
            ]
        },

        "shepherd_no_watch":{
            "title":"Do you do anything all day other than watch the sheep?",
            "hub":"shepherd",
            "requires":["shepherd_yes_what"],
            "answer_lines":[
                {"jump":"ch2_shepherd_no"}
            ]
        },

        "shepherd_no_flower":{
            "title":"Your sheep are grazing on lovely flowers! Say, do you do anything with them?",
            "hub":"shepherd",
            "requires":[],
            "answer_lines":[
                {"jump":"ch2_shepherd_no"}
            ]
        },

        "shepherd_yes_watch":{
            "title":"Sheep watch except, else anything.",
            "hub":"shepherd",
            "requires":["shepherd_yes_what"],
            "answer_lines":[
                {"who":"shepherd",
                "text":"Sometimes flowers pick."},
                
                {"who":"shepherd",
                "text":"Lovely bouquets make they."},

                {"who":"shepherd",
                "text":"Sometimes read to book bring."},

                {"who":"shepherd",
                "text":"Books in lives peaceful, never are there."},
                
                {"who":"shepherd",
                "text":"Sheep the return to, always."},
            ]
        },

        "shepherd_no_book":{
            "title":"Do you have a favourite book?",
            "hub":"shepherd",
            "requires":["shepherd_yes_watch"],
            "answer_lines":[
                {"jump":"ch2_shepherd_no"}
            ]
        },

        "shepherd_decon":{
            "title":"Are there many shepherds and goatherds wailing their romantic faliures into the mountains around here?",
            "hub":"shepherd",
            "requires":[],
            "answer_lines":[
                {"effects":{"decon":add_some}},
                {"jump":"ch2_shepherd_no"}
            ]
        },

        "shepherd_yes_bouquet":{
            "title":"Bouquets of reciever.",
            "hub":"shepherd",
            "requires":["shepherd_yes_watch"],
            "answer_lines":[
                {"who":"shepherd",
                "text":"Friend! Best!"},

                {"who":"shepherd",
                "text":"Magic & green & purple is she!"},

                {"who":"shepherd",
                "text":"Bouquets a have she. Ensure always I."},

                {"who":"shepherd",
                "text":"Her-door outside them left I."},

                {"who":"shepherd",
                "text":"Another leave. To go back go I. When usually are tehy since. Bouquets like she thinks I."},

                {"who":"shepherd",
                "text":"Morning this one. Left just I!"}
            ]
        },

        "shepherd_yes_specific":{
            "title":"Specific more bit anout the wizard?",
            "hub":"shepherd",
            "requires":["shepderd_yes_bouquet"],
            "answer_lines":[
                {"who":"shepherd",
                "text":"Her-door outside flowers left I, her-door is windchimes with green."},

                {"who":"shepherd",
                "text":"I not did you told? Already I."},

                {"who":"shepherd",
                "text":"Chrysanthemums and magnolias and roses. Some got I today."}
            ]
        },

        "shepherd_no_bouquet":{
            "title":"Who do you give these bouquets to?",
            "hub":"shepherd",
            "requires":["shepherd_yes_watch"],
            "answer_lines":[
                {"jump":"ch2_shepherd_no"}
            ]
        },

        "shepherd_yes_book":{
            "title":"Book favourite?",
            "hub":"shepherd",
            "requires":["shepherd_yes_watch"],
            "answer_lines":[
                {"who":"shepherd",
                "text":"Hm..."},

                {"who":"shepherd",
                "text":"Hm..."},

                {"who":"shepherd",
                "text":"Time of Wheel."},

                {"who":"shepherd",
                "text":"Are quests stupid? How shows it."},

                {"who":"shepherd",
                "text":"Sheep with outside. Stay to better."}
            ]
        },

        "shepherd_no_frame":{
            "title":"Please tell me more about the book?",
            "hub":"shepherd",
            "requires":["shepherd_yes_book"],
            "answer_lines":[
                {"jump":"ch2_shepherd_no"}
            ]
        },

        "shepherd_no_specific":{
            "title":"Wizard specific more bit?",
            "hub":"shepherd",
            "requires":["shepherd_yes_bouquet"],
            "answer_lines":[
                {"jump":"ch2_shepherd_no"}
            ]
        },

        "shepherd_yes frame":{
            "title":"Book about more tell.",
            "hub":"shepherd",
            "requires":["shepherd_yes_book"],
            "answer_lines":[
                {"who":"shepherd",
                "text":"Stories frame two. From told it is."},

                {"who":"shepherd",
                "text":"Sheep to tend while reading. Shepherd A is there, like me."},

                {"who":"shepherd",
                "text":"Decade a after. Down everything wrote. Who chronicler? Of perspective the from."},

                {"who":"shepherd",
                "text":"Live will they. Know to! Comfort is it."}
            ]
        },

        "shepherd_no_miller":{
            "title":"I am curious, did you know the Miller?",
            "hub":"shepherd",
            "requires":["mu_my_flag"],
            "answer_lines":[
                {"jump":"ch2_shepherd_no"}
            ]
        },

        "shepherd_yes_miller":{
            "title":"The-Miller know? You did? Curious am I.",
            "hub":"shepherd",
            "requires":["mu_my_flag"],
            "answer_lines":[
                {"who":"shepherd",
                "text":"No all at well not, thinks I."},

                {"who":"shepherd",
                "text":"Pepper to was marriage future."},

                {"who":"shepherd",
                "text":"Son his like not, also"},

                {"who":"shepherd",
                "text":"Her-door on banged. Always he."}
            ]
        },

        "shepherd_yes_upset":{
            "title":"Anyone upsets by Miller, thinks you?",
            "hub":"shepherd",
            "requires":["shepherd_yes_miller"],
            "answer_lines":[
                {"who":"shepherd",
                "text":"Gossip of lot. A know not do I."},

                {"who":"shepherd",
                "text":"Maybe Sally, seamstress."}
            ]
        },

        "shepherd_yes_son":{
            "title":"Son like? The was that?",
            "hub":"shepherd",
            "requires":["shepherd_yes_miller"],
            "answer_lines":[
                {"who":"shepherd",
                "text":"Rude, very rude."},

                {"who":"shepherd",
                "text":"Books took."},

                {"who":"shepherd",
                "text":"Language wrong."},

                {"who":"shepherd",
                "text":"Bea annoyed, important most."}
            ]
        },

        "shepherd_no_upset":{
            "title":"Can you think of if the Miller's upset anyone?",
            "hub":"shepherd",
            "requires":["shepherd_yes_miller"],
            "answer_lines":[
                {"jump":"ch2_shepherd_no"}
            ]
        },

        "shepherd_yes_relation":{
            "title":"Relationship? Miller and Pepper",
            "hub":"shepherd",
            "requires":["shepherd_yes_miller"],
            "answer_lines":[
                {"who":"shepherd",
                "text":"Either with close? Not was."},

                {"who":"shepherd",
                "text":"Bad not, thinks I."},

                {"who":"shepherd",
                "text":"Though good not also."},

                {"who":"shepherd",
                "text":"Shouting heard sometimes. Bea as street, same."}
            ]
        },

        "shepherd_no_relation":{
            "title":"Do you know anything about Pepper and Miller's relationship?",
            "hub":"shepherd",
            "requires":["shepherd_yes_miller"],
            "answer_lines":[
                {"jump":"ch2_shepherd_no"}
            ]
        },

        "shepher_no_son":{
            "title":"Anything else you know about this Miller's son?",
            "hub":"shepherd",
            "requires":["shepherd_yes_miller"],
            "answer_lines":[
                {"jump":"ch2_shepherd_no"}
            ]
        },

        #sojourn!!
        "sojourn_story_start":{
            "title":"Would you talk of your sojourn? And what of many story you saw.",
            "hub":"sojourn",
            "requires":[],
            "answer_lines":[
                {"call":"sojourn_story_one"}
            ]
        },

        "sojourn_story_tell":{
            "title":"Talk of your many story. I enjoy it.",
            "hub":"sojourn",
            "requires":["sojourn_story_start"],
            "answer_lines":[
                {"repeat":"true"},
                {"call":"sojourn_story"}
            ]
        },

        "sojourn_no_elaborate":{
            "title":"Can you elaborate? Like explain more about the hardship you mentioned.",
            "hub":"sojourn",
            "requires":[],
            "answer_lines":[
                {"jump":"ch2_sojourn_no"}
            ]
        },

        "sojourn_yes_wizard":{
            "title":"Do you know of this town's wizard?",
            "hub":"sojourn",
            "requires":[],
            "answer_lines":[
                {"who":"sojourn",
                "text":"I don't know anybody in town."},
                
                {"who":"sojourn",
                "text":"I'm similar to you, I'm also looking for things."},

                {"who":"sojourn",
                "text":"For you it may be this wizard, but I am looking for a story of worlds."},

                {"who":"sojourn",
                "text":"It sounds as if your wizard might know about that."},

                {"who":"sojourn",
                "text":"So if you do find your wizard, do inform this man in midst of sojourn on what that wizard tolf you."}
            ]
        },

        "sojourn_yes_future":{
            "title":"And if you go on? Past this village, that is?",
            "hub":"sojourn",
            "requires":["sojourn_story_start"],
            "answer_lines":[
                {"who":"sojourn",
                "text":"I think I shall go to the south. Lord knows it is far too cold for my bofy and I had a wish of warming up to a point."},

                {"who":"sojourn",
                "text":"I know sands hid many a story, but I shall still find it anyhow."}
            ]
        },

        "sojourn_yes_why":{
            "title":"Why did you go out on a sojourn?",
            "hub":"sojourn",
            "requires":["sojourn_story_start"],
            "answer_lines":[
                {"who":"sojourn",
                "text":"I want to know a world. For it is knowable, at least in part, and I know not to follow what is not."},

                {"who":"sojourn",
                "text":"It may not show it in laws or karma."},

                {"who":"sojourn",
                "text":"But it shows in a story. An always growing story. And I wish to know just a bit of that."}
            ]
        },

        "sojourn_yes_reason":{
            "title":"Why do you think Innkeep's almost husband was found cold?",
            "hub":"sojourn",
            "requires":["mu_my_flag"],
            "answer_lines":[
                {"who":"sojourn",
                "text":"I think it was just plain bad luck. Not a killing by anybody."},

                {"who":"sojourn",
                "text":"As in not Miss 椒 nor I, as I know Miss 椒 didn't maintain a good relationship with that man, but it isn't as if any of us any grounds for killing or maiming."},

                {"who":"sojourn",
                "text": "Anyhow, that man took a fall, but not a push."},

                {"who":"sojourn",
                "text":"In fact, I had to go to Miss 椒, for Miss 椒 was soundly in a think quilt, so much so that Miss 椒 did miss that trial."},

                {"who":"sojourn",
                "text":"Miss 椒 did cry, you know. I think it hurt, that a man, any man, was found cold in this inn."}
            ]
        },

        "sojourn_no_discovery":{
            "title":"How was the desceased discovered?",
            "hub":"sojourn",
            "requires":["mu_my_flag"],
            "answer_lines":[
                {"jump":"ch2_sojourn_no"}
            ]
        },

        "sojourn_no_location":{
            "title":"Do you know the place of the death?",
            "hub":"sojourn",
            "requires":["mu_my_flag"],
            "answer_lines":[
                {"jump":"ch2_sojourn_no"}
            ]
        },

        "sojourn_yes_motive":{
            "title":"Anybody in town got a motivation to kill that man and toss you into this situation?",
            "hub":"sojourn",
            "requires":["mu_my_flag"],
            "answer_lines":[
                {"who":"sojourn",
                "text":"Why no, I don't think so."},

                {"who":"sojourn",
                "text":"I'd just did get to this town so I don't know most."},

                {"who":"sojourn",
                "text":"As for Miss 椒, I think folks fancy Miss 椒 and ain't got a loathing toward Flamingo nor its host."}
            ]
        },

        "sojourn_no_hear":{
            "title":"How did you hear the Miller's fall?",
            "hub":"sojourn",
            "requires":["sojourn_yes_reason"],
            "answer_lines":[
                {"jump":"ch2_sojourn_no"}
            ]
        },

        "sojourn_yes_hear":{
            "title":"What about you? Anything you did that night?",
            "hub":"sojourn",
            "requires":["sojourn_yes_reason"],
            "answer_lines":[
                {"who":"sojourn",
                "text":"I was journaling. I always find joy in writing about my sojourn."},

                {"who":"sojourn",
                "text":"lt was kind of Miss 椒 for on the day I did show up at this town I was all out of ink."},

                {"who":"sojourn",
                "text":"Miss 椒 did aid in finding a pot along with a quill."}
            ]
        },

        "sojourn_yes_inn_motive":{
            "title":"But do you or that Miss got a motivation to kill?",
            "hub":"sojourn",
            "requires":["sojourn_yes_motive"],
            "answer_lines":[
                {"who":"sojourn",
                "text":"No, I don't think so."},

                {"who":"sojourn",
                "text":"I don't know that man at all, so I ain't got motivation to kill him."},

                {"who":"sojourn",
                "text":"Miss 椒 and that man had a flirtation, I think, but I don't think Miss Juniper would kill him if it had a quandary in that."},

                {"who":"sojourn",
                "text":"Miss 椒 is a kind to talk to about it and not go killing, you know."},
            ]
        },

        "sojourn_no_inn_motive":{
            "title":"Have either of you got a reason to? Kill the Miller, that is.",
            "hub":"sojourn",
            "requires":["sojourn_yes_motive"],
            "answer_lines":[
                {"jump":"ch2_sojourn_no"}
            ]
        },

        "sojourn_no_journal":{
            "title":"You kind of went off topic. I meant was there anything special you or Miss Pepper did the night of the murder.",
            "hub":"sojourn",
            "requires":["sojourn_yes_inn_motive"],
            "answer_lines":[
                {"jump":"ch2_sojourn_no"}
            ]
        },

        "sojourn_yes_journal":{
            "title":"Which room did you do your journaling? And do you know whst stairs that man had his fall?",
            "hub":"sojourn",
            "requires":["sojourn_yes_inn_motive"],
            "answer_lines":[
                {"who":"sojourn",
                "text":"I was upon floor two in room 230."},

                {"who":"sojourn",
                "text":"Miss 椒 and that man a floor up, third room from that stairs."},

                {"who":"sojourn",
                "text":"I got out to look for a a loud 'thump' is hard to turn my back on."},

                {"who":"sojourn",
                "text":"Which was how I found that man's body, with blood all around."},

                {"who":"sojourn",
                "text":"Miss 椒 did scrub that spot for so long, what wood is in that spot must almost rot away by now."},
            ]
        },

        "miller_son_no_wizard":{
            "title":"Can you tell me about the wizard in this town?",
            "hub":"miller_son",
            "requires":[],
            "answer_lines":[
                {"jump":"ch2_miller_son_no"}
            ]
        },

        "miller_son_no_flowers":{
            "title":"Is there a reason your holding flowers?",
            "hub":"miller_son",
            "requires":[],
            "answer_lines":[
                {"jump":"ch2_miller_son_no"}
            ]
        },

        "miller_son_yes_flowers":{
            "title":"Magnolia, those flowers you're holding, I mean. Where did you get them?",
            "hub":"miller_son",
            "requires":[],
            "answer_lines":[
                {"who":"miller_son",
                "text":"Magnolias, and also chrysanthemums and roses. Shepherd dropped them off for Bea."},

                {"who":"miller_son",
                "text":"Me, though, all I'm doing is putting them in a vase, make sure they last more than two days and all that."}
            ]
        },

        "miller_son_yes_wizard":{
            "title":"Magician in this town, right? Can you explain more?",
            "hub":"miller_son",
            "requires":[],
            "answer_lines":[
                {"who":"miller_son",
                "text":"'Magician', what bull. Bea's a full wizard!"}
            ]
        },

        "miller_son_no_living":{
            "title":"So, I heard about your Dad, does that mean you live alone?",
            "hub":"miller_son",
            "requires":[],
            "answer_lines":[
                {"jump":"miller_no"}
            ]
        },

        "miller_son_yes_where":{
            "title":"Maybe you can tell me where Bea lives? I wanted to talk magic with her.",
            "hub":"miller_son",
            "requires":["miller_son_yes_wizard"],
            "answer_lines":[
                {"who":"miller_son",
                "text":"Mmm...So I don't really remember, she used to be across my street and a bit to the right from me."},

                {"who":"miller_son",
                "text":"Might also be 'cause I located her by hearing the bronze winchimes which are just like the little bronze numbers, I think."}
            ]
        },

        "miller_son_yes_stuff":{
            "title":"May I ask why you're changing the flowers for the wizard?",
            "hub":"miller_son",
            "requires":["miller_son_yes_wizard", "miller_son_yes_flowers"],
            "answer_lines":[
                {"who":"miller_son",
                "text":"Mail like that doesn't deserve to rot and I'm even helping out Roth'la, she's the one that leaves the flowers, by the way."},

                {"who":"miller_son",
                "text":"Mona, Basil and I are also taking turns leaving bread by her door and we make sure she gets her mail as well, even if the amil is flowers."}
            ]
        },

        "miller_no_stuff":{
            "title":"Do you do anything else for the wizard other than bring her flowers?",
            "hub":"miller_son",
            "requires":["miller_son_yes_wizard", "miller_son_yes_flowers"],
            "answer_lines":[
                {"jump":"ch2_miller_son_no"}
            ]
        },

        "miller_son_no_where":{
            "title":"So can you specify where ",
            "hub":"miller_son",
            "requires":["miller_son_yes_wizard"],
            "answer_lines":[
                {"jump":"ch2_miller_son_no"}
            ]
        },

        "miller_son_yes_living":{
            "title":"Moving fine? I didn't mean to assume, it's just I heard your Dad died recently so you must either be moving or living alone, right?",
            "hub":"miller_son",
            "requires":[],
            "answer_lines":[
                {"who":"miller_son",
                "text":"Mona and Basil, they're Baltrice the Baker's children, they begged Baltrice to let me live with them."},

                {"who":"miller_son",
                "text":"Moving's going great. Basil's been helping me and I'm rooming with them, since they're my partner and its been really great actually."},

                {"who":"miller_son",
                "text":"Mostly since Da wasn't the happiest that I'd been seeing Basil."}
            ]
        },

        "miller_son_yes_murder":{
            "title":"Murdered, right? Your Dad, I mean, how are you holding up.",
            "hub":"miller_son",
            "requires":["mu_my_flag"],
            "answer_lines":[
                {"who":"miller_son",
                "text":"My Da...well, I don't think he was murdered for one."},

                {"who":"miller_son",
                "text":"Most people in town are blaming Pepper, but I don't think so even if I don't think they should get married and all, I think the whole died in an inn think was an accident."}
            ]
        },

        "miller_son_no_murder":{
            "title":"What do you know about the Miller's death?",
            "hub":"miller_son",
            "requires":["mu_my_flag"],
            "answer_lines":[
                {"jump":"ch2_miller_son_no"}
            ]
        },

        "miller_son_meet":{
            "title":"My friends and I are investiagating the Miller's death, you want to meet us in the inn around an hour before sunset and see what we find?",
            "hub":"miller_son",
            "requires":["mu_my_flag"],
            "answer_lines":[
                {"effects":{"miller_son_coming":True}},
                {"who":"miller_son",
                "text":"Mmm...Sure, I guess, it can't hurt at least"}
            ]
        },

        "drgn_okay":{
            "title":"Are you holding up alright?",
            "hub":"drgn",
            "requires":[],
            "answer_lines":[
                {"who":"boy",
                "text":"Yes. I think so."},

                {"who":"boy",
                "text":"That question was mostly for an even four wasn't it?"},

                {"who":"boy",
                "text":"Four possible dragons, four possible chapters, four possible characters going into the dragon lair."},

                {"who":"boy",
                "text":"Yes, it makes sense to end on another four."}
            ]
        },

        "drgn_will":{
            "title":"What will you do now.",
            "hub":"drgn",
            "requires":[],
            "answer_lines":[
                {"who":"boy",
                "text":"Keep travelling"},

                {"who":"boy",
                "text":"Keep finding ways to help Wolf."},

                {"who":"boy",
                "text":"Keep learning magic."},

                {"who":"boy",
                "text":"I'm self satisfied and see no reason to change my way of life."}
            ]
        },

        "drgn_future":{
            "title":"What will I do in the future?",
            "hub":"drgn",
            "requires":[],
            "answer_lines":[
                {"who":"boy",
                "text":"Whatever you want, I'm not going to control you."},

                {"who":"boy",
                "text":"But, I don't mind if you keep travelling with Wolf and I."},

                {"who":"boy",
                "text":"But in the end, it's you who makes your future."}
            ]
        },

        "drgn_why":{
            "title":"Why was the dragon...like that?",
            "hub":"drgn",
            "requires":[],
            "answer_lines":[
                {"call":"drgn_variation"}
            ]
        }
    }

    """
        "":{
            "title":"",
            "hub":"drgn",
            "requires":[],
            "answer_lines":[
                {"who":"boy",
                "text":""},
            ]
        },
    
    //basically variables that go in answer_lines, in this order, no idea if repeat can be used with stuff except call and jump
    "repeat"
    "call"
    "jump"
    """