# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:
    tag menu
    
    # Animated background
    #add Movie(size=(800, 600))
    #on "show" action Play("movie", "shuttle.ogv", loops=-1)
    
    window:
        style "mm_root"

    if persistent.clear_one == "True":
        use main_menu_one
    else:
        use main_menu_default
        
screen main_menu_default:
    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    # Animation may be replaced as game unnlocks.
    window:
        xpadding 0
        ypadding 0
        #add "animated_menu"
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .6

        has vbox

        #textbutton _("Start Game") action Start()
        #textbutton _("Load Game") action ShowMenu("load")
        #textbutton _("Preferences") action ShowMenu("preferences")
        #textbutton _("Credits") action Start("credits")
        #textbutton _("Quit") action Quit(confirm=False)
        
        imagemap:
            ground "assets/buttons/main menu/ground.png"
            idle "assets/buttons/main menu/idle.png"
            hover "assets/buttons/main menu/hover.png"
            selected_idle "assets/buttons/main menu/selected_idle.png"
            selected_hover "assets/buttons/main menu/selected_hover.png"
            
            hotspot (24,21,211,29) action Start()
            hotspot (25,68,209,28) action ShowMenu("load")
            hotspot (26,166,209,24) action ShowMenu("preferences")
            hotspot (27,213,210,27) action Start("credits")
            hotspot (24,261,212,32) action Quit(confirm=False)

screen main_menu_one:
    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    # Animation may be replaced as game unnlocks.
    window:
        xpadding 0
        ypadding 0
        #add "animated_menu"
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .625

        has vbox

        #textbutton _("Start Game") action Start()
        #textbutton _("Load Game") action ShowMenu("load")
        #textbutton _("Extras") action ShowMenu("extras")
        #textbutton _("Preferences") action ShowMenu("preferences")
        #textbutton _("Credits") action Start("credits")
        #textbutton _("Quit") action Quit(confirm=False)
        
        imagemap:
            ground "assets/buttons/main menu/ground.png"
            idle "assets/buttons/main menu/idle.png"
            hover "assets/buttons/main menu/hover.png"
            selected_idle "assets/buttons/main menu/selected_idle.png"
            selected_hover "assets/buttons/main menu/selected_hover.png"
            
            hotspot (24,21,211,29) action Start()
            hotspot (25,68,209,28) action ShowMenu("load")
            hotspot (25,116,208,28)
            hotspot (26,166,209,24) action ShowMenu("preferences")
            hotspot (27,213,210,27) action Start("credits")
            hotspot (24,261,212,32) action Quit(confirm=False)
        
        

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html #prefereces

