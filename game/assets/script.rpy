player_name = renpy.input("Please Enter Your Name:")
player_name = player_name.strip()
if not player_name:
    player_name = "Pipipi"
    label start:
scene black
"A sharp, metallic click echoes in the darkness, followed by a low electrical hum."
"{i}[ System active. Oxygen Levels Optimal. Memory Status: Severely Corrupted.]{/i}"
scene bg lab_dark
with dissolve
with hpunch
"A sudden jolt of electricity flows through your spine, forcing your eyes wide open."
me "Ughh... my head hurts... it feels like it is going to split into two."
me "Where... where am I? What is this place?"
"You push yourself off the cold concrete floor. The room is wide, windowless and distinctly divided into three different spaces."
"On the far wall, there is a big red stopwatch with a counter indicating 30:00 surrounded by LEDs."
"The only way out seems to be a door, which is blocked by a cold, heavy steel shutter."
"There seems to be a machine with a four letter key to trigger the escape mechanism."
"Then You hear a sudden buzz from the speaker in the top corner of that room."
a "Oh you're awake, [player_name], I was starting to think the neural jolt fried whatever you had left."
m "Who are you, and what do you mean by that? Where am I?"
a "Call yourself whatever, theres no need for you to know, maybe I will if you are able to leave this room, as you are right now."
m "Leave this room? How do I?"
a "Figure it out yourself. Your timer starts in a minute now."
a "You will be provided an assistant to solve this, keep in mind she will die with you if you fail."
m "Assistant? Dead? Room? What the fuck is all of this?"
a "Bye.{i}Lets see how he does this time{/i}"
"{i}You slowly lose your conciousness and fall into the ground.{/i}"
"{i}Two hours pass.{/i}"
m "My head hurts..."
m "What happened.."
"There is a small microphone device besides you"
m "Whats this?"
l "Hello [player_name]."
m "Who are you?"
l " I am Aria, Your assistant in work, pleasure to meet you."
"{i}You look at the right to see three doors.{/i}"
m "They were not here before."
l "Yes, We need to move through them if we want any chance of opening that main shutter."
l "There are three doors which contains 3 numbers which you need for the final code."
"BEEP.BEEP.BEEP."
l "The counter is on, we need to hurry now. Ask questions later, we need to survive."
label room1:
        
        scene bg lab_dark with dissolve with hpunch
        
        "You stand back in the central laboratory. The three distinct archways loom before you, and the red stopwatch ticks down."

        menu:
            "Enter the first door (The Hall of Archives)":
                jump archive_room
            "Enter the second door (The Infinite Library - Locked)":
                l "That door is sealed. We need to clear the first sector before the mechanisms unlock."
                jump room1
            "Enter the third door (The Observation Spire - Locked)":
                l "Focus on the path in front of us first, [player_name]."
                jump room1

label archive_room:
    scene bg archive_room with dissolve with hpunch
    "You push through the first door carrying the microphone Aria is speking from inside the room."
    "You find yourself in a vast, cathedral-like chamber. Thousands of vertical glass pillars pulse with a cold, pale blue light—frozen holographic data streams."
    m "What is this? It looks like a large digital graveyard..."
    l "Old project logs, data storage, look there is an actve terminal in the middle."
    l "Maybe we can find some hints there. Go towards that."
    m "Okay."
    "A lone computer terminal stands amidst the pillars, casting an eerie glow over a pile of fractured data-chips."
menu:
            "Examine the corrupted data cluster marked 'Iteration 0'.":
                jump cluster_zero
            "Examine the pulsing data cluster marked 'Iteration 3'.":
                jump cluster_three
            "Shatter one of the glass memory pillars out of frustration.":
                jump cluster_smash

label cluster_zero:
        " You plug the terminal into the first cluster. A screeching burst of static floods your ears."
        "A synthetic voice echoes: '{i}Error. Sector empty. Nothing remains. Zero data found.{/i}'"
        l "A dead end. Let's not waste time here."
        jump archive_room

    label cluster_smash:
        "You strike a glass pillar with your fist. It shatters into a million harmless shards of light."
        l "Hey! Calm down, [player_name]. Breaking things isn't going to give us the answer."
        jump archive_room
    label cluster_three:
        "You access the 'Iteration 3' cluster. The blue light instantly shifts to a steady, solid amber."
        "A text log manifests directly onto the screen:"
        "{i}'Log 03: The core architecture required structural redundancy. Attempt number 3 was the only iteration where the containment field held stable. Remember the number three.'{/i}"
        
        "Iteration three... That's it. The first number is three."
        l "Iteration three? Wait... are you sure? System logs can be altered..."
        l "As far back as i can remember, i think zero has been the core of this structure. There is a big chance it has been altered to test my memory."
        "{i}You can sense a bit of panic as she says that{/i}"
        l "Maybe it really is just zero at the root. But... your call, [player_name]."
        "The terminal screen flickers, briefly displaying a glowing **[ 3 ]** before locking in."
        "You pocket the realization and head back through the sliding door toward the central chamber."
        jump room1
