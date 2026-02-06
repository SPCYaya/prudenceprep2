define whoS = Character("???", image="sibyl", who_outlines=[ (3, "#ffffff") ])

label sl_rom:
    scene bg black with fade
    "Who did Naomi romance in {i}Secret Lilies of Prudence Prep{/i}?"
    menu:
        "Blanche":
            $ secret_lilies_romance = "blanche"
        "Veronika":
            $ secret_lilies_romance = "veronika"
        "Izzie":
            $ secret_lilies_romance = "izzie"
        "(Randomize)":
            $ secret_lilies_romance = renpy.random.choice(['blanche', 'veronika', 'izzie'])
            pause 1.5
    jump spaghetti_start

label spaghetti_start:
    play music guitar1
    scene bg path winter night with fade
    "A warm breath puffs out visibly from between my chapped lips, only to dissolve into the frigid wintry air."
    "The stillness of the chilly early evening is disturbed by my exasperated huff, sending the little white snowflakes which fall before my face into a frenzy."
    show clover annoyed at center with dd
    C "And now it's {b}snowing{/b} too."
    show clover scowl with dd
    "I stop right where I stand to ruffle my pale blonde hair back and forth, casting off all the snow which has already begun to accumulate atop my head."
    "Then, after settling my hair properly back into place with a scowl solidly plastered on my face, I hump the duffel bag strap more securely over my shoulder and proceed further down the long wooded lane."
    "\"When I was your age, I walked to school up hill both ways in the snow!\""
    "The voice of my grandfather echoes in my mind as I trudge along slowly toward the the glowing emanating eerily from the windows of buildings down the lane."
    "The private academy which I am marching toward like a death row inmate is where I'll be serving out the remainder of my freshman year of high school."
    "I'm already dressed in my new uniform: an exceptionally cute pink and white outfit totally unlike what I used to wear the year before at my old public school."
    "Just about everything related to this sudden transfer has been a headache, but the new uniform is secretly something I actually kind of like — with one exception."
    "Whether it's just my awkward fourteen-year-old body or because I'm lugging my entire worldly belongings against my hip, the warm white tights keeping the chill away don't know whether they want to droop or bunch, and so do both."
    C anxious "(Surely have a car that could have met me at the gate? Heck, send a whole school bus if you have to!)"
    scene bg mary winter snow night with dissolve
    "A wave of relief washes over me when I spy the contours of the stately buildings of Prudence Preparatory Academy emerging clearly from the concealing white cover of light snowfall."
    "Beside what are likely the school buildings and dormitory all quietly accumulating white fluff, there is also a small chapel with a grand statue of some religious figure out front."
    show clover neutral at center with dd
    C "(I'd better fix this before going any further.)"
    "I perform a clumsy half jig for a few steps in a futile attempt to correct my errant tights, then drop the duffel bag where I stand to dig my fingers into the uniform inelegantly, pinching and digging at the white material which runs up to my waist."
    who "Dear me, Vincenza, and in sight of the Virgin Mary too."
    who "The Virgin Mary always watches over us, Vittoria."
    "Unexpectedly out of the lazy snow flurries floats a pair of hazy white figures and the titter of laughter against the quiet of the evening dusting of a snowfall."
    show clover anxious at center with dd
    C "W-Who's there?"
    "I almost begin to think I've frozen to death and passed into the astral plane as a result of my desperate trek, but my corporeality is soon validated when a sudden weight presses around the back of my neck and upon my shoulders."
    stop music fadeout 0.5
    scene cg spaghetti with dissolve
    play music drama
    pause 1.0
    O "The proper young ladies of this academy do such things in the confines of their own rooms."
    "The second girl to speak, who judging by her voice was addressed as Vincenza, is close enough for me to feel the warmth of her breath tickle against the chill of my left cheek."
    "Flipping my head swiftly to the side, I catch sight of the face of the girl in question. She wears an easy grin upon a pretty face, with eyes as relaxed as her posture."
    "From her head falls a stream of fine golden hair down her back, styled with a neat ponytail in a kind of boyish look that oddly doesn't contrast at all with the girlish uniform." 
    H "It may well be that she is no proper young lady at all."
    "A hand grazed against the small of my back announces the arrival of the other girl. The touch remains there even as she swoops close across my other side in a flutter of voluminous golden curls toward my front."
    "When my head flips back the other way, I find that this girl, Vittoria, shares similar features to the first, albeit with a very different, classically feminine aura also very much suited to the uniform."
    "I might not doubt that the walk from the road to the school buildings had indeed taken my life, were it not that the angels which emerged from the snow bore no wings upon their backs."
    "The first sensible thought through my frozen brain is that they must be sisters, if not twins, and the noticeable foreign accent common between them only adds to the similarity."
    "Without warning, the more boyish of the twin phantoms draws close to my face. Her hand reaches under my chin to guide my head this way and that in inspection of my features."
    O "Do your eyes deceive you, Vittoria? She is precisely the sort you adore."
    H "A young lady she is certainly, Vincenza; of that there is no doubt. The question of her propriety, however, remains inconclusive."
    "The pair continue their mesmerizingly strange back and forth discussion with barely an acknowledgement of their brash invasion of my personal space."
    C "What... what is happening?"
    O "You've kept us waiting, Clover, and on such an unpleasantly wintry evening as this."
    C "(How does she know my name!?)"  
    O "We are destined for a rendezvous of considerable import, but first we must attend to you."
    "With her right arm still heavy around my shoulders, the girl hanging over my shoulder heedlessly picks at the leftmost strap of my skirt at my waist before following it with her fingertips all the way up my chest."
    C "My flight was delayed because of the sto— {b}h-hey{/b}...!"
    "I might have totally forgotten that I had the skirt of my uniform hiked up to pick at my tights when I was suddenly beset upon, but the girl in front of me certainly hasn't."
    "When I try to semi-politely shove off the handsy probing of the girl slumped across my shoulders, the other one suddenly becomes even more invasive."
    H "You cannot hope to make a fitting entrance while your uniform remains in such disarray. Please allow me to assist."
    "The hand of hers which isn't on my small of my back brushes against my own still pinching my tights, only to go further still in picking up where I had left off."
    C "(Is getting this close normal for these two girls? They must be Europeans!)"
    H "You desire a memorable first impression for your Vertu, do you not? You simply must look your very best."
    "She pulls at the tights bunching around my knees and slides the palm of her hand up my leg with it, smoothing the thin material across my legs."
    "My chilled thighs tingle with the sleekness of her touch, but I am otherwise struck stiff with the surprise of the stranger gliding her hand way up to places not normally dared."
    O "The poor girl is utterly chilled to the bone. Can we not keep her just a little longer, Vittoria, to warm her up?"
    "The strap of my skirt is released from the second girl's fingers, but just as I think she's about to let me go she instead extends her fingers' reach to straighten the pink necktie around my neck."
    C "Eueh...!"
    "A strange sound emerges from my lips as a consequence of all this odd attention. It too transforms into a soft puff of warm breath which dies in the cold air before me."
    "To say I'm flustered is an understatement. I'm not usually one who likes touchy-feely types. Even my overly-affectionate grandma makes me squirm, and this is going way beyond the sloppy forehead kisses she is known for."
    H "We were only asked to deliver her room key, Vincenza, and we are already late ourselves as you rightly pointed out."
    "The first girl's palm glides well higher than it has any right to up my thigh, and still further beyond to flatten out with the tights out around the curve of my hip."
    "A small shudder passes through my body from my ear into which the one girl, Vincenza, keeps speaking into, all the way down to the hand pressed closely upon the small of my back."
    O "Pity, but I've a feeling this will not be our last meeting."
    H "No, I dare say not. This is one to watch closely, sister."
    "Distracted and slowed from logical thought by the strange caresses and warmth blooming all over my body, it's only then that my mind finally comes to the heart of the matter."
    C "R-Room key?"
    "With a soft giggle, the wavy-haired girl's fingertips clip against my stomach where the white tights meet their end, followed by the cold touch of something entirely unnatural against my bare skin."
    stop music fadeout 0.5
    play music guitar1
    scene bg mary winter snow night
    show clover surprised blush at center
    with dissolve
    C "H-Hyah!?"
    "My entire body quivers instinctively against the harshly frigid metallic object wedged between my skin and my tights, breaking the dumb stupor the mysterious pair of girls had drawn over me."
    "Shaking about like mad trying to fish out the object burning cold against the heated skin inside my tights, the offending item turns out to be a metal carabiner with my own face staring back at me from the plastic id card attached to it."
    C frown blush "(Room 28.)"
    "Once my thought processes finally catch up to my comprehension of the object I'm currently holding, I spin about to let those handsy twins finally have a piece of my mind."
    C shout blush "Y-You—!"
    show clover neutral blush with dd
    "Just as I am about to let loose on the two girls beside me, I find that they're no longer clinging to me at all, which actually makes sense considering how easily I was able to retrieve the key."
    "My eyes follow the trail in the thin snow cover to find the pair strolling gaily arm-in-arm toward the academy like they weren't just a few seconds ago groping me all over in the middle of the path up to the school."
    scene bg mary winter snow night with dd
    H "{i}Le abbiamo sicuramente piegato gli spaghetti.{/i}" # we definitely bent her spaghetti
    O "{i}Certamente.{/i}" # for sure
    scene bg mary winter snow night
    show clover scowl blush
    with dd
    "I am left behind, half confused and half fuming mad. I can feel the heat swelling in my cheeks and in my chest, made visible by the form of extra puffy breaths of air which emerge from my lungs."
    C @ deer blush "(What the {b}heck{/b} was all that!?)"
    "I could chase down those two girls — not angels, but in fact demons — if I abandon my duffel bag containing all my possessions in the snow, but I don't know exactly what I'd do when I reach them anyway."
    show clover neutral blush with dd
    "What I do understand acutely is that the warmth I felt while they were close is rapidly being eaten away by the cold sting of the biting winter breeze."
    stop music fadeout 0.5
    jump vertu

