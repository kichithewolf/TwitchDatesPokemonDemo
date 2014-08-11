
#############################################
# Backgrounds
#############################################

image logo = "assets/backgrounds/logo.png"
image mm = im.Scale("assets/backgrounds/tdp_logo_mockup.png", 1280, 720)
image gm = "assets/backgrounds/dorm.jpg"
image bg black = Solid((0, 0, 0, 255))
image bg white = Solid((255,255,255,255))
image bg standard = im.Scale("assets/backgrounds/hallway.jpg", 1280, 720)
image placeholder_lunch = im.Scale("assets/backgrounds/placeholder_lunchroom.jpg", 1280, 720)
image outside = im.Scale("assets/backgrounds/outside.jpg", 1280, 720)
image dorm = im.Scale("assets/backgrounds/dorm.jpg", 1280, 720)
image placeholder_closet = im.Scale("assets/backgrounds/placeholder_closet.png", 1280, 720)



############################################
#Special effects
############################################

image animated_menu:
        "assets/backgrounds/animated/start1.png"
        pause 0.1
        "assets/backgrounds/animated/start2.png"
        pause 0.1
        "assets/backgrounds/animated/start3.png"
        pause 0.1
        repeat


image static:
    "assets/backgrounds/noise1.png" with Dissolve(0.2)
    0.2
    "assets/backgrounds/noise2.png" with Dissolve(0.2)
    0.2
    "assets/backgrounds/noise3.png" with Dissolve(0.2)
    0.2
    "assets/backgrounds/noise4.png" with Dissolve(0.2)
    0.2
    repeat

image greyout = "assets/effects/semitrans.png"

##############################
# Special text and images
##############################
image letter_map = "assets/backgrounds/letter_map.png"
image dad_map = "assets/backgrounds/dadmap.png"
image mom_note = "assets/backgrounds/momnote.png"
image id_placeholder = "assets/portraits/idplaceholder.png"

##################################
# Generic Credits
##################################
image credits_writers = im.Scale("assets/credits/credits_writers.png", 1280, 720)
image credits_editors = im.Scale("assets/credits/credits_editors.png", 1280, 720)
image credits_artists = im.Scale("assets/credits/credits_artists.png", 1280, 720)
image credits_music =  im.Scale("assets/credits/credits_music.png", 1280, 720)
image credits_va = im.Scale("assets/credits/credits_va.png", 1280, 720)
image credits_va2 = im.Scale("assets/credits/credits_va2.png", 1280, 720)
image credits_programming = im.Scale("assets/credits/credits_programming.png", 1280, 720)
image credits_special = im.Scale("assets/credits/credits_special.png", 1280, 720)
image credits_renpy = im.Scale("assets/credits/credits_renpy.png", 1280, 720)

image cont = im.Scale("assets/credits/cont.png", 1280, 720)


###################################################
# MAIN Character Images
###################################################

# Burrito
#image burrito = im.Scale("assets/portraits/burrito.png", 500, 500)

image burrito neutral = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito happy = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito smiling = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito sad = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito disappointed = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito nervous = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito embarrassed = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito panic = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito startled = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito amazed = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito shrinking = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito scolding = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito angry = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito shouting = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito veryangry = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito crying = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito reallycrying = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito thinking = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito sleeping = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito sleepy = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito dreamy = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito confident = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito sighing = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito annoyed = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito relieved = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito excited = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito surprised = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito laughing = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito serious = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito confused = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito scared = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito nervouslaughing = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito drowsy = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito exasperated = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito shocked = im.Scale("assets/portraits/burrito.png", 500, 500)
image burrito sweatdrop = im.Scale("assets/portraits/burrito.png", 500, 500)

# Katie
image katie = im.Scale("assets/portraits/katie.png", 300, 500)

