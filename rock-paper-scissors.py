from random import randint

print("...rock...\n...paper...\n...scissors...")

player = int(input("What do you choose? "))
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
elif player == 0 and computer == 2: 
    print("Player wins!")
elif player == 2 and computer == 0: 
    print("Computer wins!")
elif player == 1 and computer == 0: 
    print("Player wins!")
elif player == 0 and computer == 1: 
    print("Computer wins!")
elif player == 2 and computer == 1: 
    print("Player wins!")
elif player == 1 and computer == 2:  
    print("Computer wins!")