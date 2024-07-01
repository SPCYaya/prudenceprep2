# Character Definitions
define N = Character("Naomi", image="naomi", who_outlines=[ (3, "#ffffff") ])
define E = Character("Elodie", image="elodie", who_outlines=[ (3, "#ffffff") ])
define P = Character("Prudence", image="prudence", who_outlines=[ (3, "#ffffff") ])
define I = Character("Izzie", image="izzie", who_outlines=[ (3, "#ffffff") ])
define H = Character("Vittoria", image="vittoria", who_outlines=[ (3, "#ffffff") ])
define O = Character("Vincenza", image="vincenza", who_outlines=[ (3, "#ffffff") ])
define S = Character("Sibyl", image="sibyl", who_outlines=[ (3, "#ffffff") ])
define T = Character("Tanya", image="tanya", who_outlines=[ (3, "#ffffff") ])

# Misc Characters
define Student = Character("Student", who_outlines=[ (3, "#ffffff") ])
define Nurse = Character("Nurse", who_outlines=[ (3, "#ffffff") ])
define ch = Character("Chairwoman", image="prudence", who_outlines=[ (3, "#ffffff") ])
define mi = Character("Miss Izzie", image="izzie", who_outlines=[ (3, "#ffffff") ])

# Custom Sprite Transforms
transform mleft:
    xalign 0.15 yalign 1.0
transform mright:
    xalign 0.85 yalign 1.0
transform qleft:
    xalign 0.05 yalign 1.0
transform qmleft:
    xalign 0.35 yalign 1.0
transform qmright:
    xalign 0.65 yalign 1.0
transform qright:
    xalign 0.95 yalign 1.0

# Custom image transition.
define dd = Dissolve(0.3)

# The game starts here.
label start:
    stop music fadeout 0.5 # stops main menu music 
    jump act1

# The game ends here.
label end:
    stop music fadeout 0.5
    scene bg black with fade
    scene bg endcard with fade
    pause 3.0
    scene bg black with fade
    return