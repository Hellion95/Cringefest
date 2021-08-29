# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image school = "anime_school_winter_street_674_1920x1080.jpg"
image street = "QnFxMtN.jpg"
image loli = "1426242348863.png"
image lolicon = "finished_nerd_5535.png"
image faggot = "2125678-yup4g.png"
image bimbo = "83b6da5f7989927cff200ddef5588082.png"

define b = Character("Bimbo")
define f = Character("Faggot")
define l = Character("Loli")
define m = Character("Player")


# The game starts here.

label start:

    scene street

    show lolicon
    m "ACH!! Another boring day at school!!"
    show faggot at right
    f "Let me make it more fun for you honey." 
    menu:
        "Lets make out #nohomo":
                jump gayend
        "How about NOOOOOOOOOO!!!":
                jump school
label school:
    
    scene school
    show lolicon
    show faggot at right
    
    f "Whatever, honey, your loss." 
    hide faggot
    m "Woah, well, my ass is safe."
    show loli at left
    l "Not if you don't have my homework, you shit-for-brains."
    menu:
        "I do, but you need to make it worth my while.":
                jump lolikill
        "Yes, please don't kill me.":
                jump bitch
        "Fuck you, brat.":      
                jump lolikill

label bitch:
    m "*hands ower homework with shaking hands*"
    l "Thats right little bitch. Since I'm in good mood today, I'll let you get away without kissing my feet for having honor of doing my homework."
    hide loli
    m "Oh, God, it thought I was done for this time."
    show bimbo at right
    b "Where you always such a cunt?"
    menu:
        "STFU, you stupid cunt!":
                jump bimbokill
        "Yeah, pretty much.":
                jump goodend
                
label gayend:
    "As you get your anus ripped apart, you finally realize #nohomo can't save you."
    return
    
label lolikill:
     l "GRRRRRR, YOU STUPID PERVERT!!"
     "As you get your anus ripped apart, you finally realize empty bravodoo can't save you."
     return
     
label bimbokill:
     b "That's it, you're fucking dead!!"
     "As you get your anus ripped apart, you finally realize being asshole can't save you."
     return

label goodend:
    "You keep on living your life like miserable pussy you are. Congrats!!!"
    return
