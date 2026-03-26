#This is a Rock Paper Scissor game
import random

while True:
    #User input
    while True:
        user = input("Rock, Paper Scissor? \n")
        user = user.lower()

        if user == "rock":
            user = 1
            break
        elif user == "paper":
            user = 2
            break
        elif user == "scissor":
            user = 3
            break
        else: 
            print("Please enter a valid option")
    
    Computer = random.randint(1,3)
    Computer_str = ""
    
    if Computer == 1:
        Computer_str = "Rock"
    elif Computer == 2:
        Computer_str = "paper"
    elif Computer == 3:
        Computer_str = "scissor"


    if user == Computer:
        print(f"Computer picked: {Computer_str} \n Its a draw!")
        print("please try again")
    elif (user == 1 and Computer == 3):
        print(f"Computer picked: {Computer_str} \n You win!")
    elif (user == 2 and Computer == 1):
        print(f"Computer picked: {Computer_str} \n You win!")
    else: 
        print(f"Computer picked: {Computer_str} \n Computer win!")

