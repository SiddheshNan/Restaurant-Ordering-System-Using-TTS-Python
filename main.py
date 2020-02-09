import textToSpeech
import menu
import cart
import items
import food
import pay
import datetime
import os
import ws
import json
import threading
import browser.server2 as bw
import time
# start tornado ws server
t = threading.Thread(target=bw.startServ, name='start tornado ws')
t.daemon = True
t.start()
##
tts = textToSpeech.TextToSpeech()
menu = menu.MenuOptions()
carts = cart.Cart()
pay = pay.Payment()
#time.sleep(2)
ws = ws.Sockets()
##


def checkout():

    ws.send('{"text1":"Checkout"}')
    ws.send('{"chargeBlock":"hide"}')
    ws.send('{"text2":"Your Order is as Follows"}')
    ws.send('{"userText":"hide"}')
    ws.send('{"img":"hide"}')

    print(menu.orderis)
    tts.speak(menu.orderis)

    ordr = []

    total = 0
    for ele in range(0, len(carts.rs)):
        total = total + int(carts.rs[ele])

    if total == 0:
        ws.send(
            '{"userText":"There is nothing in the cart, Please Order somthing and then checkout, Going to main menu"}')
        ws.send('{"userText":"show"}')
        return
    else:
        ws.send('{"charge":"'+str(total)+'"}')
        ws.send('{"chargeBlock":"show"}')

    for i in carts.burger:
        ordr.append(i + " burger")
    for i in carts.shakes:
        ordr.append(i)
    for i in carts.combos:
        ordr.append(i + " combo")

    ws.send('{"userText":' + str(json.dumps(ordr))+'}')
    ws.send('{"userText":"show"}')

    if carts.burger != []:
        print(menu.burgersare)
        tts.speak(menu.burgersare)
        for i in carts.burger:
            print(i, "burgur")
            tts.speak(i + "burgur")
    else:
        print(menu.noburgers)
        tts.speak(menu.noburgers)

    if carts.shakes != []:
        print(menu.shakesare)
        tts.speak(menu.shakesare)
        for i in carts.shakes:
            print(i)
            tts.speak(i)
    else:
        print(menu.noshakes)
        tts.speak(menu.noshakes)

    if carts.combos != []:
        print(menu.combosare)
        tts.speak(menu.combosare)
        for i in carts.combos:
            print(i, "combos")
            tts.speak(i+"combos")
    else:
        print(menu.nocombos)
        tts.speak(menu.nocombos)

    total = 0
    for ele in range(0, len(carts.rs)):
        total = total + int(carts.rs[ele])

    if total == 0:
        print("There is nothing in the cart, Please Order somthing and then checkout, Going to main menu")
        tts.speak(
            "There is nothing in the cart, Please Order somthing and then checkout, Going to main menu")
        return
    else:
        print("total rupees are", total)
        tts.speak("total rupees are" + str(total))

    ws.send('{"text2":"Press 1 to select payment methods, press 0 to cancel"}')
    print("Press 1 to select payment methods, press 0 to cancel")
    tts.speak("Press 1 to select payment methods, press 0 to cancel")

    sel = input("Please enter an option: ")


