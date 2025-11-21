# Character Definitions
define H = Character("Vittoria", image="vit", who_outlines=[ (3, "#ffffff") ])
define O = Character("Vincenza", image="vin", who_outlines=[ (3, "#ffffff") ])
define S = Character("Sibyl", image="sibyl", who_outlines=[ (3, "#ffffff") ])
define T = Character("Tanya", image="tanya", who_outlines=[ (3, "#ffffff") ])
define TL = Character("Tanya", image="tlax", who_outlines=[ (3, "#ffffff") ])
define C = Character("Clover", image="clover", who_outlines=[ (3, "#ffffff") ])
define CL = Character("Clover", image="clax", who_outlines=[ (3, "#ffffff") ])
define mi = Character("Miss Izzie", image="izzie", who_outlines=[ (3, "#ffffff") ])
define mw = Character("Miss Woolsey", image="naomi", who_outlines=[ (3, "#ffffff") ])

# Misc Characters
define st = Character("Student", who_outlines=[ (3, "#ffffff") ])
define te = Character("Teacher", who_outlines=[ (3, "#ffffff") ])
define who = Character("???", who_outlines=[ (3, "#ffffff") ])
define nurse = Character("Nurse", who_outlines=[ (3, "#ffffff") ])
define phone = Character("Smartphone", who_outlines=[ (3, "#ffffff") ])
define blanche = Character("Blanche", who_outlines=[ (3, "#ffffff") ])
define veronika = Character("Veronika", who_outlines=[ (3, "#ffffff") ])
define player = Character("Player", who_outlines=[ (3, "#ffffff") ])

# Custom Sprite Transforms
transform center:
    zoom 0.8 xalign 0.5 yalign -0.2
transform left:
    zoom 0.8 xalign 0.0 yalign -0.2
transform right:
    zoom 0.8 xalign 1.0 yalign -0.2
transform mleft:
    zoom 0.8 xalign 0.15 yalign -0.2
transform mright:
    zoom 0.8 xalign 0.85 yalign -0.2
transform qleft:
    zoom 0.8 xalign 0.05 yalign -0.2
transform qmleft:
    zoom 0.8 xalign 0.35 yalign -0.2
transform qmright:
    zoom 0.8 xalign 0.65 yalign -0.2
transform qright:
    zoom 0.8 xalign 0.95 yalign -0.2

# Custom image transition.
define dd = Dissolve(0.3)

# Variable Definitions
default secret_lilies_romance = None

# The game starts here.
label start:
    stop music fadeout 0.5 # stops main menu music 
    jump test
    #jump sl_rom

# The game ends here.
label end:
    return

# testing
label test:
    scene bg cafeteria
    show naomi stern at left
    show clover scowl at right with dd
    C annoyed "dialogue 1"
    show naomi stern at center with dd
    mw excited "dialogue 2"
