define bot = Character("KIUBot")
image startingPage = im.Scale("startingPage.jpg", 1920, 1080)
image Intro2 = im.Scale("Intro2.jpg", 1920, 1080)
image spirale_fibonacci = im.Scale("spirale_fibonacci.jpg", 1920, 1080)
image pineapplefibonacci = im.Scale("pineapplefibonacci.jpg", 1920, 1080)
image Fibonacci1 = im.Scale("Fibonacci1.jpg", 1920, 1080)
image Fibonacci_Nature = im.Scale("Fibonacci_Nature.jfif", 1920, 1080)
image PetalsFibonnaci = im.Scale("PetalsFibonnaci.jfif", 1920, 1080)
image Fibonacci2 = im.Scale("Fibonacci2.jfif", 1920, 1080)
image Fractal1 = im.Scale("Fractal1.jfif", 1920, 1080)
image Fractal2 = im.Scale("Fractal2.jpg", 1920, 1080)
image Fractal3 = im.Scale("Fractal3.jpg", 1920, 1080)
image intro3 = im.Scale("intro3.jpg", 1920, 1080)
image circles = im.Scale("circles.png", 1920, 1080)
image wood = im.Scale("wood.jpg", 1920, 1080)
image pond = im.Scale("pond.jpg", 1920, 1080)
image graph = im.Scale("graph.png", 1920, 1080)
image soundWaves = im.Scale("soundWaves.jpg", 1920, 1080)
image chord = im.Scale("chord.png", 1920, 1080)
image universe = im.Scale("universe.jpg", 1920, 1080)
image ss = "splashscreen.jpg"




label start:

    scene black
    "....."
    show study at truecenter:
        zoom 0.3

    "A Wild robot appears!"

    voice "audio/beeps.mp3"
    hide study

    show genki at truecenter:
        zoom 0.3

    bot "00101101 01001010 11010100 10010010 11001101"

    stop sound
    "You don't seem to understand what is he saying."

    play sound "audio/beeps.mp3"

    hide genki

    show question at truecenter:
        zoom 0.3

    bot "67616d61726a6f62612c206765736d6973206368656d693f"
    stop sound

    "You start to get confused."

    "{i}Initializing autoTranslator..{/i}"


    bot "Hello? Can you hear me now?"

    hide question

    show genki at truecenter:
        zoom 0.3
    stop sound
    bot "Lovely! Hello there! I am KIUBot. I'll be your companion for today!"
    label query:

        stop sound

        bot "So, shall we get started?"

menu:
    "Yes, let's start!":

        jump partfirst

    "No, not ready yet.":

        label loop:
            stop sound
    
            bot "Okay! I'll wait for you..."

            bot "...."

            jump query
