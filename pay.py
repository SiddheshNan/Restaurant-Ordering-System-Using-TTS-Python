import textToSpeech
tts = textToSpeech.TextToSpeech()

class Payment:

    def cashPay(self, total):
        sayThing = "Please pay your Bill which is Rupees " + str(total) + " and Collect Your Order from the Window, 3 steps left to the Counter. Enjoy Your Meal, Thank You"
        print(sayThing)
        tts.speak(sayThing)


    def cardPay(self, total):
        sayThing = "under construction"
        print(sayThing)
        tts.speak(sayThing)