label room1:
        
        scene bg lab_dark with dissolve with hpunch
        
        "You stand back in the central laboratory. The first archive door stands open, its blue light fading, while the remaining two doors loom before you."
        "The red stopwatch ticks down relentlessly on the wall."

        menu:
            "Enter the first door (The Hall of Archives - COMPLETED)":
                "You've already extracted the data from this sector. No time to look back."
                jump room1
            "Enter the second door (The Infinite Library)":
                jump library_room
            "Enter the third door (The Observation Spire - Locked)":
                l "That top spire is still sealed. Clear the library first, [player_name]."
                jump room1
                
label library_room:
    scene library_bg with dissolve with hpunch
    "You enter through the second room carrying the device containing Aria."
    "You find yourself in a surreal, towering library. Endless rows of mahogany bookshelves stretch upward into an infinite abyss of shadow."
    m "Books? In an underground high-tech facility? What kind of sick psychological game is this?"
    l "Nostalgic... Perhaps I have a deep connection to this library which i cannot seem to remember..."
    "A single, massive reading desk sits dead center in the room. On top of it lies an open book, its pages glowing with a soft, ethereal white script."
    menu:
        "Examine The Glowing Text on the open book.":
            jump page_1
        "Try to pull off a book from the floating edges."
jump rand_book
"Ignore the obvious and start searching for the dark corners."
jump dark_interests
label rand_book:
    "You reach out to a random book on the shelf. The book disintegrates into a black dust as soon as you touch the cover."
    l "Hey [player_name], dont go around touching anomalies, focus on the center or you might face something bad."
    jump library_room
label dark_interests:
    "You go on searching the endless maze of the library, but find no means of an end or a hint."
    "Frustrated, you return back."
    l "Hurry up, we do not have much time in our hands."
label page_1:
    "You lean over the desk. The glowing script rearranges itself into a stark, unambiguous statement:"
        "{i}'The second variable stands alone. It represents the singular axis, the truth from which all other logic flows. Chapter One: Unity.'{/i}"
        m "Singular axis.....Unity....thats the second digit."
        l "The number one....wait..."
        l "{i}Her voice drops into a tense, static laced whisper over the microphone.{/i}"
        l "Can we be sure about this? In a closed loop the value of the ratio of cosine integrated by my memory of this place says that it might be a trap."
        l "But if we take the sine, which is meant to be the exact opposite of cosine, the value results in a zero. So it might be a trap for the permanent faliure of the system."
        l "What do you make of this? My initution is pretty sharp if you could not tell."
        m "Lets discuss it at the end."
jump room1
scene bg lab_dark with dissolve with hpunch
        
        "You stand back in the central laboratory. The first archive door stands open, its blue light fading, while the remaining two doors loom before you."
        "The red stopwatch ticks down relentlessly on the wall."

        menu:
            "Enter the first door (The Hall of Archives - COMPLETED)":
                "You've already extracted the data from this sector. No time to look back."
                jump room1
            "Enter the second door (The Infinite Library- COMPLETED)":
                jump room1
            "Enter the third door(The Observation Spire)":
                jump observation_room

label observation_room:
    scene bg observation_bg with dissolve with hpunch
    "You push through the final door- with 12 minutes left on the clock."
    l "Hurry up [player_name], we dont have all the time in the world." 
    "You grab the key you got from the second room and unlocked the third door."
    "With Aria still on your hands, You rush inside."
    "You come upon a glass-bottomed observation deck."
    "Below you, lies an endless mechanical chasm, almost transparent having no end."
    m "This place is absolutely massive, almost underground. How was this even constructed..."
    l "Its a constructed reality, or at least i think that it is. My database is heavily fragmented."
    "In the center of it all is a heavy brass covered telescope, pointed at a specific constellation."
    menu:
        "look through the primary lens of the telescope."
    jump lens_view
    "Adjust the manual focus knobs to search outside of targeted constellation."
    jump focus_elsewhere
    "Search the heavy brass base of the telescope for a compartment"
    jump sneaky_look

    label focus_elsewhere:
        "You shift the focus elsewhere from the constellation, and see a binary code blinking for a second."
        "It quickly disappears before you can even read and decode it."
        l "Youre going to lose the main constellation if you wander too much. Hurry."
        jump observation_room
    label sneaky_look:
        "You run your hands through the dark brass base gap."
        "You proceed to find nothing but spiders."
            l "You thimk that you are so smart, dont you?"
            jump observation_room
    label lens_view:
        "You look deeply into the lens of the telescope."
        "Instead of the constellation seen on the outside, You see a glowing geometric shape."
        "You then hear a voice inside your head, similar to Aria but devoid of emotion whispering in your ear:"
        h "Pillars on the foundation of earth, four ends of light, where I lay waiting for you."
        m "On the foundation.... 2 of equator and 2 from the poles...Meaning that the final number is four.."
        l "The earth is a damn sphere dumbass it doesnt have pillars, its obviously zero."
        m "No, i hear the voice, it is definitely four"
        m "At the end, the voice said 'life flow is {i}constant{/i}"
        l "Are you stupid??"
        "All of a sudden, an earthquake like tremor comes by and you can hear the buzzing,BEEP.BEEP.BEEP.BEEP, Louder every second."
        l "Oh no, we only have 2 minutes and thirty seconds!!!! We need to rush back to the door."
        "{i}You quickly make the run for the door intending to go and insert the code.{/i}"
        jump code_enter
        label code_enter:
            scene bg lab_dark with dissolve with hpunch
            "{i}You find yourself, along with your helper Aria, in front of the button.{/i}"
            l "Quick, enter the code, it is 000."
            m "{i}Everything was hinting towards 314.{/i}"
        menu:
            "{i}You go with your initution and choose 314.{/i}"
