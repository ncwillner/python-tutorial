import random

player = input("player1, make your choice: ").lower()
rand_num = random.randint(0, 2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"AI's choice is: {computer}")

if player == computer:
    print("it's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("player1 wins")
    elif computer == "paper":
        print("computer wins!")
elif player == "paper":
    if computer == "rock":
        print("player 1 wins!")
    elif computer == "scissors":
        print("computer wins!")
elif player == "scissors":
    if computer == "paper":
        print("player 1 wins!")
    elif computer == "rock":
        print("computer wins!")
else:
    print("something went wrong :(")
