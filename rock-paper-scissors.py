from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:

    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("...Rock...\n...Paper...\n...Scissors...")
    player = input("What do you choose? ").lower()
    if player == "quit" or player == "q":
        break
    computer = randint(0,2)

    if computer == 0:
        computer = "rock"
    elif computer == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"Computer chose {computer}")

    if player == computer:
        print("It's a tie!")

    elif player == "rock":
        if computer == "scissors": 
            print("You win!")
        else:
            print("You lose!")
    elif player == "paper":
        if computer == "rock": 
            print("You win!")
        else:
            print("You lose!")
    elif player == "scissors":
        if computer == "paper": 
            print("You win!")
        else:
            print("You lose!")
    else:
        print("Please enter a valid move!")