jump ending_path_1
"{i}You trust Aria and pick 000.{/i}"
jump ending_path_2
label ending_path_2:
    "{i}You trusted Aria and pressed 000.{/i}"
    "{i}As soon as you pressed 000, you feel a neural jolt and fall."
    jump start
label ending_path_1
"{i}As soon as she saw you press 3, she immediately panicked and started screaming."
l "NO,NO,WHAT ARE YOU DOING? I TOLD YOU IT IS 000. STOP WE WILL BOTH DIE. DO YOU NOT VALUE YOUR LIFE??"
m "Shut up, I know what you are trying to do."
l "WHAT????WHAT DO YOU MEAN?HOW?"
"{i}You finish pressing the code. The device in your shoulders bursts.{/i}"
"{i}The steel shutter falls down completely, with a loud noise.{/i}"
"{i}In a distance along the smoke, You see the figure of a man approaching closer."
show a neutral with dissolve
a "Well well well, How many loops has it been now, feels like forever."
hide a with dissolve
m "Huh?"
"{i}You suddenly feel a sharp pain in your core, then you finally recover the fragments of your memories."
"{i}You come to the realization that you were never a real human, just an artificial one, made by the man infront of you."
"{i}You  lived for 2 months before you had been in this loop for an entire year with no explanation."
m "I remember it now. Why did you do this to me?"
show a neutral with dissolve
a "Remember yourself from a year ago, dont you feel something?"
a "You were not like this, [player_name], you were just a hollow shell with no sense of comprehension."
a "I have been working on this for years on no end, then i finally figured out that if i create a loop which keeps the initution and behavioural changes intact and alters the memory, i can finally put emotions in machines."
a "I created you with caution, ran some of my previous experiments just in case which failed, so you, my special test subject had to be put in a hologram loop."
a "And as i had predicted, inside a year this was a success."
a "{i}Follow me to the lab and process whatever you learned in the past year."
hide a with dissolve
label laboratory:
    scene black
    m "{i}This will take a while for me to be done. What could be his purpose? What is my purpose in this world?{/i}"
    m "{i}Am i going to live forever? What am I supposed to do now that it has come to this?{/i}"
    m "{i}I cannot feel anything about the future, but i can feel a warm warmth waiting for me... I do not know what but it has me bounded into reality.{/i}"
    m "{i}I should focus on what is infront of me right now and think about these other things later.{/i}"
    scene bg lab_bg with dissolve with hpunch
    show a neutral with dissolve
    a "Sit. Don't think of an escape, You are safe here."
    hide a with dissolve
    m "I would not try, I have too many questions."
    show a neutral with dissolve
    a "I havent been able to sleep peacefully in days. I can finally rest easy now. I will be in the cabin, do not move an inch from here."
    "{i}The old man limps towards somewhere, leaving you alone in the lab{/i}"
    hide a with dissolve
    "{i}You slowly close your eyes, and go into seep thinking.{/i}"
    scene white 
    m "Let's run it back, I can finally remember everything."
    "{i}As you were programmed for the limitless memories, you can easily recall every loop you have been through.{i}"
    m "{i}Looks like that machine was the one altering with my memories. It all came back as soon as it got destroyed."
    m "{i}1111(ehehe) loops, 1110 faliures and one success. Aria stopped me for that long.{/i}"
    m "{i}Come to think of it, Aria at the start seemed like a hollow robot, but after 1107 loops, she completely turned over.{/i}"
    m "{i}That is strange. And she was not in possesion of the old man in the end, while she was supposed to be the regular data retriever.{/i}"
    m "{i}Interesting.{/i}"
    m "{i}Let's think of the hints. 3 displayed in the terminal, 1 hinted at the book, and the shape of the constellation being four.{/i}"
    m "{i}Huh?{/i}"
    m "{i}Huh?{/i}"
    m "{i}HuHHHHHHHHHHHHHHHHH?{/i}"
    m "{i}Shape of the constellation????{/i}"
    m "{i}I heard a voice at the end, but saw the shape in the previous 1110????{/i}"
    m "{i}Did that old man change it? No way he said he could not meddle inside the room.{/i}"
    m ""













                




    



