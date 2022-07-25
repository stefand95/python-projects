from random import randint

print("...rock...\n...paper...\n...scissors...")

player = input("What do you choose? ")
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
        print("Player wins!")
    else:
        print("Computer wins!")
elif player == "paper":
    if computer == "rock": 
        print("Player wins!")
    else:
        print("Computer wins!")
elif player == "scissors":
    if computer == "paper": 
        print("Player wins!")
    else:
        print("Computer wins!")
