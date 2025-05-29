#aidan w
#1/6/25
#rockpapsci
#init
import random #Imports random so the computer can pick an option

#func
def rockpapsci():
    print("Welcome to Rock Paper Scissors")
    print("Select rock, paper or scissors")
    player = input("Selection: ") #This is where the user makes their choice
    computer = random.randint(1,3)
    if computer == 1: #Rock is assigned to the number 1
        computer = "rock"
    elif computer == 2: #paper is assigned to the number 2
        computer = "paper"
    elif computer == 3: #scissor is assigned to the number 3
        computer = "scissor"
    if computer == "scissor" and player == "paper": #These codes show how the user will win
        print("You lose!")
    if computer == "rock" and player == "scissor":
        print("You lose!")
    if computer == "paper" and player == "rock":
        print("You lose!")
    if computer == "rock" and player == "paper":
        print("You win!")
    if computer == "scissor" and player == "rock":
        print("You win!")
    if computer == "paper" and player == "scissor":
        print("You win!")
    if player == "rock" and computer == "rock":
        print("Tie Game!")
    choice = input("Do you want to play again?: ")
    if choice == "yes":
        print("Restarting...")
        rockpapsci()
    if choice == "no":
        print("Thanks for playing!")
    
        
#main
rockpapsci() #The function
    
        
