# qunlock_questions.rpy
# Runtime UI/state for question hubs.

# Make sure this default exists so screens can read/write it.
default _current_topic = None

init 1 python:
    #import renpy

    # NOTE: `questions` must already be defined (in another file) before this init runs.
    # If it's not, move this init to run after that file or define questions earlier.

    # --- runtime state ---
    # store asked questions as a set for fast membership tests
    #if not hasattr(store, "asked_questions"):
    #    asked_questions = set()
    #else:
    #    asked_questions = set(store.asked_questions)

    # convenience list of question ids (not required, but handy)
    question_list = list(questions.keys())
    asked_questions = []

    # --- storage initialization (put in an init block or at top-level) ---
    # ensure the saved list exists (Ren'Py store uses RevertableList)
    #if not hasattr(store, "asked_questions"):
    #    store.asked_questions = []   # persists as a list in saves

    # --- helper functions ---

    # Check whether all requirements in req_list are met.
    def meets_requirements(req_list):
        if not req_list:
            return True
        # req_list is a list of ids; return True only if every item in asked_questions
        return all(item in asked_questions for item in req_list)

    # Return unlocked questions for a given hub
    def unlocked_questions(hub_key):
        out = []
        for key, meta in questions.items():
            if meta.get("hub") != hub_key:
                continue
            locked = not meets_requirements(meta.get("requires", []))
            if not locked:
                out.append((key, meta, locked))
        # optional: keep a stable order
        #out.sort(key=lambda t: t[1].get("title", t[0]))
        return out

    # Mark a question as asked (persist to store so saves work)
    def mark_answered(question_id):
        asked_questions.append(question_id)

        #templst = getattr(store, "asked_questions", [])
        #if question_id not in templst:
        #    templst.append(question_id)
        #    store.asked_questions = templst

    def create_followup_from(choice_create, hub_key):
        """
        choice_create: dict with keys like 'id', 'title', 'answer_lines', optional 'requires'
        hub_key: string, assign hub to followup so it shows in the same wheel
        Returns the id created.
        """
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

    # Play a topic at runtime (resolves Characters safely)
    def play_topic(question_id):
        meta = questions.get(question_id, None)
        if not meta:
            renpy.log("play_topic: missing question " + str(question_id))
            return
        for line in meta.get("answer_lines", []):
            who = line.get("who", None)
            text = line.get("text", "")
            char = getattr(renpy.store, who, None) if who else None
            if char:
                renpy.say(char, text)
            else:
                renpy.say(None, text)
        # after playing, mark completed for unlocks
        mark_answered(question_id)

# --- label to play topic with nested-choices support ---
label show_topic_answer:
    $ topic_id = _current_topic
    if not topic_id:
        $ renpy.log("show_topic_answer: no _current_topic set")
        return

    # run the answer lines; this label runs in a proper interaction context so renpy.say() is safe
    python:
        meta = questions.get(topic_id, None)
        if not meta:
            renpy.log("show_topic_answer: missing topic " + str(topic_id))
        else:
            lines = list(meta.get("answer_lines", []))
            i = 0
            while i < len(lines):
                line = lines[i]
                who = line.get("who", None)
                text = line.get("text", "")
                # display the line
                char = getattr(renpy.store, who, None) if who else None
                if char:
                    renpy.say(char, text)
                else:
                    renpy.say(None, text)

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
                        renpy.call(selected["jump_label"])
                        break

                    # otherwise continue to next line
                    i += 1
                    continue

                # no choices -> next line
                i += 1

            # mark the asked question (decrement asks)
            mark_answered(topic_id)

    # return to the hub: because we used Call("show_topic_answer") inside the screen,
    # the Call returns here and the original 'call screen hub_menu' returns to the hub_loop.
    return

label hub_loop(hub_key, num_asks):
    # initialize ask_remaining in store if missing

    while num_asks > 0:
        call screen hub_menu(hub_key)
        $ num_asks -= 1
    return

# --- screen: left scroll wheel of unlocked questions ---
screen hub_menu(hub_key):
    tag menu

    # capture up/down keys here if needed (optional)
    #key "up" action SetVariable("_current_topic", _current_topic)  # placeholder to capture keys
    #key "down" action SetVariable("_current_topic", _current_topic)

    frame:
        xalign 0.05
        xmaximum int(config.screen_width * 0.25)
        xminimum 220
        yalign 0.05
        ymaximum 540

        has vbox

        # Use Ren'Py expression $ to run the helper and get entries
        python:
            entries = unlocked_questions(hub_key)

        viewport id "wheel_viewport" draggable True mousewheel True:
            vbox:
                spacing 6

                if not entries:
                    text "No questions available." xalign 0.0

                for tid, meta, locked in entries:
                    # Single button: select + play. Use a list of actions so both run.
                    # SetVariable sets the selected topic (for preview/highlight).
                    # Function(play_topic, tid) immediately plays the topic.
                    if _current_topic == tid:
                        textbutton meta['title'] action [SetVariable("_current_topic", tid), Call("show_topic_answer")]
                    else:
                        textbutton meta['title'] action [SetVariable("_current_topic", tid), Call("show_topic_answer")]

