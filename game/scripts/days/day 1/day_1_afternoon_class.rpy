label day_1_afternoon_class:

    scene bg white

    show burrito neutral at left

    #voice "day 1/day_1_afternoon_class/1"
    burrito "Ok, my next class should be right here."

    "I’ll just grab this seat right next to the door."

    hide burrito

    #play sound seatsit

    show surge neutral at center

    #voice "day 1/day_1_afternoon_class/2"
    surge "All right pipsqueaks, listen up!"

    #voice "day 1/day_1_afternoon_class/3"
    surge "I’m here to teach you everything you need to know about the history of Kanto."

    show surge enthusiastic at center

    #voice "day 1/day_1_afternoon_class/4"
    surge "They say history is what's written in our textbooks. Well, I'm here to teach you that there's more to it than what's written on these measly pieces of paper!"

    show surge neutral at center

    #voice "day 1/day_1_afternoon_class/5"
    surge "But first, let me introduce myself."

    #voice "day 1/day_1_afternoon_class/6"
    surge "My name is Mister Doctor Professor Lieutenant Surge!"

    show surge proud at center

    #voice "day 1/day_1_afternoon_class/7"
    surge "Those titles were all given to me in recognition of my service in the war."

    #voice "day 1/day_1_afternoon_class/8"
    surge "Came at a price, they did..."

    show surge neutral at center

    #voice "day 1/day_1_afternoon_class/9"
    surge "...but you students can call me Mr. Lt. Surge!"

    "Wow, this guy’s really intense!"

    "Seems like he’s led an interesting life, though."

    #voice "day 1/day_1_afternoon_class/10"
    surge "Now, any questions before we get down to business?"

    show abby confused at right

    #voice "day 1/day_1_afternoon_class/11"
    charmeleon "Yes, um, which war were you talking about, exactly?"

    show surge enthusiastic at center

    #voice "day 1/day_1_afternoon_class/12"
    surge "Which war?!? The war!"

    #voice "day 1/day_1_afternoon_class/13"
    surge "The war to end all wars!"

    #voice "day 1/day_1_afternoon_class/14"
    surge "You kids think you have it easy today, but life wouldn’t be the same if that war hadn’t turned out the way it did..."

    show surge neutral at center

    #voice "day 1/day_1_afternoon_class/15"
    surge "...But I’m reminiscing! Back on topic!"

    hide abby

    show snake impressed at right

    #voice "day 1/day_1_afternoon_class/16"
    steelix "Wait... 'that war'?! Y-you don't mean... THE war?!"

    #voice "day 1/day_1_afternoon_class/17"
    surge "Aah, looks like we have someone that knows! What's your name, sol-"

    show mary neutral at right

    #voice "day 1/day_1_afternoon_class/18"
    flareon "*ahem*"

    show mary annoyed at right

    #voice "day 1/day_1_afternoon_class/19"
    flareon "Can we PLEASE get started on today’s lesson already?"

    #voice "day 1/day_1_afternoon_class/20"
    surge "Ah, yes, thank you, cadet."

    show mary noeyesblank at right

    #voice "day 1/day_1_afternoon_class/21"
    mary "*sigh*"

    hide snake

    hide mary

    #voice "day 1/day_1_afternoon_class/22"
    surge "Now, I thought I’d start us off with some basic knowledge."

    show surge enthusiastic at center

    #voice "day 1/day_1_afternoon_class/23"
    surge "You there! Let's see, um... Burrito! Care to tell us what Kanto is famous for?"

    show burrito surprised at left

    "Me? Umm... what should I say?"

    menu:
        "Its ancient traditions.":

            show burrito thinking at left

            #voice "day 1/day_1_afternoon_class/24"
            burrito "Its ancient traditions?"

            #voice "day 1/day_1_afternoon_class/25"
            surge "Wrong! But good try."

            show burrito sighing at left

            #voice "day 1/day_1_afternoon_class/26"
            burrito "Aww, I'd better try harder next time."
        
        "Its technology.":

            show burrito thinking at left
            
            
            #voice "day 1/day_1_afternoon_class/27"
            burrito "Its... technology?"

            #voice "day 1/day_1_afternoon_class/28"
            surge "Correct! You must know your history!"

            show burrito happy at left
            
            #voice "day 1/day_1_afternoon_class/29"
            burrito "Yes! I got it right!"

    "To be honest, I've only really heard a few things about Kanto history from eavesdropping, so it was just a huge guess..."

    hide burrito

    show surge neutral at center

    #voice "day 1/day_1_afternoon_class/30"
    surge "Kanto’s advances in technology have played important roles throughout our history."

    #voice "day 1/day_1_afternoon_class/31"
    surge "Why, the war could never have been won without the discoveries made by our people."

    #voice "day 1/day_1_afternoon_class/32"
    surge "Technology played a crucial role in the battle of…"

    scene bg black with fade

    scene bg white

    show surge proud at center

    #voice "day 1/day_1_afternoon_class/33"
    surge "...and that was how I was awarded the Golden Heart. One of the few to make it out of that battle alive."

    show mary noeyesannoyed at right

    #voice "day 1/day_1_afternoon_class/34"
    flareon "...sir."

    show mary annoyed at right

    #voice "day 1/day_1_afternoon_class/35"
    flareon "The bell rang 5 minutes ago."

    show surge neutral at center

    #voice "day 1/day_1_afternoon_class/36"
    surge  "Wha- Already? Well, I guess that’s it for today."

    hide mary

    show surge enthusiastic at center

    #voice "day 1/day_1_afternoon_class/37"
    surge "Homework: 20 push-ups! I wanna see some upper body strength out there!"

    "Push-ups? But I thought this was a history class!"

    show abby surprised at right

    #voice "day 1/day_1_afternoon_class/38"
    charmeleon "Homework on the first day of school?!? Are you serious?"

    show surge neutral at center

    #voice "day 1/day_1_afternoon_class/39"
    surge "I don’t kid about these things, missy."

    hide abby

    #voice "day 1/day_1_afternoon_class/40"
    surge "Now everyone, move out!"

    hide surge

    "Mr. Lt. Surge sure has some crazy stories..."

    "He must really love sharing them; they take up half of the class time!"

    $renpy.pause()

    "Well, classes are done for the day."

    "I don't really have anything else to do for now. Guess I’ll head back to my dorm."

    scene dorm with fade

    show burrito neutral at left

    "What a day! Time to relax."

    "...hm?"

    "Looks like Will is out."

    "I wonder if he’s still in class."

    "Maybe he’s in a club?"

    #play sound doorknock

    "*knock* *knock*"

    "Oh, someone’s at the door!"

    show abba neutral at right

    #voice "day 1/day_1_afternoon_class/41"
    abba "Good evening."

    #voice "day 1/day_1_afternoon_class/42"
    burrito "Oh! Hi, Abba."

    #voice "day 1/day_1_afternoon_class/43"
    abba "I stopped by to give you an update on your enrollment form."

    show burrito relieved at left

    #voice "day 1/day_1_afternoon_class/44"
    burrito "Yes...! Looks like I'm saved...!"

    show abba confused at right

    #voice "day 1/day_1_afternoon_class/45"
    abba "Err... umm..."

    #voice "day 1/day_1_afternoon_class/46"
    abba "The office has informed me..."

    show abba sad at right

    #voice "day 1/day_1_afternoon_class/47"
    abba "...that, unfortunately, they cannot make any name changes at this time."

    show burrito panic at left

    #voice "day 1/day_1_afternoon_class/48"
    burrito "W-what?! Why?!"

    "Man! I was really hopeful for a second there..."

    show abba neutral at right

    #voice "day 1/day_1_afternoon_class/49"
    abba "Apparently, the process to change your name on school records is long and involved."

    #voice "day 1/day_1_afternoon_class/50"
    abba "I brought the necessary paperwork in case you wanted it. "

    show abba thinking at right

    #voice "day 1/day_1_afternoon_class/51"
    abba "It might... take a while."

    #play sound "slight thud"

    "...!"

    show burrito nervous at left

    "Man, this stack of papers is huge! Eh, might as well. Let’s see here..."

    "Birth certificate, references, previous school records..."

    show burrito surprised at left

    #voice "day 1/day_1_afternoon_class/52"
    burrito "Woah, I’m supposed to fill all this out?"

    #voice "day 1/day_1_afternoon_class/53"
    abba "Yes, it seems they’ve had trouble in the past with students frequently trying to change their names for fun."

    show abba neutral at right

    #voice "day 1/day_1_afternoon_class/54"
    abba "As a result, the process has become more difficult over time."

    #voice "day 1/day_1_afternoon_class/55"
    abba "Unfortunately, that means you are stuck with the name “Burrito” for a while. I hope it won’t inconvenience you too much."

    show burrito nervous at left

    #voice "day 1/day_1_afternoon_class/56"
    burrito "W-well, I guess I can live with it. At least I’m already used to the nickname."

    "N-not really, but... I have to..."

    show burrito smiling at left

    #voice "day 1/day_1_afternoon_class/57"
    burrito "Thanks for all your help, though."

    show burrito neutral at left

    #voice "day 1/day_1_afternoon_class/58"
    abba "No thanks necessary."

    show abba happy at right

    #voice "day 1/day_1_afternoon_class/59"
    abba "As student council president, it was the least I could do."

    show abba neutral at right

    #voice "day 1/day_1_afternoon_class/60"
    abba "Until next time, then."

    #voice "day 1/day_1_afternoon_class/61"
    abba "Oh, and give Will my greetings."

    #voice "day 1/day_1_afternoon_class/62"
    burrito "Will do."

    hide abba

    $renpy.pause()

    #play sound door close

    show burrito annoyed at left

    "Oh, mom, why’d you fill out my form like that... now I can't change my name..."

    show burrito neutral at left

    "Well, there’s not much I can do about it now."

    show burrito embarrassed at left

    "Everyone else already knows me by that name; guess I’ll just make the best of it."

    show will neutral at right

    will "..."

    show burrito neutral at left

    #voice "day 1/day_1_afternoon_class/63"
    burrito "Oh, hey, Will. You’re back."

    #voice "day 1/day_1_afternoon_class/64"
    burrito "Listen, I know I told you my name was RJ, but there’s been a little mixup. So you can call me Burrito, if you’d like."

    will "..."

    #voice "day 1/day_1_afternoon_class/65"
    burrito "Oh, it’s a long story, but basically, the wrong name was put on my enrollment form and now I can’t change it."

    will "..."

    show burrito sad at left

    #voice "day 1/day_1_afternoon_class/66"
    burrito "Yeah... you’re right."

    show burrito smiling at left

    #voice "day 1/day_1_afternoon_class/67"
    burrito "That reminds me, Abba dropped by. He said to tell you hi."

    will "..."

    #voice "day 1/day_1_afternoon_class/68"
    burrito "Oh, you're right, it’s getting pretty late. Time for bed!"

    show burrito neutral at left

    #voice "day 1/day_1_afternoon_class/69"
    burrito "Night, Will."

    will "..."

    hide will

    show burrito sleepy at left

    "*yawn*"

    "Aah, bed..."

    "So... comfy..."

    show burrito sleeping at left

    "Zzzzz....."
    
    window hide
    scene bg black with fade

return