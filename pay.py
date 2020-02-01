import textToSpeech
tts = textToSpeech.TextToSpeech()
import time
import serial

class Payment:

    def cashPay(self, total):
        sayThing = "Please pay your Bill which is Rupees " + str(total) + " and Collect Your Order from the Window, 3 steps left to the Counter. Enjoy Your Meal, Thank You"
        print(sayThing)
        tts.speak(sayThing)


    def cardPay(self, total):
        print("Place the card")
        tts.speak("Place the card")
        data = serial.Serial(port='/dev/ttyUSB0',baudrate = 9600)
        x = data.read(12).decode()
        x = str(x)
        if x=="400031E720B6":
            print("Card No - ",x,"\n")
            print("Thank You For Payment User ABC","\n")
            tts.speak("Thank You For Payment User ABC")
            data.close()
            return x + " User : ABC"
         
        elif x=="40002E16D8A0":
            print("Card No - ",x,"\n")
            print("Thank You For Payment User XYZ","\n")
            tts.speak("Thank You For Payment User XYZ")
            data.close()
            return x + " User : XYZ"

        else:
            print("Card Not Recognized..")
            tts.speak("Card Not Recognized")
            print(" \n")
            data.close()
            return "Card Not Recognized User : Nit"

            