image katie neutral = im.Scale("assets/portraits/katie.png", 300, 500)
image katie happy = im.Scale("assets/portraits/katie.png", 300, 500)
image katie reallyhappy = im.Scale("assets/portraits/katie.png", 300, 500)
image katie shrug = im.Scale("assets/portraits/katie.png", 300, 500)
image katie reallyshrug = im.Scale("assets/portraits/katie.png", 300, 500)
image katie angry = im.Scale("assets/portraits/katie.png", 300, 500)
image katie sad = im.Scale("assets/portraits/katie.png", 300, 500)
image katie nervous = im.Scale("assets/portraits/katie.png", 300, 500)
image katie concerned = im.Scale("assets/portraits/katie.png", 300, 500)
image katie embarrassed = im.Scale("assets/portraits/katie.png", 300, 500)
image katie disappointed = im.Scale("assets/portraits/katie.png", 300, 500)
image katie ihateatvsomuchimtakingupprogrammingandtextspacefornoreasonthoughdontgetmwrongimnottsundere = im.Scale("assets/portraits/katie.png", 300, 500)
image katie crying = im.Scale("assets/portraits/katie.png", 300, 500)
image katie facepalm = im.Scale("assets/portraits/katie.png", 300, 500)
image katie annoyed = im.Scale("assets/portraits/katie.png", 300, 500)
image katie proud = im.Scale("assets/portraits/katie.png", 300, 500)
image katie blushing = im.Scale("assets/portraits/katie.png", 300, 500)

# Abby
#image abby = im.Scale("assets/portraits/abby.png", 300, 500)

image abby neutral = im.Scale("assets/portraits/abby/Abby Main Pose.jpg", 500, 500)
image abby happy = im.Scale("assets/portraits/abby.png", 300, 500)
image abby perky = im.Scale("assets/portraits/abby.png", 300, 500)
image abby sighing = im.Scale("assets/portraits/abby.png", 300, 500)
image abby shifty = im.Scale("assets/portraits/abby.png", 300, 500)
image abby reallyhappy = im.Scale("assets/portraits/abby.png", 300, 500)
image abby smile = im.Scale("assets/portraits/abby/Abby Smiling Pose.jpg", 500, 500)
image abby angry = im.Scale("assets/portraits/abby/Abby Angry Pose.jpg", 500, 500)
image abby reallyangry = im.Scale("assets/portraits/abby.png", 300, 500)
image abby shouting = im.Scale("assets/portraits/abby.png", 300, 500)
image abby cheerleader = im.Scale("assets/portraits/abby.png", 300, 500)
image abby sad = im.Scale("assets/portraits/abby/Abby Sad Pose.jpg", 500, 500)
image abby nervous = im.Scale("assets/portraits/abby.png", 300, 500)
image abby scared = im.Scale("assets/portraits/abby.png", 300, 500)
image abby crying = im.Scale("assets/portraits/abby.png", 300, 500)
image abby embarrassed = im.Scale("assets/portraits/abby.png", 300, 500)
image abby confused = im.Scale("assets/portraits/abby.png", 300, 500)
image abby surprised = im.Scale("assets/portraits/abby.png", 300, 500)
image abby smug = im.Scale("assets/portraits/abby.png", 300, 500)
image abby nervoussmile = im.Scale("assets/portraits/abby.png", 300, 500)
image abby thinking = im.Scale("assets/portraits/abby.png", 300, 500)
image abby laughing = im.Scale("assets/portraits/abby/Abby Laughing Pose .jpg", 500, 500)
image abby annoyed = im.Scale("assets/portraits/abby.png", 300, 500)
image abby thoughtful = im.Scale("assets/portraits/abby/Abby Thoughtful Pose.jpg", 500, 500)

# Abba
#image abba = im.Scale("assets/portraits/bj.png", 300, 500)
#image abba voiceover = im.Alpha(im.Scale("assets/portraits/bj.png", 300, 500), 0.5)