label vertu:
    play music piano1
    scene bg mary winter snow night with fade
    "Despite the wintry Massachusetts chill and the promise of a warm place to rest, the prospect of having to formally \"arrive\" at this new school does not speed my footsteps."
    "As I trudge deeper into the campus, I find many girls in similar uniforms hurry past me toward the living quarters, as expected given the hour of the day. I follow them at a small distance."
    scene bg dorm night
    show clover scowl blush at center
    with dissolve
    C "(That was definitely sexual assault, right?)"
    "I don't try to talk to a single one of my new fellow students. I'm still reeling from my first interaction with the strange enrollees from this academy and don't want to invite another incident."
    C annoyed blush "(She stuck her hand... {b}all{/b} the way up there!)"
    show clover neutral blush with dd
    "When I find the door with my number plastered on it, I heave a big sigh to try to douse my inflamed irritation and push it open with defeat heavy in my limbs."
    scene bg bedroom night with dissolve
    play sound doorclose
    "Another girl lies atop one of a pair of beds before me. An apology tumbles out instinctively."
    show clover neutral at center with dd
    C @ neutral talk "S-Sorry, I—"
    "I catch the words of my reflexive apology quickly, finding the girl roused neither by the door opening nor my apology, instead merely lying still on the bed."
    "Her presence, and the two beds inside the room, stoke my worst fears, which are confirmed when I double check my key card and the name plaque outside the door."
    C "(So this is a \"roommate\" type of boarding school. Not quite fancy enough to give each student her own room, huh?)"
    "This new arrangement is certainly going to be an adjustment from being an only child and having my own room. One of many adjustments in my life that I'm suddenly being forced to make."
    C @ contemplative "(I'll keep as much space between me and her as possible so that she won't be a problem. Yeah.)"
    "Even as my brain thinks I should stay as far away as humanly possible, something tickling at my curiosity draws closer to the sleeping figure on the bed."
    "I approach my new roommate cautiously, ready for anything after having already been jumped by the pair of girls from before, but still she remains unstirred."
    C "(She's not... {b}dead{/b}, is she?)"
    hide clover with dd
    show sibyl sleepy at center with dd
    "Looking more closely, I find her chest rise and fall with calm breathing. I quickly surmise through the inspection that she likely unintentionally fell asleep and is otherwise perfectly alive and healthy."
    "Lying in full uniform crossways atop her bed, she rests in the classic pose one makes when she rests her head for \"just a moment\" and suddenly loses precious hours of the day."
    "It's kind of cute in a way, like a child who plays too hard and tuckers herself right out."
    hide sibyl with dd
    show clover neutral at center with dd
    "It's only recently that I've been trying to embrace my own \"cute\" side, but so far have totally failed trying to compete with girls like this who can pull it off even in their sleep."
    C @ annoyed "(Why does dieting only make my face break out and look extra nasty? What am I doing wrong that this girl is doing right?)"
    "A long paper banner is strung across her body, draped loosely between the slim fingers of the sleeping figure where she once held it."
    "\"Welcome Clover!\" the banner reads in sparkling glitter lettering. It's even decorated with all sorts of cute little drawings, most notably a multitude of glittering green shamrocks."
    C @ scowl "(Because of my name, of course.)"
    "I've lost count by now of how many people over my lifetime have picked a clover out of the grass and pointed between it and me with a big, stupid grin plastered on their face."
    "My annoyance about my name fades with a momentary wave of guilt that I might have suspected her of something terrible when she so clearly put effort into welcoming me into what was previously solely her space."
    C contemplative blush "(Her eyelashes are so long...)"
    hide clover with dd
    show sibyl sleepy at center with dd:
        zoom 2.5 yalign 0.1
    "Replete tresses of auburn curls which stream from her head make me flame with envy as someone who has lived with straight hair her entire life."
    "A strange thought passes through my mind that this almost feels like a scene out of a fairy tale, where the prince wakes the princess with a kiss."
    C "(Gross. Why are old fairy tales always so creepy?)"
    "Little flickers of a dream in progress play cross her sleeping features and make her pale pink lips tremble. The sight is captivating in a strange way that draws me even closer to lean over the bed."
    play sound bedcreak
    pause 1.0
    hide sibyl with dd
    "The sudden creak of the bed when I shift more weight against it draws me sharply out of the trance. Pulling myself quickly away the bed, I turn around again toward the one left untouched."
    show clover anxiety blush at center with dd
    C "(What am I {b}doing{/b}?)"
    "Mental images of my roommate's sleeping face linger in my mind longer than I would like. My chest thumps loudly in my ears as I heft my luggage onto the bed and begin dumping it out as a distraction."
    C tired blush "(It's been a long day. I'm tired.)"
    show clover neutral with dd
    "The explanation fits neatly in my mind and I think nothing more of it, instead turning my remaining energy to emptying out my over-stuffed duffel bag before I hit the hay myself."
    hide clover with dd
    who "...Clover?"
    "The words float out airily behind me, soft enough for them to tickle at my ears but firm enough to force their way between all the dark thoughts brewing in the back of my head."
    "Once they worm deep enough into the my brain, I whip back around quickly toward my suddenly stirring roommate, who rests propped up on one arm where she fell asleep."
    show clover surprised blush at mright
    show sibyl neutral at mleft
    with dd
    "She is more awake than before, anyway. Her long lashes lay heavy over her crisp blue eyes. The soft pout from being pulled out of a dream too early remains on her lips."
    C neutral talk "What do you want?"
    show clover neutral with dd
    "I just sort of... blurt the words out while my brain is still working to catch up and immediately realize how rude that must sound."
    "Before I can say anything more, I'm caught speechless when she tosses her loosely bound auburn curls with the back of her hand. A wince forms on her face, her eyes cast downward."
    who bashful "A better introduction than {b}this{/b}."
    show clover anxious blush
    show sibyl frown
    with dd
    "I can feel heartbeats go entirely missing within my chest as I watch her quickly lean across her bed to check her alarm clock on the nightstand, then flash her big round eyes back at me."
    "Struggling to find the right balance of apologizing for being awful and keeping my distance, I brush a hand through my own fair strands in a show of innocuous detachment."
    C neutral talk blush "Sorry. I was surprised to hear you. I'm super late, sore from lugging my duffel bag all the way here, and I ran into two crazy girls on the way here."
    show clover neutral blush with dd
    "Why I care enough about her feelings to not just dismiss her outright I do not know, but I rationalize that it's better to be on my roommate's good side than her bad."
    S @ frown talk "I'm so sorry, I meant to be there when you arrived to help you and— oh, my name is Sibyl. Sibyl Hyltebruk."
    "She stills seems half asleep to me by the way her thoughts are coming all at once, but her dopey face is too pleasant to object all too strongly against."
    C contemplative blush "Umm... Clover Ipswich. So we're going to be roommates then, huh?"
    "What I say is merely a polite greeting and a rhetorical question, so I swiftly turn back about to begun unpacking before I get any more caught up in her pitiful, sleepy expressions."
    "From behind me, Sibyl yawns into a reply with no intention to let the conversation drop there. It's clear her sleepiness is rapidly fading away for better or worse."
    S @ neutral talk "Not merely roommates, but Vertu partners. Haven't you read the academy pamphlet?"
    show choice_darkness with dissolve
    menu:
        "\"Oh, right, the pamphlet... I think that's stuffed in here somewhere.\"":
            hide choice_darkness with dissolve
            C neutral talk "Oh, right, the pamphlet... I think that's stuffed in here somewhere."
            show clover neutral with dd
            "I hazard a glance back toward Sibyl, who surprisingly doesn't look mad at my casual dismissal of school culture as much as she does disappointed."
        "\"That's French, umm... \'green\', right?\"":
            hide choice_darkness with dissolve
            C neutral talk "That's French, umm... \"green\", right?"
            show clover neutral with dd
            "I try to humor her with my limited knowledge of the language, but the airy sigh from behind my back that tells me I wasn't quite right after all."
            S "We're going to have to catch you up on your French language skills."
        "\"My life's been pretty well flipped and turned upside down lately, so no.\"":
            hide choice_darkness with dissolve
            C neutral talk "My life's been pretty well flipped and turned upside down lately, so no." # And I'd like to take a minute, just sit right there. I'll tell you how I became the princess of a school called Prudence Prep.
            show clover neutral with dd
            S @ frown talk "I am so sorry, Clover."
            C annoyed "Yeah, well, it's not you who needs to apologize."
            "My tone comes out pretty dark, and Sibyl apparently chooses not to pry into it any further."
    show clover neutral
    show sibyl neutral
    with dd
    "Correctly surmising that I had discarded the dull school literature at first glance, my new roommate launches into her own explanation of that which I clearly do not know."
    S neutral talk "Vertu partners are like... having a best friend or an older sister to help you, and to be that person for your Vertu partner as well."
    S smile talk "More than simply sharing this room, we are meant to share our triumphs with each other, and split the burden of our tribulations."
    show sibyl smile with dd
    "Her explanation increasingly sounds like she's quoting directly from the pamphlet the longer it goes on."
    C @ neutral talk "That's pretty poetic sounding, huh?"
    "Honestly, I couldn't care less about any of that flowery language, and it probably shows in the flat tone of voice which my reply sounds out with."
    C "(We share a room. We're roommates. That's it.)"
    "Despite how she holds off on lecturing me any further about the topic, I still get the sense that Sibyl very much cares about this whole \"Vertu\" business."
    S contemplative "Do you need help unpacking?"
    "Even though she's on the other side of the room, it still feels very much like she's hovering around me."
    C @ neutral talk "No."
    "The momentary silence which follows is comfortable to me, but seemingly not to Sibyl. Her commitment to engaging in conversation with me remains as firm as ever."
    S neutral talk "You're my first Vertu partner, you know that? Our grade level had an uneven number of students and I happened to be the odd one out in our year who received no Vertu."
    C scowl "(There she goes again.)"
    show sibyl neutral with dd
    "Even though it's all just some dumb private school way of saying \"roommate\", she keeps saying \"Vertu\" with a strangely serious tone like it is some hallowed institution akin to marriage."
    C annoyed "(Like I'd ever marry a girl in the first place...)"
    show clover scowl blush with dd
    "Just thinking about two girls together \"like that\" somehow brings the pair from earlier to mind. I can already feel the heat of my boiling blood rising all over my body just thinking about what they did to me."
    "I know for sure I'll be lying awake tonight replaying the scene over and over in my head, thinking up all sorts of awesome comebacks I should have used at the time."
    S @ neutral talk "Clover, are you alright?"
    C neutral talk "Y-Yeah, I'm fine."
    show clover neutral with dd
    "Sibyl catches me momentarily zoning out back into recent events, and makes it known that she's still in the room with me."
    S smile talk "Maybe I didn't make a good first impression on account of dozing off, but I really would like to help you adjust to the academy."
    C annoyed "I don't need help."
    S "I'm your Vertu partner, Clover. This is what Vertu partners do."
    C scowl "Thank you, Sibyl, but I'm very {b}self-sufficient{/b}."
    show sibyl frown
    show clover neutral
    with dd
    "The room goes quiet between us as soon as I say the words with a cold tone of annoyance rising clearly in my voice."
    "I continue folding the clothes taken out of my luggage while purposely facing away from Sibyl behind me. An apology is considered, but I decide against it."
    C @ annoyed "(That's honestly how I feel, and if she doesn't like it, well, it's better that she doesn't get too attached to me anyway.)"
    S bashful "Have I come on too strong? I know you only just got here but I have been so anxious and excited to finally meet you."
    "The disappointment in her voice is palpable. It's making me feel like the absolute worst person alive when I only want to have absolutely nothing to do with her or anyone else here."
    C neutral talk "Sibyl—"
    "I don't find Sibyl in tears when I turn to look at her directly. There's not even a frown on her face, merely an expression of gentle concern masking a quiet determination."
    C "Sibyl, I'm sorry, you've been super nice and everything, really, and I didn't mean to shut you down like that. I've just been going through some personal things, and I need some space right now, okay?"
    show sibyl smile
    show clover neutral
    with dd
    "She smiles up hopefully to me from where she sits on her bed, her blue eyes meeting my own and lingering in the connected gaze."
    "I tear my defeated gaze away from her puppy dog stare, and swallowing my pride somewhat, ultimately throw her a bone."
    C neutral talk "But I will be counting on you to show me around campus and classes, and stuff like where to find the cafeteria and all that."
    C tired "(What's wrong with me today? When did I becomes such a pushover?)"
    S surprised "Oh no, the cafeteria!"
    C anxious "W-What wrong with it?"
    S "It's closed!"
    C surprised "For how long!?"
    S contemplative "Until tomorrow morning."
    show clover neutral with dd
    "Relief washes over me, having thought for a moment there that I'd be starving due to a permanently closed cafeteria in addition to everything else that is sure to be terrible here."
    S frown talk "I must have snoozed right through meal time, and you must be famished too after all that traveling."
    show sibyl frown with dd
    C anxious "Well... kinda..."
    "As much as I might be thinking that I don't want to rely on Sibyl any more than I absolutely need to, the sudden recognition of the emptiness in my stomach draws a meek acceptance of the situation."
    C neutral talk "Are there, like, vending machines that we can use?"
    show clover neutral with dd
    S @ smile talk "I'm afraid not... but, ah, let's go speak to Ms. Woolsey. She will definitely be able to help us."
    "I am totally willing to eat junk food out of a vending machine for dinner, but risking the wrath of some mean old teacher within hours of my arrival is much more bleak of a prospect."
    C @ frown talk "I'll be fine until the morning, I promise. We don't need to go bother a teacher."
    S smile talk "Nonsense! She's our dorm mother; this is exactly what she's here for!"
    show sibyl smile with dd
    C anxiety "But won't she be mad?"
    S laugh "Ms. Woolsey? No way. She's exceptionally kind and easygoing, you'll see."
    scene bg bedroom night with dd
    "I want to refuse again, but a sudden loud rumbling in my stomach makes it all but impossible to turn my nose up at Sibyl's plan."
    stop music fadeout 0.5
    jump woolsey_intro

label woolsey_intro:
    play music guitar2
    scene bg dorm night with fade
    "Sibyl only has to lead me to the end of the floor to reach Ms. Woolsey's room. We knock but receive no answer."
    play sound doorknock
    show clover neutral at qright
    show sibyl contemplative at qmright
    with dd
    S @ neutral talk "Hmmm. She's usually here by now. I wonder if there was a staff meeting tonight."
    C @ neutral talk "Maybe she's gone out? We should just go back to our room."
    "I wait patiently beside Sibyl, silently observing the confused thoughts play through her head as they are shown upon her profile."
    S neutral talk "We should wait."
    show sibyl neutral with dd
    C @ neutral talk "Why?"
    S @ "Some people get cranky when they're hungry, Clover."
    "I can only surmise this ambiguously worded statement is directed at my earlier performance, but to be fair, my grand arrival was promptly spoiled by two perverts."
    C @ scowl "(And you know what's also not my fault? The cheap airline only giving out a tiny pretzel snack bag.)"
    show naomi happy talk at qleft with dd
    who "Sorry girls, I got held up back in the school building."
    show naomi smile with dd
    "Before I can think of another way out of this, the teacher who must be Ms. Woolsey arrives from behind us to fully seal my doom."
    mw @ happy talk "What's the matter, Sibyl— and, oh! You must be Clover! I'm Ms. Woolsey, your athletics instructor."
    "My first very first thought when I look at my new athletics instructor is that she is probably the textbook definition of a high school gym teacher — right down to the ponytail, sneakers, and athletic zip-up hoodie."
    "The only thing that is perhaps unusual is the golden ring she wears around her neck besides the requisite silver whistle. I think for a moment she might be married, but then remember she's a gym teacher."
    mw @ sad talk "I'm so sorry I couldn't meet you at the gate tonight. I see that Sibyl was able to greet you properly though!"
    S contemplative blush "About that..."
    "With some obvious embarrassment on her part, Sibyl finally chimes in beside me."
    S frown talk "I, umm, missed her arrival too. I was just too fidgety to sleep at all last night and it finally caught up with me this afternoon."
    S "When I woke up, Clover was already in our room unpacking her belongings."
    show sibyl frown with dd
    mw neutral talk "I see. It's a good thing I asked the Royal Twins to take my place in delivering the keys then."
    show naomi neutral with dd
    C scowl "(The \"Royal Twins\"...? That must be {b}those{/b} girls. And they're {b}royalty{/b}?)"
    "Perhaps unfairly, I turn a short glare toward the teacher who sicced those perverts upon me. Thankfully, she doesn't seem to notice."
    show clover neutral with dd
    "Ms. Woolsey looks to be rather young, probably barely out of college, and not altogether unpleasant at first meeting despite her apparent association with those two sexual predators."
    mw @ talk neutral "How are you settling in, Clover? Was there something you needed to speak with me about?"
    "Before I can promptly shut down Ms. Woolsey's good-natured assistance, Sibyl speaks out ahead of me."
    S contemplative "Yes, there is! You see, it would appear that we both... entirely missed dinner."
    mw happy talk "Is that all? Let's go raid the kitchen and see what we can pull together."
    scene bg kitchen with fade
    "The cooks have long ago left for the day by the time we arrive to the cafeteria kitchens, but that doesn't stop Sibyl and Ms. Woolsey from scrounging up enough peanut butter and jelly for sandwiches."
    "It might not be much of a meal, but I am willing to admit privately to myself that having food in my grumbling stomach does lower my hot head by a few degrees."
    show clover neutral at mright with dd
    C "(I've been working hard to play nice. I deserve this extra stuffed PB&J. Shame there's no chocolate hazelnut spread or marshmallow creme...)"
    show sibyl smile talk at center
    show naomi happy talk at mleft
    with dd
    "My roommate and the gym teacher chat with each other while I try to hang back and blend into the refrigerator."
    "Once we're sitting down with sandwiches in hand, however, it's more difficult to keep their interest off me for long."
    mw neutral talk "Most students have only just returned from winter break last week, and I haven't even gotten all my class plans together yet. Clover, do you prefer tennis, disc golf, or... maybe yoga?"
    show naomi smile
    show sibyl smile
    with dd
    "Ms. Woolsey turns her gaze on me to await my response to her pointless question. Even Sibyl pauses mid-bite to stare me down in a expectation of my answer."
    C "(How about \"none of the above\"?)"
    show choice_darkness with dissolve
    menu:
        "\"Tennis.\"":
            hide choice_darkness with dissolve
            C @ neutral talk "Tennis."
        "\"Disc Golf.\"":
            hide choice_darkness with dissolve
            C @ neutral talk "Disc Golf."
        "\"Yoga.\"":
            hide choice_darkness with dissolve
            C @ neutral talk "Yoga."
    "There's no real reason for my to choose my answer, just as there wasn't for the question. I speak only what comes to me at the moment as I have no desire to participate in any of it."
    show naomi frown
    show sibyl neutral
    with dd
    "The supreme succinctness of my answer clearly does not get lost as the gym teacher frown slightly and Sibyl chooses to change the topic right away."
    S @ neutral talk "It's such a pity that you missed the masquerade ball, Clover. It was a lot of fun."
    C @ surprised "(Masquerade ball? Yikes. I'm actually thankful I missed that.)"
    mw happy talk "This year's masquerade ball was my first as a teacher. The whole event feels so different when you're on the other side of the masks!"
    show naomi smile
    show sibyl smile
    with dd
    S @ smile talk "You were a student here, Ms. Woolsey?"
    mw @ happy talk "More than just a mere student, I was the president of the student council!"
    "It's actually kind of sad how proudly Ms. Woolsey proclaims that she went from being the student council president to what is objectively the most pathetic teaching role at a school."
    mw @ happy talk "My high school masquerade ball was a big day for me in a lot of ways, so I'm glad you enjoyed it so much too. Which animal did you pick?"
    S @ "The options were sort of picked over when I got my mask so I chose the kangaroo."
    "That I have been staring at my sandwich while devouring it should indicate I don't particularly care to talk, but it seems that Ms. Woolsey isn't content with reminiscing of her school days with Sibyl."
    mw @ happy talk "It's almost Valentine's Day already. That means the first academy-wide event you'll get to take part in is making chocolates for all your new friends, Clover!"
    C @ neutral talk "Oh yeah?"
    "My reply starts out incredibly half-hearted and disinterested, so I try to raise my enthusiasm just a little so as not leave the other two entirely disappointed."
    C @ neutral talk "I'm sure that will be fun if I make any friends."
    show sibyl frown
    show naomi awkward
    show clover neutral
    with dd
    C "(Oops, shouldn't have added that last part.)"
    "My eyes shift toward Sibyl without consciously meaning to, forcing me to catch the flash of dejection present on her face after I all but admitted that she means nothing to me."
    C "(We've known each other for like, two hours, don't look at me like that!)"
    mw happy talk "I know it must be difficult to transfer in part way through the school year but you'll have your Vertu, Sibyl, by your side every step of the way."
    "Ms. Woolsey also picks up on my little faux pas easily enough, and does her best to try to smooth it over for me."
    show naomi smile
    show sibyl smile
    with dd
    C @ contemplative "(She might not actually be as thick as the average gym teacher. I should be more careful around her.)"
    "Much like Sibyl before, Ms. Woolsey goes on to tell me how special being roommates is at this school. Sibyl nods seriously at what the teacher says, giving me an encouraging smile all the while which only makes my stomach flop over inside me."
    C @ neutral talk "That's what Sibyl was telling me."
    show sibyl neutral
    show naomi neutral
    with dd
    "Returning my attention to my sandwich with a chill dismissal, I try to ignore the sideways glances that passes between Sibyl and my new teacher."
    mw @ neutral talk "If you don't mind me asking, Clover, why did you choose to attend Prudence Prep?"
    C annoyed "I didn't {b}choose{/b} to be here. My parents {b}sent{/b} me here."
    C scowl "(Like a lone button when you can't find the sweater to which it belongs. It just gets tossed in a drawer for safekeeping while you go about your life.)"
    "Ms. Woolsey, while friendly, is being awfully persistent at trying to get me to open up when I have no intention of doing so, and the annoyance leads me to say more aloud than I want to."
    "The room couldn't be getting any chillier even if we had left the refrigerator door open. I know I'm acting really terrible but I have a valid reason to be this rightfully touchy about the subject."
    C annoyed "(And it's not like either of them really cares about me anyway.)"
    "It's the teacher's job to look after me just as much as it is apparently Sibyl's responsibility to do the same as my \"Vertu\"."
    show naomi awkward with dd
    "There's a long silence after I speak where Ms. Woolsey's mental gears are clearly spinning in her head trying to formulate a response to my brusque reply."
    S frown talk "Clover, I'm so sorry..."
    show naomi neutral
    show sibyl smile
    show clover neutral
    with dd
    "To my surprise, Sibyl reaches out to lay her hand on my arm in a manner to offer her condolences, without even knowing what I'm going through at all."
    show clover surprised with dd
    "I pull away suddenly from her touch as quickly and unexpectedly as she'd touched me."
    C tired "I don't need your apologies."
    mw neutral talk "W-Well... I have long felt that the people I met here at the academy are like a second family to me, so if you ever need—"
    "She's just trying to console me, I know, but she unwittingly stepped right onto the land mine already primed to explode."
    stop music fadeout 0.5
    C shout "I already {b}have{/b} a family, I don't need a second one!"
    show naomi surprised
    show sibyl bashful
    show clover scowl
    with dd
    "The long and arduous journey here, the muddled rush of emotions in the past few hours, and everything else swirling together in my head draws yet another verbal jab which I cannot take back."
    "My shouting is shockingly ineffective on Sibyl, who only follows my angry outburst with a look of pity and understanding."
    S frown talk "Oh, Clover..."
    show sibyl smile
    show naomi frown
    with dd
    "It's unnerving, to see this strange reaction to me being so frigidly cold. Sibyl's soothing concern and big, sparkling eyes peering directly at me drive right through my icy exterior to make my stomach flutter the half-digested sandwich within."
    C annoyed "(What could she possibly be thinking now? She doesn't know a single thing about me!)"
    play music guitar2
    show naomi pensive with dd
    "Sibyl might have the mysterious expression of utmost compassion and understanding on her face, but my athletics teacher is only further troubled by everything that's happening."
    mw neutral talk "I shouldn't have pried into your personal life, Clover, I'm sorry."
    show naomi neutral with dd
    C neutral talk "I-It's fine..."
    C neutral "(I'm sure she's thinking that she's only made things worse with her persistent questioning. Maybe I can salvage my gym class grade after all?)"
    show sibyl neutral with dd
    "Awkwardly, I try to cool down and smooth things over with the teacher despite Sibyl's strangely calm expression still being foremost in the jumble of my mind."
    mw happy talk "Just know that if there's anything you don't feel comfortable talking about with Sibyl, you can always call on me to lend an ear too."
    show naomi smile with dd
    C @ neutral talk "...Thanks."
    "I feel like an amoeba under a microscope by the way Sibyl keeps looking at me sympathetically, and then doubly so with how Ms. Woolsey is still clearly fretting over our interaction under her own smile."
    C tired "(When will this day just {b}end{/b}?)"
    "Rather than make the rest of the night even worse, I resolve to focus instead on filling my mouth with sticky peanut butter and jelly so that I physically cannot reply any more."
    scene bg bedroom night with fade
    "Sibyl and I at long, long last say good night to the dorm mother, Ms. Woolsey, and make our way together back to our dorm room."
    "There's a notable difference in the way Sibyl acts toward me since the awkward conversation in the kitchen, which for some reason bothers me way more than I want to care about it."
    show cpj annoyed at mright with dd
    CPJ "(What gives? First she wants to be my BFF and now she's acting all aloof? Are {b}all{/b} the girls here totally insane?)"
    "She barely demands my attention or says any words beyond what is required. She merely goes about her own routine for the night as do I mine."
    "It's kind of infuriating actually that I don't know what she's getting at, and I find myself keep looking back at her as I make my bed and finish my nightly preparations."
    "I keep right on watching her until she starts stripping out of her uniform right in front of me, from which I suddenly jerk my head away nearly fast enough to break my neck."
    CPJ surprised "(Is this normal for roommates!?)"
    "Logically, there's nowhere else to change into my sleepwear but right here, and I can't figure out why I really care so much in the first place, so I suffer through the self-consciousness and do the same."
    scene bg bedroom night dark with dd
    S "Good night, Clover."
    "The voice of the roommate I was trying to avoid thinking about floats in my direction through the darkness."
    "The half naked form of Sibyl undressing lingers faintly in my mind despite my best effort to brush it out along with the unpleasantness of the day's events."
    "What eventually replaces that is the sour recollection of what those two girls did to me that evening, which does not help to calm me down one bit."
    pause 0.5
    "I do not manage to come up with a single awesome comeback before I drift off into a restless sleep which fades confusingly in an out of the real world around me."
    "At times I'm there sleeping in my dormitory bed, listening to the quiet breathing from the next bed over and the natural music of wind whistling through a thousand bare tree branches outside."
    scene bg path winter night with dissolve
    "Other times I'm trudging down the long tree-lined road to the academy where those two girls, the \"Royal Twins\" as they were called, circle around me like vultures with shining gold crowns."
    "Just once, I dream vividly of those vultures and their grabby claws, but this time they're both replaced by my strange new roommate, Sibyl."
    "Her wavy auburn hair bounces around me from either side as she and her double sweep their hands across my body in smooth, sensuous motions."
    "The phantom Sibyls say nothing, merely giving me that infuriatingly knowing smile she showed me in the kitchen."
    scene bg bedroom night dark
    show cpj surprised at mright
    with dd
    CPJ "Hahn!"
    "Awaking with a start, the phantom images of my roommate linger to haunt my vision with the fading dream, replaced quickly with the dark emptiness of the ceiling above my bed."
    stop music fadeout 0.5
    jump shower_time

