# 🎮 Rock Paper Scissors Game (Python - Modular Architecture)

## 🔹 Overview

This is a Command-Line Interface (CLI) based Rock Paper Scissors game built using Python.
The project follows a **modular architecture**, where the game logic, utility functions, and main execution are separated into different files for better organization and scalability.

---

## 🔹 Features

* 🎯 Play against computer (random choice)
* 🔁 Replay option after each round
* ⚠️ Input validation for user input
* 🎨 Emoji-based output for better user experience
* 🧩 Modular code structure

---

## 🔹 Project Structure

```
Rock-Paper-Scissors/
│
├── MAIN.py        # Entry point (menu + control flow)
├── RPS.py         # Game logic (rules + winner decision)
├── utils.py       # Helper functions (display, validation, etc.)
├── README.md
└── .gitignore
```

---

## 🔹 Technologies Used

* Python
* random module

---

## 🔹 How It Works

* User selects **rock, paper, or scissors**
* Computer randomly selects one option
* Game logic (in `RPS.py`) determines the winner
* `utils.py` handles helper operations like formatting output
* `MAIN.py` controls the game flow and user interaction

---

## 🔹 How to Run

1. Clone the repository:
   git clone https://github.com/Tanishk479/Rock-Paper-Scissors.git

2. Navigate to the folder:
   cd Rock-Paper-Scissors

3. Run the program:
   python MAIN.py

---

## 🔹 Example Output

You chose: 🪨 rock
Computer chose: ✂️ scissors
Result: You win! 🎉

---

## 🔹 Key Learning Outcomes

* Modular programming in Python
* Separation of concerns (logic, utilities, control flow)
* Use of random module
* CLI-based game development
* Git & GitHub workflow

---

## 🔹 Future Improvements

* Add score tracking system 📊
* Add best-of-3 / best-of-5 mode 🎯
* Build GUI version using Tkinter 🖥️
* Store game history 📁

---

## 🔹 Author

Tanishk
