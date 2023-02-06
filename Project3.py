#######
def start():
    print("Welcome to I want to Go out!")
    print("You are resting in your living room, but suddenly you feel like going out and walking for a while, find the right path so you can do it")
    livingroom()

def tryagain():
    move= input("Would you like to try again? Yes/no\n")
    if move == "Yes":
        livingroom()
    else:
        print("Thank you for try")
    
def livingroom():
    print("\nYou are in the living room")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tMy room\n\tHallway\n\tExit\n")
    if move == "My room":
        myroom()
    elif move == "Hallway":
        hallway()
    elif move == "Exit":
        exit()
    else:
        print("Sorry, I can't understand you, you entered an invalid option. I'll assume you want to stay here")
        livingroom()

def myroom():
    global haveKeys

    if not havePermission:
        print("You are in Your Room")
        move = input("\nWhat would you like to do? Say one of these choices:\n\tTurn on the TV\n\tTurn on the computer\n\tGo back to living room\n")
        if move == "Turn on the TV":
            turnTV()
        elif move == "Turn on the computer":
            turncomputer()
        elif move == "Go back to living room":
            livingroom()
        else:
            print("Sorry, I can't understand you, you entered an invalid option. I'll assume you want to stay here")
            myroom()
    elif havePermission and not haveKeys:
        print("On your desk are the keys to the house. Then you grabbed them")
        haveKeys= True
        move= input("Where would you like to go?Say one of these choices:\n\tExit\n\tStay here\n")
        if move== "Exit":
            exit()
        elif move=="Stay here":
            print("Why are you still here?. You have failed in your attempt to leave. When you stayed in your room you got sleepy and you fell asleep")
            tryagain()
        else:
            print("Sorry, I can't understand you, you entered an invalid option. I'll assume you want to stay here")
            myroom()
    elif havePermission and haveKeys:
        haveboth()

def haveboth():
    move=input("Congratulations :)\nYou have the keys of the house and mom's permission, where would you like to go? Say one of these choices:\n\tExit\n\tStay here\n")
    if move== "Exit":
        exit()
    elif move =="Stay here":
        print("Why are you still here?. You have failed in your attempt to leave. When you stayed in your room you got sleepy and you fell asleep")
        tryagain()
    else:
        haveboth()

def turnTV():
    print("You have failed in your attempt to leave. After turning on the TV and watching your favorite series, you fell asleep")
    tryagain()

def turncomputer():
    print("You have failed in your attempt to leave. After turning on the computer you realize that you have five undelivered papers from computer class and the deadline is today")
    tryagain()

def hallway():
    print("You are in the Hallway")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tGrandma room\n\tMom room\n\tBack to Living room\n")
    if move == "Grandma room":
        grandmaroom()
    elif move == "Mom room":
        momroom()
    elif move == "Back to Living room":
        livingroom()
    else:
        print("Sorry, I can't understand you, you entered an invalid option. I'll assume you want to stay here")
        hallway()

def grandmaroom():
    print("You are in grandma's room")
    move = input("\nWhat would you like to do? Say one of these choices:\n\tTalk with grandma\n\tLie next to grandma\n\tGo back to Hallway\n")
    if move == "Talk with grandma":
        talkgrandma()
    elif move == "Lie next to grandma":
        liegrandma()
    elif move =="Go back to Hallway":
        hallway()
    else:
        print("Sorry, I can't understand you, you entered an invalid option. I'll assume you want to stay here")
        grandmaroom()

def talkgrandma():
    print("You have failed in your attempt to leave. After talking to Grandma, she asks you to help her wash the dishes")
    tryagain()

def liegrandma():
    print("You have failed in your attempt to leave. After going to bed next to grandma, you fall asleep watching her novels")
    tryagain()

def momroom():
    print("You are in mom's room. The room is dark and she is sleeping")
    move = input("\nWhat would you like to do? Say one of these choices:\n\tWake her up and ask permission\n\tTry to go out without permission\n\tGo back to Hallway\n")
    if move == "Wake her up and ask permission":
        wakemomup()
    elif move == "Try to go out without permission":
        trywhitoutmom()
    elif move =="Go back to Hallway":
        hallway()
    else:
        print("Sorry, I can't understand you, you entered an invalid option. I'll assume you want to stay here")
        momroom()

def wakemomup():
    global havePermission
    print("Congratulations :)\nAfter waking up and talking to mom you have permission to go out")
    input("\nPress enter to go back out to the living room")
    havePermission= True
    livingroom()

def trywhitoutmom():
    print("You have failed in your attempt to leave. Mom wakes up and asks you where you are going without permission. You're grounded for the rest of your life")
    tryagain()

def exit():
    if not havePermission:
        trywhitoutmom()
    elif havePermission and not haveKeys:
        print("You have failed in your attemp to leave. The door is locked, and you decide to stay resting in the living room. I guess you are forgeting something.")
        tryagain()
    
    else:
        print("After having mom's permission and having the keys to the house, you can leave with peace of mind.\n\tCongratulations :)\n\tBut don't take so long")
    

########
#main
#######
#TODO: Add some global variables
havePermission= False
haveKeys= False
start()