define mc = Character("[mcname]", color="#c8ffc8")
define emily = Character("Emily", color="#ffc8c8")
define taxi_driver = Character("Taxi Driver", color="#c8c8ff")
define sarah = Character("Sarah", color="#ffffc8", italic=True)
define mys = Character("???", color="#c8ffc8")
label start:

    scene street with fade:
        zoom 1.1
    play music "soft_piano.mp3"

    "A quiet, timeworn street bathed in the soft glow of a fading sunset."
    "A taxi pulls up in front of an old, modest family home."

    scene taxi with fade:
        zoom 1.1

    show mc normal at right:
        yalign 0.6
        zoom 0.75
    show taxi_driver at left:
        yalign 0.6
        zoom 0.75

    mys "I used to believe home was a sanctuary. Now, every step feels like I'm walking through a museum of lost moments."

    taxi_driver "Huh?"
    taxi_driver "Sir, you're talking like you just came back from war..."

    mys "Yeah"

    taxi_driver "Oh... I'm sorry."

    mys "It's okay, don't worry about it."

    taxi_driver "Sir, if I may ask, what's your name?"

    $ mcname = renpy.input("I am ", length=32)
    $ mcname = mcname.strip()
    if not mcname:
        $ mcname = "Mark"
    mc "I'm [mcname]"

    taxi_driver "Welcome home, soldier."
    taxi_driver "Sometimes... the hardest part is just opening that door."
    
    mc "Thank you…"
    mc "It feels like everything I left behind is waiting for me."

    menu:
        "Step confidently toward the door.":
            jump act2

        "Pause at the threshold.":
            play music "sad_piano.mp3"
            scene lantern_solo with pixellate:
                zoom 1.1
            window hide
            "I had come a long way—from messing around and yanking my comrades' panties to standing in the ruins of my own choices."
            "We had been just kids back then, reckless, invincible... before the war stole our innocence."
            scene cornfield with pixellate:
                zoom 1.1
            window hide
            "A younger me had laughed under the sunlit cornfields, sharing quiet moments of camaraderie with the only family I had known."
            show sarah at center:
                zoom 1.5
            "Then there was Sarah—her arms around me, her warmth a lifeline in a world that was already pulling me away."
            scene war_close with dissolve:
                zoom 1.1
            window hide
            "But the warmth had faded. The sound of distant explosions had crept in, muffled cries breaking through the silence. A rain-soaked battlefield had stretched before me, and I had watched him fall—my friend, my brother in arms."
            scene war_fb with dissolve:
                zoom 1.1
            window hide
            show sarah at center:
                zoom 1.1
                alpha 0.3
            "A whispered goodbye on a foggy morning. Sarah's fingers slipping from mine. Hope in her eyes. Regret in mine."
            "Memories swirled and blurred, their weight pressing down, suffocating."
            scene war_tank with dissolve:
                zoom 1.1
            window hide
            show sarah at center:
                zoom 1.1
                alpha 0.3
            "The past had never stayed buried. It clung to me, a ghost in every shadow."
            window show

    label act2:
    scene living_room with fade:
        zoom 1.1

    show emily angry
    emily "You finally came... After all these years, you decide to show up now???"

    show mc sad
    mc "Emily, I—I never meant to leave you. I thought escaping the war would help me escape my demons, but I see now I only ran from you."

    emily "Every time I saw your silhouette disappear, I wondered if you'd ever come back."
    mc "I'm sorry I wasn't there when you needed me."

    menu:
        "Gently approach her.":
            show emily sad
            "Emily hesitates, then slowly allows [mcname] to embrace her."
        "Stand at a respectful distance.":
            show emily angry
            "Emily stares at her dad, fuming, her arms folded, as [mcname] respects her space."

    scene study with fade
    "[mcname] drifts into his old study, where he discovers a box of unsent letters."

    show mc shocked
    mc "These letters… they're pieces of a love I thought was lost."

    play voice "sarah_voiceover.mp3"
    sarah "My dearest [mcname], even amidst the chaos of war, my heart has never stopped whispering your name."

    menu:
        "Read the letters immediately.":
            # Define a list of letters
            default letter_index = 0
            default letters = [
                "Dear [mcname],\n\nThis morning, I found myself in the garden we planted together. As I gently watered each flower, I recalled the way your eyes would light up when you showed me the first blooms. I could almost feel your hand in mine, guiding me through each new sprout. It was as if the garden was whispering our secrets, reminding me of those blissful mornings when love was simple and every petal held a promise. I miss you so terribly in moments like these, when nature sings our song."
                "Dearest [mcname], Each morning, I wake hoping for a letter, a sign that you are safe. The days grow long without you. I remember that rainy afternoon when we danced around the kitchen, twirling to our favorite song while the world outside blurred into silver rain. Your laughter was the melody that made even the darkest days shine. Later, Emily tried to mimic our silly dance and laughed just as heartily—an echo of a time when our home was filled with joy and light. I miss the sound of your laughter, and the way you made every moment sparkle.",
                "I remember the night we danced under the stars. That memory is what keeps me warm when the cold sets in.",
                "No matter how far you go, no matter how much time passes, my heart will always find its way back to you.",
                "If you ever return, please promise me one thing: don't let the past steal your future.",
                "This evening, as the sun melted into a blaze of orange and pink, I sat by the window and let my thoughts wander back to our sunsets together. I remembered how we would sit in silence, content in each other’s presence, as the sky painted our dreams in vivid hues. Tonight, I held your favorite scarf close and felt the warmth of those treasured moments. The fading light stirred a gentle ache in my heart, a reminder of a love that still burns, even in the quiet of loss. I miss you with every setting sun."
            ]

            # Define the screen for reading letters
            screen letter_screen():
                modal True  # Prevent interactions outside this screen
                zorder 100

                # Background
                add "paper_texture.jpg" at truecenter

                # Display letter text
                text "[letters[letter_index]]" size 40 color "#000000" font "cursive.ttf" xalign 0.5 yalign 0.4

                # Navigation button
                imagebutton:
                    idle "left_arrow.png"
                    action If(letter_index > 0, SetVariable("letter_index", letter_index - 1))
                    xpos 100
                    ypos 400

                imagebutton:
                    idle "right_arrow.png"
                    action If(letter_index < len(letters) - 1, SetVariable("letter_index", letter_index + 1))
                    xpos 1100
                    ypos 400

                # Close button
                textbutton "Return" action Hide("letter_screen") xalign 0.5 yalign 0.9

            # Add a way to open the letter screen
            label read_letters:
                show study with fade
                "Mark hesitates before opening the first letter."
                call screen letter_screen
                return
        "Set them aside for now.":
            "He places the letters back, knowing he'll return to them when ready."


    scene battlefield with fade
    "A flashback engulfs the screen—a war-torn landscape filled with chaos."
    show mc sad
    mc "Every explosion, every loss... They weren't just echoes of war—they were shattered promises."
    mc "Each blast tore through the quiet of my soul, a stark reminder of vows I made in the heat of battle—to protect, to return, to never let the darkness consume what we built."
    mc "I remember the day we parted, the tearful goodbye where hope was our only shield against the inevitable pain."
    mc "With every fallen comrade, I felt the weight of promises broken, of futures stolen by the relentless cruelty of conflict."
    mc "And now, as I stand amidst these ruins of memory, each shattered promise whispers a lesson: that the cost of war is not measured in the fires of battle alone, but in the tender moments of love and trust we lose along the way."

    menu:
        "Linger on a memory.":
            jump sar
        "Skip ahead.":
            "[mcname] is unable to resist the memories of those angelic eyes..."
            "The woman he once held..."
            "The woman he still loves dearly to this day..."
            jump sar
    
    label sar:
    scene sunlit_room with fade
    show sarah
    "[mcname] remembers that final smile with an ache that never fades—a smile that held the warmth of countless shared mornings, the softness of whispered dreams, and the strength to face the looming darkness."
    "It was as if, in that fleeting moment, Sarah poured every hope and every unspoken goodbye into that one, final smile."
    "Even now, as the memory replays in his mind, it feels like a beacon—a light that guides him through the bleak corridors of war and loss, reminding him that love, even in its quietest moments, endures beyond the confines of time."
    sarah "Please, forgive yourself as you have always forgiven me."
    mc "Forgive myself...?"
    mc "How?"
    mc "How can I forgive a heart that's been shattered by your absense?"
    mc "I returned safely like I promised..."
    mc "But YOU..."
    mc "I had asked you to wait..."
    mc "Was it really that easy for you to leave me behind...?"
    mc "..."
    mc "You promised me that we were going to leave together..."
    mc "It was me who went to the war and yet..."
    mc "I'm still breating while you're six feet under... It should've been me instead."
    sarah "I need you need to stay. For Emily. For Us."
    mc "Alone...? It's going to feel lonely without you by my side..."
    sarah "My love..."
    sarah "Are you sure you're going to feel lonely with Emily by your side?"
    sarah "Moreover, you will always have me by your side..."
    sarah "In your heart and your memories..."
    sarah "I'll forever live on inside your memories."

    menu:
        "Embrace the emotions.":
            show mc sad
            "[mcname] lets his tears fall, a step toward healing."
        "Resist the vulnerability.":
            show mc angry
            "He snaps back to reality, unwilling to let the emotions take hold."

    scene study with fade
    "Emily comes rushing to [mcname]'s study with tears in her eyes"
    show emily sad
    emily "I just dreamt about mom... She left me a message... She's still here..."

    scene study2 with fade
    "[mcname] and Emily finally sit down together."
    mc "I left thinking I could outrun my demons. But these memories of her… they remind me of my failures."
    emily "Maybe if you'd been here, I wouldn't have felt so alone."

    menu:
        "Open up completely.":
            "[mcname] shares a painful memory, allowing Emily to understand his suffering."
        "Guard your heart.":
            "[mcname] chooses measured responses, leaving Emily yearning for more."

    scene hilltop with fade
    "[mcname] and Emily stand under the stars, releasing lanterns."
    emily "Maybe we can start rebuilding what was lost—one moment at a time."
    mc "We honor her memory not with regret, but with hope."

    menu:
        "Reflect together.":
            "[mcname] and Emily share memories, finally bridging the gap."
        "Embrace the silence.":
            "They walk together in silence, understanding unspoken but deeply felt."

    return