screen preferences:

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")
            
            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")
            
            frame:
                style_group "pref"
                has vbox
                
                label _("Main Voices")
                
                null height 5
                
                imagemap:
                    ground "assets/buttons/voice control/burrito_ground.png"
                    idle "assets/buttons/voice control/burrito_idle.png"
                    hover "assets/buttons/voice control/burrito_hover.png"
                    selected_idle "assets/buttons/voice control/burrito_selected_idle.png"
                    selected_hover "assets/buttons/voice control/burrito_selected_hover.png"
                    hotspot (1,0,195,34) action [ToggleVoiceMute("burrito_voice"), ToggleVoiceMute("uk_main_burrito")]
                imagemap:
                    ground "assets/buttons/voice control/katie_ground.png"
                    idle "assets/buttons/voice control/katie_idle.png"
                    hover "assets/buttons/voice control/katie_hover.png"
                    selected_idle "assets/buttons/voice control/katie_selected_idle.png"
                    selected_hover "assets/buttons/voice control/katie_selected_hover.png"
                    hotspot (1,0,195,34) action [ToggleVoiceMute("katie_voice"), ToggleVoiceMute("uk_main_katie")]
                    
                imagemap:
                    ground "assets/buttons/voice control/abba_ground.png"
                    idle "assets/buttons/voice control/abba_idle.png"
                    hover "assets/buttons/voice control/abba_hover.png"
                    selected_idle "assets/buttons/voice control/abba_selected_idle.png"
                    selected_hover "assets/buttons/voice control/abba_selected_hover.png"
                    hotspot (1,0,195,34) action [ToggleVoiceMute("abba_voice"), ToggleVoiceMute("uk_main_abba")]
                    
                imagemap:
                    ground "assets/buttons/voice control/air_ground.png"
                    idle "assets/buttons/voice control/air_idle.png"
                    hover "assets/buttons/voice control/air_hover.png"
                    selected_idle "assets/buttons/voice control/air_selected_idle.png"
                    selected_hover "assets/buttons/voice control/air_selected_hover.png"
                    hotspot (1,0,195,34) action [ToggleVoiceMute("air_voice"), ToggleVoiceMute("uk_main_air")]
                    
                imagemap:
                    ground "assets/buttons/voice control/abby_ground.png"
                    idle "assets/buttons/voice control/abby_idle.png"
                    hover "assets/buttons/voice control/abby_hover.png"
                    selected_idle "assets/buttons/voice control/abby_selected_idle.png"
                    selected_hover "assets/buttons/voice control/abby_selected_hover.png"
                    hotspot (1,0,195,34) action [ToggleVoiceMute("abby_voice"), ToggleVoiceMute("uk_main_abby")]
                
                imagemap:
                    ground "assets/buttons/voice control/gator_ground.png"
                    idle "assets/buttons/voice control/gator_idle.png"
                    hover "assets/buttons/voice control/gator_hover.png"
                    selected_idle "assets/buttons/voice control/gator_selected_idle.png"
                    selected_hover "assets/buttons/voice control/gator_selected_hover.png"
                    hotspot (1,0,195,34) action [ToggleVoiceMute("gator_voice"), ToggleVoiceMute("uk_main_gator")]
                    
                imagemap:
                    ground "assets/buttons/voice control/mary_ground.png"
                    idle "assets/buttons/voice control/mary_idle.png"
                    hover "assets/buttons/voice control/mary_hover.png"
                    selected_idle "assets/buttons/voice control/mary_selected_idle.png"
                    selected_hover "assets/buttons/voice control/mary_selected_hover.png"
                    hotspot (1,1,195,34) action [ToggleVoiceMute("mary_voice"), ToggleVoiceMute("uk_main_mary")]
                    
                imagemap:
                    ground "assets/buttons/voice control/brian_ground.png"
                    idle "assets/buttons/voice control/brian_idle.png"
                    hover "assets/buttons/voice control/brian_hover.png"
                    selected_idle "assets/buttons/voice control/brian_selected_idle.png"
                    selected_hover "assets/buttons/voice control/brian_selected_hover.png"
                    hotspot (1,1,195,34) action [ToggleVoiceMute("brian_voice"), ToggleVoiceMute("uk_main_brian")]

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")
                    
            frame:
                style_group "pref"
                has vbox
                
                label _("Other Voices")
                textbutton "Mute All Main Characters" action [SetVoiceMute("burrito_voice", True), SetVoiceMute("katie_voice", True),
                    SetVoiceMute("abba_voice", True), SetVoiceMute("air_voice", True), SetVoiceMute("abby_voice", True), SetVoiceMute("gator_voice", True),
                    SetVoiceMute("mary_voice", True), SetVoiceMute("brian_voice", True),  SetVoiceMute("uk_main_burrito", True),
                    SetVoiceMute("uk_main_katie", True), SetVoiceMute("uk_main_abba", True), SetVoiceMute("uk_main_air", True), SetVoiceMute("uk_main_abby", True),
                    SetVoiceMute("uk_main_gator", True), SetVoiceMute("uk_main_mary", True), SetVoiceMute("uk_main_brian", True)]
                textbutton "Unmute All Main Characters" action [SetVoiceMute("burrito_voice", False), SetVoiceMute("katie_voice", False),
                    SetVoiceMute("abba_voice", False), SetVoiceMute("air_voice", False), SetVoiceMute("abby_voice", False), SetVoiceMute("gator_voice", False),
                    SetVoiceMute("mary_voice", False), SetVoiceMute("brian_voice", False),  SetVoiceMute("uk_main_burrito", False),
                    SetVoiceMute("uk_main_katie", False), SetVoiceMute("uk_main_abba", False), SetVoiceMute("uk_main_air", False), SetVoiceMute("uk_main_abby", False),
                    SetVoiceMute("uk_main_gator", False), SetVoiceMute("uk_main_mary", False), SetVoiceMute("uk_main_brian", False)]
                textbutton "Toggle All Minor Characters" action [ToggleVoiceMute("atv_voice"), ToggleVoiceMute("gyra_voice"), ToggleVoiceMute("arc_voice"), ToggleVoiceMute("xa_voice"),
                    ToggleVoiceMute("mw_voice"), ToggleVoiceMute("fonz_voice"), ToggleVoiceMute("snake_voice"), ToggleVoiceMute("uk_minor_voice"), ToggleVoiceMute("dux_voice"),
                    ToggleVoiceMute("conductor_voice"), ToggleVoiceMute("letter_voice"), ToggleVoiceMute("whitney_voice"), ToggleVoiceMute("everyone_voice"), ToggleVoiceMute("surge_voice"),
                    ToggleVoiceMute("ponyta_voice"), ToggleVoiceMute("stua_voice"), ToggleVoiceMute("stub_voice"), ToggleVoiceMute("stuc_voice"), ToggleVoiceMute("stud_voice"),
                    ToggleVoiceMute("lance_voice"), ToggleVoiceMute("misty_voice")]
                textbutton "Toggle All Spoiler Characters" action [] # No spoiler characters yet

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")
                
            frame:
                style_group "pref"
                has vbox
                
                label _("Important Voices")
                
                null height 5
                
                imagemap:
                    ground "assets/buttons/voice control/will_ground.png"
                    idle "assets/buttons/voice control/will_idle.png"
                    hover "assets/buttons/voice control/will_hover.png"
                    selected_idle "assets/buttons/voice control/will_selected_idle.png"
                    selected_hover "assets/buttons/voice control/will_selected_hover.png"
                    hotspot (1,1,195,34) action ToggleVoiceMute("")

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            #textbutton _("Yes") action yes_action
            #textbutton _("No") action no_action
            
            imagemap:
                ground "assets/buttons/yesnoprompt/ground.png"
                idle "assets/buttons/yesnoprompt/idle.png"
                hover "assets/buttons/yesnoprompt/hover.png"
                
                hotspot (78,51,101,93) action yes_action
                hotspot (412,56,94,85) action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        #textbutton _("Back") action Rollback()
        #textbutton _("Save") action ShowMenu('save')
        #textbutton _("Q.Save") action QuickSave()
        #textbutton _("Q.Load") action QuickLoad()
        #textbutton _("Skip") action Skip()
        #textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        #textbutton _("Auto") action Preference("auto-forward", "toggle")
        #textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

