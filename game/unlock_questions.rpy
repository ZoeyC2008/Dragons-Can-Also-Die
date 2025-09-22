#this is to keep script clean
#I'm using a data-driven prerequisites (understanding? No, copy & paste code form internet is good)

init python:
    #the big list of questions (20/09 i wonder if it'll be longer than the script?)
    questions = {
        #really long, but this is basically all the text i need for my question hubs
        #which are like, a good half? of the game, and where most of the exploration is
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
                    "jump_label":"mirror_end"}
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

    }

    """"
        "":{
            "title":"",
            "hub":"mirror",
            "requires":[],
            "answer_lines":[
                {"who":"",
                "text":""},

                {"choices":[
                    {"text":"",
                    "effects":}
                ]}
            ]
        }
    
    //basically variables that go in answer_lines, in this order, repeat is to only be used with call and jump, trust
    "repeat"
    "call"
    "jump"
    

    "story_hour": {
    "title": "Tell me a story",
    # top-level answer_lines can be empty or default; we'll use variants
    "hub": "mirror",
    "variants": [
        [   # variant 0 (list of lines)
            {"who": "mirror", "text": "Once upon a time..."},
            {"who": "mirror", "text": "They lived happily ever after."}
        ],
        [   # variant 1
            {"who": "mirror", "text": "A different tale begins..."},
            {"who": "mirror", "text": "And so it goes."}
        ],
        # ...more variants...
    ],
    requirements: []
    """