label shower_time:
    scene bg transition with fade
    pause 1.0
    play music piano2
    scene bg bedroom
    show cpj tired at mright
    with fade
    "I am anything but well rested by the time the sun breaks over the horizon."
    "More than anything else in the world, I desire to remain in the assigned bed, eyes closed, pretending to be safely back in my own bed in my own room at my own house with all being well in the world."
    CPJ frown "(I want to go home! How long will I have to be here?)"
    "Daylight streams in through the open windows when my eyes do open. The restless fits of sleep must have caught up to me at some point in the early morning because I have no recollection of the dawn ever coming."
    show sibyl neutral at mleft with dd
    S @ neutral talk "Good morning, Clover. The cafeteria is already open and homeroom is at eight, so you'd better hurry up."
    "As if to answer the question which had yet to form, Sibyl emerges at that very moment from the bathroom fully dressed in her uniform and pulling a brush through her hair."
    CPJ annoyed "Dun wanna."
    "I squirm around under my warm covers, snuggling the sheets tighter around me in protest and shutting my eyes as tight as possible to block out the miserable sun."
    CPJ tired "(So what if I skip class. What are they gonna do, send me back home? That's what I want anyway.)"
    S @ neutral talk "If you don't get up you're going to miss breakfast."
    CPJ "I'll survive."
    "I'm not quite at the level of desperation that calls for a hunger strike, but I am reasonably confident that I can hold out until lunch if I have to."
    S @ neutral talk  "I understand that the necessary lifestyle changes resulting from attending this academy can be tough to adjust to, but you'll feel much better if you keep to a schedule."
    CPJ "(What does {b}she{/b} know about my \"lifestyle changes\"!?)"
    "Sibyl responds to me in a soft, chiding voice, like I'm some kind of petulant child that she needs to take a firm hand with instructing properly."
    S @ neutral talk "I know very well how you're feeling, or I think I do anyway. I've seen it many times before."
    CPJ "(What is she, a psychiatrist? Now I know why she didn't have a roommate before me.)"
    CPJ "What are you even saying?"
    CPJ "(Why does she think I need anything at all, let alone \"schedules\" and \"structure\"? I'm doing just fine by myself, aren't I?)"
    S neutral talk "What I am saying is that I am going to give you the time you need to accept your current circumstances, but also ensure that you are not worsening them."
    S smile talk "So please, get up and get ready for class."
    CPJ "No."
    hide sibyl with dd
    "All at once a wave of cool air washes over me as the topmost layers of my bed are whipped clear off my body."
    CPJ deer "{b}Nooooo!{/b}"
    "I writhe about in a frenzy against the chill air assaulting me, knowing full well and caring little about how childish and petulant I must look in that moment."
    stop music fadeout 0.5
    scene bg bedroom with dd
    play music sad
    "Defeated and increasingly more hungry by the minute, I slump off the edge of the bed, wipe the heaviest of the sleep from my eyes, and make for the shower where I stand half asleep with the water beating down on my face."
    C "Sibyl... What does she think she knows about know about how I feel anyway?"
    "She knows nothing about my parents' protracted divorce proceedings, nor anything about how they abandoned me out here all alone. Even I don't even know what they're thinking sending me here."
    "I'd obviously prefer that my parents stay together rather than split up, but my family life has recently been nothing short of suffocating even if my parents try to hide it from me."
    "It's like the only thing they agree on nowadays is dumping me in this far away place with only a frilly pink uniform and a duffel bag of life essentials to my name."
    C "(Aren't divorced parents supposed to be spoiling their only child rotten? Does that only start happening after it's finalized?)"
    "Wetness streaks down my cheeks as I blindly fumble for my shampoo. I find the bottle, squeeze it, and quickly freeze up as the sweet floral scent fills my nostrils."
    "Flashes of Sibyl's sleeping face from the night before explode into my mind's eye. They momentarily push aside the pain of my previous thoughts but make me feel no more at ease."
    "Water splashes all around me as I shake my head in a flurry of droplets. The motion manages to successfully banish the images from my mind, allowing me to find my own shampoo bottle."
    stop music fadeout 0.5
    scene bg dorm winter with dissolve
    play music piano2
    "Reluctantly, but with a growling stomach as proof that the previous night's peanut butter and jelly sandwich has not sated me, I make my way to the cafeteria alongside Sibyl."
    C "(Please, {b}please{/b}, let the food be the one good thing about this whole miserable place!)"
    scene bg cafeteria winter with dissolve
    "The cafeteria does not disappoint. The breakfast menu is surprisingly robust — so much so that my mouth starts watering just reading the options. For my first ever meal at the academy, I choose a little bit of everything offered."
    "I don't breathe a single word of it aloud to Sibyl, but I actually do feel considerably less cranky and more awake after getting out of bed, put together, and having proper food in my stomach."
    show clover neutral at qmright
    show sibyl neutral at qmleft
    with dd
    "My roommate is seemingly too distracted with something of her own to bother me, so I end up gobbling my breakfast down way too quickly and am rewarded with a minor stomach ache as a result."
    "With nothing much to entertain me but my own dark thoughts and a discontented stomach, I am forced to people watch as a means to occupy my brain."
    C "(All of these girls are going to be my classmates?)"
    "It's a little strange to be in a single-sex school after having attended normal public schooling my whole life, but that is only the surface of the oddities I find."
    "Perhaps what is most unsettling to me is how everyone seems so awfully bright and cheery, like they actually want to be stuck in this boarding school out in the boonies."
    C @ frown "(I wish I had my smartphone.)"
    "Mindlessly scrolling the internet would alleviate my boredom, but Sibyl was adamant that I leave it behind. Apparently it's some kind of school rule that everyone actually follows for real."
    C "(Everyone here's just so \"proper\". I can only imagine how snobbish the student council must be.)"
    "What's more, I find that the students all arrive in pairs. It's an obvious conclusion that they are arriving with their \"special roommates\" like Sibyl is to me."
    "As I watch various pairs file into the cafeteria, I also begin to notice how close the occasional pair seems to be, often holding hands and just generally being exceptionally chummy with one another."
    C contemplative "(Is this what Sibyl wants to be like with me? Is this what it means to be a — what's it called — \"Vertu partner\"?)"
    "And then I see one of the pairs... kiss."
    C surprised "Oh my gosh..."
    "Not on the lips, but very affectionately on the cheek. The intense eye contact alone between the pair reveals every intent behind the gesture."
    "My thoughts leak out in a soft expression of surprise, bringing Sibyl back to the present from where she was preoccupied peering toward the doorway."
    S @ neutral talk "Something wrong, Clover?"
    C "Lesbians — they're gay, Sibyl!"
    show sibyl contemplative
    show clover neutral
    with dd
    "Sibyl gives me a slightly puzzled expression right back, which I probably deserve after my nonsensical outburst."
    show sibyl neutral with dd
    "Glancing back toward where I'm gaping, Sibyl briefly checks out my discovery with a stealthy motion to make it look like she's not obviously looking their way."
    "She doesn't seem surprised at all, and I don't really know why I am either considering I have nothing against lesbians — despite not being one myself."
    S neutral talk "Oh, those two are a well-known couple."
    S smile talk "For a religious school, homosexuality is remarkably very well tolerated here. I was surprised myself."
    C @ frown "(Being religious doesn't mean hating gays. Even I know that and I'm, like, the exact opposite of religious.)"
    S laugh "When I first decided I wanted to apply here, one of my older sisters stated with such horror: \"A {b}girls'{/b} school? With no {b}boys{/b}!?\"."
    S smile talk "I've only been here a few months but I get what she means now. I guess that sort of thing is just more common at an all-girls school."
    show sibyl smile with dd
    "My eyes stay fixed on the pair of girls who had kissed long past what might be considered merely rude, watching them now enjoy their breakfast."
    "When I shift my gaze back to Sibyl I am overcome with a strange awkwardness watching her, so I turn my attention instead toward some unexceptional, empty section of the dining hall."
    C @ neutral talk "Uh huh...?"
    S @ smile talk "Our art teacher is gay too. I'd say it's an open secret but it's barely a secret at all."
    C @ neutral talk "What do you mean?"
    show sibyl contemplative with dd
    "For a moment Sibyl is quiet, no doubt trying to find the correct way to answer my question. Her gaze turns upward like she's recalling something, and her reply begins slowly."
    S contemplative "That one time in club when we did a nude study, she..."
    S laugh "Well, anyway, she's a really great art instructor!"
    C neutral talk "That's, uhh, kinda weird. You're in the art club?"
    S angry "Why is me being in the art club weird to you, Clover?"
    show sibyl annoyed with dd
    show choice_darkness with dissolve
    menu:
        "\"I meant that the teacher sounds weird. I was only surprised that you're in the art club.\"":
            hide choice_darkness with dissolve
            C "I meant that the teacher sounds weird. I was only surprised that you're in the art club."
            "I feel like there's a subtle hint of annoyance in the way Sibyl asked, and I find myself oddly quick to alleviate her condition because of it."
            C "I guess you did make that big banner for me and everything."
            show sibyl smile
            show clover neutral
            with dd
            "Sibyl turns away from a glance toward the doorway to give me a bright, genuine smile."
            S smile talk "So you did enjoy the banner! If only I weren't asleep and could have displayed it properly."
            show clover neutral blush
            show sibyl smile
            with dd
            "Sudden sneaking bashfulness overtakes me as Sibyl smiles radiantly down upon me. I can't find it in myself to tell her how much I hate being likened to clovers, so I just cooly change the subject altogether."
        "\"I thought it'd be the, uh... nagging club, I don't know.\"":
            hide choice_darkness with dissolve
            C "I thought it'd be the, uh... nagging club. I don't know."
            show clover neutral with dd
            "I fall easily back into the usual disinterested routine, having no idea why I ever really cared what club Sibyl is in to begin with."
            C impish "(She's just my roommate after all. I don't need to know her whole life story.)"
            S neutral talk "Contrary to what you might think, I did have my own life here long before you came into it yesterday."
    show sibyl neutral
    show clover neutral
    with dd
    C @ neutral talk "What do you keep looking for anyway?"
    "It's not like I want to keep talking to Sibyl or anything, but she's my only entertainment and her attention keeps getting drawn away toward the door."
    S @ neutral talk "My friend from the art club. She's unusually late this morning."
    C @ neutral talk "You have friends?"
    scene bg cafeteria winter
    show tanya neutral at left
    with dd
    "Before she can reply to my verbal jab, Sibyl stands suddenly from her seat to wave down a particular girl who walks through the doorway in that moment."
    C "(Alone, is she? Maybe I can get her to take Sibyl as her Vertu instead of me.)"
    "The newcomer turns toward where I am sitting, but seeing me already occupying the space across from Sibyl, instead sits by her side."
    show clover neutral at mleft
    show sibyl smile at center
    show tanya annoyed alt2 at mright
    with dd
    who "I'm so sorry, Sierra held me up again."
    show sibyl neutral with dd
    "It's clear from the way she speaks the name and the lightly disdainful flip of her sleek black hair that there's some bad blood between this girl and the other \"Sierra\" girl."
    S @ frown talk "We just came back from break and you're already on the outs with her?"
    show tanya neutral talk with dd
    who "Not exactly, but you know how she is..."
    show tanya neutral with dd
    S smile talk "Do I ever, but forget her for a moment. I'd like you to meet my new Vertu, Clover!"
    S laugh "Clover, meet my best friend, Tanya Yang."
    show sibyl smile
    show tanya neutral
    with dd
    "Sibyl having made the introductions for us, our eyes lock together for a brief moment before Tanya breaks into an equally friendly but decidedly more detached greeting."
    T smile talk "Nice to meet you, Clover! Are you taking good care of Sibyl for me?"
    show tanya smile with dd
    "Despite a subtle accent in her speech, Tanya speaks so fluently that it's clear that she has often spoken English for quite some time."
    S @ laugh "Taking care of {b}me{/b}? I practically had to drag her butt out of bed this morning and it's only her first day!"
    "As evidenced by how playfully Sibyl retorts, there's no real malice in her choosing to reveal this embarrassing fact, and Tanya doesn't look too hard on me for it."
    C @ contemplative "(She didn't mention the little fit I threw this morning, so I guess I owe Sibyl for that. Not that I care a single speck for what this Tanya girl thinks of me of course.)"
    S @ smile talk "We'd better go and get your breakfast before they close up the kitchen, Tanya. Want to come with, Clover?"
    "I turn them both down with an excuse about having already eaten too much despite knowing full well she wasn't asking if I wanted any more food."
    show tanya neutral alt blush with dd
    "For a moment I think I see Tanya flick another lingering glance my way as they leave me at the table, but it might just be my imagination."
    scene bg cafeteria winter
    show clover contemplative at center
    with dd
    C "(What's her deal, anyway?)"
    "Sibyl and Tanya are obviously close friends already, even after just a few months together. The latter is not at all hesitant to lean softly against Sibyl's arm as they laugh about something to one another."
    show clover frown with dd
    "The whole sickening display of friendship leaves a bitter taste in my mouth when I think about my former friends back home, all of whom seem to have slowly forgotten about me as schools change and life goes on."
    show clover neutral at mleft
    show sibyl smile at center
    show tanya smile alt2 at mright
    with dd
    "When my roommate and her friend eventually make their return, the latter immediately takes the uppermost strawberry off the top of her yogurt parfait and turns to plop it into the former's open mouth like it's an everyday ritual."
    C "(They might actually do this same this every day for all I know.)"
    "Watching them go about the motions of the day so in sync, even if it's just eating breakfast, only drives home the intimacy of their friendship."
    C @ neutral talk "So are you two, like, girlfriends?"
    show tanya surprised alt2 blush with dd
    "Tanya nearly snorts her vanilla yogurt and crunchy granola right out of her nose when I abruptly ask the question, so while her friend is still indisposed, Sibyl answers for both of them."
    S @ laugh "Best friends."
    C @ neutral talk "I've had best friends before and we never fed each other."
    S @ smile talk "Tanya hates strawberries. I love strawberries. It's a win-win."
    T annoyed blush "No fruit should have that many seeds. And why are they on the outside? It makes no sense."
    C neutral "(She sure has strong opinions about fruit.)"
    show tanya neutral with dd
    S @ smile talk "The way I see it, we need more fruit like strawberries, and star fruits, and pawpaws, and whatnot. The stranger the better."
    C @ neutral talk "How did you two ever become friends?"
    S @ smile talk "Tanya's in the art club too!"
    "With Tanya still deep into choking down her breakfast before the start of class, it's mostly Sibyl who keeps engaging me in conversation."
    "At my next question, however, Tanya does huff angrily into her yogurt parfait."
    C @ neutral talk "Uh huh. And who's Sierra?"
    show tanya scowl with dd
    S contemplative "Tanya's Vertu partner. They don't exactly see eye to eye on everything."
    "The roll in Tanya's deep brown eyes demonstrates just how much Sibyl is understating the apparent dysfunctionality of their Vertu partnership."
    C scowl "So we're allowed to not act like we're eternal BFFs with our roommate here? I almost thought it was required by the way everyone here is acting."
    S annoyed "Some people enjoy the support and companionship a Vertu partnership provides, Clover."
    T annoyed "If you're lucky enough to get a good Vertu partner."
    show tanya neutral with dd
    C impish "If it were up to me I would have my own room all to myself."
    S neutral talk "I too though the same at first, Clover."
    S contemplative "For a brief moment, it felt fortuitous that I had no Vertu partner to share my room with. I had a whole room to myself for the very first time in my life."
    C neutral talk "Do you want it back? Maybe there's an extra room I can camp out in."
    show clover neutral with dd
    "Sibyl seemingly ignores my interjection and continues on without acknowledging my interruption at all."
    S frown talk "But then I learned how lonely it can be when everyone else has a partner with whom to share each day, except you."
    S "Every night after curfew, I sat in my lonesome room, my only company being the empty bed across the way."
    show sibyl bashful with dd
    C @ neutral talk "That's a bit dramatic, don't you think?"
    show tanya scowl
    show sibyl annoyed
    with dd
    "Both Sibyl and Tanya give me a particularly hard look, and for just a moment I feel that maybe I shouldn't have spoken any quips when Sibyl is clearly being very serious."
    C @ neutral talk "But you have Tanya now, right? So you don't need me."
    S smile talk "Tanya is a wonderful friend, that much is true, but she is not my Vertu partner."
    show sibyl smile
    show tanya smile
    with dd
    C @ contemplative "Tanya hates her own Vertu. Why can't you just switch?"
    T neutral talk alt2 "I would {b}love{/b} to foist Sierra off onto you, but one cannot just {b}trade{/b} a Vertu partner."
    show sibyl frown
    show tanya frown
    with dd
    "Both of them look to be shocked and disappointed, like my suggestion is not at all a totally rational idea, is actually the most absurd thing they've ever heard, and that I'm a terrible person for ever suggesting it."
    C @ annoyed "Okay, okay, I get it. No switching Vertus. It's a sacred bond between two girls which can never be broken."
    show sibyl smile
    show tanya neutral
    with dd
    "Sibyl smiles at my sarcastic reply even though it should be clear from my tone that it is indeed incredibly sarcastic."
    C "(I suppose she hopes hearing me say it out loud will make me believe it eventually too.)"
    T @ neutral talk "I may have my differences with Sierra, but I respect the rules and traditions of this academy more than I find fault with her."
    S @ smile talk "I hope all this talk about Sierra and Vertus helped you realize how important you are to me, Clover."
    show clover anxiety with dd
    "Sibyl hits me with the guilt trip of the century out of nowhere. Her words cause a stir to flutter in my stomach more intense than simply having eaten too quickly."
    C annoyed blush "(We've barely known one another a single day! She probably only cares about \"her Vertu partner\", not {b}me{/b}!)"
    "Tanya, meanwhile, quickly finishes her yogurt parfait to allow us to head to our classroom just in time for the bell to ring."
    stop music fadeout 0.5
    jump class_intro

