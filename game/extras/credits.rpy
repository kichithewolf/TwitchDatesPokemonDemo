init python:
    
    # This prevents anything from happening. Be very careful to keep disabled when not in use.
    overriding_on = None
    def overriding_overlay():
        if not overriding_on:
            return
        ui.keymap(mousedown_1=ui.returns(None))
        ui.keymap(mouseup_1=ui.returns(None))
        ui.keymap(mousedown_3=ui.returns(None))
        ui.keymap(mouseup_3=ui.returns(None))
        ui.keymap(K_KP_ENTER=ui.returns(None))
        ui.keymap(K_RETURN=ui.returns(None))

    config.overlay_functions.append(overriding_overlay) 

label credits:
    $overriding_on = True

    window hide
    
    # Stop any other music that's playing.
    stop music
    
    scene bg standard with fade
    
    show text "{color=#962296}{size=50}{b}Twitch Dates Pokemon{/b}{/size}{/color}" at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    
    $renpy.pause(2.0)
    
    scene credits_writers with dissolve
    
    $renpy.pause(4.0)
    
    scene credits_editors with pixellate
    
    $renpy.pause(4.0)
    
    scene credits_artists with blinds
    
    $renpy.pause(4.0)
    
    scene credits_music with squares
    
    $renpy.pause(4.0)
    
    show credits_va with zoomin
    
    $renpy.pause(4.0)
    
    scene credits_va2 with wipeleft
    
    $renpy.pause(4.0)
    
    scene credits_programming with wiperight
    
    $renpy.pause(4.0)
    
    scene credits_special with irisin
    
    $renpy.pause(4.0)
    
    scene credits_renpy with irisout
    
    $renpy.pause(4.0)
    
    stop music fadeout 2.0
    
    $overriding_on = None
    
return