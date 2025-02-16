define mc = Character("[mcname]", color="#c8ffc8")
define emily = Character("Emily", color="#ffc8c8")
define taxi_driver = Character("Taxi Driver", color="#c8c8ff")
define sarah = Character("Sarah", color="#ffffc8")
define mys = Character("???", color="#c8ffc8")

label start:
    scene street with fade:
        zoom 1.1
    play music "soft_piano.mp3" loop fadein 0.5

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
            play music "sad_piano.mp3" loop fadein 1.0
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
                zoom 0.4
            "Then there was Sarah—her arms around me, her warmth a lifeline in a world that was already pulling me away."
            scene war_close with dissolve:
                zoom 1.1
            window hide
            "But the warmth had faded. The sound of distant explosions had crept in, muffled cries breaking through the silence. A rain-soaked battlefield had stretched before me, and I had watched him fall—my friend, my brother in arms."
            show sarah at center:
                zoom 0.4
                alpha 0.3
            "A whispered goodbye on a foggy morning. Sarah's fingers slipping from mine. Hope in her eyes. Regret in mine."
            "Memories swirled and blurred, their weight pressing down, suffocating."
            "The past had never stayed buried. It clung to me, a ghost in every shadow."
            window show

    label act2:
    play music "background_livingroom_low.mp3" loop fadein 2.0 volume 0.5  
    scene living_room with fade:
        zoom 1.1

    show emily angry at center:
        zoom 0.75
        yalign 0.6
    emily "You finally came... After all these years, you decide to show up now???"

    show emily angry at right:
        zoom 0.75
        yalign 0.6
    show mc sad at left:
        zoom 0.75
        yalign 0.6
    mc "Emily, I—I never meant to leave you. I thought escaping the war would help me escape my demons, but I see now I only ran from you."

    emily "Every time I saw your silhouette disappear, I wondered if you'd ever come back."
    mc "I'm sorry I wasn't there when you needed me."

    menu:
        "Gently approach her.":
            show emily sad at right:
                zoom 0.75
                yalign 0.6
            show mc happy at left:
                zoom 0.75
                yalign 0.6
            "Emily hesitates, then slowly allows [mcname] to embrace her."
        "Stand at a respectful distance.":
            "Emily stares at her dad, fuming, her arms folded, as [mcname] respects her space."

    scene study with fade:
        zoom 1.1
    "[mcname] drifts into his old study, where he discovers a box of unsent letters."

    show mc pensive at center:
        zoom 0.75
        yalign 0.6
    mc "These letters… they're pieces of a love I thought was lost."

    voice "sarah_1.mp3"
    sarah "My dearest [mcname], even amidst the chaos of war, my heart has never stopped whispering your name."

    menu:
        "Read the letters immediately.":
            play music "dramatic_sad_piano_low.mp3"
            scene letter with fade:
                zoom 1.1
            show sarah3 at center:
                zoom 0.4
                yalign 0.5
                alpha 0.7
            hide mc pensive
            sarah "My love... This morning, I found myself in the garden we planted together..."
            sarah "As I gently watered each flower, I recalled the way your eyes would light up when you showed me the first blooms."
            sarah "I could almost feel your hand in mine, guiding me through each new sprout..."
            sarah "It was as if the garden was whispering our secrets, reminding me of those blissful mornings when..."
            sarah "Love was simple and every petal held a promise..."
            sarah "I miss you so terribly in moments like these, when nature sings our song."
            show sarah3 at left:
                zoom 0.4
                yalign 0.5
                alpha 0.7
            show sarah2 at center:
                zoom 0.4
                yalign 0.5
                alpha 0.7
            sarah "My dearest, Each morning, I wake up hoping for a letter, a sign that you are safe..."
            sarah "The days grow long without you."
            sarah "I remember that rainy afternoon when we danced around the kitchen..."
            sarah "Twirling to our favorite song while the world outside blurred into silver rain."
            sarah "Your laughter was the melody that made even the darkest days shine."
            sarah "Although later, Emily tried to mimic our silly dance and laughed just as heartily..."
            sarah "I miss the sound of your laughter, and the way you made every moment sparkle..."
            show sarah2 at right:
                zoom 0.4
                yalign 0.5
                alpha 0.7
            show sarah4 at center:
                zoom 0.4
                yalign 0.5
                alpha 0.7
            sarah "I remember the night we danced under the stars. That memory is what keeps me warm when the cold sets in."
            sarah "No matter how far you go, no matter how much time passes, my heart will always find its way back to you."
            sarah "If you ever return, please promise me one thing: don't let the past steal your future."
        "Set them aside for now.":
            "He places the letters back, knowing he'll return to them when ready."
            jump bro


    scene mc cry:
        zoom 1.1
    show sarah4 at center:
        zoom 0.4
        yalign 0.5
        alpha 0.7
    play music "calm.mp3"
    mc "Every explosion, every loss... They weren't just echoes of war—they were shattered promises."
    mc "Each blast tore through the quiet of my soul, a stark reminder of vows I made in the heat of battle—to protect, to return, to never let the darkness consume what we built."
    mc "I remember the day we parted, the tearful goodbye where hope was our only shield against the inevitable pain."
    mc "With every fallen comrade, I felt the weight of promises broken, of futures stolen by the relentless cruelty of conflict."
    mc "And now, as I stand amidst these ruins of memory, each shattered promise whispers a lesson: that the cost of war is not measured in the fires of battle alone, but in the tender moments of love and trust we lose along the way."

    menu:
        "Linger on the memory.":
            jump sar
        "Skip ahead.":
            "[mcname] is unable to resist the memories of those angelic eyes..."
            "The woman he once held..."
            "The woman he still loves dearly to this day..."
            jump sar
    
    label sar:
    scene lantern_sarah with fade:
        zoom 1.1
    "[mcname] remembers that final smile with an ache that never fades—a smile that held the warmth of countless shared mornings, the softness of whispered dreams, and the strength to face the looming darkness."
    show sarah4 at right:
        zoom 0.4
        yalign 0.5
    "It was as if, in that fleeting moment, Sarah poured every hope and every unspoken goodbye into that one, final smile."
    "Even now, as the memory replays in his mind, it feels like a beacon—a light that guides him through the bleak corridors of war and loss, reminding him that love, even in its quietest moments, endures beyond the confines of time."
    sarah "Please, forgive yourself as you have always forgiven me."
    show mc sad at left:
        zoom 0.75
        yalign 0.6
        alpha 0.3
    mc "Forgive myself...?"
    mc "How?"
    mc "How can I forgive a heart that's been shattered by your absense?"
    mc "I returned safely like I promised..."
    hide mc sad
    show mc angry at left:
        zoom 0.75
        yalign 0.6
        alpha 0.3
    mc "But YOU..."
    mc "I had asked you to wait..."
    mc "Was it really that easy for you to leave me behind...?"
    mc "..."
    mc "You promised me that we were going to leave together..."
    mc "It was me who went to the war and yet..."
    hide mc angry
    show mc sad at left:
        zoom 0.75
        yalign 0.6
        alpha 0.3
    mc "I'm still breating while you're six feet under... It should've been me instead."
    sarah "I need you need to stay. For Emily. For Us."
    mc "Alone...? It's going to feel lonely without you by my side..."
    sarah "My love..."
    sarah "Are you sure you're going to feel lonely with Emily by your side?"
    sarah "Moreover, you will always have me by your side..."
    sarah "In your heart and your memories..."
    sarah "I'll forever live on inside your memories."
    hide mc sad

    menu:
        "Embrace the emotions.":
            show mc sad at left:
                zoom 0.75
                yalign 0.6
                alpha 0.3
            "[mcname] lets his tears fall, a step toward healing."
        "Resist the vulnerability.":
            show mc angry at left:
                zoom 0.75
                yalign 0.6
            "He snaps back to reality, unwilling to let the emotions take hold."

    label bro:
    scene study with fade:
        zoom 1.1
    "Emily comes rushing to [mcname]'s study with tears in her eyes"
    show emily sad at right:
        zoom 0.75
        yalign 0.6
    emily "I just dreamt about mom... She left me a message... She's still here..."

    play music "peaceful-relaxing-piano-music-271857.mp3" loop fadein 5.0
    scene black with fade:
        zoom 3
    "[mcname] and Emily go back to the dimly lit living room."
    scene living_room with fade:
        zoom 1.1
    "Shadows flicker against the walls, stretching long and tired, much like the silence between father and daughter."
    "[mcname] and Emily finally sit down together, the space between them more than just physical."
    "It's years of absence, of unsaid words, of moments stolen by time and regret."
    "The silence is heavy, pressing, but for once, neither of them runs from it."
    show mc sad at left:
        zoom 0.75
        yalign 0.6
    show emily sad at right:
        zoom 0.75
        yalign 0.6
    emily "(softly, almost to herself) I just dreamt about Mom... She left me a message... She's still here..."
    "[mcname] looks up at her, startled. There's something about the way Emily says it—"
    "Not like a dream, but like a truth she desperately wants to believe."
    "Her fingers fidget in her lap, her gaze distant, lost in the remnants of a dream she isn't ready to wake up from."
    mc "..."
    emily "..."
    "The words send a shiver down his spine."
    "A long pause stretches between them."
    "[mcname] puts a hand on Emily's head and starts patting her"
    hide emily sad
    show emily shocked at right:
        zoom 0.75
        yalign 0.6
    mc "(voice low, rough, as if speaking the words out loud makes them more real) I left thinking I could outrun my demons..."
    hide emily shocked
    show emily sad at right:
        zoom 0.75
        yalign 0.6
    mc "That if I just kept moving, kept running, I could bury them somewhere along the way."
    mc "But these memories of her... they don't fade."
    mc "They don't loosen their grip..."
    mc "Every time I close my eyes, I see her… I see the life I could have given both you and her."
    mc "I see all the ways I failed her..."
    mc "And you."
    "Emily's lips press into a thin line."
    "She looks down at her hands, twisting the hem of her sleeve between her fingers, as if grounding herself."
    "Then, without looking up, she speaks—her voice quiet, but each word like a blade to the heart."
    emily "Maybe if you'd been here, I wouldn't have felt so alone."
    mc "..."

    "The words land with the force of a gut punch, knocking the breath from [mcname]'s chest..."
    "He wants to say something..."
    "Anything..."
    "Anything to make it better..."
    "But what apology is enough to mend years of distance?"
    "What words could possibly take away the loneliness she had to endure without him?"
    
    hide emily sad
    show emily shocked at right:
        zoom 0.75
        yalign 0.6
    "Emily lifts her gaze then, and there's something in her eyes that cuts deeper than anger—"
    "Something raw..."
    "Something broken."
    "She isn't just accusing him."
    "She's asking for something..."
    "Proof that he's still here..."
    "Just maybe..."
    "He isn't just another ghost lingering in the home they both lost."

    menu:
        "Open up completely.":
            play music "redemption.mp3" loop fadein 5.0
            "[mcname] swallows hard, forcing himself to meet her gaze."
            hide mc sad
            show mc normal at left:
                zoom 0.75
                yalign 0.6
            "His hands clench into fists, then relax. He takes a slow, shaky breath."
            mc "You're right. (His voice is barely above a whisper)"
            mc "I should have been here..."
            mc "I should have fought harder to stay..."
            mc "Instead of running from the ghosts in my head."
            mc "But I was afraid, Emily."
            mc "I was afraid that if I let myself feel everything, it would consume me."
            mc "That I would lose myself in the grief, the guilt... and that you'd see me as nothing more than a broken man."

            hide emily shocked
            show emily sad at right:
                zoom 0.75
                yalign 0.6
            "Emily's eyes glisten, unshed tears brimming at the edges."
            "She shakes her head slightly, her voice cracking as she speaks."

            emily "I didn't need perfect, Dad"
            emily "I just needed you."
        "Guard your heart.":
            play music "redemption.mp3" loop fadein 5.0
            show mc angry at left:
                zoom 0.75
                yalign 0.6
            "[mcname] exhales, running a tired hand over his face."
            "He searches for words but finds only fragments, pieces of what he wants to say but can't bring himself to."
            mc "It wasn't as simple as staying or leaving, Emily. I thought I was doing what was best."
            hide emily shocked
            show emily sad at right:
                zoom 0.75
                yalign 0.6
            "Emily scoffs softly, shaking her head."
            emily "Best for who?"
            "[mcname] opens his mouth, then closes it."
            "He doesn't have an answer."
            "Not one that will fix this."
            "Not one that will make her feel any less abandoned."
            "He sees it in her expression—"
            "The quiet disappointment, the aching need for something more, something he is still too afraid to give."
            "The silence returns, stretching wide between them."
            hide emily sad
            show emily shocked at right:
                zoom 0.75
                yalign 0.6
            "Emily looks down, biting the inside of her cheek, and when she finally speaks, her voice is barely above a whisper."
            emily "You know..."
            emily "I still see her in my dreams, too. But she never says anything about you."

            "A dagger straight to the heart."
            "[mcname] flinches, but he doesn't respond. Because maybe... maybe he deserves that silence."

    
    play music calm loop fadein 3.0
    scene black with fade:
        zoom 3
    "Fast forward a few days, Emily and [mcname] visit the local lantern rite festival..." 
    scene lantern_emily with fade:
        zoom 1.1
    "A vast ocean of midnight blue stretches above them, an endless sky stitched with sparkling lanterns and stars."
    "The world feels impossibly still, as if the universe itself is listening."
    "A faint breeze carries the scent of damp earth and distant pine, rustling through the trees in a whisper"
    "Their soft glow illuminates the faces of a father and daughter standing side by side, the space between them still uncertain, still scarred, but no longer unbridgeable."
    show emily happy at right:
        zoom 0.75
        yalign 0.6
    show mc happy at left:
        zoom 0.75
        yalign 0.6
    mc "..."
    emily "..."
    mc "..."
    emily "..."
    "For a long moment, neither speaks."
    "The silence is thick, not with tension, but with the weight of all that has been left unsaid."

    show emily shocked at right:
        zoom 0.75
        yalign 0.6
    emily "(voice quiet, but filled with something hesitant, something fragile) I had a dream about Mom."
    show mc sad at left:
        zoom 0.75
        yalign 0.6
    "[mcname] turns slightly, his grip on the lantern tightening."

    emily "(swallowing, her voice barely above a whisper) She left me a message... She is still here."

    "A sharp ache coils in [mcname]'s chest."
    "He wants to ask what she means—"
    "If she really believes it..."
    "If she thinks Sarah's presence lingers in the spaces they refuse to fill."
    "But part of him is afraid to hear the answer."
    "Afraid that she has found a connection to Sarah that he has lost..."
    "Something that he has buried under years of guilt and grief."

    show emily happy at right:
        zoom 0.75
        yalign 0.6
    emily "(exhales shakily, eyes fixed on the stars) Maybe we can start rebuilding what was lost—one moment at a time."

    "[mcname] stares at her, taking in the quiet determination in her expression..."
    "The way the firelight flickers in her eyes..."
    "For so long, he thought the past was a graveyard—"
    "Something to be mourned, not revisited."
    ""
    "But here she is..."
    "Asking him to believe in something else."
    "In something more than regret."
    show mc happy at left:
        zoom 0.75
        yalign 0.6
    "His voice is rough, edged with sorrow, but steady."
    mc "We honor her memory not with regret, but with hope."

    "A gust of wind brushes past them"
    "For the first time in years, [mcname] feels something shift inside him—"
    "Like the weight of the past loosening... Just a little."
    "The swarm of warm paper stars drifts upward, carrying whispers of sorrow and love into the endless sky..."
    "Higher, higher, until the light becomes one with the stars."

    "Emily watches, her lips pressed together, her eyes glassy with something unshed."
    "[mcname] watches her instead, searching for traces of Sarah in her—"
    show sarah3 at right with fade:
        zoom 0.4
        yalign 0.5
        alpha 0.2
    hide emily happy
    show emily happy at right:
        zoom 0.75
        yalign 0.6
    "Her resilience, her quiet strength..."
    "And he finds them, in the way Emily stands tall, in the way she chooses to hold on rather than let go."
    hide sarah3

    menu:
        "Reflect together.":
            show emily happy at right:
                zoom 0.75
                yalign 0.6
            show mc happy at left:
                zoom 0.75
                yalign 0.6
            "[mcname] exhales, the cool night air filling his lungs."
            "He looks at Emily, and for the first time in years"
            "The past doesn't feel like a weight between them—"
            "It feels like a story waiting to be told..."
            mc "(softly) She used to love nights like this..."
            emily "(nods, smiling faintly through the sadness) Yeah… she always said the stars were stories waiting to be told..."
            "There's something almost peaceful about the memory..."
            "The way it settles between them like a blanket..."
            "It's rather... comforting."

            "Emily shifts closer, her voice hesitant but open."

            emily "Do you remember the time we camped in the backyard?"
            emily "You tried to teach me how to start a fire, and Mom had to step in before you burned the lawn?"
            mc "*chuckles*"
            mc "I remember. You were laughing at me the whole time."
            mc "And then you and your mom roasted marshmallows while I tried to figure out what the hell I did wrong."

            "Emily laughs softly, a sound he hasn't heard in so long that it almost knocks the air from his lungs."
            "The grief is still there—"
            "It always will be—"
            "But for once, it isn't the only thing in the space between them."
            "There is warmth, too..."
            "There is love..."
            "And for tonight, that is enough."

        "Embrace the silence.":
            show emily shocked at right:
                zoom 0.75
                yalign 0.6
            show mc normal at left:
                zoom 0.75
                yalign 0.6
            mc "..."
            "[mcname] doesn't speak..."
            "Not because he doesn't want to..."
            "But because words feel too small for a moment like this."
            "He looks at Emily, sees the weight she carries..."
            "Sees the years of absence reflected in her tired eyes..."
            "He doesn't know if anything he says will be enough..."
            "Maybe words have never been enough."

            ""

            "Emily shifts slightly.."
            hide mc normal
            show mc happy at left:
                zoom 0.75
                yalign 0.6
            "Just enough that their shoulders brush."
            "It's a small thing, barely noticeable, but [mcname] feels it."
            "He doesn't pull away."
            "Instead, he lets the silence settle..."
            "Not as a wall..."
            "But as something softer..."
            "Something shared."

            ""

            "For years, silence was his prison..."
            "Tonight, it is something else entirely..."
            "A beginning."

    play music "calm.mp3"
    scene black with fade:
        zoom 3
    "As the screen fades to black, a quiet moment lingers—"
    "An invitation, a whisper meant just for you..."
    show sarah3 at center with fade:
        zoom 0.4
        yalign 0.5
        alpha 0.5
    ""
    sarah "Grief is love that has nowhere to go."
    sarah "But love…"
    sarah "Love never truly leaves..."
    sarah "It lingers in the spaces between laughter..."
    sarah "In the echoes of old memories, in the way we carry those we've lost forward with us."

    sarah "Maybe you've lost someone..."
    sarah "Maybe you're still trying to make peace with the past..."
    sarah "Or maybe, like [mcname], you're afraid to open a door you thought was closed forever."

    sarah "But you're still here..."
    sarah "And that means there's still time—"
    sarah "To heal, to forgive, to hold on, or to let go."

    sarah "Whatever you choose… just know that you are not alone."
    hide sarah3
    ""
    "Thank you for playing this game"
    "With Love... <3"
    "From BlackNinjaKR"

    return