label class_intro:
    play music guitar1
    scene bg mary winter
    show clover neutral at mleft
    show sibyl neutral at center
    show tanya neutral at mright
    with fade
    "Sibyl keeps a close watch on me as she, Tanya, and I wind our way through the white-coated campus grounds toward the school building."
    C annoyed "(Sibyl is probably afraid I will run off, and to be fair I probably would if she weren't watching me like a hawk with binoculars.)"
    scene bg classroom winter
    show clover deer blush at center
    with dissolve
    "When I soon come to find myself standing in front of my homeroom class with a crowd of matching uniforms staring back at me, I suddenly wish I'd taken off sprinting anyway."
    C @ anxious blush "M-My name is Clover Ipswich..."
    "Standing all alone at the center of attention in front of so many people typically dissolves me into a total disaster. Knowing that a total disaster is impending always hastens its arrival like some terrible chain reaction."
    C @ tired blush "(Why do I have to introduce myself!? Can't the homeroom teacher just let me slink unnoticed into a seat in the back of the classroom like I planned!?)"
    "Sweat feels like it's pouring out all over my body, my brain pounds like mad against my skull, and to top it off I'm also suddenly way too conscious of the weight of the arms at my sides."
    C @ excited blush "(Imagine them in their underwear! Isn't that what they always say?)"
    "I try to imagine all the girls before me in their underwear, but to no avail. My attention is only brought to the one girl who I've already seen undressed the night before."
    te "I'd like you all to please assist Clover as she joins your classes today."
    "There's a chorus of agreement from the audience after the homeroom teacher makes the necessary introductions. All too quickly, however, does she put the spotlight right back on me in the worst way."
    te "Is there anything you'd like to tell your new classmates, Clover? Maybe about your hobbies, achievements, or what you have on your mind as you begin your time here at Prudence Preparatory Academy?"
    "The dreaded \"tell us about yourself\" question. It paralyses my brain, caught somewhere between frozen solid like a block of ice and overheating trying to think of a way out of this situation."
    show choice_darkness with dissolve
    menu:
        "\"I think I'm gonna throw up...\"":
            hide choice_darkness with dissolve
            C vulnerable "I think I'm gonna throw up..."
            "I obviously cannot see what I look like, but I certainly feel positively green just standing there at the front of the classroom with every eye on me."
            "From somewhere beyond my heart pounding loudly in my ears I hear the teacher ask if I need to see the nurse. On instinct I state the truth that I just need to sit down."
            show clover frown at qmleft
            show sibyl neutral at qmright
            with dd
            "It's only when I finally feel the seat under me and the brain fog clears up that I realize I could have just gone to the nurse's office and gotten out of this whole mess altogether."
            S @ neutral talk "Tell me if you start feeling bad again. I'll show you the way to the nurse."
        "\"I-I can't stop thinking about Sibyl's underwear.\"":
            hide choice_darkness with dissolve
            C anxious blush "I-I can't stop thinking about Sibyl's underwear."
            "Unbelievably, I say exactly what's on my mind despite how it's quite possibly the worst thing I could say at this moment."
            "There's an immediate round of giggles from the assembled class before me, leading me to say a quick prayer to whichever deity may be listening that I'll drop dead any second now."
            "The sweet relief of a lightning strike from the heavens never comes, however, and I quickly stammer out a weak explanation in possibly the highest pitched voice to ever leave my throat."
            C surprised blush "I-I was trying to imagine... y-you all in your u-underwear..."
            "I don't know why the class should believe me. I don't even know what I'm saying myself anymore. I just shut my mouth and quickly shuffle off toward my seat when the teacher finally takes pity on me."
            show clover frown blush at qmleft
            show sibyl laugh at qmright
            with dd
            S "I'm flattered, Clover."
            "I know Sibyl is just joking in an attempt to lighten my mood, but it's really not helping one bit."
            S smile talk "It's tough to be put on the spot, even for me."
        "\"I like k-koalas.\"":
            hide choice_darkness with dissolve
            C surprised "I like k-koalas."
            C surprised blush "..."
            "There's a small silence as everyone, including myself, takes in what I have to say. All three words of it."
            C tired blush "(What. The heck.)"
            te "Thank you, Clover. Why don't you take a seat?"
            hide clover with dd
            "I don't even have any particular interest in koalas, it's just the first thing that came to mind somehow."
            "I just {b}know{/b} that from this day forth, I'm going to be forever known as \"the koala girl\"."
            show clover frown at qmleft
            show sibyl laugh at qmright
            with dd
            S "I think koalas are cute too, Clover!"
    "Sibyl whispers some kind but unhelpful words from the seat beside me in a futile attempt to revive my pale, deathly visage."
    show sibyl smile
    show clover bangs blush
    with dd
    "The embarrassment just hits me all the more forcefully because of it, leading me to seek refuge by drawing my hair around my face like curtains in which to hide my shame."
    jump after_lunch

