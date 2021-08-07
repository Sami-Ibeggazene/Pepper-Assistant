# Requires PyAudio and PySpeech.

import speech_recognition as sr
from random import randint

options = ["Rock", "Paper", "Scissors"]
robot = options[randint(0,2)]
robot = robot.lower()
choice = False
counter = 0

print("Rock, paper, siccors: ")

# Record Audio
#r = sr.Recognizer()
#with sr.Microphone() as source:
#    print("enter your choice and wait")
#    audio = r.listen(source)




while choice == False:
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("enter your choice and wait")
        audio = r.listen(source)
    try:
        choice = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
    choice = choice.lower()
    print("you chose " + choice)
    if choice == robot:
        print("Tie!")
    elif choice == "rock":
        if robot == "paper":
            print("You lose!", robot, "covers", choice)
        else:
            print("You win!", choice, "smashes", robot)
            counter+=1
    elif choice == "paper":
        if robot == "scissors":
            print("You lose!", robot, "cut", choice)
        else:
            print("You win!", choice, "covers", robot)
            counter+=1
    elif choice == "scissors":
        if robot == "rock":
            print("You lose...", robot, "smashes", choice)
        else:
            print("You win!", choice, "cut", robot)
            counter+=1
    else:
        print("That's not a valid play!")
    #player was set to True, but we want it to be False so the loop continues
    choice = False
    robot = options[randint(0,2)]
    robot = robot.lower()
    print("your win counter is: " + str(counter))
    contin = input('enter "x" to Exit OR press enter to continue')
    if contin == "x":
        choice = True

f = open("text.txt", "w")
f.write("score: " + str(counter))
f.close()