image abba neutral = im.Scale("assets/portraits/bj.png", 300, 500)
image abba happy = im.Scale("assets/portraits/bj.png", 300, 500)
image abba reallyhappy = im.Scale("assets/portraits/bj.png", 300, 500)
image abba goodboysmile = im.Scale("assets/portraits/bj.png", 300, 500)
image abba disappointed = im.Scale("assets/portraits/bj.png", 300, 500)
image abba sad = im.Scale("assets/portraits/bj.png", 300, 500)
image abba embarrassed = im.Scale("assets/portraits/bj.png", 300, 500)
image abba thinking = im.Scale("assets/portraits/bj.png", 300, 500)
image abba angry = im.Scale("assets/portraits/bj.png", 300, 500)
image abba scolding = im.Scale("assets/portraits/bj.png", 300, 500)
image abba facepalm = im.Scale("assets/portraits/bj.png", 300, 500)
image abba truesmile = im.Scale("assets/portraits/bj.png", 300, 500)
image abba truehappy = im.Scale("assets/portraits/bj.png", 300, 500)
image abba truehappy2 = im.Scale("assets/portraits/bj.png", 300, 500)
image abba truereallyhappy = im.Scale("assets/portraits/bj.png", 300, 500)
image abba truereallyhappy2 = im.Scale("assets/portraits/bj.png", 300, 500)
image abba confused = im.Scale("assets/portraits/bj.png", 300, 500)
image abba worried = im.Scale("assets/portraits/bj.png", 300, 500)
image abba serious = im.Scale("assets/portraits/bj.png", 300, 500)
image abba smile = im.Scale("assets/portraits/bj.png", 300, 500)

# Air
#image air normal = im.Scale("assets/portraits/air.png", 300, 500)

image air neutral = im.Scale("assets/portraits/air.png", 300, 500)
image air happy = im.Scale("assets/portraits/air.png", 300, 500)
image air reallyhappy = im.Scale("assets/portraits/air.png", 300, 500)
image air sighing = im.Scale("assets/portraits/air.png", 300, 500)
image air fantasizing = im.Scale("assets/portraits/air.png", 300, 500)
image air annoyed = im.Scale("assets/portraits/air.png", 300, 500)
image air surprised = im.Scale("assets/portraits/air.png", 300, 500)
image air shifty = im.Scale("assets/portraits/air.png", 300, 500)
image air smile = im.Scale("assets/portraits/air.png", 300, 500)
image air angry = im.Scale("assets/portraits/air.png", 300, 500)
image air sad = im.Scale("assets/portraits/air.png", 300, 500)
image air nervous = im.Scale("assets/portraits/air.png", 300, 500)
image air scared = im.Scale("assets/portraits/air.png", 300, 500)
image air crying = im.Scale("assets/portraits/air.png", 300, 500)
image air embarrassed = im.Scale("assets/portraits/air.png", 300, 500)
image air reallyembarrassed = im.Scale("assets/portraits/air.png", 300, 500)
image air femalesmile = im.Scale("assets/portraits/air.png", 300, 500)
image air femaleembarrassed = im.Scale("assets/portraits/air.png", 300, 500)
image air femalesad = im.Scale("assets/portraits/air.png", 300, 500)
image air femalereallyhappy = im.Scale("assets/portraits/air.png", 300, 500)


# Brian
#image brian = im.Scale("assets/portraits/brian.png", 300, 500)

image brian neutral = im.Scale("assets/portraits/brian.png", 300, 500)
image brian happy = im.Scale("assets/portraits/brian.png", 300, 500)
image brian sad = im.Scale("assets/portraits/brian.png", 300, 500)
image brian angry = im.Scale("assets/portraits/brian.png", 300, 500)
image brian shrug = im.Scale("assets/portraits/brian.png", 300, 500)
image brian reallyhappy = im.Scale("assets/portraits/brian.png", 300, 500)
image brian disappointed = im.Scale("assets/portraits/brian.png", 300, 500)
image brian facepalm = im.Scale("assets/portraits/brian.png", 500, 500)
image brian embarrassed = im.Scale("assets/portraits/brian.png", 500, 500)
image brian blank = im.Scale("assets/portraits/brian.png", 500, 500)
image brian wat = im.Scale("assets/portraits/brian.png", 500, 500)
image brian crying = im.Scale("assets/portraits/brian.png", 500, 500)
image brian nervous = im.Scale("assets/portraits/brian.png", 300, 500)
image brian red/sweating = im.Scale("assets/portraits/brian.png", 300, 500)
image brian curious = im.Scale("assets/portraits/brian.png", 300, 500)
image brian smiling = im.Scale("assets/portraits/brian.png", 300, 500)
image brian panting = im.Scale("assets/portraits/brian.png", 300, 500)
image brian serious = im.Scale("assets/portraits/brian.png", 300, 500)
image brian nervoussmile = im.Scale("assets/portraits/brian.png", 300, 500)


# Mary
#image mary = im.Scale("assets/portraits/flareon.png", 300, 500)
#image mary voiceover serious = im.Alpha(im.Scale("assets/portraits/flareon.png", 300, 500), 0.5)

