import items
import textToSpeech
import ws
import json
foods = items.food()
tts = textToSpeech.TextToSpeech()
burgers = items.Burgers()
shakes = items.Shakes()
combos = items.Combos()
ws = ws.Sockets()


def getFood():
    count = 1
    food2 = []
    ws.send('{"chargeBlock":"hide"}')
    ws.send('{"userText":"hide"}')
    ws.send('{"img":"show"}')
    for i in foods:
        say = 'Press ' + str(count) + ' for ' + i
        food2.append(say)
        count += 1
    ws.send('{"text2":' + str(json.dumps(food2))+'}')
    for i in food2:
        print(i + '\n')
        tts.speak(i)
    return count - 1


def getBurgers():
    count = 1
    berg = []
    berg2 = []
    ws.send('{"text2":"Burgers Selected"}')
    print("burgers selected\n")
    tts.speak("burgers selected")
    for burger in burgers.burgers:
        say = 'Press ' + str(count) + ' for ' + \
            burger.thing + ' burger , Rupees ' + burger.rs
        berg.append(say)
        berg2.append(say)
        count = count + 1

    berg.append("Press "+str(len(berg)+1)+" for Main Menu")
    berg.append("Press "+str(len(berg)+1)+" for Checkout")

    ws.send('{"chargeBlock":"hide"}')
    ws.send('{"userText":' + str(json.dumps(berg))+'}')
    ws.send('{"userText":"show"}')
    ws.send('{"img":"hide"}')
    ws.send('{"text1":"Burgers"}')
    ws.send('{"text2":"Please Select Burgers"}')

    for ber in berg2:
        print(ber + '\n')
        tts.speak(ber)

    return count - 1


def getShakes():
    count = 1
    shak = []
    shak2 = []
    ws.send('{"text2":"Shakes Selected"}')
    print("shakes selected\n")
    tts.speak("shakes selected")
    for shake in shakes.shakes:
        say = 'Press ' + str(count) + ' for ' + \
            shake.thing + ' , Rupees ' + shake.rs
        shak.append(say)
        shak2.append(say)
        count = count + 1

    shak.append("Press "+str(len(shak)+1)+" for Main Menu")
    shak.append("Press "+str(len(shak)+1)+" for Checkout")

    ws.send('{"chargeBlock":"hide"}')
    ws.send('{"userText":' + str(json.dumps(shak))+'}')
    ws.send('{"userText":"show"}')
    ws.send('{"img":"hide"}')
    ws.send('{"text1":"Shakes"}')
    ws.send('{"text2":"Please Select Shakes"}')

    for sha in shak2:
        print(sha + '\n')
        tts.speak(sha)
    return count - 1


def getCombos():
    count = 1
    comb = []
    comb2 = []
    ws.send('{"text2":"Combos Selected"}')
    print("combos selected\n")
    tts.speak("combos selected")
    for combo in combos.combos:
        say = 'Press ' + str(count) + ' for ' + \
            combo.thing + ' combo , Rupees ' + combo.rs
        comb.append(say)
        comb2.append(say)
        count = count + 1

    comb.append("Press "+str(len(comb)+1)+" for Main Menu")
    comb.append("Press "+str(len(comb)+1)+" for Checkout")

    ws.send('{"chargeBlock":"hide"}')
    ws.send('{"userText":' + str(json.dumps(comb))+'}')
    ws.send('{"userText":"show"}')
    ws.send('{"img":"hide"}')
    ws.send('{"text1":"Combos"}')
    ws.send('{"text2":"Please Select Combo"}')

    for com in comb2:
        print(com + '\n')
        tts.speak(com)
    return count - 1


def getEnd(indx):
    say = 'Press ' + str(indx + 1) + ' for Main Menu'
    print(say + '\n')
    tts.speak(say)
    say = 'Press ' + str(indx + 2) + ' for Checkout'
    print(say + '\n')
    tts.speak(say)
    return indx + 2