label after_lunch:
    scene bg classroom winter with fade
    "The classes I attend during the first half of the day pass in a blur. The lessons themselves go in one ear and out the other."
    "While all the others students quickly fall back in the groove of how things work at the academy, I am absolutely lost in every way despite Sibyl trying her best to keep me up to speed."
    C "(I just arrived the previous day. I don't even want to be here. And now I have a quiz on material I've never learned!?)"
    "Her notebooks are very detailed, but it's all entirely too overwhelming for me. I feel like my first day at the academy skipped the frying pan and threw me directly into the fire."
    scene bg cafeteria winter with dissolve
    "The coming of lunch time and an extra large dollop of creamy macaroni and cheese eases my mind to a small degree, but the foreboding of the latter half of classes remains."
    "Feigning a trip to get a second helping, I sneak away from Sibyl and out of the cafeteria entirely in favor of wandering around until I find someplace quiet to finally be alone."
    scene bg library winter with dissolve
    "My first stop is to the library, which I am at first surprised to find entirely deserted, until I remember that most people are likely to be eating lunch or attending classes at such a time."
    "I idly pace down the rows of shelves while scanning the spines. One book's fancy gilded edges catch my attention, so I pull it from the shelf and subsequently flop down into a nearby chair."
    "The words of the open book read line-by-line through my brain without being processed as anything sensible, much like the titles before them."
    stop music fadeout 0.5
    play music sad
    show clover vulnerable at center with dd
    C "(Where did everything go so wrong?)"
    "I've only been at the academy for less than twenty-four hours and yet I've already been both sexually assaulted and then humiliated in front of the whole class."
    "All of that just feels like extra bitter icing on the burnt cake of my life, which truly started unraveling long before I ever arrived at the academy."
    "It still feels like just yesterday that I was at home playing with my dog Abraxas in the backyard or enjoying Monday pizza-and-a-movie night while sandwiched between my parents on the sofa."
    C anxiety "(Now Mom and Dad are probably fighting over me, Abraxas, and everything else like we're both items to be traded and bartered!)"
    "Just thinking about it infuriates me so much that I chuck the open book at random into the emptiness of the otherwise still library."
    show clover distraught with dd
    "I don't know exactly when it starts, but the tickle of a wet drop running down my arm soon informs the remaining logical part of my brain that I'm just barely choking back tears."
    C teary "(Gosh, I'm pathetic. Like, \"barely holding it together\" pathetic.)"
    stop music fadeout 0.5
    scene bg black with dissolve
    "My head drops onto my arms atop the the table with finality. The futility of reading to distract myself is apparent. The end result would only have been a wet book."
    "The same cruel thoughts pass through my brain over and over, back and forth between desperation to know where I went wrong and how I could have prevented my current fate."
    play music guitar1
    scene bg library winter
    show clover neutral at center
    with dissolve
    "The sound of a door opening behind me startles my head back upright from the table. I shrug my shoulders softly, suddenly feeling a stiffness there which I hadn't before."
    "A girl I've never met gives nothing but a passing glance my direction on her way to the shelves on the opposite side of the room."
    C "(Guess I'm not the only person skipping class today.)"
    "Perhaps in a touch better spirits now than before, I rise from my seat to replace the book I had thrown and continue on to the next stop in my meandering exploration of the school building."
    scene bg hallway
    show clover contemplative at center
    with dissolve
    "There are many more girls in the hallway than just a short time ago, I quickly find. I don't pay them any mind in particular and none of them seem to notice me being out of place either."
    "What does quickly catch my attention is how strangely long my shadow is cast by the deep orange glow pouring through the academy's tall windows."
    C "(Just how long was I in the library...?)"
    "It suddenly makes sense why I feel so much less stressed and more fully refreshed than I did at lunch time. After sleeping so poorly in my new bed, a little nap is exactly what I needed."
    "As I progress down the hallway, I turn a corner off toward a less traveled route and slip through a quiet looking doorway."
    scene bg aquarium winter with dissolve
    "What I find is an impressively equipped aquarium room, which this school has for some reason I cannot begin to fathom."
    "Most importantly, the room is deserted and soothingly silent. Only the unblinking eyes of the fish around me trace my footsteps."
    show clover neutral talk at center with dd
    C "You don't have a care in the world, do you?"
    show clover neutral with dd
    "The fish crowd around my finger as I tap it softly against the glass of their tanks, and in return I imitate their wide open fish mouths right back at them."
    "That is, until a breathy sigh heaves from my chest to chase away the assembled fish back into various corners of the tank."
    C shout "Fine, I came here to be alone anyway."
    show clover frown with dd
    "As I sit and stare at the fish swimming about their circuits in their stiflingly small tanks, I cannot help but feel the academy will be the same prison to me."
    C @ tired "(Confined to campus, making me speak in front of the class, loading me all up with homework...)"
    "The amount of homework I have already been assigned seems overkill for just half a day of lessons."
    "One of the earliest classes of the day was French language studies. Helplessly lost, Sibyl whispered translations of every word for me until the teacher made her stop."
    "In addition to normal subjects there was also an etiquette class, which was just about the last thing I expected, but maybe should not have been given the state of the rest of the school."
    C @ anxiety "(I {b}really{/b} need to read that academy pamphlet. I don't think I can handle another surprise like that.)"
    "Thinking about my awful classes instead of my awful life makes me come around slightly, but it also dredges up all the bad thoughts which had been suppressed by the soothing balm of sleep."
    "Clenching my fists to my side, I try to stem the tide of bad feelings before they well up further."
    C tired "(I'm alright. You're alright. Clover's alright. We're all alright.)"
    show clover neutral with dd
    "Releasing the tension in my fists, I raise my loosened fingers to toss my blonde tresses out in a physical manifestation of doing away with my emotional instability."
    C @ neutral talk "Hahn..."
    "I stand still like I'm calm, trying to will away the resurging angst, but deep down I can feel the pain swelling inside me. Much like my anxiety in front of crowds, my other emotions follow the same chain reactions."
    C "(If I don't suppress it now—)"
    play sound doorclose
    pause 0.5
    show clover surprised with dd
    "It's just at that moment that the door clicks open. My head raises instinctively to identify who could be coming to discover me in such a terrible state."
    C "Sibyl?"
    scene bg aquarium winter with dd
    "There's a light swell in my chest which surprises even me as I look expectantly toward the doorway, but it's not luxurious auburn curls which I discover fluttering through the doorway."
    "Rather, it's straight black tresses shining like a negative of my own fair-toned strands."
    show clover neutral at qmleft
    show tanya neutral at qmright
    with dd
    T @ neutral talk "So this is where you ran off to."
    "Deep down I know it was foolish to have assumed I would know some random person entering the room, let alone that it would be my roommate. That it's someone I've met in the short time I've been here is miraculous enough."
    C @ neutral talk "Y-Yeah. I needed some time alone."
    "My tone of voice sounds out rather dismissively, having no particular feelings about making terribly nice with my new roommate's best friend that I only just met a few hours before."
    "Knowing that my expression must be quite dark, I turn my head aside away from Tanya and back toward the fish swimming in their tanks. The blurry figure of my roommate's friend is visible by reflection."
    T @ contemplative "That's what Sibyl thought."
    C scowl "She knows me so well."
    "What should probably be positive praise is actually ironic when I speak the words. Tanya maybe can also sense it judging by her rising impatience."
    T neutral talk alt2 "Look, it's almost curfew time so you really should be getting back to the dorms."
    show tanya neutral alt2 with dd
    C @ surprised "(Is it that late already? Wait, I have a curfew!?)"
    "I distinctly recall Sibyl saying something about that, but like many other important things, it fell silently on deaf ears."
    C @ neutral talk "So why didn't Sibyl come for me?"
    T surprised "Huh?"
    "The question must have caught her off guard because she's momentarily quieted into staring back at me. I'm a little surprised at it myself even though it came from my own lips."
    C annoyed "She's the one always saying that we're partners and we're supposed to support each other. Why didn't she come looking for me?"
    T shout "We {b}both{/b} went looking for you, Clover, and a couple others besides. It's a big school."
    show clover neutral
    show tanya frown alt2
    with dd
    "I glance back blankly at Tanya, unsure what to feel about the answer or how to follow it up. She follows with a sighs of dismay and shakes her head side to side, then tosses a hand to rest at her hip to reset."
    T neutral talk "Hey, are you feeling alright, Clover?"
    show tanya neutral with dd
    "The soft tone of concern about a girl she barely knows ticks me off. I cannot stop myself from letting it come out through my words again."
    C scowl "What's it matter to you anyway? Don't you have your own \"Virtue\" to worry about?"
    show tanya scowl with dd
    "Tanya's tone again turns, this time more firmly, which is really no surprise with how obstinate I'm being toward her."
    T neutral talk "{b}Vertu{/b}. It's a French word, {b}Vertu{/b}, and it is a foundational aspect of this academy."
    "Tanya corrects me with a measure of her fading patience clear in her choice of words and the hardness with which they are spoken, but some of the concern yet remains as she continues right on pestering me."
    T "It matters to me because it matters to Sibyl. You're all she's talked about all day. She's barely said a word to me that wasn't about {b}you{/b}!"
    T neutral talk alt2 "So please, quit arguing with me and let's hurry back before the bell rings for curfew."
    hide tanya neutral
    hide clover surprised
    with dd
    "Tanya reaches out toward me to clutch at my hand in a total invasion of my personal space. She's surprisingly strong and is already pulling me toward the door by the time I manage to brush her off and shove back at her."
    show clover shout at qmleft
    show tanya scowl alt2 at qmright
    C "Don't touch me!"
    show clover scowl with dd
    T @ shout "{b}Augh!{b}"
    stop music fadeout 0.5
    play music drama
    "My cantankerous behavior has clearly ticked Tanya off, bringing the grand total of off ticks in the room up to two."
    T @ shout "Don't you know how hard Sibyl is trying to help you? Could you please at least {b}try{/b} to not fight her every step of the way?"
    C @ shout "I didn't {b}ask{/b} for, and I don't {b}need{/b} any help."
    show clover annoyed with dd
    T shout "That's exactly what she said you would say. You're infuriating, you know that?"
    T "Maybe Sibyl isn't pissed off, but I sure am. And the worst part is that I've only known you for a single day."
    T "You should count yourself fortunate that Sibyl has enough patience and compassion to put up with your moody bullshit."
    show tanya scowl alt2
    show clover scowl
    with dd
    "Amidst her tirade, Tanya steps closer, nearly backing me into a fish tank as she presses a finger angrily sharp into my chest. I'm taller than her, if only barely, but somehow she feels so much more dangerous in the moment."
    T shout alt2 "You {b}do{/b} need help. There's clearly something wrong with you. Every time someone tries to help you or even say a single thing nice to you, you have to spit it back in their faces!"
    T "You don't deserve someone as special as Sibyl for a Vertu partner, and if you aren't going to respect her, then stay away from her."
    show tanya scowl with dd
    "Tanya's rant doesn't scare me, even if she is stronger than she looks. I've had worse language thrown in my face before and half of that stupid rant was just praising Sibyl anyway."
    show clover impish
    show tanya surprised
    with dd
    "As for my reprisal, I hiss a childish \"if you love her so much, why don't you marry her\" which succeeds beautifully in getting under little-miss-best-friend's skin."
    show tanya annoyed alt with dd
    "Tanya nearly looks like she's about to claw my face off, but instead only shoves me back against the fish tank to herself turn away and stomp out of the aquarium."
    hide tanya with dd
    stop music fadeout 0.5
    play sound doorslam
    C scowl "(Good riddance!)"
    "With the irate presence before me now gone, I slump down right there with my back against the cold, hard glass. Fresh painful memories accompany those I've already been nursing."
    C frown "(She was the one getting all up in my business. She was asking for that.)"
    scene bg aquarium winter with dissolve
    "The irritable mood brought on by Tanya's presence gradually fades back into the creeping darkness, and consequently my brain replays everything that just happened."
    "In one moment my mood shifts such that I feel like I deserved all that abuse, and in the next my mood shifts again such that I'm certain Tanya is a fake and pushy bitch who deserved it."
    "I find no conclusions, merely yet another writhing mass of conflicted emotions to add to the pile."
    pause 0.5
    play sound bingbong
    pause 0.5
    show clover surprised at center with dd
    C "Crap. That's got to be the curfew bell."
    "As much as I don't want to return to the shared dorm room where Sibyl, and my doom, most assuredly awaits me, my blanket-laden bed is preferable to literally sleeping with the fishes in the aquarium."
    play music guitar1
    scene bg hallway night with dissolve
    "I creep down the hallway as stealthily as I can like the heroine of a spy movie — mostly successfully, until I turn around a corner straight into an even worse obstacle than the dorm mother."
    show twins smile talk at center with dd
    H smile talk "There she is, our missing Clover!"
    O neutral talk "Flaunting curfew on your first da—"
    hide twins with dd    
    "Before the twin demons can even think about doing anything intolerable again, I take off running down the hallway. Thankfully, they don't appear to be taking up chase behind."
    scene bg dorm night with dissolve
    "I'm way out of breath by the time I make it back to my dorm building, but otherwise make it back unmolested, and without drawing attention of any of the teachers."
    show sibyl contemplative at qmright with dd
    "The first thing I see when I sneak down the hallway toward my room is Sibyl, pacing anxiously in place outside the door."
    C "(Uh oh.)"
    show clover surprised at qmleft
    show sibyl smile
    with dd
    "I brace myself for whatever unpleasantness is about to happen, but Sibyl's face alights only with simple relief upon spotting me."
    "She throws her arms around my body without hesitation in a warm hug which could thaw the coldest outdoor chill."
    S @ smile talk "You made it back!"
    C anxious "Y-Yeah..."
    show clover vulnerable with dd
    "I don't even know what to say. Feeling Sibyl's warmth around me saps all the anger and angst right out of my body, leaving me a weak, emotionally-tired wreck."
    S frown talk "Clover, you're freezing!"
    scene bg dorm night with dissolve
    "Sibyl squeezes my hands in her own and pulls me in through the door to our room like she's afraid I'm going to get lost again if she were to let me slip from her grasp."
    play sound doorclose
    scene bg bedroom night
    show clover vulnerable blush at qmright
    show sibyl neutral talk at qmleft
    with dissolve
    S "I was so worried when you didn't come back!"
    show sibyl frown with dd
    "Feelings of guilt swell now that I'm back in my dorm room getting lectured by Sibyl, such that I can scarcely bear to look at her face."
    "Coming to my senses, I whip my hand out of Sibyl's and turn back to my own bed before she starts trying to chip away at the carefully maintained distance between us any further."
    C anxious "...I just needed to be alone. It's been a long day."
    "Something about Sibyl keeps getting me all out of whack, or at least even more than I have been lately, and while it's not painful I do find it disconcerting."
    S @ neutral talk "I knew you weren't going back for seconds of mac and cheese, you know. I meant to let you have your time alone, but as the clock kept ticking later I became more and more worried."
    C neutral talk "You could have just left me. Is the penalty for braking curfew that steep?"
    show clover neutral with dd
    S @ frown talk "No. I wasn't worried about getting in trouble for breaking curfew. I was concerned about {b}you{/b}, Clover."
    C anxious blush "Why? I'm just your roommate."
    S bashful "The hours dragged on and on and on and you still did not show up back at our room! I was afraid you might have done something more rash than just skip classes."
    show sibyl frown
    show clover contemplative
    with dd
    "I cannot begin to fathom what she thought I might have done. I'm already regretting merely having skipped eating a proper dinner for the second day in a row, which feels to be more than punishment enough."
    C neutral talk "Why do you care so much about me? You don't even {b}know{/b} me."
    show clover neutral with dd
    "I try to spit out the words with as much edge as I can to give off the impression that I don't really care, but deep down the mystery is eating at me for reasons unknown."
    S @ frown talk "I know you enough to know that you're in a lot of pain, and I know that you've been through a big life adjustment by coming here. That's not easy for anyone, Clover."
    "Women of ancient days who sat in their high temples and divined the Gods' truths bore the name \"sibyl\", but my roommate is not one of those women."
    C @ tired "(Sibyl does not know a single thing about me and has no hope of understanding anything about the reasons I'm suffering.)"
    S neutral talk "I'll wait as long as it takes for you to come around, so when you're ready to talk about anything I'll be right here."
    show sibyl neutral with dd
    "Just like Ms. Woolsey, Sibyl is doing the whole \"patience and understanding\" routine like she's certain I'm going to eventually come running to cry on her shoulder."
    C @ annoyed "(At least Tanya tells me how she really feels about me.)"
    S neutral talk "Oh, and before I forget, your phone was ringing like crazy earlier."
    scene bg bedroom night with dd
    stop music fadeout 0.5
    "The warmth of my dorm room which had slowly been returning to my body all of a sudden dissipates into thin air."
    play music drama
    show clover surprised at mright with dd
    "I jump across my bed to clutch at my smartphone. One missed call and a text message blink on the display. \"Hi sweetie, how was your first day at school?\""
    C scowl "(Like she cares a single bit about me anymore!)"
    "It's from Mom. She's asking about my first day at school like it wasn't half her fault for abandoning me here in the first place."
    "Or like she and Dad aren't tearing our family apart and destroying our lives together — the life I've always known and loved up until just recently."
    show sibyl surprised at mleft with dd
    "I chuck the smartphone into my pillow at full force, clearly alarming Sibyl across the room."
    S "C-Clover?"
    C @ shout "I'm {b}fine{/b}! It's just my mom."
    S smile talk "Your mom? That's great!"
    show sibyl smile with dd
    "Whatever Sibyl thinks is so great about it, I cannot possibly understand. What would be great is if she said the divorce was canceled, I can come home, and we are going to be a whole family again."
    "But that's definitely not going to happen. They may try to hide it from me but I can tell how bad Mom and Dad's relationship has become."
    show sibyl neutral with dd
    "Contrary to the act of having just pitched my smartphone into the bed, I immediately swipe it back up again to be sure it's safe. It is, after all, my only precious line outside of this nightmare school."
    S contemplative "I've found, Clover, that I feel better when I talk out my issues. Would you like to try it?"
    "It's clear that Sibyl is being cautious with her approach into poking at what is definitely a sore subject, which is beyond annoying in itself."
    C shout "You wouldn't understand!"
    show sibyl bashful
    show clover annoyed
    with dd
    stop music fadeout 0.5
    "There's a silence for a few moments after the stinging reply before Sibyl's soft, calming voice returns."
    S frown talk "I truly would not understand, but I also might be able to empathize with your troubles more than you might think."
    scene bg bedroom night dark with dd
    "After showing absolutely no signs that I am going to say anything more, Sibyl finally leaves me alone with my own misery once again."
    "I expect my mind to wander familiar dark pathways as it has often in recent weeks, but with all the emotional toil of the day I've endured, sleep takes me before I even know it."
    jump a1_art

