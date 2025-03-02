define mc = Character("[mcname]", color="#c8ffc8")
define emily = Character("Emily", color="#ffc8c8")
define taxi_driver = Character("Taxi Driver", color="#c8c8ff")
define sarah = Character("Sarah", color="#ffffc8")
define mys = Character("???", color="#c8ffc8")

label splashscreen:
    scene black
    with Pause(1)

    show text "BlackNinjaKR presents" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return


label start:
    scene street with fade:
        zoom 1.1
    play music "soft_piano.mp3" loop fadein 0.5

    ""
    "A taxi pulls up in front of an old, modest family home."

    scene taxi with fade:
        zoom 1.1

    show mc normal at right:
        yalign 0.6
        zoom 0.75
    show taxi_driver at left:
        yalign 0.6
        zoom 0.75

    mys "I never imagined I'd be able to revisit this place alive..."
    mys "Every step feels like I'm walking barefoot on glass shards of the moments I missed..."

    taxi_driver "Huh?"
    taxi_driver "Sir, you're talking like you just came back from war..."

    mys "Yeah..."

    taxi_driver "Oh... I'm sorry."

    mys "It's okay, don't fret about it."

    taxi_driver "Sir, if I may ask, what's your name?"

    $ mcname = renpy.input("I am ", length=32)
    $ mcname = mcname.strip()
    if not mcname:
        $ mcname = "Mark"
    mc "I'm [mcname]"

    taxi_driver "Welcome home, soldier."

    mc "I can't help but feel bittersweet about reuniting with the people I had left behind..."

    taxi_driver "I understand sir... Duty called and you couldn't say no."
    taxi_driver "Although sometimes... the hardest part is just taking the first step."
    
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
            mc "I had come a long way—from messing around and yanking my comrades' panties to standing amidst the corpses of my brother-in-arms."
            mc "We had been just kids back then, reckless, invincible... before the war stole our innocence."
            scene cornfield with pixellate:
                zoom 1.1
            window hide
            mc "A younger me had laughed under the sunlit cornfields, sharing quiet moments of camaraderie with the only family I had known."
            show sarah at center:
                zoom 0.4
            mc "Then there was her—Sarah..."
            mc "Whenever I close my eyes, I can still feel her arms around me,"
            mc "Her warmth felt like a lifeline in a world that was already pulling me away."
            scene war_close with dissolve:
                zoom 1.1
            window hide
            mc "But the warmth had faded sooner than I wanted it to."
            mc "The sound of distant explosions had crept in, muffled cries breaking through the silence. A rain-soaked battlefield stretching before me, as I watched all of them fall—my friends, my comrades, my brother in arms."
            show sarah at center:
                zoom 0.4
                alpha 0.3
            mc "Sarah was like a whispered goodbye on a foggy morning..."
            mc "I still get nightmares about her fingers slipping from mine... Hope in her eyes... Regret in mine."
            mc "And now... After surviving that nightmare, I never expected her to be one to get to be the ghost amongst us..."
            window show

    label act2:
    play music "background_livingroom_low.mp3" loop fadein 2.0 volume 0.5  
    scene living_room with fade:
        zoom 1.1

    show emily angry at center:
        zoom 0.75
        yalign 0.6
    emily "You came..."
    emily "After all these years... You decide to show up NOW!?!"


    show emily angry at right:
        zoom 0.75
        yalign 0.6
    show mc sad at left:
        zoom 0.75
        yalign 0.6
    mc "Emily, I—"
    emily "YOU DIDN'T BOTHER VISITING US EVEN WHEN MOM DIED..."
    emily "YOU WEREN'T THERE FOR US..."
    mc "Emi—"
    emily "YOU WEREN'T EVEN THERE FOR ME WHEN {b}{i}I{/i}{/b} NEEDED YOU THE MOST!"
    emily "I HAD NO ONE AND YOU LEFT ME TO FEND FOR MYSELF!"
    mc "Emily, I—I never meant to leave you or Sarah behind..."
    mc "I thought escaping the war would help me escape that nightmare and return to you guys, but I was caught and deported back to the battlefield."

    show emily sad at right:
        zoom 0.75
        yalign 0.6
    emily "Every time I saw your silhouette disappear, I wondered if you'd ever come back."
    emily "And now that I finally accepted that you weren't coming... You have the audacity to show up at our door?"
    mc "I'm sorry I wasn't there when you needed me... But I'm here now"
    mc "You've been a really strong girl throughout this ordeal..."
    mc "But you can let loose now... I'm here, aren't I?"
    emily "..."

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
            show emily angry at right:
                zoom 0.75
                yalign 0.6
            "Emily stares at her dad, fuming, her arms folded, as [mcname] respects her space."

    scene study with fade:
        zoom 1.1
    "[mcname] walks into his old study, where he discovers a box of unsent letters."

    show mc pensive at center:
        zoom 0.75
        yalign 0.6
    mc "These letters… they're pieces of a love I thought was lost."

    voice "sarah_1.mp3"
    sarah "My dearest [mcname], even amidst the chaos of war, my heart has never stopped whispering your name."

    menu:
        "Read the letters immediately.":
            play music "dramatic_sad_piano_low.wav"
            scene letter with fade:
                zoom 1.1
            show sarah3 at center:
                zoom 0.4
                yalign 0.5
                alpha 0.7
            hide mc pensive
            voice "p1 L1.ogg"
            sarah "My love... This morning, I found myself in the garden we planted together..."
            voice "P1 L2.ogg"
            sarah "As I gently watered each flower, I recalled the way your eyes would light up when you showed me the first blooms."
            voice "P1 L3.ogg"
            sarah "I could almost feel your hand in mine, guiding me through each new sprout..."
            voice "P1 L4.ogg"
            sarah "It was as if the garden was whispering our secrets, and reminding me of those blissful mornings when..."
            voice "P1 L5.ogg"
            sarah "Love was simple and every petal held a promise..."
            voice "P1 L6(last).ogg"
            sarah "I miss you... I miss you so terribly in moments like these, when nature sings our song."
            show sarah3 at left:
                zoom 0.4
                yalign 0.5
                alpha 0.7
            show sarah2 at center:
                zoom 0.4
                yalign 0.5
                alpha 0.7
            voice "P2 L1.ogg"
            sarah "My dearest, Each morning, I wake up hoping for a letter, a sign that you are safe..."
            voice "P2 L2.ogg"
            sarah "The days grow long without you."
            voice "AUD-20250218-WA0010.ogg"
            sarah "I remember that rainy afternoon when we danced around the kitchen..."
            voice "P2 L3.ogg"
            sarah "Twirling to our favorite song while the world outside blurred into silver rain."
            voice "P2 L4.ogg"
            sarah "Your laughter was the melody that made even the darkest days shine."
            voice "P2 L5.ogg"
            sarah "Although later, Emily tried to mimic our silly dance and laughed just as heartily..."
            voice "P2 L6(last).ogg"
            sarah "I miss the sound of your laughter, and the way you made every moment sparkle..."
            show sarah2 at right:
                zoom 0.4
                yalign 0.5
                alpha 0.7
            show sarah4 at center:
                zoom 0.4
                yalign 0.5
                alpha 0.7
            voice "P3 L1.ogg"
            sarah "I remember the night we danced under the stars. The memory is what keeps me warm when the cold sets in."
            voice "P3 L2.ogg"
            sarah "No matter how far you go, no matter how much time passes, my heart will always find its way back to you."
            voice "P3 L3(last).ogg"
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
    mc "Every explosion, every corpse... They weren't just echoes of the war—they were shattered promises."
    mc "Each blast tore through the quiet of my soul, a stark reminder of vows I made in the heat of battle—to protect my comrades, my country and to return to your loving arms."
    mc "I remember the day we parted, the tearful goodbye where hope was our only shield against the inevitable pain."
    mc "With every fallen comrade, I felt the weight of promises broken, of futures stolen by the relentless cruelty of conflict."
    mc "And as I stood amidst those ruins of broken promises and heartbreaks, every man whispered a lesson: that the cost of war is not measured in the fires of battle alone, but in the tender moments of love and trust we lost along the way."

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
    "[mcname] remembers that final smile with an ache that never faded—a smile that held the warmth of countless shared mornings, the softness of whispered dreams, and the strength to face the inevitable."
    show sarah4 at right:
        zoom 0.4
        yalign 0.5
    "It was as if, in that fleeting moment, Sarah poured every hope and every unspoken goodbye into that one, final smile."
    "Even now, as the memory replays in his mind, it feels like a beacon—a light that guides him through the bleak corridors of war and loss, reminding him that love, even in its quietest moments, endures beyond the confines of time."
    voice "P5 L1.ogg"
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
    voice "P5 L2.ogg"
    sarah "I need you to stay. For Emily. For Us."
    mc "Alone...? It's going to feel lonely without you by my side..."
    voice "P5 L3.ogg"
    sarah "My love..."
    voice "P5 L4.ogg"
    sarah "Are you sure you're going to feel lonely with Emily by your side?"
    voice "P5 L5.ogg"
    sarah "Moreover, you will always have me by your side..."
    voice "P5 L6(last).ogg"
    sarah "In your heart and your memories."
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
    "Shadows flicker against the walls, stretching long and tired, just like the silence between father and daughter."
    "[mcname] and Emily finally sit down together, the space between them more than just physical."
    "The years of absence, of unsaid words, of moments stolen by time and regret finally catching up."
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

    scene black
    with Pause(0.5)

    show text "Fast forward a few days, Emily and [mcname] visit the local lantern rite festival..."  with dissolve
    with Pause(1.5)

    hide text with dissolve
    with Pause(0.5)
    
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
    "Minutes pass but neither speaks."
    "The silence is thick, not with tension, but with the weight of all that has been left unsaid."

    show emily shocked at right:
        zoom 0.75
        yalign 0.6
    emily "(voice quiet, but filled with something hesitant, something fragile) I had a dream about Mom."
    show mc sad at left:
        zoom 0.75
        yalign 0.6
    "[mcname] turns slightly, frowning with a grim expression of misery and sadness."

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
    show sarah3 at right:
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
            "And for tonight, that is {i}enough{/i}."

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
            "{i}A new beginning{/i}."

    play music "calm (mp3cut.net).wav"
    scene black with fade:
        zoom 3
    "As the screen fades to black, a quiet moment lingers—"
    "An invitation, a whisper meant just for you..."
    show sarah3 at center with fade:
        zoom 0.4
        yalign 0.5
        alpha 0.5
    ""
    voice "P6 L1.ogg"
    sarah "Grief is love that has nowhere to go."
    voice "P6 L2.ogg"
    sarah "But love… Love never truly leaves..."
    voice "P6 L3.ogg"
    sarah "It lingers in the spaces between laughter..."
    voice "P6 L4(last).ogg"
    sarah "It lingers in our memories of those we've lost along the way."

    voice "P4 L1.ogg"
    sarah "*inhale*...*sigh*"
    voice "P4 L2.ogg"
    sarah "Maybe you've lost someone..."
    voice "P4 L3.ogg"
    sarah "Maybe you're still trying to make peace with the past..."
    voice "P4 L4.ogg"
    sarah "Or maybe, like [mcname], you're afraid to open a door you thought was closed forever."

    voice "P4 L5.ogg"
    sarah "But you're still here..."
    voice "P4 L6.ogg"
    sarah "And that means there's still time—"
    voice "P4 L7.ogg"
    sarah "To heal, to forgive, to hold on, or to let go."

    voice "P4 L8(last).ogg"
    sarah "Whatever you choose… just know that you are not alone."
    hide sarah3
    "THE END"

    scene black
    with Pause(0.5)

    show text "Thank you for playing \"The Echoes of Silence.\"" with dissolve
    with Pause(1.5)

    hide text with dissolve
    with Pause(0.5)

    show text "This is my first visual novel project which I completed until the very end, and I know it's far from perfect.\nI truly appreciate you taking the time to experience it, despite any flaws or mistakes I may have made." with dissolve
    with Pause(2.5)

    hide text with dissolve
    with Pause(0.5)

    show text "🎭 Credits 🎭" with dissolve
    with Pause(1)

    hide text with dissolve
    with Pause(0.5)

    show text "🖼️ Art: AI-generated\n🎵 Music: Pixabay\n🎙️ Voice Acting: Manami Sarkar\n✍️ Writing & Development: BlackNinjaKR" with dissolve
    with Pause(1.5)

    hide text with dissolve
    with Pause(0.5)

    show text "I'm still learning, and your support means the world to me." with dissolve
    with Pause(1.5)

    hide text with dissolve
    with Pause(0.5)

    show text "Thank you for being a part of this journey with me. ❤️" with dissolve
    with Pause(1.5)

    hide text with dissolve
    with Pause(0.5)

    show text "~BlackNinjaKR" with dissolve
    with Pause(1.5)

    hide text with dissolve
    with Pause(0.5)

    return