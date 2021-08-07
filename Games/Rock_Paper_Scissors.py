from random import randint

options = ["Rock", "Paper", "Scissors"]
robot = options[randint(0,2)]
robot = robot.lower()
choice = False

print("Rock, paper, siccors: ")


while choice == False:

    choice = input("enter your choice:")
    choice = choice.lower()
    if choice == robot:
        print("Tie!")
    elif choice == "rock":
        if robot == "paper":
            print("You lose!", robot, "covers", choice)
        else:
            print("You win!", choice, "smashes", robot)
    elif choice == "paper":
        if robot == "scissors":
            print("You lose!", robot, "cut", choice)
        else:
            print("You win!", choice, "covers", robot)
    elif choice == "scissors":
        if robot == "rock":
            print("You lose...", robot, "smashes", choice)
        else:
            print("You win!", choice, "cut", robot)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    robot = options[randint(0,2)]
    robot = robot.lower()