image mary neutral = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary blank = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary noeyesblank = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary angry = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary noeyesangry = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary redeyesangry = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary redeyesreallyangry = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary disappointed = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary reallydisappointed = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary noeyesreallydisappointed = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary yelling = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary noeyesyelling = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary redeyesyelling = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary embarrassed = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary noeyesembarrassed = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary nervous = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary cutenervous = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary smallsmile = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary smile = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary happy = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary crying = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary reallycrying = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary blankcrying = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary blanknoeyescrying = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary redeyescryingyelling = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary annoyed = im.Scale("assets/portraits/flareon.png", 300, 500)
image mary noeyesannoyed = im.Scale("assets/portraits/flareon.png", 300, 500)

# Gator
#image gator = im.Scale("assets/portraits/gator.png", 400, 500)

image gator neutral = im.Scale("assets/portraits/gator.png", 400, 500)
image gator happy = im.Scale("assets/portraits/gator.png", 400, 500)
image gator proud = im.Scale("assets/portraits/gator.png", 400, 500)
image gator shifty = im.Scale("assets/portraits/gator.png", 400, 500)
image gator salsadrink = im.Scale("assets/portraits/gator.png", 400, 500)
image gator firebreathing = im.Scale("assets/portraits/gator.png", 400, 500)
image gator attract = im.Scale("assets/portraits/gator.png", 400, 500)
image gator nervous = im.Scale("assets/portraits/gator.png", 400, 500)
image gator smirking = im.Scale("assets/portraits/gator.png", 400, 500)
image gator reallyhappy = im.Scale("assets/portraits/gator.png", 400, 500)
image gator joking = im.Scale("assets/portraits/gator.png", 400, 500)
image gator reallyjoking = im.Scale("assets/portraits/gator.png", 400, 500)
image gator laughing = im.Scale("assets/portraits/gator.png", 400, 500)
image gator sad = im.Scale("assets/portraits/gator.png", 400, 500)
image gator reallysad = im.Scale("assets/portraits/gator.png", 400, 500)
image gator disappointed = im.Scale("assets/portraits/gator.png", 400, 500)
image gator reallydisappointed = im.Scale("assets/portraits/gator.png", 400, 500)
image gator crying = im.Scale("assets/portraits/gator.png", 400, 500)
image gator reallycrying = im.Scale("assets/portraits/gator.png", 400, 500)
image gator angry = im.Scale("assets/portraits/gator.png", 400, 500)
image gator reallyangry = im.Scale("assets/portraits/gator.png", 400, 500)
image gator shouting = im.Scale("assets/portraits/gator.png", 400, 500)
image gator noVisor_neutral = im.Scale("assets/portraits/gator.png", 400, 500)
image gator noVisor_angry = im.Scale("assets/portraits/gator.png", 400, 500)
image gator noVisor_shouting = im.Scale("assets/portraits/gator.png", 400, 500)
image gator noVisor_ICANNOTCONTROLMYRAGEATALLDAMMIT = im.Scale("assets/portraits/gator.png", 400, 500)
image gator noVisor_sad = im.Scale("assets/portraits/gator.png", 400, 500)
image gator noVisor_reallysad = im.Scale("assets/portraits/gator.png", 400, 500)
image gator noVisor_crying = im.Scale("assets/portraits/gator.png", 400, 500)
image gator noVisor_reallycrying = im.Scale("assets/portraits/gator.png", 400, 500)
image gator noVisor_roaring = im.Scale("assets/portraits/gator.png", 400, 500)
image gator noVisor_happy = im.Scale("assets/portraits/gator.png", 400, 500)
image gator noVisor_joking = im.Scale("assets/portraits/gator.png", 400, 500)

###########################
# Minor Character Images
###########################

# Fonz
image fonz = "assets/gallery/placeholder_generic.png"

image fonz neutral = "assets/gallery/placeholder_generic.png"
image fonz shocked = "assets/gallery/placeholder_generic.png"
image fonz happy = "assets/gallery/placeholder_generic.png"
image fonz shouting = "assets/gallery/placeholder_generic.png"
image fonz attract = "assets/gallery/placeholder_generic.png"


