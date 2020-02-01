import items
import textToSpeech
foods = items.food()
tts = textToSpeech.TextToSpeech()
burgers = items.Burgers()
shakes= items.Shakes()
combos = items.Combos()

def getFood():
    count = 1
    for i in foods:
        say = 'Press ' + str(count) + ' for ' + i
        print(say + '\n')
        tts.speak(say)
        count +=1
    return count - 1

def getBurgers():
    count = 1
    print("burgers selected\n")
    tts.speak("burgers selected")
    for burger in burgers.burgers:
        say =  'Press '+ str(count) + ' for '+ burger.thing + ' burger , Rupees ' + burger.rs
        print(say + '\n')
        tts.speak(say)
        count = count + 1
    return count - 1

def getShakes():
    count = 1
    print("shakes selected\n")
    tts.speak("shakes selected")
    for shake in shakes.shakes:
        say =  'Press '+ str(count) + ' for '+ shake.thing + ' , Rupees ' + shake.rs
        print(say + '\n')
        tts.speak(say)
        count = count + 1
    return count - 1

def getCombos():
    count = 1
    print("combos selected\n")
    tts.speak("combos selected")
    for combo in combos.combos:
        say =  'Press '+ str(count) + ' for '+ combo.thing + ' combo , Rupees ' + combo.rs
        print(say + '\n')
        tts.speak(say)
        count = count + 1
    return count - 1

def getEnd(indx):
    say =  'Press '+ str(indx + 1) + ' for Main Menu'
    print(say + '\n')
    tts.speak(say)
    say =  'Press '+ str(indx + 2) + ' for Checkout'
    print(say + '\n')
    tts.speak(say)
    return indx + 2