label a1_art:
    scene bg transition with fade
    pause 1.0
    play music piano1
    scene bg black with fade
    "I skip the next day or two of classes. It's too much effort to keep count exactly."
    "Sibyl brings food back to our dorm room for me even though I refuse to eat it when she's around. I don't want to see her compassionate smile while I'm sulking so hard."
    scene bg bedroom with dissolve
    "On the third day, I am awoken by the gentle sound of Sibyl's voice calling my name."
    S "Clover..."
    S "Clover... please wake up. It's time for breakfast. I'm not going to bring you anything today so you'll have to get up if you want to eat."
    show cpj scowl at mright with dd
    CPJ "No."
    "As my brain comes around to processing the shining light of day that streams in through the large windows, so too does it process Sibyl's words more clearly."
    show sibyl neutral at center with dd
    S @ neutral talk "I'm going to pull the sheets off again if you don't get up."
    CPJ @ shout "Do your worst."
    S frown talk "Okay, but you asked for this. Literally."
    scene bg bedroom with dd
    "Whoosh, off come the top sheets. I brace against the shock of the cold air but remain flopped resolutely on my bed."
    show sibyl neutral talk at center
    show cpj scowl at mright
    with dd
    S "Clover..."
    show sibyl neutral with dd
    CPJ annoyed "No."
    S contemplative "Hmmm."
    scene bg bedroom with dd
    "I believe for a moment that I've won against all odds, but then I feel cold fingers tighten around my ankles."
    show cpj annoyed at mright
    show sibyl smile at center
    with dd
    CPJ shout "What happened to leaving me alo—"
    S excited "{b}Hngg!{/b}"
    show cpj surprised
    show sibyl smile
    with dd
    "With one big tug, Sibyl pulls my legs right off the bed all the way up to my knees."
    S @ smile talk "Having a proper daily routine will help, I promise. You've had time to stew on what is bothering you, so now please get up and come to class."
    CPJ annoyed "Nuh-uh."
    S excited "{b}Hnng!{/b}"
    show cpj scowl
    show sibyl annoyed
    with dd
    "My hips leave the bed with another tremendous pull, leaving me hanging limp between where she holds my legs like a wheelbarrow and where my upper body rests on the bed."
    S laugh "One last chance, Clover. You're going to attend class today, aren't you?"
    C shout "N—"
    scene bg bedroom with dd
    S laugh "{b}Hnnnnnngggg!{/b}"
    scene bg cafeteria winter with fade
    "Sibyl and Tanya start chatting the moment they meet in the cafeteria, apparently about Sierra once again. I don't pay much attention, instead wandering off in search of French toast."
    "Just as I've gotten back to my seat and stuffed the first bite of fluffy bread into my mouth, Sibyl goes off to get her own food, leaving me alone with Tanya."
    show clover contemplative at mleft
    show tanya neutral at mright
    with dd
    C "(Awkward. Think she's still angry about the other day?)"
    show tanya scowl with dd
    "A quick glance while I've still got my fork in my mouth catches Tanya's eyes. All she does is give me a sharp, dismissive glare and return to her yogurt parfait."
    show tanya neutral with dd
    C impish "(Oh well, maybe I can make friends with Sierra instead. That'll really burn her behind.)"
    show sibyl smile at center
    show clover neutral
    with dd
    "When Sibyl returns, the two of them continue their lively chatting while I remain silent and stare down at the syrup remaining on the plate which formerly contained French toast."
    "While still replaying in my mind what I learned about licking plates in my first ever etiquette class, which was namely \"do not lick plates\", I manage to catch Sibyl calling my name."
    S @ neutral talk "Hello, Earth to Clover."
    C @ neutral talk "Huh? What is it?"
    S @ smile talk "I was just saying that we have art class today so you'll finally get to meet Miss Izzie."
    C @ frown talk "What's so special about her?"
    "I'm sure she must have a good reason to bring up the topic, but it's hard to be excited for something which I have no idea about in the first place."
    S @ neutral talk "I mentioned her briefly a few days ago. She's a popular teacher amongst the students. She's, well, pretty strange, but also fun."
    "I don't say anything in reply, instead rebelliously defying etiquette to lick the syrup off my plate. Sibyl continues her one-sided conversation without any further input from my end."
    S laugh "Maybe getting to work on something creative might snap you out of this funk too!"
    C @ neutral talk "I've never had a single artistic bone in my body."
    show sibyl contemplative with dd
    T @ neutral talk "Oh, just leave her be, Sibyl. If she wants to be miserable, let her be miserable without dragging {b}us{/b} down with her."
    "Tanya and I agree on something in an unlikely turn of events, but Sibyl remains adamant that going to art class will be good for me."
    scene bg artroom winter
    show izzie excited at qleft
    show clover surprised at qmleft
    show sibyl smile at qmright
    show tanya neutral at qright
    with fade
    who "So cute! And such beautiful hair too!"
    "I try desperately to duck out of some surprise head-patting foisted upon me by a smaller girl at the exact moment I enter the art room."
    show izzie smile talk with dd
    who "No wonder the HimeOuji twins couldn't keep their hands off of her! You'd better not wait too long, Miss Yang."
    T @ contemplative alt2 "I have no idea what you're talking about, Miss Izzie."
    C scowl "Umm... could you not?"
    show izzie excited with dd
    who "So {i}tsun{/i} too!"
    show izzie smile with dd
    C contemplative "(\"Soon?\" Was she expecting me later?)"
    "As I shift away from her overbearing fixation with patting my head, I begin to realize just how strange my current assailant really is. She's wearing what is sure to be a grave violation of the uniform code for starters."
    C tired "(This one is big trouble. I hope I don't have any other classes with her.)"
    show clover neutral with dd
    "Whatever is up with this oddity, I don't like it. She clearly knows who I am already, and is maybe in league with my two previous assailants as she clearly also has no issue with invading my personal space."
    S @ smile talk "Clover, this is—"
    mi @ excited "Miss Izzie!"
    "Striking a silly pose, she sticks a hand out to raise two fingers toward me like a peace sign."
    mi @ smile talk "I'm your art teacher!"
    C @ surprised "You're a {b}teacher{/b}!?"
    mi @ smile talk "Five years and counting!"
    "None of the other students seem to acknowledge anything odd as happening, and neither does Sibyl beside me, so I am forced to conclude this woman is in fact my art teacher."
    S @ neutral talk "I think that's enough, Miss Izzie. Clover has been... sick the past few days and is still recovering, so she needs to take things slow and have her space."
    "Now that Sibyl has helpfully dragged Miss Izzie back to a respectable student-teacher distance, I am able to better formulate my appraisal of my strange art teacher."
    "Her debasement of the uniform code makes sense now as she is obviously not bound to it, though I swear that she's wearing a uniform issue skirt."
    "I may have soured right away when she chose to get right up in my face, but in a way I actually respect how fearlessly she chooses to be different."
    C @ frown "(My old inclination toward non-conformity has resurfaced. Better push that back down, quickly.)"
    mi @ smile talk "So what's your medium, Clover?"
    C contemplative "(What a strange question to ask for an art teacher...)"
    show choice_darkness with dissolve
    menu:
        "\"I've done a few séances in the past...\"":
            hide choice_darkness with dissolve
            C "I've done a few séances in the past..."
            "I can still remember the huge smile on my friend's little brother's face when he was able to speak with their deceased pet hamster again."
            C tired "(That boy absolutely adored me. Until someone told him that séances are all fake.)"
        "\"My former classmate told me I was the state's foremost expert with Ouija boards.\"":
            hide choice_darkness with dissolve
            C "My former classmate told me I was the state's foremost expert with Ouija boards."
            "What I say is the total truth, except that she said it in a way less flattering manner."
            C impish "(The spirits were not very kind to her after that.)"
    show izzie contemplative
    show sibyl laugh
    show tanya frown
    show clover neutral
    with dd
    "From behind me there's a quiet snicker, and with a quick glance I'm both surprised and even a little hurt to find the sound originate from Sibyl rather than Tanya as I had expected."
    mi smile talk "No, no, I mean with regard to your creative pursuits! We have everything: clay, graphite, acrylics... I want to know how best to unleash your artistic passions!"
    C frown talk blush "O-Oh..."
    show izzie smile
    show clover frown blush
    show sibyl smile
    show tanya neutral
    with dd
    "I got so caught up thinking about my past self that I went and said something totally unnecessary and embarrassing about the old \"me\" that no one needed to know."
    mi excited "The freedom of creative expression is a salve for the soul!"
    mi smile talk "I know from experience how tough it can be transferring to a new school like this so I'd like to see you get started on your own project right away."
    show izzie smile with dd
    C neutral talk "Sorry, Miss Izzie, but I'm not much of an artist."
    show clover neutral with dd
    "Just as I'm getting geared up to fight off my teacher's idea of throwing me into some dumb art project, Sibyl unexpectedly comes to my rescue."
    S @ neutral talk "Miss Izzie? Could I have Clover sit with me while I get accustomed to the oil pastels again? I think my skills are rusty after the long break and she can learn from me while she considers what she wants to start with for herself."
    mi excited "Approved! You know where to find the pastel paper, Sibyl. Hop to it!"
    hide tanya
    hide izzie
    with dd
    "Tanya follows after Miss Izzie to speak further about something. I'm glad to have the latter's high energy presence kept away so I can regain control over my personal space, and the former too because I just don't like her."
    C @ neutral talk "Thanks for saving me, Sibyl."
    S @ smile talk "You're very welcome, but you will have to take on your own project when I'm finished, so try to pay attention."
    C @ frown talk "Urgh... alright. So what do I have to do for your portrait anyway?"
    S laugh "Just sit here and watch what I'm doing. If you have any questions, please ask!"
    "Sibyl pats at a nearby wooden stool with a cheerful grin plastered on her face, then sets up her work easel and paints to begin work."
    show sibyl neutral
    show clover contemplative blush
    with dd
    C "(She looks so serious when she's drawing.)"
    S @ neutral talk "The oil pastels are thick, so they can be layered like this... and then some of the top layer can be scraped off like..."
    "My roommate's striking blue eyes shift dramatically back and forth from her easel to me and back again, while at the same time her lips remain thin and pursed."
    "It's clear that she's concentrating hard even as she tries to explain certain techniques to me, like \"sgraffito\" and whatever she was doing with the bottle of turpentine."
    C scowl blush "(It's really unfair how pretty she is too.)"
    "I don't think I've ever felt as jealous about another girl as I do while staring back at Sibyl. I've wished to have been born with wavy hair all my life."
    S neutral talk "So, were you able to communicate with the spirits, Clover?"
    C surprised "W-What?"
    show sibyl smile with dd
    "Being so focused on Sibyl's face, I stumble for my thoughts when she suddenly drops her attention from the canvas to speak to me instead."
    S smile talk "...When you did all that medium stuff."
    S frown talk "Sorry, that's probably out of the blue, but you looked like you were on the verge of rigor mortis just now."
    show sibyl neutral with dd
    C tired blush "It was just some stupid little thing I did with my friends in middle school."
    "I try to save face by acting all casual and dismissive, but Sibyl doesn't seem to take the hint — or maybe refuses to."
    S laugh "Oh, is that so? It sounds fun either way."
    C neutral talk "Do you actually believe in the supernatural?"
    show clover neutral with dd
    "After trying so hard to put these juvenile interests from middle school behind me, to find someone like Sibyl interested, and in this Christian school of all places, is a definite surprise."
    S sleepy blush "There are many people who would be willing to go to great lengths to speak to the departed."
    S neutral talk "I know that it's all nothing but fluff, but even so it's still fun to think about. And I'm very open-minded in general, or so I like to think."
    show sibyl neutral with dd
    C contemplative "I just can't imagine that you or anyone else at a school like this would find the supernatural and macabre to be interesting. Everyone here seems so... formal and stuffy."
    C neutral "(Except Miss Izzie...)"
    S laugh "Do you really see me as that type of person, Clover? After covering for you skipping class for two days?"
    "It really is difficult to imagine Sibyl as someone serious and stuck up while watching her grin so brightly with a stripe of blue paint accidentally flecked across the tip of her nose."
    S smile talk "Clover, if you'd just shoo away those storm clouds you've built around your head, you might learn something surprising about me and everyone else here too."
    show sibyl smile with dd
    C annoyed "So this was all a little ploy to get me to open up, was it? Somewhere I can't make a scene?"
    show sibyl annoyed with dd
    "Sibyl's eyes turn from her canvas to look directly at me, stabbing her blue pearls into me not angrily, but with a clear rebuke of my changing tone. Her own expression remains stern but supportive."
    S frown talk "No, Clover. I'm not out to get you. No one here is."
    show sibyl frown with dd
    C neutral talk "It sure feels like it the way you keep trying to pry into my personal life."
    C tired "(And I'm pretty sure Tanya does have it out for me.)"
    S smile talk "Clover, I'm only trying to help you realize that you're not alone. Your world isn't ending, it has only expanded to include this academy and all of us in it."
    show sibyl smile with dd
    C annoyed "That's easy for you to say."
    show sibyl neutral with dd
    "Sibyl sighs softly and drops the discussion altogether to return to her work. She may quite possibly be trying to arrive at another route to get to me, so I think."
    C scowl "(I know plenty about Sibyl! Like how she's into art, likes strawberries, and... she has pretty blue eyes and her shampoo smells nice.)"
    "We both are quiet all the way through to the end of class when the bell rings to signal the migration to our next torturous lesson."
    play sound schoolbell
    C excited "(Finally!)"
    show clover neutral with dd
    "Despite still holding onto a bit of a grudge from our earlier talk, I cannot resist the invitation to see what Sibyl has been working so hard on this whole time that I've been ignoring her."
    S laugh "I call it \"The Birth of Clover\"!"
    show clover surprised blush with dd
    "It's a picture of me, obviously, but stark naked and covering up my lady bits with my arms. Not only that, but I appear to be bursting out of a four leaf clover."
    S smile talk "So? What do you think?"
    show sibyl smile with dd
    show choice_darkness with dissolve
    menu:
        "\"Why am I naked?\"":
            hide choice_darkness with dissolve
            C anxious blush "Why am I naked?"
            S @ laugh "It just felt \"right\", y'know?"
            C "No, I really don't."
            show izzie smile talk at qright with dd
            mi "It's {i}The Birth of Venus{/i} by Botticelli, but with Clover and her namesake. That's so clever, Sibyl!"
            show clover surprised with dd
            "I nearly jump through the ceiling when Miss Izzie shows up suddenly behind us unannounced."
            S @ smile talk "Exactly! I knew you would understand, Miss Izzie."
            hide izzie with dd
            "With another eerie glance between the faux nude drawing of me and the real thing, the strange teacher finally wanders off to attend to other students again."
            C frown talk "I still don't understand why you needed me to be naked."
            show clover frown with dd
            S neutral talk "The human form has long been a subject of artists' curiosity. It's okay if you don't quite get it yet."
        "\"It's a pun on my name.\"":
            hide choice_darkness with dissolve
            C annoyed "It's a pun on my name."
            show sibyl frown with dd
            "This is the kind of thing that's been done a billion times before and my disinterest is evident in the flat tone of voice."
            S @ frown talk "What's the matter, you don't like it?"
            C anxious "Not really. Everyone is always making puns on my name. How would you feel if I painted you like a Greek oracle or something?"
            S laugh "I think that would be lovely."
            C annoyed "Well don't get your hopes up. I'm bad at art, remember?"
    S laugh "I'll help you develop your sense of artistry in no time!"
    C tired "I've already warned you that it's an impossible task."
    S smile talk "I'm up to the challenge."
    "My heart sinks when I think about how long of a day it's going to be, and then drops all the way through the floor when I think about the whole rest of the year too."
    stop music fadeout 0.5
    jump home_ec

