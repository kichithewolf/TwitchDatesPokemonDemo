label introduction:
    
    scene bg black
        
    show burrito sleeping at left

    #voice "day 1/introduction/1"
    espeon "Zzzzz..."
    
    # Treating this as music to sustain it
    #play music "train"
    #$ renpy.music.set_volume(0.5, .5, channel="music")

    #voice "day 1/introduction/2"
    espeon "...Zzzzzz..."

    #$ renpy.music.set_volume(1.0, .5, channel="music")

    #voice "day 1/introduction/3"
    espeon "Zzzzz..."

    #voice "day 1/introduction/4"
    conductor "Next stop: Twitch Academy. Next stop: Twitch Academy."

    show burrito drowsy at left

    #voice "day 1/introduction/5"
    espeon "...Zzzzzhngh?"

    scene bg standard

    show burrito neutral at left

    "...oh yeah, I’m... I’m in the train."

    "Guess I fell asleep on the way here. Funny how moving can really tire you out."

    "The conductor's voice reminds me of my destination."

    "Twitch Academy."

    "Twitch Academy. Twitch. Academy."

    "I keep repeating the words in my head, but it doesn't make it seem any more real."

    "Ever since I was a young Eevee, everyone spoke of how incredible a school it is."

    show burrito dreamy at left

    "The high standards, the prestigious teachers - and past students who went on to illustrious careers! - everything a star school should have."

    "And now, as an Espeon, I will be one of those students!... Hopefully."

    show burrito happy at left

    "Heh. \"Espeon\"... Even that is new to me. For the longest time I knew I wanted to be an Espeon. It was taking me forever to evolve."
    
    "So many of my old teachers suggested I just be like all the other Eevees and use a stone to evolve, but... I finally did it."

    show burrito confident at left

    "I’m an Espeon, The Sun Pokémon. Symbol of a new day, and a new beginning!"

    espeon "And now I’ll have a chance to prove myself at Twitch Academy."

    show burrito thinking at left

    "I wonder what my classmates will be like... I just hope I can make some friends."

    "Of course, I'll still need to keep my grades up."

    show burrito nervous at left

    "But I can't focus too much on my studies or I won't have any friends!"

    "B-but if I slack off too much, I'll have bad grades, which could get me expelled!"

    "Oh, Arceus, I also need to work on my schedule, and make sure tha-!"

    #play sound "ding dong"

    #voice "day 1/introduction/6"
    conductor "Arriving at: Twitch Academy."

    show burrito excited at left

    #voice "day 1/introduction/7"
    espeon "...it's my stop!"

    stop music

    scene dorm with pixellate
    
    $renpy.show("greyout", layer='overlay')
    $renpy.show("id_placeholder", at_list=[Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)], layer='overlay')
    $renpy.pause()
    
    #scene burrito train cg
    "BURRITO CG WOULD BE HERE BUT I GOT NOTHING RIGHT NOW NEED TO COME BACK AND MAKE THIS A SLOWER MOVE"
    "ALSO THE DORM IS JUST A PLACEHOLDER TO SHOW THE SEMI TRANSPARENT FOR THE ID"

    show outside behind burrito with easeinbottom
    hide bg standard with easeouttop

    #play sound "train door opening"

    "The station is rather empty. That's good, I can at least move around pretty quickly and not worry about 'mon traffic. I wanna get settled in as quickly as possible."

    "Let’s see... where did I put that map?"

    "...hm? Oh, there’s a note from mom!"

    #play sound "ruffling paper"

    scene bg standard with dissolve
    window hide
    show mom_note at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $renpy.pause(1.5)

    #voice "day 1/introduction/8"
    letter "Dear Burrito,"

    #voice "day 1/introduction/9"
    burrito "She still uses that nickname..."

    #voice "day 1/introduction/10"
    letter "Hope you have a wonderful first day at school! Your father and I are so proud of you! We know you'll do the best you can, whatever it is you choose to do."

    #voice "day 1/introduction/11"
    letter "On the back of this letter is a map to help you find your way from the train station. (Your father made it, so it might be a good idea to just buy your own.) Take care!"

    #voice "day 1/introduction/12"
    letter "P.S. There's a surprise waiting for you in your new room. Hope it 'spices' things up!"

    #voice "day 1/introduction/13"
    burrito "Dad made a map? This... this can’t be good."
    
    window hide

    show dad_map at Pan((0, 0), (0, 600), 5.0) with dissolve
    
    $renpy.pause(6.0)

    burrito "{cps=5}. . . . .{/cps}"

    #voice "day 1/introduction/14"
    burrito "Oh. Uh... I think I go this way? Or maybe this way? Um..."

    scene bg white
    scene outside with Fade(0.5, 0.0, 0.5, color="#fff")

    show burrito relieved at left

    #voice "day 1/introduction/15"
    burrito "Finally!"

    show burrito neutral at left

    "As I make my way to the dorms, I can hear different conversations going on."

    "Some are talking about that popular sport, Ultraball. I can also hear something about a group called the 'A Team'. Could it be some special team from the school?"

    "I guess I'll have to talk to my classmates to find out more."

    show burrito sleepy at left

    #voice "day 1/introduction/16"
    burrito "Fuaaa..."

    #voice "day 1/introduction/17"
    burrito "For now, I need to get to the dorms. The trip was pretty tiring..."

    show bg black with fade

    scene dorm

    show burrito neutral at left

    "So this is my dorm!"

    "...hmm?"

    "Looks like my roommate is already here, but he's wrapped head to toe in blankets. I better try not to wake him up."

    "I see my luggage is already on my bed, and there's even a package on top of it."

    show burrito neutral at left

    #voice "day 1/introduction/18"
    burrito "I guess this is the surprise that mom mentioned?"

    #voice "day 1/introduction/19"
    letter "\"Burrito,"

    #voice "day 1/introduction/20"
    burrito "Inside is a special treat; it’s one of your favorites! There should be enough in here to last you the rest of the school year. Remember to keep it cold! Love, Mom.\""

    #voice "day 1/introduction/21"
    burrito "Is it... No way! Aha! It is! Mom's special homemade salsa!"

    show burrito neutral at left
    "This is definitely going on my lunch tomorrow. And the day after. And the day after. And the day after..."

    "..."

    "Even though I slept on the train, I'm still dead tired from the trip going here."


    "And my bed looks reeeeeeeeeally comfy right now..."

    show burrito sleepy at left

    #voice "day 1/introduction/22"
    burrito "It's REALLY... comfy..."

    "Really... Fuaa..."

    "...REALLY comfy..."

    "..."
    
    scene bg black with fade
    show text "{color=#962296}{size=20}Tablefort Studios Presents...{/size}{/color}" at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with Pause(4.0)
    hide text
    show logo with fade
    $renpy.pause(4.0)
    scene bg black with fade

return