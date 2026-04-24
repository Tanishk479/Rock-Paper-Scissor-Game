
from RPS import rock_paper_scissors
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