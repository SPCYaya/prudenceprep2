﻿## This file contains options that can be changed to customize your game.

## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Wild Roses of Prudence Prep")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "0.1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""

Created and written by the Society for the Prevention of Cruelty to Yayas (SPCYaya).
All questions and concerns may be addressed to yaya.did.nothing.wrong@gmail.com!

Character art and CGs by Hiwonoafu - https://hiwonoafu.tumblr.com/

Special Thanks - /u/


Music:




SFX:


door close 2.wav
https://freesound.org/people/THE_bizniss/sounds/53269/

Door Unlock
https://freesound.org/people/angelkunev/sounds/519065/

Hotel room door unlocking
https://freesound.org/people/wlabarron/sounds/494128/

door knock
https://freesound.org/people/SubwaySandwitch420/sounds/540770/

Door slam 2.wav
https://freesound.org/people/bennstir/sounds/80929/

dial tone_us.mp3
https://freesound.org/people/Felfa/sounds/188694/

Cell Phone Vibrate.wav
https://freesound.org/people/SmartWentCody/sounds/179012/

Other:

lace border PNG Designed By Raya Design https://pngtree.com/freepng/elegant-white-lace-pattern_7509897.html


All rights belong to their respective owners.

""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "wildroses"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

define config.sample_sound = "audio/sfx/doorclose.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

#define config.main_menu_music = "audio/music/aquarium.ogg"                #### add back eventually


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve

## If not None, a transition that is used when exiting the yes/no prompt screen.

define config.enter_yesno_transition = dissolve

## If not None, a transition that is used when returning to the main menu from the game menu, using the MainMenu() action.

define config.game_main_transition = dissolve

## Between screens of the game menu.

define config.intra_transition = dissolve

## A transition that is used after a game has been loaded.

define config.after_load_transition = dissolve

## Used when entering the main menu after the game has ended.

define config.end_game_transition = fade

## If not None, a transition to use when the image is changed by a say statement with image attributes.

define config.say_attribute_transition = Dissolve(.3)

## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 70


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 10


## Audio channels are stopped when the window is minimized, and resumed when
## the window is restored.

default preferences.audio_when_minimized = False


## Audio channels are stopped when the window loses keyboard focus, and resumed
## when the window regains keyboard focus.

default preferences.audio_when_unfocused = False


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "wildroses-4265909628"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"

## Developer Console ########################################################################
##
## Enables the developer console (SHIFT+O).

define config.developer = True


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "spcyaya/wildroses"
