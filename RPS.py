import random
from utils import outcomes, emoji

def rock_paper_scissors():
    while True:
        user = input("\nEnter rock, paper, or scissors: ").lower()
        if user not in outcomes:
            print("Invalid input. Please try again.")
        else:
            comp = random.choice(outcomes)
            if user == comp:
                print(f"Both chose {user} {emoji[user]}.")
                print("It's a tie! 🤝")
            elif (user == "rock" and comp == "scissors") or (user == "paper" and comp == "rock") or (user == "scissors" and comp == "paper"):
                print(f"\nYou chose: {user} {emoji[user]}")
                print(f"Computer chose: {comp} {emoji[comp]}")
                print("Result: You win! 🎉")
            else:
                print(f"\nYou chose: {user} {emoji[user]}")
                print(f"Computer chose: {comp} {emoji[comp]}")
                print("Result: You lose! 😭")
            again = input("Do you want to play again? (y/n): ").lower()
            if again == 'n':
                break