# Payment Screen
    if sel == '1':
        sayThing = "Please Select Suitable Payment Method, Press 1 For Cash Payment, Press 2 for Card Payment, Press 0 to Cancel"
        ws.send('{"text1":"Checkout"}')
        ws.send('{"text2":"Payment Screen"}')
        ws.send('{"userText":"'+sayThing+'"}')
        ws.send('{"userText":"show"}')
        ws.send('{"chargeBlock":"show"}')
        print(sayThing)
        tts.speak(sayThing)
        sel = input("Please enter an option: ")

        if sel == '1':
            ws.send('{"text1":"Checkout"}')
            ws.send('{"text2":"Selected: Cash Payment"}')
            ws.send('{"userText":"Please pay your Bill which is Rupees ' + str(total) +
                    ' and Collect Your Order from the Window, 3 steps left to the Counter. Enjoy Your Meal, Thank You"}')
            ws.send('{"userText":"show"}')
            ws.send('{"chargeBlock":"show"}')
            pay.cashPay(total)
            addTextToFile("Cash")
            clearCart()
        elif sel == '2':
            ws.send('{"text1":"Checkout"}')
            ws.send('{"text2":"Selected: Card Payment"}')
            card_no = pay.cardPay(total)
            addTextToFile("Card | " + card_no)
            clearCart()
        else:
            sayThing = "Canceling Order, Going to main menu"
            print(sayThing)
            tts.speak(sayThing)
            clearCart()
            pass

    else:
        sayThing = "Canceling Order, Going to main menu"
        print(sayThing)
        tts.speak(sayThing)
        clearCart()
        pass


def clearCart():
    print("Clearing Cart")
    carts.burger.clear()
    carts.shakes.clear()
    carts.combos.clear()
    carts.rs.clear()


def addTextToFile(paym):
    time = datetime.datetime.now()
    orderText = "New Order at " + str(time) + " For :"

    if carts.burger != []:
        for i in carts.burger:
            orderText = orderText + " | Burger: " + i + " | "

    if carts.shakes != []:
        for i in carts.shakes:
            orderText = orderText + " | Shakes: " + i + " | "

    if carts.combos != []:
        for i in carts.combos:
            orderText = orderText + " | Combos: " + i + " | "

    total = 0
    for ele in range(0, len(carts.rs)):
        total = total + int(carts.rs[ele])

    orderText = orderText + " | Total Rs: " + \
        str(total) + " | Payment Method : " + paym + " \n"

    f = open("OrderLists.txt", "a+")
    f.write(orderText)
    f.close()
    print("Added Text to File")


