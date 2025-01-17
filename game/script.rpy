# Character Definitions
define H = Character("Vittoria", image="vittoria", who_outlines=[ (3, "#ffffff") ])
define O = Character("Vincenza", image="vincenza", who_outlines=[ (3, "#ffffff") ])
define S = Character("Sibyl", image="sibyl", who_outlines=[ (3, "#ffffff") ])
define T = Character("Tanya", image="tanya", who_outlines=[ (3, "#ffffff") ])
define C = Character("Clover", image="clover", who_outlines=[ (3, "#ffffff") ])

# Misc Characters
define st = Character("Student", who_outlines=[ (3, "#ffffff") ])
define te = Character("Teacher", who_outlines=[ (3, "#ffffff") ])
define mi = Character("Miss Izzie", image="izzie", who_outlines=[ (3, "#ffffff") ])
define mw = Character("Miss Woolsey", image="naomi", who_outlines=[ (3, "#ffffff") ])
define g1 = Character("Girl 1", image="vittoria", who_outlines=[ (3, "#ffffff") ])
define g2 = Character("Girl 2", image="vincenza", who_outlines=[ (3, "#ffffff") ])
define rm = Character("Roommate", image="sibyl", who_outlines=[ (3, "#ffffff") ])
define who = Character("???", who_outlines=[ (3, "#ffffff") ])

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

# Variable Definitions
default secret_lilies_romance = None

# The game starts here.
label start:
    stop music fadeout 0.5 # stops main menu music 
    jump sl_rom

# The game ends here.
label end:
    stop music fadeout 0.5
    scene bg black with fade
    scene bg endcard with fade
    pause 3.0
    scene bg black with fade
    return