label home_ec:
    play music guitar2
    scene bg cafeteria winter with fade
    "Sibyl doesn't seem to be holding any grudge against me, as usual, but things are no less awkward between me and Tanya by the time lunch arrives."
    "She continues to pretty much ignore my existence altogether and instead holds onto Sibyl's attention near entirely with talk of their separate works of art in progress."
    show clover excited at center with dd
    C "(Ooh, ham cubes!)"
    "I inspect the contents of the salad bar a couple times, picking out the loudest, crunchiest vegetables to go with my ham and ranch dressing so that I don't have to hear Tanya talk."
    scene bg classroom winter with dissolve
    "To my surprise and great fortune, I find out later in Family and Consumer Sciences class that Tanya actually is not in every single one of our daily lessons."
    "Though most classes are common between everyone in our homeroom, some students have alternate class periods to suit their individual needs."
    show clover neutral at qmleft
    show sibyl neutral talk at qmright
    with dd
    S "Tanya was placed in an English as a Second Language class because she grew up speaking Chinese at home."
    "Sibyl is also quick to remind me that I would have known this already if I hadn't skipped so many days of class."
    S contemplative "I suppose they did not know she was already fluent in English when she enrolled."
    "I also think that Tanya's English is really, really good considering it's not her first language, but I am loath to compliment her out loud even when she is not around to hear the compliment."
    C @ neutral talk "It's nice to have a class without Tanya."
    S angry "Clover, don't be rude!"
    C surprised "W-Hwa!"
    "I jump sideways after feeling a firm thwack against my rear, and whip my head around to see Sibyl wielding her wooden spatula with a stern but playful grin."
    S neutral talk "You earned that smack. You really ought to be nicer to Tanya; she's very sweet."
    show sibyl neutral
    show clover annoyed
    with dd
    C "I'm not exactly feeling the love."
    S frown talk "What do you expect? You were mean to her!"
    S neutral talk "That's right, she told me about what happened in the aquarium."
    show sibyl neutral
    show clover neutral
    with dd
    "At that moment, our pot of water begins to bubble and I am thankful to have a change of subject."
    C @ neutral talk "Sibyl, we're ready for the spaghetti."
    S @ smile talk "Oh! Let me quickly weigh it out so we can calculate the calories for our worksheet."
    C smile "(It's easy {b}and{/b} we get to eat food. This class is the best.)"
    "Making food isn't the entirety of the class. We also have boring lessons like sewing and tax preparation too, which are far less enjoyable."
    S @ smile talk "Got it! Here we go!"
    "The spaghetti clatters into the pot, the boiling hot water slowly turning each stalk more translucent and less perfectly straight until they're all loose and wriggly in the water."
    show clover neutral with dd
    "The sight jogs something loose in my mind — some particular piece of unfinished business I've yet to attend to."
    C @ neutral talk "...Sibyl?"
    S @ neutral talk "What is it, Clover?"
    C @ neutral talk "Tell me more about the \"Royal Twins\", Vittoria and Vincenza."
    S @ frown talk "You want to know more about them and not me? Here I was hoping you'd finally opened up."
    C @ surprised "I-I'm not opening up, I just want to get revenge... or something."
    "I totally didn't mean to say the part about revenge out loud, but thankfully Sibyl remains as understanding as ever."
    S @ frown talk "Revenge? For what?"
    C annoyed blush "Those two twins kind of... sexually assaulted me when I first arrived."
    S angry "Did they now? They told me you were in a little tizzy when they gave you the key card to our room, but I should have figured they were the reason for it."
    S neutral talk "I don't condone their actions, of course, but there are quite a few girls here who would gladly have taken your place to be subject to their flirting."
    S smile talk "Instead of getting revenge, you should go talk to them earnestly and clear things up."
    C shout "It was way more than just a little unwanted flirting!"
    show clover neutral
    show sibyl neutral
    with dd
    "My outburst comes out a little too loud, leading me to quiet myself down before I start drawing more attention to myself, which is the last thing I want."
    S @ neutral talk "Okay, well, to begin with they're in the junior class, and my understanding is that they have had a huge following in the school ever since they arrived as freshmen."
    C deer "{b}Why?{/b}"
    "I interrupt just as Sibyl is getting started, still very irritated with how they treated me and only further angered to hear that it's a common thing for them to do to others."
    C scowl "(Not that I care about anyone else here, but I want to see them apologize to {b}me{/b} at least!)"
    S @ neutral talk "Some students really admire Vittoria's ladylike attitude, and others are drawn to Vincenza's playful behavior."
    C annoyed "(Ladylike? Is that what you call shoving your hand up someone else's skirt?)"
    S @ neutral talk "They're basically the prince and princess of the school. That's why they're called the \"Royal Twins\"."
    C contemplative "So they're not actually some sort of European royalty then?"
    S smile talk "No, but they are Italian. They are in the same ESL class as Tanya."
    show clover smile
    show sibyl neutral
    with dd
    "I am, for a moment, full of glee to imagine that Tanya is probably suffering the same fate as I did on my first day, every single class period she shares with those two devils."
    C anxious blush "Which one are you most a fan of then, Sibyl?"
    "I don't even know why I'm asking. Morbid curiosity I suppose."
    S @ neutral talk "I said it was common among students, not that I personally am in either of their sizeable fan clubs."
    "My plan to get revenge is starting to sound more and more problematic but I still want my payback for them jumping me before I even had the chance to step foot onto school grounds proper."
    C contemplative "(I could get a teacher involved, but that might be a little too much.)"
    C @ neutral talk "Sibyl, where is the student council located?"
    S smile talk "Are you going to visit? That's great!"
    S "Vittoria and Vincenza really are nice when you get past their eccentric personalities, Clover. They even helped look for you when you went missing."
    show sibyl smile with dd
    "I commit to memory Sibyl's detailed instructions on how to find the student council meeting room while stirring the tomato sauce in a separate sauce pan."
    S @ smile talk "Would you like me to come along with you?"
    show clover neutral with dd
    "Maybe she's expecting that I need more help or just hoping to get more information out of me, because Sibyl keeps talking even after I learn what I needed."
    C "(Why would I need her to come with me for this? This is my own personal revenge here.)"
    C @ neutral talk "No, I'm going alone after classes. You don't have to think about me at all."
    show sibyl frown talk with dd
    S "Maybe not, but I want to. You're my Vertu after all."
    show sibyl neutral with dd
    C frown "(There she goes again with the \"helpful roommate\" routine.)"
    "Something warm and wriggly stirs in my stomach, but the pot boiling over on the nearby burner draws my attention away from whatever is eating at me inside."
    stop music fadeout 0.5
    jump student_council

label student_council:
    scene bg black with fade
    play music piano2
    scene bg classroom winter with dissolve
    "I wind up scheming the whole rest of the day about what I'm going to tell the student council so that those twins get their just desserts."
    show clover contemplative at qmleft with dd
    C "(Maybe not expelled but, like, getting called to the principal over the PA system. That'll be sure to embarrass them.)"
    C surprised "Yow!"
    "My hand strays a little too close to an active bunsen burner for my nerves' liking. On instinct, I shove the slightly singed finger into my mouth to suck away the pain."
    show sibyl frown talk at qmright with dd
    S "Clover, honestly, you've had your head even deeper in the clouds than usual..."
    scene bg hallway with dissolve
    "I part ways with Sibyl at the end of the day's classes. She starts back deeper into the school building to go to her art club with Tanya while I make for the chamber where the student council meets."
    "Before she leaves, Sibyl asks once again whether I would like her to accompany me. Why she's so nervous about me going to the student council alone, I have no clue."
    show clover contemplative at center with dd
    C @ annoyed "(She probably wants to make sure I can't get anyone into trouble at all. She's too nice to let her special roommate do anything bad!)"
    "From outside the doorway to the meeting room muffled voices seep through the edges of the doorway, confirming to me that I've found the right room."
    C excited "Here we go!"
    "I knock at the door then push it open while the vim and vigor of son-to-be-satisfied revenge yet flows through me."
    play sound doorclose
    scene bg meeting winter
    show clover happy talk at left
    with dissolve
    C happy talk "Hello, Student Council. I have an important issue to bring to your attention."
    "Triumphantly I stand just through the entryway and announce my intentions. It's only when the entire student council turns their gaze my way that everything falls apart."
    C deer "(W-Wow... there's a lot of girls on the student council, huh...?)"
    "Nine of them. Eighteen eyes in total. All staring at the girl who just burst into the room like a total idiot."
    C bangs blush "I-I have a... c-complaint..."
    "All the fiery passion for getting revenge on the twins suddenly flies right out the window, replaced with a deathly pallor weighing down on me like a block of concrete."
    C tired "(This must be what Sibyl was concerned—)"
    "And then, before I even finish my thought, I notice {b}them{/b}. It's such a genuine surprise that I even raise my arm to point with dramatic fervor."
    C shout "{b}Y-You!{/b}"
    show twins smile talk at qright
    show clover scowl
    with dd
    H "Me!"
    O "Us!"
    show twins smile with dd
    "At the very head of the meeting table sit my two tormentors, gently taking turns sipping from their steaming tea cups with dignified amusement."
    C @ shout "What are {b}you{/b} both doing here?"
    st "Pardon me, but I believe that is a better question for you."
    "One of the other girls seated around the table politely asks why I just busted through their door, but I am still too laser focused on the evil twins sitting at the head of the table opposite me to answer."
    show twins smile talk with dd
    H "We can end today's session early. Vice President Vincenza and I will manage the remainder of the paperwork."
    st "President Vittoria?"
    C surprised "(Vice President!? {b}President!?{/b})"
    "There's a momentary glance between the twins before Vincenza leans toward the vocal member. She casually flits a finger through one side of her bangs while coolly looking into her face."
    O "Sorry, Kayleigh. I'll personally make it up to you later if that's alright?"
    hide twins
    hide clover
    with dd
    "The girl referred to as Kayleigh grows pink to the face and appears like she wants to object, but in the end everyone except the twins exits the room in short order."
    show clover scowl at left
    show vitti alt smile at qright
    show vinci alt smile at qmright
    with dd
    H @ alt smile talk "That was smooth, Vincenza."
    O @ alt smile talk "Izzie taught me that move."
    "All of my devious plans fly right out the window, leaving me staring down my immoral assailants directly as they quip to one another like I'm not even in the room."
    O @ smile talk "She sure knows how to make an entrance, that Clover."
    H @ smile talk "Quite on time too. I know she means well but I do wish Kayleigh would quit plying us with tea."
    play sound soda
    "From within Vincenza's bag appears a can of cola, which is quickly popped with a short hiss of escaping gases and passed between the pair of twins in turn."
    H @ alt neutral talk "Now then, I think we owe you an apology, Clover."
    "Though I remain infuriated by their presence, the absence of the crowd watching me revives my frozen self enough to converse clearly once again."
    C @ shout "You {b}think{/b}?"
    O @ alt neutral talk "Won't you please sit down, Clover?"
    show vitti alt smug
    hide clover
    with dd
    "Vincenza motions toward one of the recently vacated chairs nearby, while at the same time Vittoria grins and pats her lap from where she sits beside her twin."
    show clover scowl at qleft with dd
    "I opt to take a seat at the complete opposite end of the table, which is also a short dash away from the door. Should the need for a hasty escape present itself, this is my best chance of survival."
    show vinci alt contemplative
    show vitti alt vulnerable2
    with dd
    H "It is our understanding that you have had a troubled beginning to your education here at Prudence Preparatory Academy."
    O "We may be partially to blame for that. Therefore, we would like to apologize for any offense we may have paid to you."
    C surprised "(They are... apologizing!?)"
    "It's eerie the way in which they finish each others' thoughts. Not only that, but it's also freaky how they can merely look at one another to understand what both are thinking."
    C "(Is this for-real ESP!?)"
    "Rather than continue to contemplate their uniquely close relationship, the first words out of my mouth are far less philosophical."
    C scowl "How did two sexual... {b}criminals{/b} get elected to the student council!?"
    H alt smile talk "What an odd way to accept an apology, Vincenza."
    O alt smile talk "She's a most peculiar girl in every way, Vittoria."
    "Rather than respond to my outburst, the pair once again make show of their crazy back and forth dialogue that is addressed to one another but also clearly meant for me to hear."
    C annoyed "Are you going to answer me or keep talking to yourselves in that creepy way?"
    H alt contemplative2 "How did we attain these lofty positions you ask?"
    O smug "With my boyish charm..."
    show vinci alt smug
    show vitti smug
    with dd
    H "...And my feminine grace!"
    show vitti alt smug with dd
    C @ shout "Does the academy staff know about this? Do I need to go public? How many others have you victimized!?"
    O alt frown talk "Clover, {i}per favore{/i}, calm yourself."
    show vinci alt frown
    show clover shout
    with dd
    C "Calm down? You and your sister touched my... {b}everything{/b}!"
    show clover scowl
    show vitti alt frown talk
    with dd
    H "We helped you fix your ill-fitted uniform, nothing more."
    show vitti frown
    show clover impish
    with dd
    C "That's not going to hold up in court."
    show vitti alt frown
    show vinci alt frown
    with dd
    "I'm not really going to sue them but I'm also not above sneaking some fear into them that I might try."
    "I'm clear out of ideas of what to do to get my revenge now and that the twins themselves are not frightened in the slightest is taking all the wind out of my efforts."
    C annoyed "Just... promise you won't do it again, okay?"
    H alt neutral talk "We are sorry for having been too forward too quickly, Clover."
    O alt smile talk "We promise not to touch you until you ask for it."
    show vinci alt neutral
    show vitti alt smug
    show clover shout
    with dd
    C "I will {b}never{/b} \"ask for it\"!"
    C scowl "(There is something seriously wrong with these two's heads! Where's a brain doctor when you need one?)"
    "This isn't exactly how I expected my revenge to go. I spent all day plotting and scheming for what now feels only like a hollow victory. The twins are the ones taking me on a ride when it was I who wanted to crush them."  
    C annoyed "Okay, fine, I accept your apology. But if I catch you doing it again, I won't go so easy on you! I'm a lot more dangerous than I look!"
    show vinci alt awkward
    show vitti alt contemplative2
    show clover frown
    with dd
    "The twins share another glance amongst themselves but keep their lips shut this time. To my surprise, the blazing emotions inside me don't feel any less chilled now that I've taken some of my frustration out on these girls."
    "Getting these two out of my sight immediately and hopefully for the last time is my most immediate desire, but Vincenza stops me before I even get out of my seat."
    show vitti alt neutral
    show vinci alt neutral
    with dd
    O @ alt neutral talk "Clover, wait up a moment."
    "I'm rightfully annoyed by their continued behavior, that's for sure, but her tone doesn't seem confrontational so my curiosity wins out in the end."
    C @ frown talk "What is it now?"
    H @ alt neutral talk "There's something else we'd like to discuss."
    "For the life of me I cannot think about what these two would care to talk to me about which I haven't already received an apology for."
    "Then I remember how many classes I have already skipped in the short time I've been here, and that I had run into them after the curfew bell that first day too."
    C neutral talk "I think you owe me enough not to tell the teachers about how I skipped class."
    show clover neutral
    show vitti alt smile
    show vinci alt smile
    with dd
    "I start off the negotiations from a strong position at the table and am confident that I'll be out the door posthaste."
    H @ alt smile talk "It's not about that."
    C contemplative "It's not?"
    O @ alt smile talk "No, but we do expect you to properly attend your classes."
    "My mind races to come up with what else I could have possibly done to get in trouble, but I cannot land on anything conclusive before Vittoria speaks again to set the record."
    H @ alt smile talk "We know you've been struggling to adjust to your surroundings here and would like to help you."
    show clover smile
    show vitti alt neutral
    show vinci alt neutral
    with dd
    "I almost don't believe my ears. I even go so far as to chuckle at the comical statement before my attitude shifts right back to knife sharp."
    C annoyed "In the first place, I definitely don't want whatever \"help\" you think you can provide; secondly, I don't {b}need{/b} help; and thirdly, my life is none of your business."
    O @ alt contemplative "We thought you'd say that. Or rather, we were warned you would."
    C surprised "Who said that? Sibyl?"
    H @ alt contemplative2 "Your Vertu partner, Sibyl, may have mentioned how concerned she was about you."
    C scowl "Did she ask you to try to \"fix\" me or something?"
    H @ alt smile talk "She asked us only to quietly help smooth over your issues transitioning to academy life."
    O @ alt smile talk "It is touching how deeply she cares about you, Clover."
    "Vittoria nods sagely and adds onto the end a note about how wonderful of a Vertu partner she has been for me. I can only manage a scowl in response."
    C annoyed "I am not {b}struggling{/b} with anything."
    show vinci alt frown
    show vitti alt frown
    with dd
    "I say my piece with the utmost defiance even though I know fully well that I am indeed struggling with my entire life falling apart around me."
    "The twins blink back at me from across the table with deeply concerned looks of the type I did not expect they were capable of making."
    C anxious "Okay, fine, I've had some... stuff happening at home, but it's really not anyone's concern but mine."
    show vinci alt awkward
    show vitti alt contemplative2
    show clover frown
    with dd
    "The twins do that frustrating thing where they glance at one another in silence again, then turn back to me as if they just exchanged a whole conversation in that one glance."
    show vinci alt neutral
    show vitti alt neutral
    with dd
    H @ alt neutral talk "You have the attention of more than just Sibyl. Right now is your best opportunity to make a good impression with your classmates."
    C surprised "What do you mean?"
    C "(I'm pretty sure I can never talk to any of my classmates again after that introduction, so...)"
    O @ alt smile talk "Did you think a new transfer student coming to the school wouldn't draw interest?"
    C anxious "Well, no, but I'm just me. I don't even want to be the center of attention."
    H @ alt smile talk "You still have time to turn around your image. You could really play up being a transfer student."
    O @ alt neutral talk "You are absolutely perfect for the \"cool mysterious beauty\" type who could drive girls wild."
    C deer "What do you mean \"turn around my image\"?"
    C "(And why would I want to be \"driving girls wild\" anyway?)"
    show vinci alt awkward
    show vitti alt contemplative2
    show clover frown
    with dd
    "Once again the twins go silent to perform their creepy \"twin telepathy\". I'm just about to leave for good when they finally speak once more."
    show vinci alt frown
    show vitti alt frown
    with dd
    O @ alt frown talk "Clover, there's no easy way to say this so we're just going to tell you plain and simple."
    H @ alt frown talk "Your attitude is unpleasant. Everyone you've come into direct contact with has come away with major concerns or negative feelings about you."
    C scowl "So what? I don't want to be popular!"
    stop music fadeout 0.5
    O alt awkward "One student told us you were, quote: \"an unstable self-centered bitch\"."
    play music drama
    C @ shout "{b}Who said that!? Was it Tanya!?{/b}"
    show vinci alt smug
    show vitti alt smug
    with dd
    "The twins before me completely disregard my outburst in favor of sharing a quick smirk between them, which to me only confirms the theory."
    C "(I'll show {b}her{/b} \"unstable\"...!)"
    H @ alt neutral talk "Clover, all we want is to see you happy and thriving here at Prudence Prep."
    O @ alt neutral talk "It is the responsibility of the office of the presidency to look after the welfare of the students in our care."
    "Vittoria pleasantly reminds her sister that she's only vice president, which Vincenza merely brushes off with an indifferent dismissal of the difference in the roles altogether."
    C @ shout "Hmph. Why should I listen to the girls who molested me right after taking my first step through the gate?"
    O @ alt smile talk "I believe we already apologized for that incident."
    H @ alt smile talk "Let's not keep pretending you didn't enjoy it, Clover."
    C @ shout "{b}Enjoy{/b} it!?"
    H @ alt smile talk "It's okay to like it. Many girls here do."
    O @ alt neutral talk "{i}Sta' zitto, Vincenza, dovrà capirlo da sola.{/i}" # hush, Vincenza, she must come to terms with it on her own
    C @ shout "Don't start talking about me in Italian! I {b}know{/b} you're talking about me!"
    H @ alt smile talk "Clover, your anger is unwarranted. We only want to help make your transfer to the academy easier."
    C shout "I don't need help; there's nothing wrong with me! It's {b}everything else{/b} in my life that's all screwed up!"
    stop music fadeout 0.5
    jump introspection