def clss():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    while True:
        clss()
        ws.send('{"text1":"'+menu.AnyKey+'"}')
        ws.send('{"text2":""}')
        ws.send('{"userText":"hide"}')
        ws.send('{"img":"hide"}')
        ws.send('{"chargeBlock":"hide"}')

        tts.speak(menu.AnyKey)
        inp = input(menu.AnyKey + "\n")
        if inp != '':
            ws.send('{"text1":"'+menu.WelcomeText+'"}')
            print(menu.WelcomeText + '\n')
            tts.speak(menu.WelcomeText)
            food.getFood()

            inp = input("Enter the selection : ")

            if inp == '1':
                foodIndex = food.getEnd(food.getBurgers())
                sel = input("Enter the selection : ")
                selection = int(sel)

                if selection in range(1, foodIndex-1):  # push thing to arry only
                    selection = selection-1
                    burger = items.Burgers().burgers[selection].thing
                    rs = items.Burgers().burgers[selection].rs
                    carts.burger.append(burger)
                    carts.rs.append(rs)

                    ws.send('{"text1":"Order Selection"}')
                    ws.send(
                        '{"text2":"Press 1 for Checkout OR Press 2 to go to main menu and add more items to cart"}')

                    ws.send('{"userText":" Selected '+burger +
                            ' burger for Rupees ' + str(rs)+'"}')

                    ws.send('{"img":"hide"}')
                    ws.send('{"userText":"show"}')

                    print("Selected " + burger +
                          " burger for Rupees " + str(rs))
                    print(
                        "Press 1 for Checkout OR Press 2 to go to main menu and add more items to cart")
                    tts.speak("Selected " + burger +
                              " burger for Rupees " + str(rs))
                    tts.speak(
                        "Press 1 for Checkout OR Press 2 to go to main menu and add more items to cart")
                    sel = input("Enter the selection : ")
                    sel = int(sel)

                    if sel == 1:
                        ws.send('{"text1":"'+menu.goingCheck+'"}')
                        ws.send('{"text2":""}')
                        ws.send('{"img":"hide"}')
                        ws.send('{"userText":"hide"}')
                        print(menu.goingCheck)
                        tts.speak(menu.goingCheck)
                        checkout()
                    else:
                        ws.send('{"text1":"'+menu.goingMain+'"}')
                        ws.send('{"text2":""}')
                        ws.send('{"img":"hide"}')
                        ws.send('{"userText":"hide"}')
                        print(menu.goingMain)
                        tts.speak(menu.goingMain)
                        continue

                elif selection == foodIndex-1:  # going to main - none selected
                    ws.send('{"text1":"'+menu.goingMain+'"}')
                    ws.send('{"text2":""}')
                    ws.send('{"img":"hide"}')
                    ws.send('{"userText":"hide"}')
                    print(menu.goingMain)
                    tts.speak(menu.goingMain)
                    continue

                elif selection == foodIndex:  # going to check - check out // has nothin to do with order id only checkout with cart items pushed
                    ws.send('{"text1":"'+menu.goingCheck+'"}')
                    ws.send('{"text2":""}')
                    ws.send('{"img":"hide"}')
                    ws.send('{"userText":"hide"}')
                    print(menu.goingCheck)
                    tts.speak(menu.goingCheck)
                    checkout()
                else:
                    print(menu.invSel)  # invalid Selection return to Home
                    ws.send('{"text1":"'+menu.invSel+'"}')
                    ws.send('{"text2":""}')
                    ws.send('{"img":"hide"}')
                    ws.send('{"userText":"hide"}')
                    tts.speak(menu.invSel)
                    continue

            elif inp == '2':
                foodIndex = food.getEnd(food.getShakes())
                sel = input("Enter the selection : ")
                selection = int(sel)

                if selection in range(1, foodIndex-1):  # push thing to arry only
                    selection = selection-1
                    shakes = items.Shakes().shakes[selection].thing
                    rs = items.Shakes().shakes[selection].rs
                    carts.shakes.append(shakes)
                    carts.rs.append(rs)

                    ws.send('{"text1":"Order Selection"}')
                    ws.send(
                        '{"text2":"Press 1 for Checkout OR Press 2 to go to main menu and add more items to cart"}')

                    ws.send('{"userText":" Selected '+shakes +
                            ' for Rupees ' + str(rs)+'"}')

                    ws.send('{"img":"hide"}')
                    ws.send('{"userText":"show"}')

                    print("Selected " + shakes + " for Rupees " + str(rs))
                    print(
                        "Press 1 for Checkout OR Press 2 to go to main menu and add more items to cart")
                    tts.speak("Selected " + shakes + " for Rupees " + str(rs))
                    tts.speak(
                        "Press 1 for Checkout OR Press 2 to go to main menu and add more items to cart")
                    sel = input("Enter the selection : ")
                    sel = int(sel)

                    if sel == 1:
                        ws.send('{"text1":"'+menu.goingCheck+'"}')
                        ws.send('{"text2":""}')
                        ws.send('{"img":"hide"}')
                        ws.send('{"userText":"hide"}')
                        print(menu.goingCheck)
                        tts.speak(menu.goingCheck)
                        checkout()
                    else:
                        ws.send('{"text1":"'+menu.goingMain+'"}')
                        ws.send('{"text2":""}')
                        ws.send('{"img":"hide"}')
                        ws.send('{"userText":"hide"}')
                        print(menu.goingMain)
                        tts.speak(menu.goingMain)
                        continue

                elif selection == foodIndex-1:  # going to main - none selected
                    ws.send('{"text1":"'+menu.goingMain+'"}')
                    ws.send('{"text2":""}')
                    ws.send('{"img":"hide"}')
                    ws.send('{"userText":"hide"}')
                    print(menu.goingMain)
                    tts.speak(menu.goingMain)
                    continue

                elif selection == foodIndex:  # going to check - check out // has nothin to do with order id only checkout with cart items pushed
                    ws.send('{"text1":"'+menu.goingCheck+'"}')
                    ws.send('{"text2":""}')
                    ws.send('{"img":"hide"}')
                    ws.send('{"userText":"hide"}')
                    print(menu.goingCheck)
                    tts.speak(menu.goingCheck)
                    checkout()
                else:
                    print(menu.invSel)  # invalid Selection return to Home
                    ws.send('{"text1":"'+menu.invSel+'"}')
                    ws.send('{"text2":""}')
                    ws.send('{"img":"hide"}')
                    ws.send('{"userText":"hide"}')
                    tts.speak(menu.invSel)
                    continue

            elif inp == '3':
                foodIndex = food.getEnd(food.getCombos())
                sel = input("Enter the selection : ")
                selection = int(sel)

                if selection in range(1, foodIndex-1):  # push thing to arry only
                    selection = selection-1
                    combo = items.Combos().combos[selection].thing
                    rs = items.Combos().combos[selection].rs
                    carts.combos.append(combo)
                    carts.rs.append(rs)

                    ws.send('{"text1":"Order Selection"}')
                    ws.send(
                        '{"text2":"Press 1 for Checkout OR Press 2 to go to main menu and add more items to cart"}')

                    ws.send('{"userText":" Selected '+combo +
                            ' Combo for Rupees ' + str(rs)+'"}')

                    ws.send('{"img":"hide"}')
                    ws.send('{"userText":"show"}')

                    print("Selected " + combo + " combo for Rupees " + str(rs))
                    print(
                        "Press 1 for Checkout OR Press 2 to go to main menu and add more items to cart")
                    tts.speak("Selected " + combo +
                              " combo for Rupees " + str(rs))
                    tts.speak(
                        "Press 1 for Checkout OR Press 2 to go to main menu and add more items to cart")
                    sel = input("Enter the selection : ")
                    sel = int(sel)

                    if sel == 1:
                        ws.send('{"text1":"'+menu.goingCheck+'"}')
                        ws.send('{"text2":""}')
                        ws.send('{"img":"hide"}')
                        ws.send('{"userText":"hide"}')
                        print(menu.goingCheck)
                        tts.speak(menu.goingCheck)
                        checkout()
                    else:
                        ws.send('{"text1":"'+menu.goingMain+'"}')
                        ws.send('{"text2":""}')
                        ws.send('{"img":"hide"}')
                        ws.send('{"userText":"hide"}')
                        print(menu.goingMain)
                        tts.speak(menu.goingMain)
                        continue

                elif selection == foodIndex-1:  # going to main - none selected
                    ws.send('{"text1":"'+menu.goingMain+'"}')
                    ws.send('{"text2":""}')
                    ws.send('{"img":"hide"}')
                    ws.send('{"userText":"hide"}')
                    print(menu.goingMain)
                    tts.speak(menu.goingMain)
                    continue

                elif selection == foodIndex:  # going to check - check out // has nothin to do with order id only checkout with cart items pushed
                    ws.send('{"text1":"'+menu.goingCheck+'"}')
                    ws.send('{"text2":""}')
                    ws.send('{"img":"hide"}')
                    ws.send('{"userText":"hide"}')
                    print(menu.goingCheck)
                    tts.speak(menu.goingCheck)
                    checkout()
                else:
                    ws.send('{"text1":"'+menu.invSel+'"}')
                    ws.send('{"text2":""}')
                    ws.send('{"img":"hide"}')
                    ws.send('{"userText":"hide"}')
                    print(menu.invSel)  # invalid Selection return to Home
                    tts.speak(menu.invSel)
                    continue

            else:
                ws.send('{"text1":"'+menu.invSel+'"}')
                ws.send('{"text2":""}')
                ws.send('{"img":"hide"}')
                ws.send('{"userText":"hide"}')
                print(menu.invSel)
                tts.speak(menu.invSel)
                continue
