import textToSpeech
import menu
import cart
import items
import food
import pay
import datetime

##
tts = textToSpeech.TextToSpeech()
menu = menu.MenuOptions()
carts = cart.Cart()
pay = pay.Payment()
##

def checkout():
    print(menu.orderis)
    tts.speak(menu.orderis)

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
        tts.speak("There is nothing in the cart, Please Order somthing and then checkout, Going to main menu")
        return
    else:
        print("total rupees are", total)
        tts.speak("total rupees are" + str(total))


    print("Press 1 to select payment methods, press 0 to cancel")
    tts.speak("Press 1 to select payment methods, press 0 to cancel")
        
    sel = input("Please enter an option: ")


#### Payment Screen
    if sel=='1':
        sayThing = "Please Select Suitable Payment Method, Press 1 For Cash Payment, Press 2 for Card Payment, Press 0 to Cancel"
        print(sayThing)
        tts.speak(sayThing)
        sel = input("Please enter an option: ")

        if sel == '1':
            pay.cashPay(total)
            addTextToFile("Cash")
            clearCart()
        elif sel == '2':
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

    orderText = orderText + " | Total Rs: " + str(total) + " | Payment Method : "+ paym +" \n"
    
    
    f=open("OrderLists.txt", "a+")
    f.write(orderText)
    f.close()
    print("Added Text to File")
    
            


if __name__ == '__main__':
    while True:
        tts.speak(menu.AnyKey)
        inp = input(menu.AnyKey + "\n")
        if inp != '':
            print(menu.WelcomeText + '\n')
            tts.speak(menu.WelcomeText)
            food.getFood()

            inp = input("Enter the selection : ")

            if inp == '1':
                foodIndex = food.getEnd(food.getBurgers())
                sel = input("Enter the selection : ")
                selection = int(sel)

                if selection in range(1,foodIndex-1): # push thing to arry only
                    selection  = selection-1
                    burger = items.Burgers().burgers[selection].thing
                    rs = items.Burgers().burgers[selection].rs
                    carts.burger.append(burger)
                    carts.rs.append(rs)
                    print("Selected " + burger + " burger for Rupees " + str(rs))
                    print("Press 1 for Checkout OR Press 2 to go to main menu and add more items to cart")
                    tts.speak("Selected " + burger + " burger for Rupees " + str(rs))
                    tts.speak("Press 1 for Checkout OR Press 2 to go to main menu and add more items to cart")
                    sel = input("Enter the selection : ")
                    sel = int(sel)

                    if sel==1:
                        print(menu.goingCheck)
                        tts.speak(menu.goingCheck)
                        checkout()
                    else:
                        print(menu.goingMain)
                        tts.speak(menu.goingMain)
                        continue


                elif selection == foodIndex-1: # going to main - none selected
                    print(menu.goingMain)
                    tts.speak(menu.goingMain)
                    continue

                elif selection == foodIndex: # going to check - check out // has nothin to do with order id only checkout with cart items pushed
                    print(menu.goingCheck)
                    tts.speak(menu.goingCheck)
                    checkout()
                else:
                    print(menu.invSel) #invalid Selection return to Home
                    tts.speak(menu.invSel)
                    continue




            elif inp == '2':
                foodIndex = food.getEnd(food.getShakes())
                sel = input("Enter the selection : ")
                selection = int(sel)

                if selection in range(1,foodIndex-1): # push thing to arry only
                    selection  = selection-1
                    shakes = items.Shakes().shakes[selection].thing
                    rs = items.Shakes().shakes[selection].rs
                    carts.shakes.append(shakes)
                    carts.rs.append(rs)
                    print("Selected " + shakes + " for Rupees " + str(rs))
                    print("Press 1 for Checkout OR Press 2 to go to main menu and add more items to cart")
                    tts.speak("Selected " + shakes + " for Rupees " + str(rs))
                    tts.speak("Press 1 for Checkout OR Press 2 to go to main menu and add more items to cart")
                    sel = input("Enter the selection : ")
                    sel = int(sel)

                    if sel==1:
                        print(menu.goingCheck)
                        tts.speak(menu.goingCheck)
                        checkout()
                    else:
                        print(menu.goingMain)
                        tts.speak(menu.goingMain)
                        continue


                elif selection == foodIndex-1: # going to main - none selected
                    print(menu.goingMain)
                    tts.speak(menu.goingMain)
                    continue
                
                elif selection == foodIndex: # going to check - check out // has nothin to do with order id only checkout with cart items pushed
                    print(menu.goingCheck)
                    tts.speak(menu.goingCheck)
                    checkout()
                else:
                    print(menu.invSel) #invalid Selection return to Home
                    tts.speak(menu.invSel)
                    continue

              


            elif inp == '3':
                foodIndex = food.getEnd(food.getCombos())
                sel = input("Enter the selection : ")
                selection = int(sel)

                if selection in range(1,foodIndex-1): # push thing to arry only
                    selection  = selection-1
                    combo = items.Combos().combos[selection].thing
                    rs = items.Combos().combos[selection].rs
                    carts.combos.append(combo)
                    carts.rs.append(rs)
                    print("Selected " + combo + " combo for Rupees " + str(rs))
                    print("Press 1 for Checkout OR Press 2 to go to main menu and add more items to cart")
                    tts.speak("Selected " + combo + " combo for Rupees " + str(rs))
                    tts.speak("Press 1 for Checkout OR Press 2 to go to main menu and add more items to cart")
                    sel = input("Enter the selection : ")
                    sel = int(sel)

                    if sel==1:
                        print(menu.goingCheck)
                        tts.speak(menu.goingCheck)
                        checkout()
                    else:
                        print(menu.goingMain)
                        tts.speak(menu.goingMain)
                        continue


                elif selection == foodIndex-1: # going to main - none selected
                    print(menu.goingMain)
                    tts.speak(menu.goingMain)
                    continue
                
                elif selection == foodIndex: # going to check - check out // has nothin to do with order id only checkout with cart items pushed
                    print(menu.goingCheck)
                    tts.speak(menu.goingCheck)
                    checkout()
                else:
                    print(menu.invSel) #invalid Selection return to Home
                    tts.speak(menu.invSel)
                    continue

            else:
                print(menu.invSel)
                tts.speak(menu.invSel)
                continue

