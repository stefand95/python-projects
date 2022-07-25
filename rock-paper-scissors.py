from random import randint

print("...rock...\n...paper...\n...scissors...")

player = input("What do you choose? ").lower()
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