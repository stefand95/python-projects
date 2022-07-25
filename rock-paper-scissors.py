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
elif player == "rock" and computer == "scissors": 
    print("Player wins!")
elif player == "scissors" and computer == "rock": 
    print("Computer wins!")
elif player == "paper" and computer == "rock": 
    print("Player wins!")
elif player == "rock" and computer == "paper": 
    print("Computer wins!")
elif player == "scissors" and computer == "paper": 
    print("Player wins!")
elif player == "paper" and computer == "scissors":  
    print("Computer wins!")