label day_1_lunch:
    
    scene placeholder_lunch

    "I probably should have gotten here earlier; this cafeteria is pretty packed! At least I don’t have to wait in line since I brought lunch today."

    "It’s definitely better than anything that a school cafeteria could ever prepare, anyway."

    #play sound crinkle

    "Aaaand yes it is!"

    "Super-ultra-deluxe Cheri burritos with Mom’s special homemade salsa! The perfect lunch!"

    "Hmm, now where should I sit? Most of the tables are already filled up."

    "Hmm..."

    $renpy.pause()

    "There's a lone table sitting at the corner."

    "I don't know if I should sit with others yet. I really don't know any of them, so I feel like I'd be a bit of a bother..."

    show burrito neutral at left
    
    #voice "day 1/day_1_lunch/1"
    burrito "It would be nice to join in and make some friends. But until then..."

    show burrito sad at left
    
    #voice "day 1/day_1_lunch/2"
    burrito "I'll... just sit by myself for now."

    hide burrito

    #play sound sit

    #play sound crinkle

    "Mom sent me the family’s celebratory burritos for today’s lunch." 

    "Aaah, I can already hear my stomach growling in excitement."

    "Ooh, salsa... yeah that's it..."

    "These just look even more delicious with the salsa on it."                
    
    #voice "day 1/day_1_lunch/3"    
    burrito "Oh my lovely burritos, keep me company for today..."

    "..."

    "Even if I can’t sit with other students right now, I really shouldn't be upset."

    "After all, how can I be anything but happy with delicious burritos for lunch?"

    "*munch munch*"

    "Mmm... just... aaah..."
    
    #voice "day 1/day_1_lunch/4"
    uk_brian "E-excuse me?"

    show burrito startled at left
    
    #voice "day 1/day_1_lunch/5"
    burrito "A-aah! H-huh?"

    hide burrito

    #{scene change: CG - Brian introduction}
    "BRIAN CG"
    
    #voice "day 1/day_1_lunch/6"
    brian "Um, hello there. My name is Brian. Would you mind if I... sit with you?"
        
    #voice "day 1/day_1_lunch/7"
    burrito "Of course! I mean, if you really want to."
            
    #voice "day 1/day_1_lunch/8"
    brian "Sure!"
        
    #{Brian character panel appears}
    "BRIAN CHAR PAN"
    #{Brian - Pidgeot
    #Nicknames: Just Brian, Lil' Abba, Pudgy
    #Hobby: Just chillin'.
    #"Just be yourself."}

    "How nice! I got someone to sit with on the first day! He looks like a pretty nice guy too."

    "Brian, huh. He must also not have a group that he can sit with."

    "Alright, great opportunity to make a new friend!"

    scene placeholder_lunch
        
    "Brian sits across from me and I notice his lunch; it’s a salad with lots of sunflower seeds, and some sort of vegetable sandwich."

    show brian neutral at right
    
    #voice "day 1/day_1_lunch/9"
    brian "So, um... you're Burrito, right? I heard that you've seen my brother already..."

    show burrito surprised at left
    
    #voice "day 1/day_1_lunch/10"
    burrito "Your brother? Wait, do you mean..."

    hide burrito

    hide brian

    show abba neutral at center

    $ renpy.pause(0.5)

    hide abba with fade

    show burrito surprised at left

    show brian neutral at right
    
    #voice "day 1/day_1_lunch/11"
    brian "Yes, Abba's my older brother."
    
    #voice "day 1/day_1_lunch/12"
    burrito "Oh, I've met Abba! You're his brother? You sound nothing like him!"
    
    #voice "day 1/day_1_lunch/13"
    brian "Well, my brother decided to drop his accent a long time ago. Now, I don't think he could sound like me if he tried."
    
    show burrito smiling at left
    #voice "day 1/day_1_lunch/14"
    burrito "That's pretty interesting. He seems like a really nice guy!"

    show brian nervous at right
    
    #voice "day 1/day_1_lunch/15"
    brian "Y-yeah, he is."

    show burrito confused at left
    
    #voice "day 1/day_1_lunch/16"
    burrito "Huh?"

    show brian neutral at right
    
    #voice "day 1/day_1_lunch/17"
    brian "Oh, it's nothing."

    show brian nervous at right
    
    #voice "day 1/day_1_lunch/18"
    brian "Umm..."

    "..."

    "...?"

    "Looks like he can't talk that well eith-"

    show brian happy at right
    
    #voice "day 1/day_1_lunch/19"
    brian "Say, could I try some of that salsa?"

    show burrito neutral at left
    
    #voice "day 1/day_1_lunch/20"
    burrito "Sure. But I have to warn you, it can be a little... spicy."
    
    #voice "day 1/day_1_lunch/21"
    brian "Oh, thanks so much."

    show brian smiling at right
    
    #voice "day 1/day_1_lunch/22"
    brian "A little spicy, huh..."

    "He scooped some of my salsa into a spoon and gave it a taste."

    "..."

    show brian red/sweating at right

    "..."

    show burrito nervous at left

    "U... Uh-oh... I knew it..."
    
    #voice "day 1/day_1_lunch/23"
    brian "W-well... that salsa really is... something!"
    
    #voice "day 1/day_1_lunch/24"
    brian "It's so... so..."

    show burrito startled at left
    
    #voice "day1/day_1_lunch/25
    burrito "..."
    
    show brian red/sweating left at right
    hide brian with moveoutright

    #play sound gulp

    "A-aaah?!"

    "He immediately went for his bottle of water and drank it all up!"

    show burrito embarrassed at left

    "Maybe I should have been a bit more stern with the warning..."

    show brian red/sweating at right with moveinright
    
    #voice "day 1/day_1_lunch/26"
    brian "That...is....spicy...."
    
    #voice "day 1/day_1_lunch/27"
    burrito "Well, that’s because it was made with lots of Tamato and Kelpsy berries grown to be super spicy."

    show burrito neutral at left
    
    #voice "day 1/day_1_lunch/28"
    burrito "Also, water isn’t the best choice when it comes to combating spiciness."
    
    #voice "day 1/day_1_lunch/29"
    brian "Then what’s the best way to..."

    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    
    #voice "day 1/day_1_lunch/30"
    brian "...*cough* fight it?"
    
    #voice "day 1/day_1_lunch/31"
    burrito "Milk and other dairy products."

    show burrito smiling at left
    
    #voice "day 1/day_1_lunch/32"
    burrito "In fact, I happen to have a bottle of Moomoo Milk to sha--"

    show brian red/sweating at left with move

    #play sound "swipe"

    show burrito surprised at left

    "?!"
    
    show brian red/sweating left at left
    hide brian with moveoutright
    
    #voice "day 1/day_1_lunch/33"
    brian "*gulp gulp*"

    "He just drank that one all up too!"

    show burrito laughing at left

    "I'm trying hard not to laugh, but... hahaha..."

    show brian nervous at right with moveinright
    
    #voice "day 1/day_1_lunch/34"
    brian "Haah..."

    show brian neutral at right
    
    #voice "day 1/day_1_lunch/35"
    brian "Aah."

    show brian happy at right
    
    #voice "day 1/day_1_lunch/36"
    brian "Wow, that really did the trick!"

    show burrito smiling at left
    
    #voice "day 1/day_1_lunch/37"
    burrito "I know, right?"

    show brian neutral at right
    
    #voice "day 1/day_1_lunch/38"
    brian "And you know what? This salsa's actually pretty good!"

    show brian happy at right
    
    #voice "day 1/day_1_lunch/39"
    brian "Think you can give me a recipe for this?"

    show burrito surprised at left
    
    #voice "day 1/day_1_lunch/40"
    burrito "Huh? But when you ate it..."

    show brian nervous at right
    
    #voice "day 1/day_1_lunch/41"
    brian "I-I mean, maybe a milder version of it... if it’s not too much trouble."

    show burrito happy at left
    
    #voice "day 1/day_1_lunch/42"
    burrito "Oh! Sure thing!"

    show brian happy at right
    
    #voice "day 1/day_1_lunch/43"
    brian "Cool, thanks!"

    "I may not be the salsa expert in the family, but I've helped with the cooking long enough for me to know how it's done. Maybe I can finally try my hand at making my own now!"

    #play sound "munch munch mp3"

    "The two of us continue to eat and chat about school."
    
    "Turns out, we were actually in the same Biology class earlier, he just didn't get the chance to say much. Wonder why I didn't notice him, though?"

    "Still, it feels really nice to have a friend, especially on the first day."

    #play sound "bell"

    show brian neutral at right
    
    #voice "day 1/day_1_lunch/44"
    brian "Oh, looks like lunch is over. Thanks for letting me sit here, Burrito!"

    show burrito smiling at left
    
    #voice "day 1/day_1_lunch/45"
    burrito "No problem! It was great talking with you. I hope we can have another lunch like this."

    show brian happy at right
    
    #voice "day 1/day_1_lunch/46"
    brian "Me too! Bye!"
    
    #voice "day 1/day_1_lunch/47"
    burrito "Bye!"

    hide burrito

    hide brian

    "And with that, my first lunch at school just ended. Having someone to talk to really makes my day!"

    "Though... what was with his reaction earlier when I mentioned Abba?"

    "I hope it's nothing too troublesome. Maybe I should ask him about it next time..."

    "Anyway, I need to get back to class."
    
return