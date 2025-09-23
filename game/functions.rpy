# qunlock_questions.rpy
# Runtime UI/state for question hubs.

# Make sure this default exists so screens can read/write it.
default _current_topic = None
default asked_questions = []


init 2 python:
    #random magic exposition or story!
    import random
    
    #variables
    question_list = list(questions.keys())

    # --- helper functions ---

    # Check whether all requirements in req_list are met.
    def meets_requirements(req_list):
        #empty list is good
        if not req_list:
            return True
        # req_list is a list of ids; return True only if every item in asked_questions
        
        for req in req_list:
            if isinstance(req, str):
                if req not in asked_questions:
                    return False
            if not req:
                return False
        #everything else evaluates to true        
        return True

    # Return unlocked questions for a given hub
    def unlocked_questions(hub_key):
        out = []
        for key, meta in questions.items():
            #if it's not the right hub, don't retrieve it!
            if meta.get("hub") != hub_key:
                continue
            #avoid repeats (i'll need to figure out a way to ignore this for wolf & sojourn)
            if key in asked_questions:
                continue

            #i'm afraid to mess with locked, but i'm think this is just a requiremnets check
            locked = not meets_requirements(meta.get("requires", []))
            if not locked:
                out.append((key, meta, locked))
        return out

    # Mark a question as asked (persist to store so saves work)
    def mark_answered(question_id):
        #no dupes!
        if question_id not in asked_questions:
            asked_questions.append(question_id)

    #we making the options even if there isn't much branching (at least I try not to have to much)
    def create_followup_from(choice_create, hub_key):
        # generate id if none given
        fid = choice_create.get("id")
        if not fid:
            # simple unique id generation
            base = choice_create.get("title", "followup").lower().replace(" ", "_")
            i = 1
            while base + "_" + str(i) in questions:
                i += 1
            fid = f"{base}_{i}"
        # build minimal meta
        meta = {
            "title": choice_create.get("title", fid),
            "hub": hub_key,
            "requires": choice_create.get("requires", []),
            "answer_lines": choice_create.get("answer_lines", [])
        }
        questions[fid] = meta
        renpy.log(f"Created followup question {fid}")
        return fid

# --- label to play topic with nested-choices support ---
label show_topic_answer:
    $ topic_id = _current_topic
    if not topic_id:
        $ renpy.log("show_topic_answer: no _current_topic set")
        return
    
    python: 
        #what if a i want to call or jump stuff
        call_label = None
        jump_label = None

        #pre-scan data
        is_repeatable = False

        #interactable
        interact_flag = True

    # run the answer lines; this label runs in a proper interaction context so renpy.say() is safe
    python:
        meta = questions.get(topic_id, None)
        if not meta:
            renpy.log("show_topic_answer: missing topic " + str(topic_id))
        else:
            # copy the lines
            lines = list(meta.get("answer_lines", []))

            #look for that yummy pre-scan data
            if meta.get("repeatable", False):
                is_repeatable = True
                interact_flag = False
            else:
                for L in lines:
                    if "repeat" in L and L.get("repeat"):
                        is_repeatable = True
                        interact_flag = False
                        break
            
            #main loop for displaying stuff
            i = 0
            while i < len(lines):
                line = lines[i]
                
                #there's a call
                if "call" in line:
                    call_label = line["call"]
                    break
                #if there a jump
                if "jump" in line:
                    jump_label = line["jump"]
                    break
                
                
                who = line.get("who", None)
                text = line.get("text", "")
                
                #interact (prevent a double click issue)
                if "call" in line or "jump" in line or "choices" in line or "effects" in line:
                    interact_flag = False
                
                # display the line
                char = getattr(renpy.store, who, None) if who else None
                if char:
                    renpy.say(char, text, interact=interact_flag)
                else:
                    renpy.say(None, text, interact=interact_flag)
                
                if "effects" in line:
                    for stat, amount in selected["effects"].items():
                        setattr(renpy.store, stat, getattr(renpy.store, stat, 0) + amount) 
                
                # if this line has choices, present them
                if "choices" in line:
                    menu_list = []
                    for choice in line["choices"]:
                        menu_list.append((choice.get("text", "..."), choice))

                    selected = renpy.display_menu(menu_list)

                    # if choice wants to create a followup in the hub, create it now
                    if "create_followup" in selected:
                        create_followup_from(selected["create_followup"], meta.get("hub"))
                        # After creating followup, we want to return to the hub (not auto-play followup).
                        # So break out and finish this label.
                        break

                    # if choice has a next_index, jump there in same answer_lines
                    if "next_index" in selected:
                        i = int(selected["next_index"])
                        continue

                    # if choice asks to jump to another label, do it
                    if "jump_label" in selected:
                        renpy.jump(selected["jump_label"])
                        break
                    
                    #if there are any effects
                    if "effects" in selected:
                        for stat, amount in selected["effects"].items():
                            setattr(renpy.store, stat, getattr(renpy.store, stat, 0) + amount)  
                    # otherwise continue to next line
                    i += 1
                    continue

                # no choices -> next line
                i += 1

    #actually call/jump
    if call_label is not None:
        call expression call_label
    if jump_label is not None:
        hide screen choice_hub
        jump expression jump_label
    
    # mark the asked question
    python:
        if not is_repeatable:
            mark_answered(topic_id)
        

    # return to the hub: because we used Call("show_topic_answer") inside the screen,
    # the Call returns here and the original 'call screen hub_menu' returns to the hub_loop.
    return

default hub_loop_num = 0
default hub_key = None
default num_asks = 0

label hub_loop:    
    # hub loop
    
    $ hub_loop_num = 0

    while hub_loop_num < num_asks:        
        $ entries = unlocked_questions(hub_key)
        
        call screen choice_hub (items=entries)

        call show_topic_answer

        if hub_key == "mirror":
            call mirror_reaction
        
        if hub_key == "travel" and num_asks == 0:
            $ travel_early_flag = False
            call wolf_sleep

        $ hub_loop_num += 1    
    return