# ATV
image atv = im.Scale("assets/portraits/atv.png", 300, 500)

image atv neutral = im.Scale("assets/portraits/atv.png", 300, 500)
image atv excited = im.Scale("assets/portraits/atv.png", 300, 500)
image atv annoyed = im.Scale("assets/portraits/atv.png", 300, 500)
image atv teasing = im.Scale("assets/portraits/atv.png", 300, 500)
image atv nervous = im.Scale("assets/portraits/atv.png", 300, 500)

# Digrat
image digrat = im.Scale("assets/portraits/digrat.png", 300, 500)

image digrat neutral = im.Scale("assets/portraits/digrat.png", 300, 500)

# Snake
image snake = im.Scale("assets/portraits/snake.png", 300, 500)

image snake neutral = im.Scale("assets/portraits/snake.png", 300, 500)
image snake nervous = im.Scale("assets/portraits/snake.png", 300, 500)
image snake sighing = im.Scale("assets/portraits/snake.png", 300, 500)
image snake impressed = im.Scale("assets/portraits/snake.png", 300, 500)
image snake angry = im.Scale("assets/portraits/snake.png", 300, 500)

# Arc
image arc = im.Scale("assets/portraits/aj.png", 300, 500)
image arc neutral = im.Scale("assets/portraits/aj.png", 300, 500)
image arc angry = im.Scale("assets/portraits/aj.png", 300, 500)
image arc shrug = im.Scale("assets/portraits/aj.png", 300, 500)

# Dux
image dux neutral = "assets/gallery/placeholder_generic.png"
image dux = "assets/gallery/placeholder_generic.png"

# Will
image will neutral = "assets/portraits/will.png"
image generic_character = "assets/gallery/placeholder_generic.png"

# Whitney
image whitney neutral = "assets/gallery/placeholder_generic.png"
image whitney smiling = "assets/gallery/placeholder_generic.png"
image whitney sadistic = "assets/gallery/placeholder_generic.png"

# Surge
image surge neutral = "assets/gallery/placeholder_generic.png"
image surge proud = "assets/gallery/placeholder_generic.png"
image surge enthusiastic = "assets/gallery/placeholder_generic.png"
image surge annoyed = "assets/gallery/placeholder_generic.png"

# Lance & Lancebot
image lance neutral = "assets/gallery/placeholder_generic.png"
image lance happy = "assets/gallery/placeholder_generic.png"
image lance surprised = "assets/gallery/placeholder_generic.png"

image lancebot neutral = "assets/gallery/placeholder_generic.png"
image lancebot hyperbeam = "assets/gallery/placeholder_generic.png"

# Misty
image misty neutral = "assets/gallery/placeholder_generic.png"
image misty annoyed = "assets/gallery/placeholder_generic.png"

#AAAAAAAAA AAAAAAAAA (AAA for short)
image AAA = "assets/gallery/placeholder_generic.png"

# Etc.
image gyra = "assets/portraits/gyra.jpg"

###################
# Old placeholders
###################
image gallery_button_test = "assets/buttons/gallerybuttontest.png"
image gallery_test_1 = "assets/gallery/gallerytest1.png"
image gallery_test_2 = "assets/gallery/gallerytest2.png"
image gallery_test_3 = "assets/gallery/gallerytest3.png"
image gallery_test_4 = "assets/gallery/gallerytest4.png"
image start_placeholder = im.Scale("assets/backgrounds/start.png", 800, 600)
image lunch_placeholder = "assets/backgrounds/placeholder_lunchroom.jpg"
image dorm_placeholder = im.Scale("assets/backgrounds/dorm.jpg", 800, 600)
image outside_placeholder = "assets/backgrounds/outside.jpg"
image burrito_placeholder = "assets/gallery/burrito.png"
image generic_character = "assets/gallery/placeholder_generic.png"
image katie_placeholder = im.Scale("assets/gallery/katie.png", 300, 500)
image atv_placeholder = im.Scale("assets/gallery/atv.png", 300, 500)
image abby_placeholder = im.Scale("assets/gallery/abby.png", 300, 500)
image digrat_placeholder = im.Scale("assets/gallery/digrat.png", 300, 500)
image snake_placeholder = im.Scale("assets/gallery/snake.png", 300, 500)
image arc_placeholder = im.Scale("assets/gallery/aj.png", 300, 500)
image bj_placeholder = im.Scale("assets/gallery/bj.png", 300, 500)
image air_placeholder = im.Scale("assets/gallery/air.png", 300, 500)
image brian_placeholder = im.Scale("assets/gallery/brian.png", 300, 500)
image flareon_placeholder = im.Scale("assets/gallery/flareon.png", 300, 500)
image gator_placeholder = im.Scale("assets/gallery/gator.png", 300, 500)
image fonz_placeholder = im.Scale("assets/gallery/gator.png", 300, 500)
image gyra_placeholder = "assets/gallery/gyra.jpg"

