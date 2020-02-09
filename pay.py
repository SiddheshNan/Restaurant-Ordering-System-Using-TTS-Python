import ws
import serial
import time
import textToSpeech
tts = textToSpeech.TextToSpeech()
ws = ws.Sockets()


class Payment:

    def cashPay(self, total):
        sayThing = "Please pay your Bill which is Rupees " + \
            str(total) + " and Collect Your Order from the Window, 3 steps left to the Counter. Enjoy Your Meal, Thank You"
        print(sayThing)
        tts.speak(sayThing)

    def cardPay(self, total):
        ws.send(
            '{"userText":"Please Tap your Card on the Tag Right to the Keyboard"}')
        ws.send('{"userText":"show"}')
        print("Please Tap your Card on the Tag Right to the Keyboard")
        tts.speak("Please Tap your Card on the Tag Right to the Keyboard")
        data = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
        x = data.read(12).decode()
        x = str(x)
        if x == "400031E720B6":
            ws.send(
                '{"userText":"Payment Successful! Thank You For Payment User ABC, Enjoy Your Meal, Thank You"}')
            ws.send('{"userText":"show"}')
            ws.send('{"text2":"Card No - '+x+'"}')
            print("\nCard No - ", x, "\n")
            print(
                "Payment Successful! Thank You For Payment User ABC, Enjoy Your Meal, Thank You", "\n")
            tts.speak(
                "Payment Successful! Thank You For Payment User ABC, Enjoy Your Meal, Thank You")
            data.close()
            return x + " | User : ABC"

        elif x == "40002E16D8A0":
            ws.send(
                '{"userText":"Payment Successful! Thank You For Payment User XYZ, Enjoy Your Meal, Thank You"}')
            ws.send('{"userText":"show"}')
            ws.send('{"text2":"Card No - '+x+'"}')
            print("\nCard No - ", x, "\n")
            print(
                "Payment Successful! Thank You For Payment User XYZ, Enjoy Your Meal, Thank You", "\n")
            tts.speak(
                "Payment Successful! Thank You For Payment User XYZ, Enjoy Your Meal, Thank You")
            data.close()
            return x + " | User : XYZ"

        else:
            print("Card Not Recognized..")
            tts.speak("Card Not Recognized")
            print(" \n")
            data.close()
            return "Card Not Recognized | User : N/A"