label introspection:
    play music sad
    scene bg hallway with dissolve
    play sound doorslam
    "I storm out of the room with my passions ablaze, but quickly cool off as I'm left alone to wander the academy hallways without Vittoria and Vincenza's smirking faces in front of me."
    "The hollow emptiness of my now-resolved conflict with the twins lingers in the depths of my being, so I search the faces of the other students around me to refute what they had told me."
    "Most confirm my own suspicions that they are far too engaged with their own friends to notice me, but after passing a few more doors down the hallway, a pair of students do look my way in passing."
    show clover contemplative at center with dd
    C "(I think those two are in my homeroom.)"
    "My introduction was a spectacular failure so I had written off ever speaking to anyone from then on, but despite my worst fears the pair only seem to have glanced my way out of curiosity."
    "I whip my head around to semi-discreetly stare after the girls who had looked at me in the hallway. I find them whispering to themselves further down the hallway, but it doesn't strike me as especially conspiratorial."
    C tired "(Can I pull off \"cool\"? Probably not. \"Mysterious\"? Maybe. \"Beautiful\"? Sounds like a lot of work.)"
    hide clover with dd
    "Some part of me refuses to accept those two classmates were merely curious about me, and instead believe that they must have instead been secretly mocking me."
    "I would believe anything if it meant not having to admit that Vittoria and Vincenza may have been right about this one thing, and even more dangerously, right about everything else they said too."
    stop music fadeout 0.5
    scene bg bedroom with dissolve
    "It's a relief when I finally get back to my room, far away from any invasively inquisitive or potentially judgemental eyes."
    "To my surprise, a small cardboard box sits atop my desk. I slump my schoolbag onto the chair and creep over to it like it might explode in my face, or worse."
    show clover neutral at center with dd
    C "(\"Clover Ipswich\". It's for me. From...)"
    show clover anxiety with dd
    "A strange mixture of excitement and dread fills my stomach, like it's full of butterflies on fire madly flapping their wings to put each other out but only fanning the flames harder in the process."
    "I step over to my bed and flop onto it in a daze, but ultimately my body is hypnotically drawn right back to the box on the desk."
    show clover vulnerable at center with dd
    C "(Do Mom and Dad need me to sign some papers for their divorce? Is this box the sum of my inheritance after being entirely written out of their lives?)"
    hide clover with dd
    "Many terrible thoughts pass through my head, each one more awful than the last. I apprehensively trace the sharp edge of a pair of scissors around the tape holding the box flaps closed."
    "Sitting cross-legged on the bed with the package before me, I expel my hesitation with a deep breath then finally flip the cardboard flaps open."
    pause 0.5
    play music happy
    show clover happy talk at center with dd
    C "Abraxas!"
    show clover smile with dd
    "What greets me is a familiar goofy face which draws an equally goofy expression of my own."
    "First out of the box is a whole bundle of the picture frames I used to keep on the desk in my room. Topmost among them is a photo of my furry best friend back from when he was still a puppy."
    "The other frames behind it I also recognize but strategically choose to leave covered."
    C @ surprised "(It's a whole care package!)"
    "Beneath those surprises lie yet more wonders — a veritable treasure trove of my favorite things, from my choice in candy bars to a full set of sparkly glitter gel pens."
    "The last thing I pull out of the box I can smell before I even see what's wrapped up in the glass jar."
    C excited "(It can't be...)"
    "But as I unwrap it, yes, it is."
    C happy talk "Mom's famous peanut brittle! I don't believe it!"
    "I say it out loud to my empty room, it's that unbelievable. This particular treat is something she only makes around Thanksgiving."
    C smile blush "(She must have made it special for me.)"
    show clover tired with dd
    "I eagerly unwrap a little piece of the sugary wonderfulness and take a nibble out of it. The nostalgic tastes spreads across my tongue instantly, transporting me back home if only for a moment."
    show clover teary with dd
    "The second nibble is saltier, and more wet than the first. By the time I finish the little piece, the tears splash unceasingly onto my lap."
    "The colors of my room begin to smear and blend together, but a brush of the back of my hand against my eyes brings focus finally upon the folded letter waiting at the bottom of the box."
    show clover distraught with dd
    "Just that the little piece of peanut brittle fills my stomach with a new-found warmth, smothering the fires of anger and fear enough for me to read the note."
    "I fight back my tears through every word full of love and encouragement."
    stop music fadeout 0.5
    C distraught blush "(Mom... Dad...)"
    "I've always known deep down that my parents still love me, but seeing it written after unwrapping all the thoughtful gifts they've sent makes the weight of that love rest especially heavy in my chest."
    "They write nothing about the divorce that I know is still looming like the blade of a guillotine over my neck."
    "The letter merely contains only the same love and comfort I've always known, and which I've been terribly missing since I left home."
    "I begin re-reading again from the top, the tears picking up in volume out of my eyes as I read the words written in familiar script."
    hide clover with dd
    "I'm only through the first paragraph by the time my rampaging emotions overflow and I am forced to stuff my face into the pillow to muffle the wails of my bawling."
    scene bg bedroom night with fade
    play sound doorclose
    play music piano1
    "A soft clatter from across the room finally stirs my wet face from my pillow. With a sniffle to contain my ugly runny nose, I glance up at it."
    show sibyl contemplative at left with dd
    "Sibyl stands at the door, leaning back against it, her face politely turned away from staring at me. There are tiny paint flecks across her nose and cheeks, no doubt evidence of her club activities."
    show clover vulnerable blush at qmright with dd
    C "S-Sibyl..."
    S @ neutral talk "Would you like to be alone, Clover?"
    show clover tired with dd
    "My gaze turns down toward the ground as I judge the state of my being. I find it poor but with the strength of an intense cathartic release buoying my head above water."
    C vulnerable "No..."
    "Even so, my voice comes out shaky and quiet. I'm trembling all over, but I feel neither sad nor angry. It's a surprise to me that I want Sibyl to stay, but then again, maybe it shouldn't be."
    "I pick up the letter again, read a few of the lines written there, and somehow find my head clearer than it has been in recent memory."
    "\"Keep your head up and your heart open. Good things are sure to find their way in if you let them.\""
    "I do what Dad asks, raising my head to regard Sibyl across the room."
    C smile blush "No. I'm... going to be alright. You can stay."
    show sibyl smile at qmleft with dd
    "With an understanding smile that I've come expect from her, Sibyl sets down her bag and moves to sit on my bed across from me at a comfortable distance."
    S @ smile talk "What'cha got here?"
    "I can sense a little tentativeness in her actions like I'm some sort of wild animal eating seed out of her hand and she doesn't want to spook me."
    "For the first time, I find it more silly than annoying how careful she's being around me."
    C @ neutral talk "A care package."
    S @ smile talk "From your parents?"
    "I offer a little nod instead of vocalizing, and Sibyl responds with a pleasant exclamation which rings just as sweetly in my ears as the peanut brittle did in my mouth."
    S @ laugh "Would you like to show me?"
    "I distinctly feel as though she's treating me like a little kid, but presently allow it with consideration toward my delicate emotional state."
    C happy talk "It's a whole bunch of my favorite things."
    show clover smile with dd
    "Digging into the peanut brittle, I offer her a piece which she gladly accepts."
    S @ smile talk "It's delicious!"
    C "(Sibyl probably has no idea how much this peanut brittle means to me, but she also probably deserves a little bit for having put up with me the past few days.)"
    "That's right, I am all but forced to admit that Sibyl might have been right about those \"storm clouds\" and that I may have been a touch dramatic ever since I arrived at the academy."
    C "(All it takes is a little peanut brittle to remember I'm not out of my parents' hearts forever just because they suddenly sent me away.)"
    "None of this excuses what they've put me through so far, but after seeing all this I am unable to feel as hurt now as when they first kicked me out of our home to send me here."
    "Turning again to the photos, I pluck the photo of my beloved pet off the top of the stack to push toward Sibyl."
    C @ neutral talk "They sent some of my photo frames too. It feels like I haven't seen Abraxas in months even though I know it's only been a week or two."
    S neutral talk "What's a \"braxas\"?"
    show clover contemplative
    show sibyl neutral
    with dd
    "I'm rightly confused for a moment, an expression similarly shared by Sibyl, but when what she asked finally gets through my head I burst out into a lighthearted fit of laughter."
    show clover happy talk with dd
    S angry blush "D-Don't laugh at me! I don't know about everything!"
    show sibyl annoyed
    show clover happy talk
    with dd
    C "\"Abraxas\" is my dog. That's his name."
    show clover smile
    show sibyl smile
    with dd
    "It's only when I push the photo of Abraxas more firmly into her face that she finally understands."
    S @ laugh "He's cute! How did you come up with the name?"
    show clover tired blush with dd
    "My gaze shifts away from Sibyl's face as I feel the surge of warmth I know to be intense embarrassment rush to color my cheeks."
    C "(Head up. Heart open.)"
    C anxious blush "It's a word of mystic meaning in the system of the Gnostic Basilides applied to the {i}megas archōn{/i}, {i}princeps{/i} of the three hundred sixty five {i}ouranoi{/i}."
    show sibyl neutral with dd
    "I tell Sibyl all in the tiniest quiet voice I can manage, no matter how embarrassing it is to say it."
    show clover anxiety blush with dd
    "I wince after finishing the recitation, expecting raucous laughter out of Sibyl, but to my surprise she's merely curious about all the strange things I've just said aloud."
    S @ smile talk "Wow, I have no idea what any of that means but it's quite a mouthful. Where did you learn all that?"
    "The shame of the question weighs on me again. With sweat beginning to gather on my forehead, I draw my blonde hair across my face to hide in my traditional fashion."
    C bangs blush "I was pretty deep in an occult goth phase in middle school."
    S laugh "That explains this photo!"
    C surprised "(Wait, what?)"
    "I toss my hair away quickly to confirm what I most feared. In picking up the photo of Abraxas, I exposed to view the dangerous photo underneath."
    S smile "Wow..."
    C teary blush "(Oh no, here comes the mockery. I'll never be able to meet Sibyl's gaze again!)"
    S @ smile talk "You look so different with black hair! How old is this photo?"
    C surprised blush "H-Huh?"
    show sibyl smile with dd
    "Sibyl holds up the photo of me and my three friends decked out in the most embarrassing, all-black outfits we could possibly muster, each of us with pitch black hair to match."
    C anxious blush "O-Oh, well... I've been trying to grow it out naturally but my hair is actually carefully bleached and re-dyed from about here down."
    "Sibyl reaches out unbidden to twirl my hair through her fingers and tease the ends. I know she's looking for any telltale breakage, but if there's anything I'm an expert with by now, it's hair dye."
    S @ smile talk "Really? Your hair must grow super fast! It's so strong and smooth. I can barely tell it's dyed."
    C contemplative blush "(Well, duh, most of it is my real hair! I didn't swallow all those sketchy hair growth supplements for nothing!)"
    "Sibyl's attention to my hair is even more unbearably embarrassing than I could possibly have expected it to be, but actually feels really nice to have her play it with too."
    C tired blush "(This is not how I wanted to \"open my heart\", Dad!)"
    C anxious blush "You don't think I'm weird, Sibyl? For being into all this freakish occult stuff?"
    "Sibyl laughs shortly at my question, not with malice, but apparently at how absurd it is — and probably also at whatever pitiful expression I have plastered on my face."
    S laugh blush "Of course not, Clover. We've all done goofy things, haven't we?"
    "A soft flush emerges on Sibyl's cheeks despite her apparent reluctance to elaborate upon whatever she is presently remembering to herself."
    S smile talk "Besides, you shouldn't be afraid to show who you are. You might meet people who share the same interests too."
    show sibyl smile
    show clover frown talk
    with dd
    C "I understand what you're saying Sibyl, okay? But you have to {b}promise{/b} me you won't tell {b}anyone{/b} about this. I put all this stuff behind me for good when I started high school."
    show clover frown with dd
    "It's clear that Sibyl doesn't agree with my request, but she honors it anyway and motions once more to the photo."
    S @ neutral talk "Are these your friends?"
    C @ neutral talk "From middle school."
    S neutral talk "Not anymore?"
    show clover vulnerable
    show sibyl neutral
    with dd
    "The way I toss the photo aside should provide enough of an answer, but if I've already said this much a little more won't kill me."
    C @ anxious "Not anymore. We all quit the goth stuff shortly before we started high school and kind of went separate ways."
    "Two of my friends got boyfriends, the third made softball her entire life, and I just stayed... me."
    S @ frown talk "I'm so sorry, Clover. You four of you look like you had a lot of fun together."
    "A quiver of a sob threatens to burst up through my chest but ultimately dies there before being born into the cruel world."
    "It's fully a surprise because I've long since written off all three of them from my life ever since we went our separate ways, but nostalgia, it seems, almost gets the best of me this time."
    C frown talk "We did. Honestly, it was... kind of hard, starting high school like that, with no friends, and no place to belong. And even when I got home, things were still kinda rough..."
    C tired "(Oh gosh, what am I saying? I didn't mean to \"open my heart\" this much! Make it stop!)"
    show clover frown
    show sibyl neutral talk
    with dd
    S "That's one of the reasons I wanted to come to Prudence Prep, Clover. The Vertu system ensures we're never alone and always have a supportive environment to fall back on when we need it."
    show sibyl smile with dd
    "It might not have been a big thing to Sibyl, but what she says leaves me dazed. All at once I realize what I fool I've been."
    C tired "(Of course... I'm such an idiot.)"
    show sibyl frown with dd
    "Not hearing me reply, Sibyl stops to look back at me in concern, whispering my name with uncertainty."
    S @ frown talk "Clover...?"
    C "(Mom, Dad, I'm so sorry.)"
    "For weeks I've felt that being sent here to the academy must be some kind of cruel punishment, if not just plain old abandonment. Now I realize just how wrong I have been all this time."
    C teary "(Being sent here was for {b}my{/b} benefit.)"
    "My parents surely miss me just as much as I miss them, but between my troubles fitting in at school and the complex home life caused by their divorce—"
    C distraught "(They just wanted me to be happy. That's all they've ever wanted for me.)"
    "Tears start rolling down my cheeks thicker than a monsoon. Sibyl worriedly calls out my name again so I reach out to touch her arm and calm her concern."
    stop music fadeout 0.5
    C teary "I'm sorry, I just... need a moment to process some things, like, in my head."
    S frown talk "Of course, Clover. Take all the time you need."
    jump sibyl_talk