##########################################
# Declare characters used by this game.
#########################################

# Major Characters
define burrito = Character('Burrito', color="#c046c0", voice_tag="burrito_voice", show_two_window=True)
define katie = Character('Katie', color="#00afc8", voice_tag="katie_voice", show_two_window=True)
define abba = Character('Abba', color="AB7555", voice_tag="abba_voice", show_two_window=True)
define air = Character('Air', color="0000AA", voice_tag="air_voice", show_two_window=True)
define brian = Character('Brian', color="FFD9AF", voice_tag="brian_voice", show_two_window=True)
define abby = Character('Abby', color="AA0000", voice_tag="abby_voice", show_two_window=True)
define gator = Character('Gator', color="4E97AB", voice_tag="gator_voice", show_two_window=True)
define mary = Character('Mary', color="AA0000", voice_tag="mary_voice", show_two_window=True)

# Minor Characters
define atv = Character('ATV', color="#550000", voice_tag="atv_voice", show_two_window=True)
define digrat = Character('Digrat', color="#AA66AA", voice_tag="digrat_voice", show_two_window=True)
define gyra = Character('Gyra', color="4455CC", voice_tag="gyra_voice", show_two_window=True)
define arc = Character('AJ', color="777777", voice_tag="arc_voice", show_two_window=True)
define will = Character('Will',color="#84EFE5", voice_tag="xa_voice", show_two_window=True) #Does he even need a voice?
define mw = Character('Ms. Whitney', color= "#FFAA99", voice_tag="mw_voice", show_two_window=True)
define fonz = Character('Fonz', color="777777", voice_tag="fonz_voice", show_two_window=True)
define snake = Character('Solid Snake', color="777777", voice_tag="snake_voice", show_two_window=True)
define dux = Character('Dux', color="#855C33", voice_tag="dux_voice", show_two_window=True)
define whitney = Character('Ms. Whitney', color="777777", voice_tag="whitney_voice", show_two_window=True)
define surge = Character('Lt. Surge', color="777777", voice_tag="surge_voice", show_two_window=True)
define lance = Character('Lance', color="777777", voice_tag="lance_voice", show_two_window=True)
define lancebot = Character('Lancebot', color="777777", voice_tag="lance_voice", show_two_window=True)
define misty = Character('Misty', color="777777", voice_tag="misty_voice", show_two_window=True)

# More minor things
define conductor = Character('Conductor', color="777777", voice_tag="conductor_voice", show_two_window=True)
define letter = Character('Letter', color="777777", voice_tag="letter_voice", show_two_window=True)
define everyone = Character('Everyone', color="777777", voice_tag="everyone_voice", show_two_window=True)
define stua = Character('Student A', color="777777", voice_tag="stua_voice", show_two_window=True)
define stub = Character('Student B', color="777777", voice_tag="stub_voice", show_two_window=True)
define stuc = Character('Student C', color="777777", voice_tag="stuc_voice", show_two_window=True)
define stud = Character('Student D', color="777777", voice_tag="stud_voice", show_two_window=True)

# When a character is unknown. For voiceing purposes each of the main characters have a seperate control.
define uk_gator = Character('???',color="4E97AB", voice_tag="uk_main_gator", show_two_window=True)
define uk_katie = Character('???',color="#FFFFFF", voice_tag="uk_main_katie", show_two_window=True)
define uk_burrito = Character('???',color="#FFFFFF", voice_tag="uk_main_burrito", show_two_window=True)
define uk_abba = Character('???',color="AB7555", voice_tag="uk_main_abba", show_two_window=True)
define uk_air = Character('???',color="#FFFFFF", voice_tag="uk_main_air", show_two_window=True)
define uk_brian = Character('???',color="FFD9AF", voice_tag="uk_main_brian", show_two_window=True)
define uk_abby = Character('???',color="#FFFFFF", voice_tag="uk_main_abby", show_two_window=True)
define uk_mary = Character('???',color="#FFFFFF", voice_tag="uk_main_mary", show_two_window=True)
define uk_minor = Character('???',color="#FFFFFF", voice_tag="uk_minor_voice", show_two_window=True)

