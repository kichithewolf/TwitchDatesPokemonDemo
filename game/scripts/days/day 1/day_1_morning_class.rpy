label day_1_morning_class:

    scene bg standard with fade

    show burrito nervous at left
    
    #voice "day 1/day_1_morning_class/1"
    burrito "I’d better get to class. I just-"

    #play sound "thud"

    show burrito startled at left with vpunch
    
    #voice "day 1/day_1_morning_class/2"
    burrito "-oof!"
    
    #voice "day 1/day_1_morning_class/3"
    uk_gator "Hey, Junior. Just where do you think you're going in such a hurry? It looks to me like you’re running in the hallway."

    show burrito nervous at left

    #voice "day 1/day_1_morning_class/4"
    burrito "W...what? Who said that?"
    
    #voice "day 1/day_1_morning_class/5"
    uk_gator "Over here, new kid."

    hide burrito

    #{scene change: CG - LazorGator intro. Pan from bottom-to-top}
    "EPIC GATOR CG HERE"
    
    #voice "day 1/day_1_morning_class/6"
    gator "The name's Lazor. Lazor Gator. Hasn't anyone told you that running in the halls is an offense worthy of expulsion?"

    #voice "day 1/day_1_morning_class/7"
    burrito "S... sorry, Lazor Gator..."

    show bg standard

    show burrito embarrassed at left

    show gator neutral at right
    
    #voice "day 1/day_1_morning_class/8"
    gator "Sorry? Why’re you apologizing to me? You’re the one who’s going to get kicked out."

    show gator shouting at right
    
    #voice "day 1/day_1_morning_class/9"
    gator "And on your first day, too. Tch..."

    show burrito panic at left

    "K-kicked out...? Surely he can't be serious?"
    
    #voice "day 1/day_1_morning_class/10"
    uk_abba "Gator..."
    
    #voice "day 1/day_1_morning_class/11"
    uk_abba "Do you have to do this to every new student on their first day?"

    show gator joking at right
    
    #voice "day 1/day_1_morning_class/12"
    gator "Hey! I was just getting started with this poor fella!"

    show gator neutral at right
    
    #voice "day 1/day_1_morning_class/13"
    gator "Well, since that joke’s been ruined..."

    show gator happy at right
    
    #voice "day 1/day_1_morning_class/14"
    gator "It's nice to meet you!"
    
    $renpy.show("greyout", layer='overlay')
    $renpy.show("id_placeholder", at_list=[Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)], layer='overlay')
    $renpy.pause()

    #{Lazor character panel appears}
    #{Lazor - Feraligatr
    #Nicknames: Gator, General, Nibbles
    #Hobby: Making people laugh. Usually himself.
    #"Want to hear a joke?"}
    "GATOR CHAR PANEL"

    #{scene effect: screen shake} with Shake
    
    #voice "day 1/day_1_morning_class/15"
    uk_abba "Excuse me but don't you have a class to get to, Gator?"

    show gator neutral at right
    
    #voice "day 1/day_1_morning_class/16"
    gator "I dunno, do I?"
    
    #voice "day 1/day_1_morning_class/17"
    uk_abba "Mmm. Well, if your intent is to play this little game of yours, so be it. I've important matters to attend to, like directing this little Espeon here to class."

    show gator shouting at right
    
    #voice "day 1/day_1_morning_class/18"
    gator "Ugh. Boring. I’m off."

    hide gator

    show burrito nervous at left

    "Err... t-that guy was a bit creepy, but I guess he does have a sense of humor..."

    show burrito shouting at left

    "A really screwed up sense of humor, that is!!!"

    "I was really scared for a bit there!"

    show burrito neutral at left

    "He seems like a nice guy underneath, though. But I might need to get used to this..."

    show burrito thinking at left

    "By the way, who's the other guy...?"

    hide burrito

    #{scene change: CG - Abba intro. Pan from bottom-to-top]
    "EPIC ABBA CG"
    
    #voice "day 1/day_1_morning_class/19"
    uk_abba "Hello, sophomore. My name is Abba. I am the head of the student council, third year class rep, and your guide to your first class."
    
    $renpy.show("greyout", layer='overlay')
    $renpy.show("id_placeholder", at_list=[Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)], layer='overlay')
    $renpy.pause()

    #{Abba character panel appears}
    #{Abba - Pidgeot
    #Nicknames: Bird Jesus, Messiah, Tweety
    #Hobby: Perfecting perfection.
    #"Of course I donate to the orphaned Lillipup. Who doesn't?"}
    "ABBA CHAR PAN HERE"
    
    #voice "day 1/day_1_morning_class/20"
    abba "Incidentally, I noticed that you are slightly early for your first class. I approve."

    #voice "day 1/day_1_morning_class/21"
    burrito "T-thanks. Good habits have to start early, after all!"

    "I'm still a bit early, thank goodness! If I hadn't stopped myself from talking to Will earlier, I might have gotten carried away a bit too much."

    scene bg standard

    show burrito neutral at left
    show abba neutral at right
    
    #voice "day 1/day_1_morning_class/22"
    abba "Now, on to business. It seems the only Espeon currently enrolled is named..."

    show abba thinking at right
    
    #voice "day 1/day_1_morning_class/23"
    abba "“...Burrito.” Is that you?"

    show burrito panic at left

    #voice "day 1/day_1_morning_class/24"
    burrito "B-b-b-burrito...?!"

    "What?!"

    "Mom didn't really... She couldn’t have...!"

    show burrito startled at left

    #voice "day 1/day_1_morning_class/25"
    burrito "No way! My name is RJ! RJ the first!"

    show abba confused at right
    
    #voice "day 1/day_1_morning_class/26"
    abba "Hmm? But that would mean you are not enrolled in this school."

    show burrito panic at left

    #voice "day 1/day_1_morning_class/27"
    burrito "No, I am! I'm a transfer student; today is my first day."

    show burrito nervous at left

    "But, well... Mom does call me Burrito. Maybe I should admit it to clear up some of the misunderstanding?"

    menu:
        "Admit Nickname":
            
            show burrito embarrassed at left
            
            #voice "day 1/day_1_morning_class/28"
            burrito "L-look, this is just a big misunderstanding. See..."
            
            show burrito nervous at left

            #voice "day 1/day_1_morning_class/29"
            burrito "...Burrito is what they called me back home, but it's just a nickname."
            
            show abba goodboysmile at right
    
            #voice "day 1/day_1_morning_class/30"
            abba "Hmm. Cute. I'm not quite sure how it got on the enrollment form... Nevertheless, I'll take it down to the office and get it sorted out."
            
            #voice "day 1/day_1_morning_class/31"
            abba "You may have to endure a class of everyone calling you Burrito, but knowing Ms. Whitney... Well, Burrito is probably better than Fluffy Sunray or the like."

            "'F... Fluffy... Sunray..?!’ What kind of nickname is ‘Fluffy Sunray’?!"
                                                                                                                                     
        "Don’t Admit Nickname":

            "Well, I don't like lying, but... I just can't...!"
            
            show burrito serious at left

            #voice "day 1/day_1_morning_class/32"
            burrito "It's RJ. There's no way I've ever been called Burrito. "
            
            show burrito shouting at left
            
            #voice "day 1/day_1_morning_class/33"
            burrito "N-Never!"
            
            show abba neutral at right
                
            #voice "day 1/day_1_morning_class/34"
            abba "Hmm. I'm not quite sure how it got on the enrollment form... Nevertheless, I'll take it down to the office and get it sorted out."
            
            # voice "day 1/day_1_morning_class/35"
            abba "You may have to endure a class of everyone calling you Burrito, but knowing Ms. Whitney... well, Burrito is probably better than Fluffy Sunray or the likes."
            
            show abba disappointed at right
                
            #voice "day 1/day_1_morning_class/36"
            abba "Oh, and please don't shout in the hallway..."
            
            show burrito embarrassed at left

            #voice "day 1/day_1_morning_class/37"
            burrito "Aaah, I-I'm so sorry...!"

            "I... I probably should have just admitted it."

    show abba neutral at right
    
    #voice "day 1/day_1_morning_class/38"
    abba "Speaking of Ms. Whitney, I am sure you know she runs your first class. Biology, correct?"

    show burrito neutral at left

    #voice "day 1/day_1_morning_class/39"
    burrito "Yep."
    
    #voice "day 1/day_1_morning_class/40"
    abba "Do you know the way to Ms. Whitney’s room?"

    show burrito thinking at left

    #voice "day 1/day_1_morning_class/41"
    burrito "Let's see, um..."

    show burrito nervous at left

    #voice "day 1/day_1_morning_class/42"
    burrito "Err..."
    
    #voice "day 1/day_1_morning_class/43"
    abba "I thought not. Walk straight out of this building, go down the ledge, then head straight. You’ll end up straight in front of the biology lab."

    show burrito smiling at left

    #voice "day 1/day_1_morning_class/44"
    burrito "A-ah. Thanks so much, Abba."
    
    #voice "day 1/day_1_morning_class/45"
    abba "My pleasure. I hope to see you again soon."

    hide abba

    "Alright, I just need to follow Abba’s directions to the letter and... hey! Is that... yeah, it is. The biology lab!"

    hide burrito with moveoutright

    scene bg white

    show burrito neutral at left with moveinleft

    "Looks like I got here just in time- class is starting!"

    hide burrito

    show whitney smiling at center
    
    #voice "day 1/day_1_morning_class/46"
    whitney "Hello, dears, and welcome to the start of a fun new school year! But before we can get to the wonders of biology-"
    
    #voice "day 1/day_1_morning_class/47"
    everyone "Groan…"
    
    #voice "day 1/day_1_morning_class/48"
    whitney "We need to take roll! Look alive, everybody. Abby?"

    "*silence*"

    show whitney neutral at center
    
    #voice "day 1/day_1_morning_class/49"
    whitney "Ok, absent."
    
    #voice "day 1/day_1_morning_class/50"
    whitney "ATV?"
        
    #voice "day 1/day_1_morning_class/51"
    atv "Vehvehveh."

    #voice "day 1/day_1_morning_class/52"
    whitney "Katie?"
    
    #voice "day 1/day_1_morning_class/53"
    katie "Here."

    "There's quite a number of students in here. This might take a while..."

    "..."

    "..."
    
    #voice "day 1/day_1_morning_class/54"
    whitney "Lastly, Burrito?"

    "Oh, I'm up!"

    "W-wait..."

    show burrito embarrassed at left

    #voice "day 1/day_1_morning_class/55"
    burrito "I-I’m here! But my name isn’t-"

    show whitney smiling at center
    
    #voice "day 1/day_1_morning_class/56"
    whitney "Ahh, Burrito! You’re our new student, aren’t you? I’m sure we’re going to be VERY good friends."

    #voice "day 1/day_1_morning_class/57"
    burrito "Oh, uh..."
    
    #voice "day 1/day_1_morning_class/58"
    whitney "Burrito transferred here from Little Cup High School. What a cutie, huh?"

    #voice "day 1/day_1_morning_class/59"
    burrito "Um..."

    show whitney neutral at center
    
    #voice "day 1/day_1_morning_class/60"
    whitney "It was a rhetorical question, sweetie. We all know you are. Does anyone have any questions for the new student before we move on with class?"

    hide burrito

    show atv neutral at left
        
    #voice "day 1/day_1_morning_class/61"
    atv "What’s your dorm number? As though I couldn’t find out myself. Vehvehvehveh..."

    hide atv

    show fonz neutral at left
    
    #voice "day 1/day_1_morning_class/62"
    nidoking "Are you a boy or a girl? I can’t tell with that doofy sweater of yours!"

    show whitney sadistic at center
    
    #voice "day 1/day_1_morning_class/63"
    whitney "...Fonzie-pie, see me after class."

    show fonz shocked at left
    
    #voice "day 1/day_1_morning_class/64"
    nidoking "...!!!"

    hide fonz

    show brian curious at left
    
    #voice "day 1/day_1_morning_class/65"
    pidgeot "Excuse me Miss, you missed my n-"

    show whitney neutral at center
    
    #voice "day 1/day_1_morning_class/66"
    whitney "Katie, you have your hand raised. What is it?"

    hide brian

    show katie facepalm at left
    
    #voice "day 1/day_1_morning_class/67"
    katie "Um... can we please get back to the main topic now?"
    
    #voice "day 1/day_1_morning_class/68"
    whitney "Right you are! I'm sure you are all itching to find out more about Burrito, but for now, it's time to learn!"

    hide katie

    show burrito shouting at left

    #voice "day 1/day_1_morning_class/69"
    burrito "My name is actually-"
    
    #voice "day 1/day_1_morning_class/70"
    whitney "Learning time, Burrito. Start learning."

    show burrito embarrassed at left

    "Well, I guess that could have been worse... at least it’s not Fluffy Sunray. Still, I hope Abba gets things sorted out in time."

    scene bg white with fade

    show burrito nervous at left

    #voice "day 1/day_1_morning_class/71"
    burrito "But then again, Burrito is kind of cute..."

    show burrito disappointed at left

    #voice "day 1/day_1_morning_class/72"
    burrito "I just wish I knew what Mom was thinking when she put that as my official name..."

    show whitney neutral at center
    
    #voice "day 1/day_1_morning_class/73"
    whitney "Huh...? Burrito, who are you talking to?"

    show burrito startled at left

    #voice "day 1/day_1_morning_class/74"
    burrito "W-wah! N-no one, Miss!"
    
    #voice "day 1/day_1_morning_class/75"
    whitney "No one? Well you better snap out of it, or everyone will think you're weird!"
    
    #voice "day 1/day_1_morning_class/76"
    whitney "No spacing out! Here, hand out the syllabus to wake yourself up."

    #play sound "thud"

    #voice "day 1/day_1_morning_class/77"
    burrito "A-ah!" 

    "Th-this syllabus..."

    "It's so thick!"

    show burrito nervous at left

    #voice "day 1/day_1_morning_class/78"
    burrito "Y-yes Miss..."

    "There are only a few pawfuls of students in this class, but the thick syllabus is making it a bit hard to hand them out quickly..."

    "Guess this is kinda waking me up."

    "Though I could swear that I'm not sleepy, it's just... "

    "\"Burrito\"... uuu..."

    show burrito sighing at left

    "*sigh*"

    show burrito shouting at left

    "Mom...!!!"

    hide burrito

    hide whitney

    "After I finally handed out all the syllabi, we proceeded to review them line by line."

    "...as if Ms. Whitney was assuming we didn't know how to read."

    "Other than the frequent protests from students whenever she gave someone a ridiculously 'cute' nickname, class went pretty smoothly."

    #play sound "bell"

    "Aah, is it time for lunch already?"

    "Somehow I'm glad this class is over. I'm still not used to being called Burrito out of home..."
    
    scene bg black with fade

return