
#ROCK PAPER SCISSORS GAME
import random   
outcomes = ["rock", "paper", "scissors"]
emoji = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}
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

#menu
def game():
    while True:
        print("\n====WELCOME TO THE ROCK-PAPER-SCISSORS GAME====")
        print("👉 1. Start Game")
        print("👉 2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print("Starting the game...")
            rock_paper_scissors()
        elif choice == '2':
            print("Goodbye!👋")
            break
        else:
            print("Invalid choice. Please try again.")

game()