# Before a character is introduced. TODO Character Colors!
define nidoking = Character('Nidoking', color="777777", voice_tag="fonz_voice", show_two_window=True)
define pidgeot = Character('Pidgeot', color="FFD9AF", voice_tag="brian_voice", show_two_window=True)
define charmeleon = Character('Charmeleon', color="AA0000", voice_tag="abby_voice", show_two_window=True)
define steelix = Character('Steelix', color="777777", voice_tag="snake_voice", show_two_window=True)
define flareon = Character('Flareon', color="AA0000", voice_tag="mary_voice", show_two_window=True)
define dragonite = Character('Dragonite', color="#00afc8", voice_tag="katie_voice", show_two_window=True)
define venomoth = Character('Venomoth', color="#550000", voice_tag="atv_voice", show_two_window=True)
define espeon = Character('Espeon', color="#c046c0", voice_tag="burrito_voice", show_two_window=True)

# AAAAAAAAAAAAAAAAAAAHHHHHHHH
define ponyta = Character('???', color="#CC3300", voice_tag="ponyta_voice", show_two_window=True)
define AAA = Character('AAAAAAAAA AAAAAAAAA', color="#CC3300", voice_tag="ponyta_voice", show_two_window=True)

#############################

label splashscreen:
    #if persistent.clear_intro == "True":
        show bg standard
    
        show logo
        $ renpy.pause(1.0)
        hide logo with dissolve

        return
    #else:
    #   call introduction
    #   $persistent.clear_intro = "True"
    #   return

# The game starts here.
label start:
    $ relationships = { 'katie': 0,
                        'katie_major': 0,
                        'gator': 0,
                        'gator_major': 0,
                        'brian': 0,
                        'brian_major': 0,
                        'abba': 0,
                        'abba_major': 0,
                        'abby': 0,
                        'abby_major': 0,
                        'flareon': 0,
                        'flareon_major': 0,
                        'air': 0,
                        'air_major': 0
                      }
    
    # Character panel checks - Do we even need this anymore?
    $ introduced = {    'atv': False,
                        'katie': False,
                        'gator': False,
                        'snake': False,
                        'brian': False,
                        'abba': False,
                        'flareon': False,
                        'arc': False,
                        'air': False
                      }
    
    # Extra variables just in case - not the best practice but better than starting new saves.
    $ extra_one = True
    $ extra_two = 0
    $ extra_three = "none"
    
    # First dateable wins!
    $ date = "none"
    
    # Day counter - changed method in case days need to be skipped.
    # If days need to be iterated in a scene that should now be possible.
    $ day = 1
    
    # Stop the menu music
    stop music

    # Introduction goes here
    call introduction

    # 1 day insanity
    while day <= 1:
        
        # Window should be hidden during last scene of the day.
        window hide
        # Week 1
        if day == 1:
            scene black with dissolve
            show text "{color=#FFFFFF}Week 1{/color}" with Pause(1.5)
            scene black with dissolve
        if day == 7:
            scene black with dissolve
            show text "{color=#FFFFFF}Week 2{/color}" with Pause(1.5)
            scene black with dissolve
        
        #Say what day it is.
        show text "{color=#FFFFFF}Day [day]{/color}" with Pause(1.5)
        window show
        
        if day == 1:
            call day_1_morning_dorm
            call day_1_morning_class
            call day_1_lunch
            call day_1_afternoon_class
            
        # Check for character date
        # if(charpoints >= num and date=="none") date="character"
        
        #Increment day
        $day+=1
    
    # Day Cycle is complete. Credits and ending specific credits here.
    if date == "none":
        call credits
        
    # TO BE CONTINUED (DISABLE FOR FINAL RELEASE!)
    $overriding_on = True
    show cont with fade
    $renpy.pause(5.0)
    $overriding_on = None
    
    return