label partfirst:
    scene startingPage with dissolve
    stop sound
    show genki at right:
        zoom 0.3
    bot "Alright! I promise you, that after finishing this game you will have a proper idea of how the universe is so good at math."
    
    hide genki
    stop sound
    show question at right:
        zoom 0.3
    bot "You may wonder, universe? Math? How are those two connected to each other?"
    
    hide question
    stop sound
    show genki at right:
        zoom 0.3
    bot "Let me walk you through this magnificent world, full of mathematics..."
    scene Intro2 with dissolve
    hide genki
    stop sound
    show loveeye at right:
        zoom 0.3
    bot "Have you ever stopped to look around and notice all the amazing shapes and patterns we see in the environment around us?"
    stop sound
    bot "Mathematics form the building blocks of the natural world, which can be seen in stunning ways."
    stop sound
    hide loveeye
    show study at right:
        zoom 0.3
    bot "Here are a few of my favourite examples of math in nature:"
    stop sound
    scene Fibonacci1 with dissolve
    hide study
    show conf at right:
        zoom 0.3
    bot "You may be concerned and ask yourself: \"Should I be seeing math here?\""
    stop sound
    hide conf
    show genki at right:
        zoom 0.3
    bot "Answer is simple: Yes. Have you ever heard Of \"The Fibonnaci Sequence?\""
    scene Fibonacci2 with dissolve
    hide genki
    stop sound
    show study at right:
        zoom 0.3
    bot "Based on Fibonacchi's \"rabbit problem\", this sequence begins with the numbers 1 and 1, and then each subsequent number is found by adding the two previous numbers."
    stop sound
    bot "Therefore, after 1 and 1, the next number is 2 (1+1). The next number is 3 (1+2) and then 5 (2+3) and so on."
    hide study
    stop sound
    show genki at right:
        zoom 0.3
    bot "What's remarkable is that the numbers in the sequence are often seen in around us, for example:"
    stop sound
    scene pineapplefibonacci with dissolve
    show study at right:
        zoom 0.3
    bot "Pineapples"
    scene PetalsFibonnaci with dissolve
    hide study
    stop sound
    show study at right:
        zoom 0.3
    bot "Number of petals on a flower"
    hide genki
    show study at right:
        zoom 0.3
    scene spirale_fibonacci with dissolve
    stop sound
    show study at right:
        zoom 0.3
    bot "The numbers in this sequence also form a unique shape known as the \"Fibonacci spiral\""
    scene Fibonacci_Nature with dissolve
    show study at right:
        zoom 0.3
    hide study
    stop sound
    show genki at right:
        zoom 0.3
    bot "Which again, we see in nature in the form of shells, the shape of hurricanes and etc."    
    stop sound
    hide genki
    show study at right:
        zoom 0.3
    scene Fractal1
    show study at right:
        zoom 0.3
    bot "Fractals are another intriguing mathematical shape that we see in the outside world. A fractal is a repetitive shape,"
    stop sound
    bot "meaning that the same basic shape is seen again and again in the shape itself."
    stop sound
    hide study
    show genki at right:
        zoom 0.3
    bot "In other words, if you were to zoom in or out, the same shape is seen throughout."
    stop sound
    hide genki
    show loveeye at right:
        zoom 0.3
    bot "Fractals make up many aspects of our world, such as:"
    stop sound
    hide loveeye
    show genki at right:
        zoom 0.3
    scene Fractal2 with dissolve
    show genki at right:
        zoom 0.3
    bot "The leaves of ferns"
    stop sound
    scene Fractal3 with dissolve
    show genki at right:
        zoom 0.3
    bot "and tree branches"
    stop sound
    scene intro3 with dissolve
    show loveeye at right:
        zoom 0.3
    bot "Let's have a look at some more amusing representatives, that can be seen throughout our very own universe"
    hide loveeye
    scene circles with dissolve
    show study at right:
        zoom 0.3
    stop sound
    bot "Another common shape in nature is a set of concentric circles, in other words, this circles are all different sizes, one inside the other"
    hide study
    scene wood with dissolve
    show loveeye at right: 
        zoom 0.3
    stop sound
    bot "This must look familiar..."
    scene pond with dissolve
    hide loveeye
    show conf at right:
        zoom 0.3
    stop sound
    bot "Ripples of a pond when something hits the surface of the water..."
    hide conf
    show genki at right:
        zoom 0.3
    stop sound
    bot "Now you can brag with your friends with word \"concentric\" everytime you see a pond or any water surface!"
    hide genki
    show conf at right:
        zoom 0.3
    stop sound
    bot "Oops, this should not be here. This material is meant to be covered in the next chapters of this game.."
    hide conf
    scene graph with dissolve
    show loveeye at right:
        zoom 0.3
    stop sound
    bot "But this is interesting..."
    hide loveeye
    show genki at right:
        zoom 0.3
    stop sound
    bot "Fasten your seatbelts!"
    hide genki
    show study at right:
        zoom 0.3
    stop sound
    bot "I'm about to tell you something unusual..."
    hide study
    scene soundWaves with dissolve
    show genki at right:
        zoom 0.3
    stop sound
    bot "Math and music are connected... "
    hide genki
    show study at right:
        zoom 0.3
    stop sound
    bot "Not only music, every sound that you hear can be translated into mathematical formulas!"
    stop sound
    bot "Music involves creating patterns of sound, whereas mathematics is the study of patterns."
    hide study
    scene chord with dissolve
    show loveeye at right:
        zoom 0.3
    stop sound
    bot "Research has found out that popular pieces of music have definite mathematical structures that are less evident in others."
    hide loveeye
    show genki at right:
        zoom 0.3
    stop sound
    bot "We will later explain how trigonometry and sounds, that we hear everyday, can be connected and be forming musical chords.."
    hide genki
    scene universe with dissolve
    show sad at center:
        zoom 0.5
        yalign 0.5

    bot "But for now, I think we have to say good-bye and wish each other good luck exploring this wonderfull world of mathematics"
    stop sound
    "{i}Disabling Auto-translator...{/i}"    
    play sound "audio/beeps.mp3"
    bot "01101001 00100000 01101100 01101111 01110110 01100101 00100000 01111001 01101111 01110101"
    stop sound
return