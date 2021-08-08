# Requires PyAudio and PySpeech.

#importing speech_recogntion and random libaries
import speech_recognition as sr
from random import randint

#making it so that the robot randomly picks "rock", "paper or "scissors"
options = ["Rock", "Paper", "Scissors"]
robot = options[randint(0,2)]
#setting the robot selection to lowercase
robot = robot.lower()
#defining the players choice variable as empty
choice = False
#setting the win counter to 0
counter = 0
#printing what the game is
print("Rock, paper, siccors: ")
#opening the txt file holding the win counter, saving it to data and asigning the integer form to the counter variable 
a = open('counter.txt')
data = a.read()
print(data)
a.close()
counter = int(data)
#while choice is false the game will keep running
while choice == False:
    # r is set as the speech recognizer
    r = sr.Recognizer()
    #source is set as what is passed through the microphone
    with sr.Microphone() as source:
        #prompted say your choice and audio is set as your answer
        print("say your choice and wait")
        audio = r.listen(source)
    #choice is set as what google recognizes the sound to be otherwise the correlating error is printed 
    try:
        choice = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    #choice is set to lowercase
    choice = choice.lower()
    #prints what the user said
    print("you chose " + choice)
    #if user and robot choice the same thing a tie is stated
    if choice == robot:
        print("Tie!")
    #if you chose rock and the robot chose paper it'll state you lost
    #but if you chose rock and the robot chose scissors it'll state you won
    elif choice == "rock":
        if robot == "paper":
            print("You lose!", robot, "covers", choice)
        else:
            print("You win!", choice, "smashes", robot)
            #1 is added onto the win counter
            counter+=1
    #if you chose paper and the robot chose scissors it'll state you lost
    #but if you chose paper and the robot chose rock it'll state you won
    elif choice == "paper":
        if robot == "scissors":
            print("You lose!", robot, "cut", choice)
        else:
            print("You win!", choice, "covers", robot)
            #1 is added onto the win counter
            counter+=1
    #if you chose scissors and the robot chose rock it'll state you lost
    #but if you chose scissors and the robot chose paper it'll state you won
    elif choice == "scissors":
        if robot == "rock":
            print("You lose...", robot, "smashes", choice)
        else:
            print("You win!", choice, "cut", robot)
            #1 is added onto the win counter
            counter+=1
    #if you didn't enter rock, paper or scissors it will state it wasn't valid
    else:
        print("That's not a valid play!")
    #player was set to True, but we want it to be False so the loop continues
    choice = False
    #robot choses new selection
    robot = options[randint(0,2)]
    #set to lowercase
    robot = robot.lower()
    #states how many times you have won
    print("your win counter is: " + str(counter))
    #asks if you want to exit or continue
    contin = input('enter "x" to Exit OR press enter to continue')
    #if x is input the loop will end and the program will close
    if contin == "x":
        choice = True
#the new counter value is overwritten on the txt file
f = open("counter.txt", "w")
f.write(str(counter))
f.close()
