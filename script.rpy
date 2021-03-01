# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Gov-Chan", color="#800000")

define f = Character("Teri", color="#0000ff")

define g = Character("[name]")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "music/guitar-melancholy-2.ogg" fadeout 1

    scene bg main

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "Welcome to this test game"
    "Everything is very rough because this is simply to show this idea works"

    stop music fadeout 1

    python:
        name = renpy.input("What's your name?")

        name = name.strip() or "Ren"

    play music "music/bgmain.mp3" fadeout 1

    show govchan full:
        xalign .5
        yalign 1.05
    image govchan full = im.Scale("govchan full.png", 300, 500)

    e "?"
    pause (.5)
    show govchan happy:
        xalign .5
        yalign 1.15

    image govchan happy = im.Scale("govchan happy.png", 450, 500)
    with Dissolve(1)

    # These display lines of dialogue.

    e "Hey! You're the new student right?"
    e "Nice to meet ya!"
    e "My name is Gov-Chan!"

    show govchan cute
    image govchan cute = im.Scale("govchan cute.png", 550, 600)

    e "The super cute mascot of the AMGS!"

    show govchan happy
    image govchan happy = im.Scale("govchan happy.png", 450, 500)

    e "My job is to introduce you to Farrington High School!"

    e "Would you be interested in a tour, [name]?"

    menu:

        "Yes":
            jump choice1_yes

        "No":
            jump choice1_no

    label choice1_yes:
        $ menu_flag = True

        e "Great! Then let's being the GREAT GOV-CHAN TOUR!"

        jump choice1_done

    label choice1_no:

        $ menu_flag = False

        e "Do you... already know where everything is?"

        jump choice1_done

    label choice1_done:

    e "Well then..."

    e "Uh..."

    "..."

    g "Getting real uncomfortable here."

    if menu_flag:

        e "Right the tour"

        e "Let's begin by talking about where we currently are"

    else:

        e "I'll be seeing you then I guess?"

        return


    e "The front of the building is part of the much larger A building."

    e "The building has historical significance because it was actually used as
    a medical building by the U.S Military during WW2."

    e "The campus boasts the sculpture The Seed by renowned Japanese-American
    artist Satoru Abe."

    e "The front of the campus features important offices, such as the attendance,
    registrars, conselors office, and tons more."


    menu:

        e "Would you like to continue the tour?"

        "Of course!":

            e "That's what we like to hear."

        "No thanks.":

            e "Well, okay I guess"

            e "Be seeing you around later."

            return

    e "If you look to your right..."

    with Dissolve(.5)

    scene bg audi
    image bg audi = im.Scale("bg audi.jpg", 1280, 720)

    show govchan happy
    image govchan happy = im.Scale("govchan happy.png", 450, 500)

    e "This is the auditorium."

    e "It was rebuilt after it broke a couple of years back."

    menu:

        e "Would you like to go inside or go somewhere else?"

        "Sure why not":

            e "In we go!"

        "Let's go somewhere else.":

            e "Alright we'll go somewhere else then."

    e "But first..."
    e "Let's play a game!"

    # This ends the game.

    return
