init python:
    class SmallCapsCharacter(Character):
        def __call__(self, what, *args, **kwargs):
            new_text = ""
            for char in what:
                if char.islower():  # turn lowercase into shrunk uppercase
                    new_text += "{size=-5}" + char.upper() + "{/size}"
                else:  # leave uppercase, punctuation, etc.
                    new_text += char
            return super(SmallCapsCharacter, self).__call__(new_text, *args, **kwargs)