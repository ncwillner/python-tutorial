import random
player_wins = 0
computer_wins = 0
winning_score = 3
while computer_wins < winning_score and player_wins < winning_score:
        print(f"player score: {player_wins} / computer score: {computer_wins}")
        print("...rock...")
        print("...paper...")
        print("...scissors...")

        player = input("player1, make your choice: ").lower()
        if player == "quit" or player == "q":
            break
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
                player_wins += 1
            elif computer == "paper":
                print("computer wins!")
                computer_wins += 1
        elif player == "paper":
            if computer == "rock":
                print("player 1 wins!")
                player_wins += 1
            elif computer == "scissors":
                print("computer wins!")
                computer_wins += 1
        elif player == "scissors":
            if computer == "paper":
                print("player 1 wins!")
                player_wins += 1
            elif computer == "rock":
                print("computer wins!")
                computer_wins += 1
        else:
            print("something went wrong :(")
if player_wins > computer_wins:
    print("CONGRATS, YOU WON!")
elif player_wins == computer_wins:
    print("it's a tie!")
else:
    print("OH NO :(, YOU LOST")
print(f"FINAL SCORES: player: {player_wins} / computer: {computer_wins}")