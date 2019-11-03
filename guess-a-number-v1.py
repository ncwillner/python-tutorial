import random

random_number = random.randint(1,10)

while True:
    choice = int(input("Guess a number between 1 and 10: "))
    if choice > random_number:
        print("too big, try again")
    elif choice < random_number:
        print("too low, try again")
    else:
        print("YOU WON!!!")
        play_again = input("Do you want to play again? (y/n)  ")
        if play_again == "y":
            random_number = random.randint(1, 10)
            choice = None
        else:
            print("thank you for playing!")
            break